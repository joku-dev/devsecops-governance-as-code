#!/usr/bin/env python3
"""Generate a flat control traceability CSV from the YAML control library."""

from pathlib import Path
import csv
import yaml


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "xlsx" / "traceability_matrix.csv"


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def main() -> int:
    controls = {}
    for path in sorted((ROOT / "controls").glob("dscb-*.yaml")):
        data = load_yaml(path)
        level = data.get("level")
        for requirement in data.get("requirements", []):
            controls[requirement["id"]] = {
                **requirement,
                "level": level,
            }

    traceability = load_yaml(ROOT / "traceability" / "control-to-platform.yaml")
    rows = []
    for mapping in traceability.get("mappings", []):
        control = controls[mapping["control"]]
        rows.append(
            {
                "control_id": control["id"],
                "level": control["level"],
                "domain": control["domain"],
                "title": control["title"],
                "requirement": control["requirement"],
                "required_platform_level": mapping["platform_level"],
                "platform_capabilities": "; ".join(mapping.get("platform_capabilities", [])),
                "evidence": "; ".join(mapping.get("evidence", [])),
                "verification_method": control.get("verification", {}).get("method", ""),
                "verification_frequency": control.get("verification", {}).get("frequency", ""),
                "policy_candidate": str(mapping.get("policy_candidate", False)).lower(),
                "policy_rule": control.get("policy_as_code", {}).get("rule", ""),
                "waiver_allowed": str(control.get("waiver", {}).get("allowed", "")).lower(),
                "waiver_authority": control.get("waiver", {}).get("authority", ""),
            }
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {OUT.relative_to(ROOT)} with {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
