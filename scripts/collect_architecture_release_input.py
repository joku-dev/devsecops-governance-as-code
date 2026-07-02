#!/usr/bin/env python3
"""Collect a demo architecture release-readiness input from a target repo.

This collector is intentionally conservative. It does not claim compliance from
intent alone; it translates observable repository signals into marker scores and
evidence flags that the OPA release-readiness policy can evaluate.
"""

from argparse import ArgumentParser
from pathlib import Path
import json
import re
import subprocess


RELEASE_CRITICAL_MARKERS = ["E6", "E7", "E8", "S3", "S5", "S6", "S8", "P5", "P6", "P8", "P9", "P10", "P13"]


def exists(repo: Path, relative: str) -> bool:
    return (repo / relative).exists()


def any_exists(repo: Path, patterns: list[str]) -> bool:
    return any(any(repo.glob(pattern)) for pattern in patterns)


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def git_commit(repo: Path) -> str:
    result = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return "unknown"
    return result.stdout.strip()


def score(present: bool, verified: bool = False, continuous: bool = False) -> int:
    if continuous:
        return 5
    if verified:
        return 4
    if present:
        return 3
    return 1


def evidence_ref(repo: Path, relative: str) -> str | None:
    if exists(repo, relative):
        return relative
    return None


def compact(items: list[str | None]) -> list[str]:
    return [item for item in items if item]


