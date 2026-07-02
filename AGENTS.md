# Agent Instructions

## Purpose

This file gives Codex and other AI agents the minimum operating context for this repository.

This repository is a governance-as-code engine. Treat it as a controlled governance system, not as a generic documentation repository.

## Repository Mission

The repository translates governance source documents into:

- structured DevSecOps control models
- structured architecture runtime governance models
- OPA policy-as-code
- JSON schemas
- released baselines
- generated reports
- downstream result intake indexes
- a static governance status viewer

The current demo target is `joku-dev/ha-CPsWMS`.

## Source Of Truth

Prefer these sources when changing behavior:

| Area | Primary files |
|---|---|
| Source documents | `docs/governance/source-documents/` |
| Source document intake | `model/documents/source-document-register.yaml`, `docs/governance/governance-change-lifecycle.md` |
| DevSecOps controls | `model/controls/` |
| Platform mapping | `model/platform/`, `model/traceability/` |
| Architecture governance | `architecture/` |
| OPA policies | `policies/opa/` |
| Schemas | `schemas/` |
| Result indexes | `status/` |
| Release packages | `releases/` and `docs/releases/` |
| Viewer | `generated/viewer/status-viewer.html` |
| AI navigation | `docs/ai-index.md` |

Generated reports under `generated/` should normally be updated by scripts, not by manual editing, except for narrowly scoped timestamp cleanup after validation noise.

## Current Released Baselines

| Domain | Baseline |
|---|---|
| DevSecOps L1 | `l1-baseline-v1.1.3` |
| Architecture L1 | `architecture-baseline-l1-v0.1.0` |

Do not silently change released baseline packages or tags. If a baseline changes, create an explicit new release or release-candidate flow.

## Current Demo State

The `ha-CPsWMS` mainline demo state is:

| Domain | Status | Baseline | Run |
|---|---|---|---|
| DevSecOps | `pass` | `l1-baseline-v1.1.3` | `28592257991` |
| Architecture | `PASS` | `architecture-baseline-l1-v0.1.0` | `28592256765` |

Use `docs/demo-end-to-end-governance.md` as the primary demo runbook.

## Required Validation

Before committing governance behavior, schemas, generated reports, viewer data, or docs that describe current results, run:

```bash
python3 scripts/validate_runtime_governance.py
python3 scripts/validate_governance_repo.py
python3 -m unittest discover -s tests
```

For very small documentation-only changes, the same validation is still preferred because docs and generated indexes are tightly connected in this repo.

## Commit And Push Practice

The maintainer preference is:

1. Make one coherent change.
2. Validate it.
3. Commit it.
4. Push it.
5. Report the commit hash.

Keep commits focused. Do not mix unrelated generated output, local OS files, and source changes.

## Files To Avoid Committing

Never add local OS or editor artifacts, especially:

```text
.DS_Store
docs/.DS_Store
docs/governance/.DS_Store
```

If they are present as untracked files, leave them alone unless explicitly asked to remove them.

## Report-Only Versus Blocking

The current demo should remain report-only unless explicitly changed.

- Report-only means findings are visible in reports, artifacts, indexes and the viewer.
- Blocking means the workflow fails on findings.

DevSecOps supports manual mode selection. Architecture is currently demonstrated as report-only and can be hardened later by enabling fail-on-findings in consuming workflows.

## Safe Change Rules

- Do not rewrite source document history casually.
- Do not modify released baseline packages unless creating an intentional release update.
- Do not change OPA enforcement behavior without updating docs and tests.
- Do not change schemas without validating existing examples and generated results.
- Do not edit status indexes by hand when an intake or generator script should be used.
- Do not delete historical status results unless explicitly requested.
- Preserve source-document lineage when adding new governance artifacts.

## Useful Starting Points

Read these first for most future work:

```text
docs/ai-index.md
docs/official-entrypoints.md
docs/governance/governance-change-lifecycle.md
docs/demo-end-to-end-governance.md
docs/operations/governance-result-intake-and-viewer-usage.md
docs/releases/index.md
generated/reports/source-lineage-report.md
```
