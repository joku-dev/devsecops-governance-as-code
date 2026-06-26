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
import sys
import yaml


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_COUNTS = {"L1": 16, "L2": 14, "L3": 11, "GOV": 5}
VALID_AUTOMATION_TYPES = {"blocking_gate", "warning_gate", "evidence_check", "review_check"}
VALID_AUTOMATION_MATURITY = {"immediate", "tool_integration_required", "future"}
VALID_CHECK_TYPES = {"presence", "linkage", "threshold", "configuration", "approval", "review", "integrity", "provenance"}


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def main() -> int:
    errors = []
    controls = []
    governance_requirements = []

    for path in sorted((ROOT / "controls").glob("dscb-*.yaml")):
        data = load_yaml(path)
        level = data.get("level")
        for requirement in data.get("requirements", []):
            requirement["_source_file"] = str(path.relative_to(ROOT))
            requirement["_level_file"] = level
            controls.append(requirement)

    for path in sorted((ROOT / "governance").glob("*-requirements.yaml")):
        data = load_yaml(path)
        for requirement in data.get("requirements", []):
            requirement["_source_document"] = data.get("source_document")
            requirement["_source_file"] = str(path.relative_to(ROOT))
            governance_requirements.append(requirement)

    ids = [item["id"] for item in controls]
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        errors.append(f"Duplicate control IDs: {duplicates}")

    for level, expected in EXPECTED_COUNTS.items():
        actual = sum(1 for item in controls if item.get("_level_file") == level)
        if actual != expected:
            errors.append(f"Unexpected {level} count: expected {expected}, got {actual}")

    traceability = load_yaml(ROOT / "traceability" / "control-to-platform.yaml")
    traced = {item["control"] for item in traceability.get("mappings", [])}
    known = set(ids)

    missing_traceability = sorted(known - traced)
    if missing_traceability:
        errors.append(f"Controls missing traceability: {missing_traceability}")

    unknown_traceability = sorted(traced - known)
    if unknown_traceability:
        errors.append(f"Traceability references unknown controls: {unknown_traceability}")

    stages_path = ROOT / "pipeline-baseline" / "stages.yaml"
    placement_path = ROOT / "pipeline-baseline" / "control-placement.yaml"
    if stages_path.exists() and placement_path.exists():
        stages = load_yaml(stages_path)
        valid_stages = {item["id"] for item in stages.get("stages", [])}
        placements = load_yaml(placement_path)
        placed = {item["control"] for item in placements.get("control_placements", [])}
        missing_placement = sorted(known - placed)
        if missing_placement:
            errors.append(f"Controls missing pipeline placement: {missing_placement}")
        unknown_placement = sorted(placed - known)
        if unknown_placement:
            errors.append(f"Pipeline placement references unknown controls: {unknown_placement}")
        invalid_stages = sorted({item.get("stage") for item in placements.get("control_placements", []) if item.get("stage") not in valid_stages})
        if invalid_stages:
            errors.append(f"Pipeline placement uses invalid stages: {invalid_stages}")
    else:
        errors.append("Pipeline baseline stages or control placement file missing")

    for item in controls:
        if not item.get("verification_requirement"):
            errors.append(f"Verification requirement missing for {item['id']}")

        automation = item.get("automation")
        if not automation:
            errors.append(f"Automation classification missing for {item['id']}")
            continue
        if automation.get("type") not in VALID_AUTOMATION_TYPES:
            errors.append(f"Invalid automation type for {item['id']}: {automation.get('type')}")
        if automation.get("maturity") not in VALID_AUTOMATION_MATURITY:
            errors.append(f"Invalid automation maturity for {item['id']}: {automation.get('maturity')}")
        if automation.get("check_type") not in VALID_CHECK_TYPES:
            errors.append(f"Invalid automation check_type for {item['id']}: {automation.get('check_type')}")
        if not isinstance(automation.get("machine_readable_evidence_required"), bool):
            errors.append(f"Invalid machine_readable_evidence_required for {item['id']}: {automation.get('machine_readable_evidence_required')}")
        if not automation.get("rationale"):
            errors.append(f"Automation rationale missing for {item['id']}")

        policy = item.get("policy_as_code", {})
        rule = policy.get("rule")
        if policy.get("candidate") and rule and not (ROOT / rule).exists():
            errors.append(f"Policy rule missing for {item['id']}: {rule}")

    governance_ids = [item["id"] for item in governance_requirements]
    governance_duplicates = sorted({item for item in governance_ids if governance_ids.count(item) > 1})
    if governance_duplicates:
        errors.append(f"Duplicate governance requirement IDs: {governance_duplicates}")

    for item in governance_requirements:
        if not item.get("verification_requirement"):
            errors.append(f"Governance verification requirement missing for {item['id']}")
        automation = item.get("automation")
        if not automation:
            errors.append(f"Governance automation classification missing for {item['id']}")
            continue
        if automation.get("type") not in VALID_AUTOMATION_TYPES:
            errors.append(f"Invalid governance automation type for {item['id']}: {automation.get('type')}")
        if automation.get("maturity") not in VALID_AUTOMATION_MATURITY:
            errors.append(f"Invalid governance automation maturity for {item['id']}: {automation.get('maturity')}")
        if automation.get("check_type") not in VALID_CHECK_TYPES:
            errors.append(f"Invalid governance automation check_type for {item['id']}: {automation.get('check_type')}")
        linked = item.get("derived_controls", item.get("implemented_by", []))
        unknown = sorted(set(linked) - known)
        if unknown:
            errors.append(f"Governance requirement {item['id']} links unknown controls: {unknown}")

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
    if (ROOT / "pipeline-baseline" / "control-placement.yaml").exists():
        placements = load_yaml(ROOT / "pipeline-baseline" / "control-placement.yaml")
        print(f"- pipeline placements: {len(placements.get('control_placements', []))}")
    print(f"- policy candidates: {sum(1 for item in controls if item.get('policy_as_code', {}).get('candidate'))}")
    print(f"- governance requirements: {len(governance_requirements)}")
    print(f"- policy document requirements: {sum(1 for item in governance_requirements if item.get('_source_document') == 'DevSecOps Policy')}")
    print(f"- directive document requirements: {sum(1 for item in governance_requirements if item.get('_source_document') == 'DevSecOps Directive')}")
    for automation_type in sorted(VALID_AUTOMATION_TYPES):
        print(f"- automation {automation_type}: {sum(1 for item in controls if item.get('automation', {}).get('type') == automation_type)}")
    for maturity in sorted(VALID_AUTOMATION_MATURITY):
        print(f"- maturity {maturity}: {sum(1 for item in controls if item.get('automation', {}).get('maturity') == maturity)}")
    for check_type in sorted(VALID_CHECK_TYPES):
        print(f"- check_type {check_type}: {sum(1 for item in controls if item.get('automation', {}).get('check_type') == check_type)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
