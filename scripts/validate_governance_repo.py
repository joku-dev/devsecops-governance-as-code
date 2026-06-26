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


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def main() -> int:
    errors = []
    controls = []

    for path in sorted((ROOT / "controls").glob("dscb-*.yaml")):
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

    traceability = load_yaml(ROOT / "traceability" / "control-to-platform.yaml")
    traced = {item["control"] for item in traceability.get("mappings", [])}
    known = set(ids)

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
