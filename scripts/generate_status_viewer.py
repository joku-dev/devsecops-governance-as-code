#!/usr/bin/env python3
"""Generate a static governance status viewer."""

from __future__ import annotations

from html import escape
from pathlib import Path
import csv
import json

import yaml


ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "model"
OUT = ROOT / "generated" / "viewer" / "status-viewer.html"


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_csv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def html_table(headers: list[str], rows: list[list[str]]) -> str:
    thead = "".join(f"<th>{escape(header)}</th>" for header in headers)
    body_rows = []
    for row in rows:
        body_rows.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>")
    return (
        "<table>"
        f"<thead><tr>{thead}</tr></thead>"
        f"<tbody>{''.join(body_rows)}</tbody>"
        "</table>"
    )


def badge(text: str, tone: str) -> str:
    return f'<span class="badge {tone}">{escape(text)}</span>'


def build_summary_cards(documents, gaps, controls):
    automated = sum(1 for control in controls if control.get("verification", {}).get("method") == "automated")
    policy_candidates = sum(1 for control in controls if control.get("policy_as_code", {}).get("candidate"))
    status_counts = {}
    for document in documents:
        status_counts[document["status"]] = status_counts.get(document["status"], 0) + 1
    gap_counts = {"high": 0, "medium": 0, "low": 0}
    for gap in gaps:
        gap_counts[gap["severity"]] = gap_counts.get(gap["severity"], 0) + 1

    cards = [
        ("Documents", str(len(documents)), f"Draft: {status_counts.get('draft', 0)}"),
        ("Controls", str(len(controls)), f"Automated: {automated}"),
        ("Policy Candidates", str(policy_candidates), f"Coverage: {policy_candidates}/{automated or 1} automated"),
        ("Open Gaps", str(len(gaps)), f"Medium: {gap_counts.get('medium', 0)}"),
    ]
    html = []
    for title, value, detail in cards:
        html.append(
            "<section class=\"card\">"
            f"<h3>{escape(title)}</h3>"
            f"<div class=\"value\">{escape(value)}</div>"
            f"<p>{escape(detail)}</p>"
            "</section>"
        )
    return "".join(html)


def build_operational_cards(integration_status: dict, results_index: dict) -> str:
    summary = integration_status.get("summary", {})
    results_summary = results_index.get("summary", {})
    baseline_refs = sorted(
        {
            repository.get("latest_result", {}).get("governance_baseline_ref")
            for repository in results_index.get("repositories", [])
            if repository.get("latest_result", {}).get("governance_baseline_ref")
        }
    )
    central_baseline = ", ".join(baseline_refs) if baseline_refs else summary.get("central_baseline_repository", "unknown")
    cards = [
        ("Operational State", str(summary.get("operational_state", "unknown")), f"Rollout: {summary.get('rollout_phase', 'unknown')}"),
        (
            "Integrated Repositories",
            str(results_summary.get("repository_count", summary.get("integrated_repositories", 0))),
            f"Passing results: {results_summary.get('passing_results', summary.get('successful_baseline_runs', 0))}",
        ),
        (
            "Central Baseline",
            "Active",
            str(central_baseline),
        ),
    ]
    html = []
    for title, value, detail in cards:
        html.append(
            "<section class=\"card\">"
            f"<h3>{escape(title)}</h3>"
            f"<div class=\"value\">{escape(value)}</div>"
            f"<p>{escape(detail)}</p>"
            "</section>"
        )
    return "".join(html)


