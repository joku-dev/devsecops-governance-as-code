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


def html_table_with_row_attrs(headers: list[str], rows: list[dict]) -> str:
    thead = "".join(f"<th>{escape(header)}</th>" for header in headers)
    body_rows = []
    for row in rows:
        attrs = " ".join(f'{escape(key)}="{escape(value)}"' for key, value in row.get("attrs", {}).items())
        attr_text = f" {attrs}" if attrs else ""
        cells = "".join(f"<td>{cell}</td>" for cell in row["cells"])
        body_rows.append(f"<tr{attr_text}>{cells}</tr>")
    return (
        "<table>"
        f"<thead><tr>{thead}</tr></thead>"
        f"<tbody>{''.join(body_rows)}</tbody>"
        "</table>"
    )


def badge(text: str, tone: str) -> str:
    return f'<span class="badge {tone}">{escape(text)}</span>'


def first_non_empty(*values: str) -> str:
    for value in values:
        if value:
            return value
    return ""


def summarize_control_delta(current_summary: dict, previous_summary: dict | None) -> str:
    if not current_summary:
        return "No structured control summary"
    if not previous_summary:
        return "First structured control summary"

    pass_delta = current_summary.get("pass", 0) - previous_summary.get("pass", 0)
    fail_delta = current_summary.get("fail", 0) - previous_summary.get("fail", 0)
    not_tested_delta = current_summary.get("not_tested", 0) - previous_summary.get("not_tested", 0)
    return (
        f"Δ pass {pass_delta:+d}, "
        f"Δ fail {fail_delta:+d}, "
        f"Δ not_tested {not_tested_delta:+d}"
    )


def short_sha(value: str) -> str:
    if not value or value == "unknown":
        return "unknown"
    return value[:12]


def format_control_summary(summary: dict) -> str:
    if not summary:
        return "No structured summary"
    passed = summary.get("pass", 0)
    failed = summary.get("fail", 0)
    not_tested = summary.get("not_tested", 0)
    applicable = summary.get("applicable_controls", 0)
    return f"{passed}/{failed}/{not_tested} pass/fail/not tested · {applicable} applicable"


def run_link(run_id: str, url: str) -> str:
    run_text = escape(run_id or "unknown")
    if not url:
        return f"<code>{run_text}</code>"
    return f'<a href="{escape(url)}"><code>{run_text}</code></a>'


