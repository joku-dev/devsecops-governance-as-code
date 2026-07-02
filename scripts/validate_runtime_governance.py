#!/usr/bin/env python3
"""Validate the SDD runtime governance addendum.

The addendum is intentionally model-first: YAML and JSON files are the
machine-readable layer, Markdown is the explanatory view, and OPA is the first
executable policy gate. This validator keeps those pieces aligned.
"""

from pathlib import Path
import json
import shutil
import subprocess
import sys

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]

SCHEMA_CHECKS = [
    ("architecture/quality-markers.yaml", "schemas/quality-marker.schema.json", "yaml"),
    ("architecture/guardrails.yaml", "schemas/architecture-guardrail.schema.json", "yaml"),
    ("architecture/review-gates.yaml", "schemas/review-gate.schema.json", "yaml"),
    (
        "policies/example-input.architecture-release-candidate.json",
        "schemas/architecture-release-candidate.schema.json",
        "json",
    ),
]

EXPECTED_MARKERS = (
    {f"B{i}" for i in range(1, 6)}
    | {f"E{i}" for i in range(0, 11)}
    | {f"S{i}" for i in range(0, 11)}
    | {f"P{i}" for i in range(0, 14)}
)


def load_data(path: Path, kind: str):
    text = path.read_text(encoding="utf-8")
    if kind == "json":
        return json.loads(text)
    return yaml.safe_load(text)


def validate_schema(data_path: str, schema_path: str, kind: str, errors: list[str]) -> None:
    try:
        data = load_data(ROOT / data_path, kind)
        schema = json.loads((ROOT / schema_path).read_text(encoding="utf-8"))
        jsonschema.validate(data, schema)
    except Exception as exc:  # noqa: BLE001 - validator should report all failures cleanly
        errors.append(f"{data_path} failed schema validation against {schema_path}: {exc}")


def validate_marker_catalogue(errors: list[str]) -> None:
    try:
        data = yaml.safe_load((ROOT / "architecture" / "quality-markers.yaml").read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Could not load architecture/quality-markers.yaml: {exc}")
        return

    markers = data.get("markers", [])
    ids = [marker.get("id") for marker in markers]
    duplicates = sorted({marker_id for marker_id in ids if ids.count(marker_id) > 1})
    missing = sorted(EXPECTED_MARKERS - set(ids))
    unknown = sorted(set(ids) - EXPECTED_MARKERS)

    if duplicates:
        errors.append(f"Duplicate architecture marker IDs: {duplicates}")
    if missing:
        errors.append(f"Missing architecture marker IDs: {missing}")
    if unknown:
        errors.append(f"Unknown architecture marker IDs: {unknown}")


def validate_opa_policy(errors: list[str]) -> None:
    if not shutil.which("opa"):
        errors.append("OPA executable not found; cannot validate architecture release-readiness policy")
        return

    command = [
        "opa",
        "eval",
        "--data",
        str(ROOT / "policies" / "opa" / "architecture_release_readiness.rego"),
        "--input",
        str(ROOT / "policies" / "example-input.architecture-release-candidate.json"),
        "data.architecture.release_readiness.deny",
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        errors.append(f"OPA evaluation failed: {result.stderr.strip() or result.stdout.strip()}")
        return

    try:
        payload = json.loads(result.stdout)
        value = payload["result"][0]["expressions"][0]["value"]
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Could not parse OPA evaluation result: {exc}")
        return

    if value:
        errors.append(f"Example architecture release candidate failed policy: {value}")


def main() -> int:
    errors: list[str] = []

    for data_path, schema_path, kind in SCHEMA_CHECKS:
        validate_schema(data_path, schema_path, kind, errors)

    for schema_path in ["schemas/architecture-exception.schema.json"]:
        try:
            json.loads((ROOT / schema_path).read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{schema_path} is not valid JSON: {exc}")

    validate_marker_catalogue(errors)
    validate_opa_policy(errors)

    if errors:
        print("Runtime governance validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Runtime governance validation passed")
    print(f"- expected markers: {len(EXPECTED_MARKERS)}")
    print(f"- schema checks: {len(SCHEMA_CHECKS)}")
    print("- OPA release-readiness example: passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