def collect(repo: Path, release_id: str, baseline: str) -> dict:
    architecture_doc = exists(repo, "docs/ARCHITECTURE.md")
    deployment_doc = exists(repo, "docs/DEPLOYMENT.md")
    compose_file = exists(repo, "docker-compose.yml")
    dockerfiles = sorted(str(path.relative_to(repo)) for path in repo.glob("**/Dockerfile"))
    requirements = sorted(str(path.relative_to(repo)) for path in repo.glob("**/requirements.txt"))
    tests = sorted(str(path.relative_to(repo)) for path in repo.glob("tests/**/*.py"))
    schemas = sorted(str(path.relative_to(repo)) for path in repo.glob("**/schemas/*.json"))
    benchmark_reports = sorted(str(path.relative_to(repo)) for path in repo.glob("benchmark/reports/*benchmark.json"))

    architecture_text = read_text(repo / "docs/ARCHITECTURE.md").lower()
    deployment_text = read_text(repo / "docs/DEPLOYMENT.md").lower()
    compose_text = read_text(repo / "docker-compose.yml").lower()

    has_interfaces = any(keyword in architecture_text for keyword in ["http", "rest", "websocket", "bolt", "api", "endpoint"])
    has_security_notes = any(keyword in deployment_text for keyword in ["secret", "token", "password", "api_key", "nie committen"])
    has_health_checks = "health-check" in deployment_text or "docker compose ps" in deployment_text
    has_rollback = "rollback" in deployment_text
    has_resilience = any(keyword in architecture_text + deployment_text for keyword in ["restart", "failure", "failover", "recovery", "degraded"])
    has_performance = bool(benchmark_reports)
    has_release_baseline = any_exists(repo, ["*baseline*", "docs/*BASELINE*", "docs/*baseline*"])
    has_compatibility_declaration = any_exists(repo, ["*compatibility*", "docs/*COMPATIBILITY*", "docs/*compatibility*"])
    has_security_tests = any_exists(repo, ["*security*", "tests/**/*security*.py", ".github/workflows/*security*"])

    deployment_evidence_refs = compact(
        [
            evidence_ref(repo, "docs/DEPLOYMENT.md"),
            evidence_ref(repo, "docker-compose.yml"),
            *dockerfiles,
        ]
    )
    compatibility_refs = compact(
        [
            evidence_ref(repo, "docs/ARCHITECTURE.md"),
            *schemas[:20],
        ]
    )
    security_refs = compact(
        [
            evidence_ref(repo, "docs/DEPLOYMENT.md") if has_security_notes else None,
            *[path for path in tests if "security" in path.lower()],
        ]
    )

    minimum_architecture_refs = compact(
        [
            evidence_ref(repo, "docs/ARCHITECTURE.md"),
            evidence_ref(repo, "README.md"),
            evidence_ref(repo, "docs/DEPLOYMENT.md"),
        ]
    )
    has_component_description = architecture_doc and all(component in architecture_text for component in ["neo4j", "ha-sync", "semantic-enrichment", "query-api"])
    has_process_description = deployment_doc and compose_file
    has_ownership_hint = any(keyword in architecture_text for keyword in ["verantwortung", "responsibility", "owner"])

    marker_assessments = [
        {"id": "B1", "score": score(architecture_doc), "evidence": minimum_architecture_refs},
        {"id": "B2", "score": score(architecture_doc and deployment_doc), "evidence": minimum_architecture_refs},
        {"id": "B3", "score": score(has_process_description), "evidence": minimum_architecture_refs},
        {"id": "B4", "score": score(has_ownership_hint), "evidence": minimum_architecture_refs},
        {"id": "P0", "score": score(architecture_doc), "evidence": minimum_architecture_refs},
        {"id": "P1", "score": score(architecture_doc), "evidence": minimum_architecture_refs},
        {"id": "P2", "score": score(architecture_doc), "evidence": minimum_architecture_refs},
        {"id": "P3", "score": score(has_component_description), "evidence": minimum_architecture_refs},
        {"id": "P7", "score": score("designentscheidungen" in architecture_text or "decision" in architecture_text), "evidence": minimum_architecture_refs},
        {"id": "S0", "score": score(architecture_doc), "evidence": minimum_architecture_refs},
        {"id": "S1", "score": score(architecture_doc and has_component_description), "evidence": minimum_architecture_refs},
        {"id": "S2", "score": score(has_component_description), "evidence": minimum_architecture_refs},
        {"id": "E6", "score": score(has_security_notes, has_security_tests), "evidence": security_refs},
        {"id": "E7", "score": score(bool(tests or requirements), bool(tests)), "evidence": tests[:20] + requirements},
        {"id": "E8", "score": score(compose_file or bool(dockerfiles), deployment_doc), "evidence": deployment_evidence_refs},
        {"id": "S3", "score": score(has_interfaces, bool(schemas)), "evidence": compatibility_refs},
        {"id": "S5", "score": score(has_security_notes, has_security_tests), "evidence": security_refs},
        {"id": "S6", "score": score(has_release_baseline, has_compatibility_declaration), "evidence": compatibility_refs},
        {"id": "S8", "score": score(has_resilience, False), "evidence": deployment_evidence_refs},
        {"id": "P5", "score": score(compose_file or bool(dockerfiles), deployment_doc and compose_file), "evidence": deployment_evidence_refs},
        {"id": "P6", "score": score(has_interfaces or bool(schemas), bool(schemas)), "evidence": compatibility_refs},
        {"id": "P8", "score": score(has_security_notes, has_security_tests), "evidence": security_refs},
        {"id": "P9", "score": score(has_performance, has_performance), "evidence": benchmark_reports[-10:]},
        {"id": "P10", "score": score(has_resilience, False), "evidence": deployment_evidence_refs},
        {"id": "P13", "score": score(has_compatibility_declaration, False), "evidence": compatibility_refs},
    ]

    service_count = len(re.findall(r"^  [a-zA-Z0-9_-]+:", read_text(repo / "docker-compose.yml"), flags=re.MULTILINE))

    return {
        "release_candidate": True,
        "target_repository": {
            "path": str(repo),
            "commit": git_commit(repo),
            "release_id": release_id,
            "detected_services": service_count,
        },
        "architecture": {
            "marker_assessments": marker_assessments,
            "release_compatibility_declaration": {
                "exists": has_compatibility_declaration,
                "baseline_version": baseline,
                "approved": False,
                "declaration_id": "",
            },
            "solution_baseline": {
                "exists": has_release_baseline,
                "baseline_id": baseline,
                "version": baseline,
            },
            "compatibility_evidence": {
                "exists": bool(compatibility_refs),
                "evidence_refs": compatibility_refs,
            },
            "security_evidence": {
                "exists": bool(security_refs),
                "evidence_refs": security_refs,
            },
            "deployment_evidence": {
                "exists": bool(deployment_evidence_refs),
                "evidence_refs": deployment_evidence_refs,
            },
            "exceptions": [],
        },
    }


def main() -> int:
    parser = ArgumentParser(description="Collect architecture release-readiness input from a target repository.")
    parser.add_argument("--repo", required=True, help="Target repository path")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--release-id", default="demo-release-candidate", help="Release candidate identifier")
    parser.add_argument("--baseline", default="demo-solution-baseline", help="Expected solution baseline")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    if not repo.exists():
        raise SystemExit(f"Target repository does not exist: {repo}")

    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = collect(repo, args.release_id, args.baseline)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print(f"Generated {output}")
    print(f"- target repo: {repo}")
    print(f"- marker assessments: {len(payload['architecture']['marker_assessments'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