def build_latest_repository_cards(results_index: dict) -> str:
    cards = []
    for repository in results_index.get("repositories", []):
        repo_id = repository.get("repository_id", "unknown")
        latest = repository.get("latest_result", {})
        history = repository.get("history", [])
        latest_history = next(
            (
                entry
                for entry in reversed(history)
                if entry.get("pipeline_run_id") == latest.get("pipeline_run_id")
            ),
            {},
        )
        summary = latest.get("control_evaluation_summary", {})
        status = latest.get("status", "unknown")
        status_tone = "ok" if status == "pass" else "danger"
        run_id = latest.get("pipeline_run_id", "unknown")
        run_url = latest_history.get("pipeline_url", "")
        baseline = latest.get("governance_baseline_ref", "unknown")
        generated_at = latest.get("generated_at", "unknown")
        commit_id = latest.get("commit_id", "unknown")
        summary_class = "ok" if summary.get("fail", 0) == 0 and summary.get("not_tested", 0) == 0 else "warn"
        cards.append(
            "<section class=\"latest-card\">"
            "<div class=\"latest-card-header\">"
            f"<div><h3>{escape(repo_id)}</h3><p>Mainline governance status</p></div>"
            f"{badge(status, status_tone)}"
            "</div>"
            "<dl class=\"latest-grid\">"
            f"<div><dt>Baseline</dt><dd><code>{escape(baseline)}</code></dd></div>"
            f"<div><dt>Last Main Run</dt><dd>{run_link(run_id, run_url)}</dd></div>"
            f"<div><dt>Commit</dt><dd><code>{escape(short_sha(commit_id))}</code></dd></div>"
            f"<div><dt>Generated</dt><dd>{escape(generated_at)}</dd></div>"
            "</dl>"
            f"<div class=\"control-score {summary_class}\">"
            f"<strong>{escape(format_control_summary(summary))}</strong>"
            "<span>Control summary</span>"
            "</div>"
            "</section>"
        )
    if not cards:
        return ""
    return (
        "<section class=\"latest-results\">"
        "<div class=\"section-heading\">"
        "<h2>Latest Repository Results</h2>"
        "<p>Official latest main push result per downstream repository.</p>"
        "</div>"
        "<div class=\"latest-grid-cards\">"
        + "".join(cards)
        + "</div>"
        "</section>"
    )


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
    mainline_results = results_summary.get("mainline_results", 0)
    branch_results = results_summary.get("branch_results", 0)
    manual_results = results_summary.get("manual_results", 0)
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
        (
            "Run Mix",
            str(mainline_results),
            f"Mainline push runs, branch/PR: {branch_results}, manual: {manual_results}",
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


def build_control_report_cards(control_report: dict | None) -> str:
    if not control_report:
        return ""
    summary = control_report.get("summary", {})
    cards = [
        ("Evaluated Controls", str(summary.get("tested_controls", 0)), f"Applicable: {summary.get('applicable_controls', 0)}"),
        ("Control Failures", str(summary.get("fail", 0)), f"Passed: {summary.get('pass', 0)}"),
        ("Untested Controls", str(summary.get("not_tested", 0)), f"Not applicable: {summary.get('not_applicable', 0)}"),
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


def build_control_coverage_cards(control_coverage: dict | None) -> str:
    if not control_coverage:
        return ""
    summary = control_coverage.get("summary", {})
    counts = summary.get("automation_status_counts", {})
    cards = [
        ("Automated Controls", str(counts.get("automated", 0)), f"Planned: {counts.get('planned', 0)}"),
        ("Manual Controls", str(counts.get("manual", 0)), f"Not applicable: {counts.get('not_applicable', 0)}"),
        ("Planned Controls", str(summary.get("planned_controls", 0)), "Priority backlog"),
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


def build_repository_history_rows(results_index: dict) -> list[list[str]]:
    rows = []
    for repository in results_index.get("repositories", []):
        history = repository.get("history", [])
        for index in range(len(history) - 1, -1, -1):
            entry = history[index]
            current_summary = entry.get("control_evaluation_summary", {})
            previous_summary = None
            for older_index in range(index - 1, -1, -1):
                candidate = history[older_index].get("control_evaluation_summary", {})
                if candidate:
                    previous_summary = candidate
                    break

            status_tone = "ok" if entry.get("status") == "pass" else "danger"
            branch_name = entry.get("branch", "unknown")
            pipeline_event = entry.get("pipeline_event", "unknown")
            if pipeline_event == "workflow_dispatch":
                scope = "manual"
                scope_tone = "plain"
            else:
                scope = "mainline" if branch_name == "main" else "branch"
                scope_tone = "ok" if scope == "mainline" else "warn"
            tested_controls = current_summary.get("tested_controls")
            pass_controls = current_summary.get("pass")
            fail_controls = current_summary.get("fail")
            not_tested_controls = current_summary.get("not_tested")
            coverage_text = (
                f"{pass_controls}/{tested_controls} pass, {fail_controls} fail, {not_tested_controls} not_tested"
                if current_summary
                else "No structured control summary"
            )
            rows.append(
                [
                    f"<code>{escape(repository.get('repository_id', 'unknown'))}</code>",
                    escape(entry.get("generated_at", "")),
                    badge(scope, scope_tone),
                    badge(entry.get("status", "unknown"), status_tone),
                    f"<code>{escape(entry.get('governance_baseline_ref', 'unknown'))}</code>",
                    escape(branch_name),
                    run_link(entry.get("pipeline_run_id", "unknown"), entry.get("pipeline_url", "")),
                    coverage_text,
                    summarize_control_delta(current_summary, previous_summary),
                ]
            )
    return rows


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
    control_report_path = ROOT / "generated" / "control-evaluation-report.json"
    control_report = load_json(control_report_path) if control_report_path.exists() else None
    control_coverage_path = ROOT / "generated" / "reports" / "control-coverage-report.json"
    control_coverage = load_json(control_coverage_path) if control_coverage_path.exists() else None
    latest_result_with_summary = None
    for repository in results_index.get("repositories", []):
        latest_summary = repository.get("latest_result", {}).get("control_evaluation_summary", {})
        if latest_summary:
            latest_result_with_summary = repository.get("latest_result", {})
            break
    control_summary_source = latest_result_with_summary.get("control_evaluation_summary") if latest_result_with_summary else None
    control_cards_source = {"summary": control_summary_source} if control_summary_source else control_report

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

    control_coverage_rows = []
    if control_coverage:
        for row in control_coverage.get("controls", []):
            tone = {
                "automated": "ok",
                "manual": "plain",
                "planned": "warn",
                "not_applicable": "plain",
            }.get(row["automation_status"], "plain")
            control_coverage_rows.append(
                [
                    f"<code>{escape(row['control_id'])}</code>",
                    f"<code>{escape(row['level'])}</code>",
                    badge(row["automation_status"], tone),
                    badge(row["priority"], "warn" if row["priority"] != "low" else "plain"),
                    escape(row["next_action"]),
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
        latest_branch_result = None
        for history_entry in reversed(repository.get("history", [])):
            if history_entry.get("branch") != "main":
                latest_branch_result = history_entry
                break
        tone = "ok" if latest_result.get("status") == "pass" and integration.get("status") == "operational" else "warn"
        notes = integration.get("notes") or f"Latest mainline commit {latest_result.get('commit_id', 'unknown')} evaluated at {latest_result.get('generated_at', 'unknown')}."
        if latest_branch_result:
            notes += (
                f" Latest branch/PR run: {latest_branch_result.get('pipeline_run_id', 'unknown')}"
                f" on {latest_branch_result.get('branch', 'unknown')}"
                f" with coverage "
                f"{latest_branch_result.get('control_evaluation_summary', {}).get('pass', 'n/a')}/"
                f"{latest_branch_result.get('control_evaluation_summary', {}).get('tested_controls', 'n/a')} pass."
            )
        integration_rows.append(
            [
                f"<code>{escape(repo_id)}</code>",
                badge(integration.get("baseline_level", repository.get("baseline_level", "unknown")), "plain"),
                badge(integration.get("status", latest_result.get("status", "unknown")), tone),
                escape(integration.get("pipeline_result", latest_result.get("status", "unknown"))),
                f"<code>{escape(latest_result.get('governance_baseline_ref', integration.get('governance_workflow_ref', 'unknown')))}</code>",
                f"<code>{escape(latest_result.get('pipeline_run_id', integration.get('pipeline_run_id', 'unknown')))}</code>",
                escape(notes),
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
            "repository_result_history_entries": sum(len(repository.get("history", [])) for repository in results_index.get("repositories", [])),
            "mainline_history_entries": sum(
                1
                for repository in results_index.get("repositories", [])
                for entry in repository.get("history", [])
                if entry.get("branch") == "main" and entry.get("pipeline_event") == "push"
            ),
            "branch_history_entries": sum(
                1
                for repository in results_index.get("repositories", [])
                for entry in repository.get("history", [])
                if entry.get("branch") != "main"
            ),
            "manual_history_entries": sum(
                1
                for repository in results_index.get("repositories", [])
                for entry in repository.get("history", [])
                if entry.get("pipeline_event") == "workflow_dispatch"
            ),
    }
    if control_cards_source:
        payload["control_evaluation_summary"] = control_cards_source.get("summary", {})

    control_rows = []
    if control_report:
        status_order = {"fail": 0, "pass": 1, "not_tested": 2, "not_applicable": 3}
        sorted_controls = sorted(
            control_report.get("controls", []),
            key=lambda item: (status_order.get(item["status"], 9), item["control_id"]),
        )
        for control in sorted_controls[:20]:
            tone = {"pass": "ok", "fail": "danger", "not_tested": "warn", "not_applicable": "plain"}.get(control["status"], "plain")
            control_rows.append(
                {
                    "attrs": {
                        "data-control-row": "true",
                        "data-status": control["status"],
                        "data-control-id": control["control_id"],
                    },
                    "cells": [
                        f"<code>{escape(control['control_id'])}</code>",
                        f"<code>{escape(control['level'])}</code>",
                        escape(control["verification_method"]),
                        badge(control["status"], tone),
                        escape(control["message"]),
                    ],
                }
            )
    control_cards_html = f"<section class=\"cards\">{build_control_report_cards(control_cards_source)}</section>" if control_cards_source else ""
    coverage_cards_html = f"<section class=\"cards\">{build_control_coverage_cards(control_coverage)}</section>" if control_coverage else ""
    control_snapshot_html = (
        "<section class=\"panel\"><h2>Latest Control Evaluation Snapshot</h2>"
        "<div class=\"filters\">"
        "<label for=\"control-status-filter\">Status</label>"
        "<select id=\"control-status-filter\">"
        "<option value=\"all\">All</option>"
        "<option value=\"fail\">Fail</option>"
        "<option value=\"pass\">Pass</option>"
        "<option value=\"not_tested\">Not tested</option>"
        "<option value=\"not_applicable\">Not applicable</option>"
        "</select>"
        "<label for=\"control-search-filter\">Search</label>"
        "<input id=\"control-search-filter\" type=\"search\" placeholder=\"DSCB-L1-REQ-003 or artifact\" />"
        "</div>"
        + html_table_with_row_attrs(["Control", "Level", "Method", "Status", "Message"], control_rows)
        + "<p id=\"control-filter-summary\" class=\"filter-summary\"></p>"
        + "</section>"
        if control_rows
        else ""
    )
    repository_history_rows = build_repository_history_rows(results_index)
    history_panel_html = (
        "<section class=\"panel history-compact\">"
        "<h2>Repository Result History</h2>"
        "<p class=\"filter-summary\">Compact run history with baseline evolution, linked run IDs, and control summary deltas.</p>"
        + html_table(
            ["Repository", "Generated At", "Scope", "Status", "Baseline Ref", "Branch", "Run ID", "Coverage", "Trend"],
            repository_history_rows,
        )
        + "</section>"
        if repository_history_rows
        else ""
    )

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
    .latest-results {{ margin-bottom: 24px; }}
    .section-heading {{ display: flex; justify-content: space-between; gap: 16px; align-items: end; margin-bottom: 12px; }}
    .section-heading h2 {{ margin: 0; }}
    .section-heading p {{ margin: 0; color: var(--muted); }}
    .latest-grid-cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 16px; }}
    .latest-card {{ background: var(--panel); border: 1px solid var(--border); border-radius: 14px; padding: 20px; box-shadow: 0 10px 26px rgba(13, 79, 108, 0.08); }}
    .latest-card-header {{ display: flex; justify-content: space-between; gap: 16px; align-items: start; margin-bottom: 16px; }}
    .latest-card h3 {{ margin: 0 0 4px; font-size: 1.25rem; }}
    .latest-card p {{ margin: 0; color: var(--muted); }}
    .latest-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; margin: 0 0 16px; }}
    .latest-grid div {{ min-width: 0; }}
    .latest-grid dt {{ color: var(--muted); font-size: 0.78rem; text-transform: uppercase; }}
    .latest-grid dd {{ margin: 4px 0 0; overflow-wrap: anywhere; }}
    .control-score {{ border-radius: 10px; padding: 12px; display: flex; justify-content: space-between; gap: 12px; align-items: center; }}
    .control-score.ok {{ background: var(--ok); }}
    .control-score.warn {{ background: var(--warn); }}
    .control-score span {{ color: var(--muted); font-size: 0.9rem; }}
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
    .filters {{ display: flex; flex-wrap: wrap; gap: 10px; align-items: center; margin-bottom: 14px; }}
    .filters label {{ font-size: 0.9rem; color: var(--muted); }}
    .filters select, .filters input {{ padding: 0.45rem 0.6rem; border: 1px solid var(--border); border-radius: 8px; font: inherit; }}
    .filters input {{ min-width: 240px; }}
    .filter-summary {{ margin: 10px 0 0; color: var(--muted); font-size: 0.9rem; }}
    .history-compact table {{ font-size: 0.92rem; }}
    .history-compact th, .history-compact td {{ padding: 8px 7px; }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    @media (max-width: 700px) {{
      main {{ padding: 16px; }}
      .latest-grid-cards {{ grid-template-columns: 1fr; }}
      .latest-grid {{ grid-template-columns: 1fr; }}
      .section-heading {{ display: block; }}
      table {{ display: block; overflow-x: auto; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>Governance Status Viewer</h1>
    <p class="meta">Static snapshot of repository health, governance document status, traceability coverage, and open gaps.</p>
  </header>
  <main>
    {build_latest_repository_cards(results_index)}
    <section class="cards">
      {build_operational_cards(integration_status, results_index)}
    </section>
    <section class="cards">
      {build_summary_cards(documents, gaps, controls)}
    </section>
    {control_cards_html}
    {coverage_cards_html}
    <section class="panel">
      <h2>Artifacts</h2>
      <ul class="artifact-list">
        <li><a href="../reports/open-gap-report.md">Open Gap Report</a></li>
        <li><a href="../reports/document-control-matrix.md">Document To Control Matrix</a></li>
        <li><a href="../reports/control-coverage-report.md">Control Coverage Report</a></li>
        <li><a href="../documents/devsecops-pol-001.html">Rendered Policy</a></li>
        <li><a href="../documents/devsecops-dir-001.html">Rendered Directive</a></li>
        <li><a href="../control-evaluation-report.json">Control Evaluation Report JSON</a></li>
        <li><a href="../control-evaluation-report.md">Control Evaluation Report Markdown</a></li>
        <li><a href="../../operations/current-governance-platform-state/">Current Governance Platform State</a></li>
        <li><a href="../../operations/ha-cpswms-governance-validation-status/">ha-CPsWMS Validation Status</a></li>
        <li><a href="../../releases/l1-baseline-v1.1.3/">L1 Baseline v1.1.3</a></li>
        <li><a href="../../releases/l1-baseline-v1.1.3-release-statement/">L1 Release Statement</a></li>
        <li><a href="../../onboarding/how-other-repos-use-this-governance-repo/">Integration Guide</a></li>
        <li><a href="../../governance/policy-directive-baseline-verification-and-governance-as-code-explained/">Governance Relationship Explanation</a></li>
      </ul>
    </section>
    <section class="panels">
      <section class="panel">
        <h2>Operational Integration Status</h2>
        {html_table(["Repository", "Level", "Status", "Pipeline Result", "Workflow Ref", "Run ID", "Notes"], integration_rows)}
      </section>
      {history_panel_html}
      {control_snapshot_html}
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
        <h2>Control Automation Coverage</h2>
        {html_table(["Control", "Level", "Automation Status", "Priority", "Next Action"], control_coverage_rows)}
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
  <script>
    (() => {{
      const statusFilter = document.getElementById('control-status-filter');
      const searchFilter = document.getElementById('control-search-filter');
      const summary = document.getElementById('control-filter-summary');
      const rows = Array.from(document.querySelectorAll('tr[data-control-row="true"]'));
      if (!statusFilter || !searchFilter || !summary || rows.length === 0) {{
        return;
      }}
      const applyFilters = () => {{
        const status = statusFilter.value;
        const query = searchFilter.value.trim().toLowerCase();
        let visible = 0;
        for (const row of rows) {{
          const rowStatus = row.dataset.status || '';
          const text = row.textContent.toLowerCase();
          const statusMatch = status === 'all' || rowStatus === status;
          const queryMatch = query === '' || text.includes(query);
          const show = statusMatch && queryMatch;
          row.style.display = show ? '' : 'none';
          if (show) {{
            visible += 1;
          }}
        }}
        summary.textContent = `${{visible}} of ${{rows.length}} controls shown`;
      }};
      statusFilter.addEventListener('change', applyFilters);
      searchFilter.addEventListener('input', applyFilters);
      applyFilters();
    }})();
  </script>
</body>
</html>
"""

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
