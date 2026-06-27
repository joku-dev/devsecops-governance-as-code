#!/usr/bin/env python3
"""Validate the DevSecOps governance-as-code repository MVP.

The validator intentionally performs repository-level checks that are more
useful for the pilot than pure schema validation:

- all control IDs are unique
- expected L1/L2/L3/GOV counts are present
- every control has traceability
- policy candidate rules exist on disk
- every traceability target points to a known control
"""

from pathlib import Path
import json
import shutil
import subprocess
import sys

import yaml

try:
    from jsonschema import Draft202012Validator
except ModuleNotFoundError:
    Draft202012Validator = None


ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "model"
EXPECTED_COUNTS = {"L1": 16, "L2": 14, "L3": 11, "GOV": 5}


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_schema(errors, schema_path: Path, instance_path: Path):
    if Draft202012Validator is None:
        print(
            "Warning: jsonschema is not installed; skipping schema validation for "
            f"{instance_path.relative_to(ROOT)}",
            file=sys.stderr,
        )
        return
    validator = Draft202012Validator(load_json(schema_path))
    instance = load_yaml(instance_path)
    for issue in validator.iter_errors(instance):
        location = " -> ".join(str(part) for part in issue.absolute_path) or "<root>"
        errors.append(f"Schema validation failed for {instance_path.relative_to(ROOT)} at {location}: {issue.message}")


def run_opa_check(errors):
    opa = shutil.which("opa")
    if not opa:
        errors.append("OPA CLI not found on PATH.")
        return

    result = subprocess.run(
        [opa, "check", str(ROOT / "policies" / "opa")],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        details = result.stderr.strip() or result.stdout.strip() or "unknown OPA error"
        errors.append(f"OPA policy validation failed: {details}")


def main() -> int:
    errors = []
    controls = []
    capabilities = load_yaml(MODEL / "platform" / "platform-capabilities.yaml")
    evidence_catalog = load_yaml(MODEL / "evidence" / "evidence-types.yaml")
    governance_documents = load_yaml(MODEL / "documents" / "governance-documents.yaml")
    document_traceability = load_yaml(MODEL / "traceability" / "document-to-control.yaml")

    validate_schema(errors, ROOT / "schemas" / "control.schema.json", MODEL / "controls" / "dscb-l1.yaml")
    validate_schema(errors, ROOT / "schemas" / "control.schema.json", MODEL / "controls" / "dscb-l2.yaml")
    validate_schema(errors, ROOT / "schemas" / "control.schema.json", MODEL / "controls" / "dscb-l3.yaml")
    validate_schema(errors, ROOT / "schemas" / "control.schema.json", MODEL / "controls" / "dscb-gov.yaml")
    validate_schema(errors, ROOT / "schemas" / "governance-document-catalog.schema.json", MODEL / "documents" / "governance-documents.yaml")
    validate_schema(errors, ROOT / "schemas" / "document-control-traceability.schema.json", MODEL / "traceability" / "document-to-control.yaml")
    validate_schema(errors, ROOT / "schemas" / "governance-document-rendering.schema.json", MODEL / "documents" / "governance-document-rendering.yaml")
    validate_schema(errors, ROOT / "schemas" / "governance-compliance-result.schema.json", ROOT / "docs" / "governance-compliance-result.example.json")
    validate_schema(errors, ROOT / "schemas" / "governance-run-input.schema.json", ROOT / "docs" / "governance-run-input.example.json")

    for path in sorted((MODEL / "controls").glob("dscb-*.yaml")):
        data = load_yaml(path)
        level = data.get("level")
        for requirement in data.get("requirements", []):
            requirement["_source_file"] = str(path.relative_to(ROOT))
            requirement["_level_file"] = level
            controls.append(requirement)

    ids = [item["id"] for item in controls]
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        errors.append(f"Duplicate control IDs: {duplicates}")

    for level, expected in EXPECTED_COUNTS.items():
        actual = sum(1 for item in controls if item.get("_level_file") == level)
        if actual != expected:
            errors.append(f"Unexpected {level} count: expected {expected}, got {actual}")

    traceability = load_yaml(MODEL / "traceability" / "control-to-platform.yaml")
    traced = {item["control"] for item in traceability.get("mappings", [])}
    known = set(ids)
    known_capabilities = {item["id"] for item in capabilities.get("capabilities", [])}
    known_evidence = {item["id"] for item in evidence_catalog.get("evidence_types", [])}
    known_documents = {item["id"] for item in governance_documents.get("documents", [])}

    missing_traceability = sorted(known - traced)
    if missing_traceability:
        errors.append(f"Controls missing traceability: {missing_traceability}")

    unknown_traceability = sorted(traced - known)
    if unknown_traceability:
        errors.append(f"Traceability references unknown controls: {unknown_traceability}")

    for item in controls:
        policy = item.get("policy_as_code", {})
        rule = policy.get("rule")
        if policy.get("candidate") and rule and not (ROOT / rule).exists():
            errors.append(f"Policy rule missing for {item['id']}: {rule}")
        for capability in item.get("platform_capabilities", []):
            if capability not in known_capabilities:
                errors.append(f"Unknown platform capability on {item['id']}: {capability}")
        for evidence in item.get("evidence", []):
            if evidence not in known_evidence:
                errors.append(f"Unknown evidence type on {item['id']}: {evidence}")

    for document in governance_documents.get("documents", []):
        document_path = ROOT / document["repository_path"]
        if not document_path.exists():
            errors.append(f"Governance document path missing for {document['id']}: {document['repository_path']}")

    for mapping in traceability.get("mappings", []):
        control_id = mapping["control"]
        for capability in mapping.get("platform_capabilities", []):
            if capability not in known_capabilities:
                errors.append(f"Unknown traceability platform capability on {control_id}: {capability}")
        for evidence in mapping.get("evidence", []):
            if evidence not in known_evidence:
                errors.append(f"Unknown traceability evidence on {control_id}: {evidence}")

    for mapping in document_traceability.get("mappings", []):
        document_id = mapping["document_id"]
        if document_id not in known_documents:
            errors.append(f"Document traceability references unknown document: {document_id}")
        for control_id in mapping.get("control_ids", []):
            if control_id not in known:
                errors.append(f"Document traceability references unknown control: {control_id}")

    run_opa_check(errors)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed")
    print(f"- controls: {len(controls)}")
    for level in ["L1", "L2", "L3", "GOV"]:
        print(f"- {level}: {sum(1 for item in controls if item.get('_level_file') == level)}")
    print(f"- traceability mappings: {len(traced)}")
    print(f"- policy candidates: {sum(1 for item in controls if item.get('policy_as_code', {}).get('candidate'))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
