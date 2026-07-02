# Demo: ha-CPsWMS Architecture Runtime Governance

## Purpose

This document is the architecture-specific companion to the full end-to-end demo runbook:

```text
docs/demo-end-to-end-governance.md
```

Use this document when the demo audience wants to go deeper into the architecture runtime governance part only.

## Current Demo State

| Field | Value |
|---|---|
| Application repository | `joku-dev/ha-CPsWMS` |
| Application branch | `main` |
| Architecture governance baseline | `architecture-baseline-l1-v0.1.0` |
| Solution baseline | `ha-CPsWMS-demo-baseline` |
| Latest mainline run | `28592256765` |
| Latest mainline commit | `4a86f0c5b3d7aa1883533fa787530a1f5ff886e7` |
| Generated | `2026-07-02T13:05:12Z` |
| Current result | `PASS`, `4/4 gates`, `0 findings` |

Interpretation:

- The architecture checks are demo-ready on mainline.
- The checks are currently used report-only for the demo.
- A `PASS` means the current evidence satisfies the released L1 architecture governance checks. It is not a formal production approval.

## Demo Flow

1. Show the source architecture framework document.
2. Show the machine-readable architecture addendum.
3. Show the released architecture baseline.
4. Show the app repository evidence.
5. Show the GitHub Actions run.
6. Show the viewer result.
7. Explain what would create findings.

## Source-To-Runtime Mapping

Start with:

```text
docs/governance/source-documents/SDD_Architecture_Governance_Framework_20260630v2.md
```

Then show the derived runtime governance artifacts:

```text
architecture/quality-markers.yaml
architecture/guardrails.yaml
architecture/review-gates.yaml
architecture/arch-l1.yaml
architecture/arch-l2.yaml
architecture/arch-l3.yaml
architecture/arch-gov.yaml
policies/opa/architecture_readiness.rego
policies/opa/architecture_integration_readiness.rego
policies/opa/architecture_operation_readiness.rego
policies/opa/architecture_release_readiness.rego
schemas/architecture-release-candidate.schema.json
```

Why:

- The original framework remains the human governance reference.
- The YAML, schemas and OPA policies are the machine-readable runtime addendum.
- The addendum allows CI/CD to evaluate architecture evidence repeatably.

## Released Baseline

Open:

```text
docs/releases/architecture-baseline-l1-v0.1.0.md
docs/releases/architecture-baseline-l1-v0.1.0-release-statement.md
releases/architecture/l1/v0.1.0/baseline-package.md
releases/architecture/l1/v0.1.0/release-metadata.json
```

Explain:

- `architecture-baseline-l1-v0.1.0` is the released governance baseline.
- `ha-CPsWMS-demo-baseline` is the solution/product baseline supplied by the application evidence.
- The app workflow should report the governance baseline as `architecture-baseline-l1-v0.1.0` and keep the solution baseline inside the collected release input.

## Application Evidence

In the application repository:

```bash
cd /workspace/ha-CPsWMS
find .governance/architecture -maxdepth 2 -type f | sort
```

Expected evidence areas:

```text
.governance/architecture/solution-baseline.json
.governance/architecture/release-compatibility-declaration.json
.governance/architecture/security-evidence.json
.governance/architecture/resilience-evidence.json
.governance/architecture/operation-evidence.json
.governance/architecture/feedback-evidence.json
```

Why:

- The app repository owns product evidence.
- The governance repository owns reusable policy logic.
- Findings should be resolved by improving evidence or approved exceptions, not by changing policy logic for one application.

## Local Reproduction

Generate architecture release input:

```bash
cd /workspace/devsecops-governance-as-code
python3 scripts/collect_architecture_release_input.py \
  --repo /workspace/ha-CPsWMS \
  --output generated/demo/ha-cpswms-architecture-release-input.json \
  --release-id ha-CPsWMS-demo \
  --baseline ha-CPsWMS-demo-baseline
```

Generate the architecture governance report:

```bash
python3 scripts/generate_architecture_governance_report.py \
  --input generated/demo/ha-cpswms-architecture-release-input.json \
  --output-json generated/demo/ha-cpswms-architecture-governance-report.json \
  --output-md generated/demo/ha-cpswms-architecture-governance-report.md
```

Expected current gate summary:

| Gate | Status | Findings |
|---|---:|---:|
| Architecture Readiness | `PASS` | `0` |
| Integration Readiness | `PASS` | `0` |
| Operation Readiness | `PASS` | `0` |
| Release Readiness | `PASS` | `0` |

## GitHub Actions Result

Current known-good architecture run:

```text
https://github.com/joku-dev/ha-CPsWMS/actions/runs/28592256765
```

Expected interpretation:

- The workflow ran on `main`.
- The result was ingested by the governance repository.
- The viewer shows this as the latest architecture result for `joku-dev/ha-CPsWMS`.

## Viewer

Open:

```text
http://localhost:8000/status-viewer.html
```

Show:

- Latest Architecture Results
- Runtime Governance
- Runtime Governance Artifacts
- Source Lineage Report

Expected current viewer values:

| Viewer value | Expected |
|---|---|
| Repository | `joku-dev/ha-CPsWMS` |
| Status | `PASS` |
| Baseline | `architecture-baseline-l1-v0.1.0` |
| Last Mainline Run | `28592256765` |
| Summary | `4/4 gates pass`, `0 findings` |

## What Would Produce Findings

Findings are generated by OPA `deny` rules when required evidence is missing or too weak.

Examples:

| Situation | Expected effect |
|---|---|
| Missing solution baseline | Release readiness finding |
| Missing release compatibility declaration | Release readiness finding |
| Missing runtime evidence | Operation readiness finding |
| Missing interface or schema evidence | Integration readiness finding |
| Expired architecture exception | Finding instead of accepted exception |

In report-only mode, these findings are visible in the report, GitHub Actions summary, artifacts and viewer. Blocking behavior is an enforcement choice that can be enabled later without changing the basic evidence model.

## Demo Message

The architecture framework has been moved into the same operating model as the DevSecOps controls:

1. Human source document.
2. Machine-readable markers and levels.
3. OPA policies.
4. Released baseline.
5. Application evidence.
6. GitHub Actions execution.
7. Governance repository intake.
8. Viewer status.

This is the bridge from document-oriented architecture governance to runtime governance as code.
