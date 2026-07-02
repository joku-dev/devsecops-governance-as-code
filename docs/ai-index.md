# AI Index

## Purpose

This index helps AI agents and human maintainers find the right files before changing the repository.

Use it as the first navigation point after `AGENTS.md`.

## Fast Orientation

| Need | Read first |
|---|---|
| Understand the repository | `README.md`, `docs/official-entrypoints.md` |
| Run the live demo | `docs/demo-end-to-end-governance.md` |
| Understand current ha-CPsWMS status | `docs/operations/ha-cpswms-governance-validation-status.md`, `docs/ha-cpswms-architecture-governance-results.md` |
| Understand source-document lineage | `generated/reports/source-lineage-report.md` |
| Intake updated input documents | `docs/governance/governance-change-lifecycle.md`, `model/documents/source-document-register.yaml` |
| Understand DevSecOps baseline releases | `docs/releases/index.md`, `docs/releases/l1-baseline-v1.1.3.md` |
| Understand architecture baseline releases | `docs/releases/architecture-baseline-l1-v0.1.0.md` |
| Understand intake and viewer | `docs/operations/governance-result-intake-and-viewer-usage.md` |
| Understand report-only versus blocking | `docs/operations/operational-governance-enforcement-options.md` |
| Work as an AI agent | `AGENTS.md`, `docs/operations/ai-working-rules.md` |

## Source Documents

The source documents live in:

```text
docs/governance/source-documents/
```

Current source documents:

| Source document | Main derived area |
|---|---|
| `DevSecOps-Control-Baseline-Standard_aligned_with_Platform_Levels.docx` | DevSecOps controls and OPA policy candidates |
| `DevSecOps-Platform-Reference-Architecture-Standard_aligned_with_Control_Baseline.docx` | Platform levels and pipeline baseline |
| `DevSecOps_Directive_Version_0_draft1.docx` | Governance directive |
| `DevSecOps_Policy_Version_1_draft3.docx` | Governance policy |
| `SDD_Architecture_Governance_Framework_20260630v2.md` | Architecture runtime governance |

When adding or changing derived governance artifacts, update or validate lineage:

```bash
python3 scripts/generate_source_lineage_report.py
python3 scripts/validate_governance_repo.py
```

Use the lifecycle and template for future updates:

```text
docs/governance/governance-change-lifecycle.md
docs/governance/change-requests/TEMPLATE.md
model/documents/source-document-register.yaml
```

## DevSecOps Governance Map

| Concern | Files |
|---|---|
| Controls | `model/controls/dscb-l1.yaml`, `model/controls/dscb-l2.yaml`, `model/controls/dscb-l3.yaml`, `model/controls/dscb-gov.yaml` |
| Coverage | `model/controls/control-coverage.yaml`, `generated/reports/control-coverage-report.md` |
| Evidence | `model/evidence/evidence-types.yaml`, `docs/operations/governance-evidence-contract.md` |
| Pipeline placement | `pipeline-baseline/` |
| OPA policies | `policies/opa/*` |
| Current release | `releases/l1/v1.1.3/`, `docs/releases/l1-baseline-v1.1.3.md` |
| Reusable workflow | `.github/workflows/devsecops-baseline-l1-v1.1.3.yml` |

Typical validation:

```bash
python3 scripts/validate_governance_repo.py
python3 -m unittest discover -s tests
```

## Architecture Runtime Governance Map

| Concern | Files |
|---|---|
| Runtime addendum | `docs/runtime-governance-addendum.md` |
| Levels | `architecture/arch-l1.yaml`, `architecture/arch-l2.yaml`, `architecture/arch-l3.yaml`, `architecture/arch-gov.yaml` |
| Markers | `architecture/quality-markers.yaml` |
| Guardrails and gates | `architecture/guardrails.yaml`, `architecture/review-gates.yaml` |
| Remediation | `architecture/remediation-actions.yaml` |
| OPA policies | `policies/opa/architecture_*.rego` |
| Schemas | `schemas/architecture-release-candidate.schema.json`, `schemas/app-architecture-evidence.schema.json` |
| Current release | `releases/architecture/l1/v0.1.0/`, `docs/releases/architecture-baseline-l1-v0.1.0.md` |
| Reusable workflow | `.github/workflows/architecture-baseline-l1-v0.1.0.yml` |

Typical validation:

```bash
python3 scripts/validate_runtime_governance.py
python3 -m unittest discover -s tests
```

## Viewer And Status Map

| Concern | Files |
|---|---|
| DevSecOps result index | `status/repository-results-index.json` |
| DevSecOps result history | `status/results/` |
| Architecture result index | `status/architecture-results-index.json` |
| Architecture result history | `status/architecture-results/` |
| Viewer generator | `scripts/generate_status_viewer.py` |
| Viewer output | `generated/viewer/status-viewer.html` |
| Intake docs | `docs/operations/governance-result-intake-and-viewer-usage.md` |

Regenerate viewer:

```bash
python3 scripts/generate_status_viewer.py
```

## Demo Map

| Demo need | File |
|---|---|
| Full end-to-end demo | `docs/demo-end-to-end-governance.md` |
| Architecture-only demo | `docs/demo-ha-cpswms-runtime-governance.md` |
| Architecture result explanation | `docs/ha-cpswms-architecture-governance-results.md` |
| DevSecOps historical demo guide | `docs/operations/demo-guide-2026-07-02-ha-cpswms.md` |
| Viewer | `generated/viewer/status-viewer.html` |

Current known-good ha-CPsWMS runs:

| Domain | Run | Expected |
|---|---:|---|
| DevSecOps Baseline | `28592257991` | pass, `16/16` controls |
| Architecture Runtime Governance | `28592256765` | PASS, `4/4` gates |

## Release Map

| Domain | Current release | Key files |
|---|---|---|
| DevSecOps L1 | `l1-baseline-v1.1.3` | `docs/releases/l1-baseline-v1.1.3.md`, `releases/l1/v1.1.3/` |
| Architecture L1 | `architecture-baseline-l1-v0.1.0` | `docs/releases/architecture-baseline-l1-v0.1.0.md`, `releases/architecture/l1/v0.1.0/` |

When creating a new release, update:

- release docs
- technical release package
- checksums
- reusable workflow or template if applicable
- source lineage
- README and official entrypoints if the release becomes the recommended baseline

## Before Committing

Run:

```bash
python3 scripts/validate_runtime_governance.py
python3 scripts/validate_governance_repo.py
python3 -m unittest discover -s tests
git status --short
```

Commit only intentional files. Do not add `.DS_Store`.
