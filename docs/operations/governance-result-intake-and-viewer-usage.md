# Governance Result Intake And Viewer Usage

## Purpose

This guide explains two operational capabilities of this repository:

1. how to create normalized governance result snapshots for downstream repositories
2. how the status viewer distinguishes `main` results from branch or pull-request results

## Part 1: Result Intake

### Goal

The goal of result intake is to convert a successful downstream governance run into a standardized JSON snapshot under:

- `status/results/`

This keeps downstream evidence history:

- Git-tracked
- comparable across repositories
- reusable for the central viewer

## Intake Script

Use:

```bash
python3 scripts/intake_governance_result.py
```

## What The Script Produces

The script writes one normalized file to:

```text
status/results/<owner>__<repo>/<timestamp>-run-<run-id>.json
```

## Example

```bash
python3 scripts/intake_governance_result.py \
  --repository-id joku-dev/ha-CPsWMS \
  --baseline-level L1 \
  --governance-baseline-ref l1-baseline-v1.1.2 \
  --pipeline-name "DevSecOps Baseline" \
  --pipeline-run-id 28293749755 \
  --pipeline-url https://github.com/joku-dev/ha-CPsWMS/actions/runs/28293749755 \
  --pipeline-event push \
  --pipeline-status success \
  --branch main \
  --branch-protected true \
  --commit-id a7c0f5beef39405887a0caaac23fa785147151b9 \
  --baseline-gate-status success \
  --ci-status success \
  --governance-control-evaluation-status success \
  --governance-control-report true \
  --governance-run-input true \
  --static-analysis-summary true \
  --traceability-mapping true \
  --operations-evidence true \
  --overall-status pass \
  --control-evaluation-summary-file generated/control-evaluation-report.json \
  --notes "Full structured L1 coverage reached on main."
```

## Recommended Intake Rule

Use the script for:

- successful `main` runs
- important PR or branch runs that show meaningful governance improvement

Do not use it for:

- broken experiments
- partial local tests without a real pipeline run
- duplicate snapshots without new information

## Part 2: Viewer Usage

## Mainline Versus Branch Results

The viewer now distinguishes between:

- `mainline`
- `branch`
- `manual`

Meaning:

- `mainline` means the recorded run belongs to a `push` event on the repository's `main` branch
- `branch` means the recorded run belongs to a feature branch or PR flow
- `manual` means the recorded run was started through `workflow_dispatch`

This matters because:

- `mainline` is the official operational state
- `branch` shows improvement work in progress
- `manual` shows diagnostic checks without replacing the official push-based mainline state

## Latest Result Rule

The repository results index intentionally keeps:

- `latest_result` = latest `main` `push` result if one exists

This prevents a feature-branch result from replacing the official mainline state.

It also prevents a manual diagnostic run from replacing the official push-based operational state.

At the same time:

- branch, PR, and manual runs still remain visible in `history`

## How To Refresh The Viewer

After adding or updating result snapshots, run:

```bash
python3 scripts/generate_repository_results_index.py
python3 scripts/generate_status_viewer.py
```

## Recommended Workflow

Use this order:

1. record the downstream result with `scripts/intake_governance_result.py`
2. regenerate `status/repository-results-index.json`
3. regenerate `generated/viewer/status-viewer.html`
4. validate the governance repository
5. commit the updated result and viewer state

## Practical Benefit

With this model, the viewer can now show:

- official operational `main` status
- branch-level improvement runs
- coverage trends over time
- baseline version changes across runs
