# Governance Change Impact Report

Generated: `2026-07-02T16:47:09Z`

## Inputs

- Source document register: `model/documents/source-document-register.yaml`
- Source lineage report: `generated/reports/source-lineage-report.json`

## Summary

- Registered source documents: `5`
- Source documents with lineage: `5`
- Derived artifact links: `84`

## Domain Coverage

| Domain | Source documents |
|---|---:|
| `architecture` | `1` |
| `devsecops` | `4` |
| `directive` | `1` |
| `platform` | `1` |
| `policy` | `1` |

## Release Considerations

| Consideration | Source documents |
|---|---:|
| `baseline_release_review` | `2` |
| `no_release_by_default` | `3` |

## Review Lanes

| Review lane | Source documents |
|---|---:|
| `architecture-review` | `1` |
| `devsecops-review` | `4` |
| `governance-review` | `2` |
| `platform-review` | `1` |
| `policy-as-code-review` | `2` |
| `release-review` | `2` |
| `schema-review` | `1` |
| `viewer-status-review` | `2` |

## Source Impact Details

### `DEVSECOPS-POL-SRC-001`

- Title: DevSecOps Policy Version 1 draft 3
- Source: `docs/governance/source-documents/DevSecOps_Policy_Version_1_draft3.docx`
- Status: `draft`
- Owner: `governance-owners`
- Version: `1 draft 3`
- Domains: `policy, devsecops`
- Lineage artifacts: `5`
- Release consideration: `no_release_by_default`
- Review lanes: `devsecops-review, governance-review`

Derived artifact areas:

- `docs/governance/devsecops-policy.md`
- `model/documents/governance-documents.yaml`
- `model/traceability/document-to-control.yaml`

Suggested validation:

- `python3 -m unittest discover -s tests`
- `python3 scripts/validate_governance_repo.py`

Representative artifacts:

- `docs/governance/devsecops-policy.md`
- `generated/reports/governance-change-impact.json`
- `generated/reports/governance-change-impact.md`
- `model/documents/source-document-register.yaml`
- `model/traceability/document-to-control.yaml`

### `DEVSECOPS-DIR-SRC-001`

- Title: DevSecOps Directive Version 0 draft 1
- Source: `docs/governance/source-documents/DevSecOps_Directive_Version_0_draft1.docx`
- Status: `draft`
- Owner: `governance-owners`
- Version: `0 draft 1`
- Domains: `directive, devsecops`
- Lineage artifacts: `5`
- Release consideration: `no_release_by_default`
- Review lanes: `devsecops-review, governance-review`

Derived artifact areas:

- `docs/governance/devsecops-directive.md`
- `model/documents/governance-documents.yaml`
- `model/traceability/document-to-control.yaml`

Suggested validation:

- `python3 -m unittest discover -s tests`
- `python3 scripts/validate_governance_repo.py`

Representative artifacts:

- `docs/governance/devsecops-directive.md`
- `generated/reports/governance-change-impact.json`
- `generated/reports/governance-change-impact.md`
- `model/documents/source-document-register.yaml`
- `model/traceability/document-to-control.yaml`

### `DSCB-STD-SRC-001`

- Title: DevSecOps Control Baseline Standard aligned with Platform Levels
- Source: `docs/governance/source-documents/DevSecOps-Control-Baseline-Standard_aligned_with_Platform_Levels.docx`
- Status: `intake`
- Owner: `devsecops-owners`
- Version: `imported`
- Domains: `devsecops`
- Lineage artifacts: `25`
- Release consideration: `baseline_release_review`
- Review lanes: `devsecops-review, policy-as-code-review, release-review`

Derived artifact areas:

- `model/controls`
- `model/evidence`
- `policies/opa`
- `releases/l1`
- `generated/reports`

Suggested validation:

- `python3 -m unittest discover -s tests`
- `python3 scripts/validate_governance_repo.py`
- `verify release package metadata and checksums`

Representative artifacts:

- `docs/governance/source-documents/DevSecOps-Control-Baseline-Standard_aligned_with_Platform_Levels.docx`
- `generated/reports/governance-change-impact.json`
- `generated/reports/governance-change-impact.md`
- `model/controls/control-coverage.yaml`
- `model/controls/dscb-gov.yaml`
- `model/controls/dscb-l1.yaml`
- `model/controls/dscb-l2.yaml`
- `model/controls/dscb-l3.yaml`
- `model/documents/source-document-register.yaml`
- `model/evidence/evidence-types.yaml`

### `PRA-STD-SRC-001`

- Title: DevSecOps Platform Reference Architecture Standard aligned with Control Baseline
- Source: `docs/governance/source-documents/DevSecOps-Platform-Reference-Architecture-Standard_aligned_with_Control_Baseline.docx`
- Status: `intake`
- Owner: `platform-owners`
- Version: `imported`
- Domains: `platform, devsecops`
- Lineage artifacts: `21`
- Release consideration: `no_release_by_default`
- Review lanes: `devsecops-review, platform-review, viewer-status-review`

Derived artifact areas:

- `model/platform`
- `pipeline-baseline`
- `model/traceability`
- `generated/reports`
- `generated/viewer`

Suggested validation:

- `python3 -m unittest discover -s tests`
- `python3 scripts/generate_status_viewer.py`
- `python3 scripts/validate_governance_repo.py`

Representative artifacts:

- `docs/governance/source-documents/DevSecOps-Platform-Reference-Architecture-Standard_aligned_with_Control_Baseline.docx`
- `generated/reports/control-coverage-report.md`
- `generated/reports/document-control-matrix.md`
- `generated/reports/governance-change-impact.json`
- `generated/reports/governance-change-impact.md`
- `generated/viewer/status-viewer.html`
- `generated/xlsx/document_control_matrix.csv`
- `generated/xlsx/traceability_matrix.csv`
- `model/documents/source-document-register.yaml`
- `model/platform/platform-capabilities.yaml`

### `ARCH-SDD-SRC-001`

- Title: SDD Architecture Governance Framework
- Source: `docs/governance/source-documents/SDD_Architecture_Governance_Framework_20260630v2.md`
- Status: `intake`
- Owner: `architecture-owners`
- Version: `20260630v2`
- Domains: `architecture`
- Lineage artifacts: `28`
- Release consideration: `baseline_release_review`
- Review lanes: `architecture-review, policy-as-code-review, release-review, schema-review, viewer-status-review`

Derived artifact areas:

- `architecture`
- `policies/opa/architecture_*.rego`
- `schemas/architecture-*.json`
- `releases/architecture`
- `status/architecture-results-index.json`
- `generated/viewer`

Suggested validation:

- `python3 -m unittest discover -s tests`
- `python3 scripts/generate_status_viewer.py`
- `python3 scripts/validate_governance_repo.py`
- `python3 scripts/validate_runtime_governance.py`
- `verify release package metadata and checksums`

Representative artifacts:

- `architecture/arch-gov.yaml`
- `architecture/arch-l1.yaml`
- `architecture/arch-l2.yaml`
- `architecture/arch-l3.yaml`
- `architecture/guardrails.yaml`
- `architecture/quality-markers.yaml`
- `architecture/remediation-actions.yaml`
- `architecture/review-gates.yaml`
- `generated/csv/architecture_runtime_traceability.csv`
- `generated/reports/governance-change-impact.json`

## Open Questions For Change Requests

- Does the source document update change governance behavior or only explanatory text?
- Is the intended rollout report-only or blocking?
- Does the change require a release candidate or a new baseline release?
- Which downstream repositories need migration or communication?