def main() -> int:
    controls = []
    for path in sorted((MODEL / "controls").glob("dscb-*.yaml")):
        data = load_yaml(path)
        level = data.get("level")
        for requirement in data.get("requirements", []):
            controls.append({**requirement, "level": level})

    documents = load_yaml(MODEL / "documents" / "governance-documents.yaml").get("documents", [])
    gaps = load_csv(ROOT / "generated" / "xlsx" / "open_gap_report.csv")
    traceability_rows = load_csv(ROOT / "generated" / "xlsx" / "traceability_matrix.csv")
    document_rows = load_csv(ROOT / "generated" / "xlsx" / "document_control_matrix.csv")
    integration_status = load_yaml(ROOT / "status" / "application-repository-integrations.yaml")
    results_index = load_json(ROOT / "status" / "repository-results-index.json")

    document_table_rows = []
    for document in documents:
        tone = "warn" if document["status"] == "draft" else "ok"
        document_table_rows.append(
            [
                f"<code>{escape(document['id'])}</code>",
                escape(document["type"]),
                escape(document["title"]),
                badge(document["status"], tone),
                f"<code>{escape(document['repository_path'])}</code>",
            ]
        )

    gap_table_rows = []
    for gap in gaps[:15]:
        tone = {"high": "danger", "medium": "warn", "low": "ok"}[gap["severity"]]
        gap_table_rows.append(
            [
                f"<code>{escape(gap['gap_id'])}</code>",
                badge(gap["severity"], tone),
                escape(gap["category"]),
                f"<code>{escape(gap['subject'])}</code>",
                escape(gap["summary"]),
            ]
        )

    coverage_rows = []
    for row in traceability_rows[:20]:
        tone = "ok" if row["policy_candidate"] == "true" else "plain"
        coverage_rows.append(
            [
                f"<code>{escape(row['control_id'])}</code>",
                f"<code>{escape(row['level'])}</code>",
                escape(row["title"]),
                badge(row["policy_candidate"], tone),
                escape(row["authority_document_titles"]),
            ]
        )

    authority_rows = []
    for row in document_rows[:20]:
        authority_rows.append(
            [
                f"<code>{escape(row['document_id'])}</code>",
                escape(row["document_title"]),
                f"<code>{escape(row['control_id'])}</code>",
                escape(row["control_title"]),
                escape(row["rationale"]),
            ]
        )

    integration_lookup = {row["repository"]: row for row in integration_status.get("integrations", [])}
    integration_rows = []
    for repository in results_index.get("repositories", []):
        repo_id = repository.get("repository_id", "unknown")
        integration = integration_lookup.get(repo_id, {})
        latest_result = repository.get("latest_result", {})
        tone = "ok" if latest_result.get("status") == "pass" and integration.get("status") == "operational" else "warn"
        integration_rows.append(
            [
                f"<code>{escape(repo_id)}</code>",
                badge(integration.get("baseline_level", repository.get("baseline_level", "unknown")), "plain"),
                badge(integration.get("status", latest_result.get("status", "unknown")), tone),
                escape(integration.get("pipeline_result", latest_result.get("status", "unknown"))),
                f"<code>{escape(latest_result.get('governance_baseline_ref', integration.get('governance_workflow_ref', 'unknown')))}</code>",
                f"<code>{escape(latest_result.get('pipeline_run_id', integration.get('pipeline_run_id', 'unknown')))}</code>",
                escape(
                    integration.get("notes")
                    or f"Latest commit {latest_result.get('commit_id', 'unknown')} evaluated at {latest_result.get('generated_at', 'unknown')}."
                ),
            ]
        )
    for row in integration_status.get("integrations", []):
        if row["repository"] in {repository.get("repository_id") for repository in results_index.get("repositories", [])}:
            continue
        tone = "ok" if row.get("pipeline_result") == "success" and row.get("status") == "operational" else "warn"
        integration_rows.append(
            [
                f"<code>{escape(row['repository'])}</code>",
                badge(row.get("baseline_level", "unknown"), "plain"),
                badge(row.get("status", "unknown"), tone),
                escape(row.get("pipeline_result", "unknown")),
                f"<code>{escape(row.get('governance_workflow_ref', 'unknown'))}</code>",
                f"<code>{escape(row.get('pipeline_run_id', 'unknown'))}</code>",
                escape(row.get("notes", "")),
            ]
        )

    payload = {
        "documents": len(documents),
        "controls": len(controls),
        "gaps": len(gaps),
        "policy_candidates": sum(1 for control in controls if control.get("policy_as_code", {}).get("candidate")),
        "integrated_repositories": results_index.get("summary", {}).get(
            "repository_count", integration_status.get("summary", {}).get("integrated_repositories", 0)
        ),
        "successful_baseline_runs": results_index.get("summary", {}).get(
            "passing_results", integration_status.get("summary", {}).get("successful_baseline_runs", 0)
        ),
        "latest_governance_baselines": [
            repository.get("latest_result", {}).get("governance_baseline_ref")
            for repository in results_index.get("repositories", [])
            if repository.get("latest_result", {}).get("governance_baseline_ref")
        ],
    }

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Governance Status Viewer</title>
  <style>
    :root {{
      --bg: #f4f6f8;
      --panel: #ffffff;
      --ink: #1c2733;
      --muted: #5d6b7a;
      --accent: #0d4f6c;
      --ok: #e8f5e9;
      --warn: #fff4e5;
      --danger: #fdecea;
      --border: #d8e0e6;
    }}
    body {{ font-family: Arial, sans-serif; margin: 0; background: var(--bg); color: var(--ink); }}
    header {{ background: linear-gradient(120deg, #0d4f6c, #1f7a8c); color: white; padding: 32px; }}
    main {{ padding: 24px; max-width: 1280px; margin: 0 auto; }}
    .cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 24px; }}
    .card, .panel {{ background: var(--panel); border: 1px solid var(--border); border-radius: 14px; padding: 18px; box-shadow: 0 8px 20px rgba(13, 79, 108, 0.06); }}
    .card h3, .panel h2 {{ margin-top: 0; }}
    .value {{ font-size: 2rem; font-weight: 700; margin: 8px 0; }}
    .panels {{ display: grid; grid-template-columns: 1fr; gap: 18px; }}
    table {{ width: 100%; border-collapse: collapse; }}
    th, td {{ border-bottom: 1px solid var(--border); text-align: left; padding: 10px 8px; vertical-align: top; }}
    th {{ color: var(--muted); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.04em; }}
    code {{ background: #eef2f5; padding: 0.1rem 0.35rem; border-radius: 6px; }}
    .badge {{ display: inline-block; padding: 0.2rem 0.5rem; border-radius: 999px; font-size: 0.82rem; }}
    .badge.ok {{ background: var(--ok); }}
    .badge.warn {{ background: var(--warn); }}
    .badge.danger {{ background: var(--danger); }}
    .badge.plain {{ background: #eef2f5; }}
    .meta {{ color: rgba(255,255,255,0.85); }}
    .artifact-list a {{ color: var(--accent); text-decoration: none; }}
    .artifact-list li {{ margin: 0.35rem 0; }}
  </style>
</head>
<body>
  <header>
    <h1>Governance Status Viewer</h1>
    <p class="meta">Static snapshot of repository health, governance document status, traceability coverage, and open gaps.</p>
  </header>
  <main>
    <section class="cards">
      {build_operational_cards(integration_status, results_index)}
    </section>
    <section class="cards">
      {build_summary_cards(documents, gaps, controls)}
    </section>
    <section class="panel">
      <h2>Artifacts</h2>
      <ul class="artifact-list">
        <li><a href="../reports/open-gap-report.md">Open Gap Report</a></li>
        <li><a href="../reports/document-control-matrix.md">Document To Control Matrix</a></li>
        <li><a href="../documents/devsecops-pol-001.html">Rendered Policy</a></li>
        <li><a href="../documents/devsecops-dir-001.html">Rendered Directive</a></li>
        <li><a href="../../docs/operations/current-governance-platform-state.md">Current Governance Platform State</a></li>
        <li><a href="../../docs/operations/ha-cpswms-governance-validation-status.md">ha-CPsWMS Validation Status</a></li>
        <li><a href="../../docs/releases/l1-baseline-v1.0.0.md">L1 Baseline v1.0.0</a></li>
        <li><a href="../../docs/releases/l1-baseline-v1.0.0-release-statement.md">L1 Release Statement</a></li>
        <li><a href="../../docs/onboarding/how-other-repos-use-this-governance-repo.md">Integration Guide</a></li>
        <li><a href="../../docs/governance/policy-directive-baseline-verification-and-governance-as-code-explained.md">Governance Relationship Explanation</a></li>
      </ul>
    </section>
    <section class="panels">
      <section class="panel">
        <h2>Operational Integration Status</h2>
        {html_table(["Repository", "Level", "Status", "Pipeline Result", "Workflow Ref", "Run ID", "Notes"], integration_rows)}
      </section>
      <section class="panel">
        <h2>Governance Documents</h2>
        {html_table(["ID", "Type", "Title", "Status", "Source"], document_table_rows)}
      </section>
      <section class="panel">
        <h2>Top Open Gaps</h2>
        {html_table(["Gap", "Severity", "Category", "Subject", "Summary"], gap_table_rows)}
      </section>
      <section class="panel">
        <h2>Policy Coverage Snapshot</h2>
        {html_table(["Control", "Level", "Title", "Policy Candidate", "Authority Documents"], coverage_rows)}
      </section>
      <section class="panel">
        <h2>Authority Mapping Snapshot</h2>
        {html_table(["Document", "Title", "Control", "Control Title", "Rationale"], authority_rows)}
      </section>
      <section class="panel">
        <h2>Machine Summary</h2>
        <pre>{escape(json.dumps(payload, indent=2))}</pre>
      </section>
    </section>
  </main>
</body>
</html>
"""

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
