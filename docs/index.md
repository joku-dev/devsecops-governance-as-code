# DevSecOps Governance as Code

This documentation space separates governance content into a few clear areas so teams can find the right entry point quickly.

## Start Here

- If you want the official entrypoint overview, read `official-entrypoints.md`.
- If you are new, begin with `onboarding/application-repo-onboarding.md`.
- If you want the operational flow, read `operations/beginner-step-by-step-operations-guide.md`.
- If you want the downstream evidence contract, read `operations/governance-evidence-contract.md`.
- If you want to record downstream runs and understand the viewer, read `operations/governance-result-intake-and-viewer-usage.md`.
- If you want the current overall situation, read `operations/current-governance-platform-state.md`.
- If you want a concrete rollout retrospective, read `operations/ha-cpswms-governance-lessons-learned.md`.
- If you want the documentation publishing flow, read `operations/mkdocs-and-github-pages-step-by-step.md`.
- If you want the governance logic, read `governance/policy-directive-baseline-verification-and-governance-as-code-explained.md`.
- If you want the platform relationship, read `platform/control-baseline-and-platform-architecture-relationship-explained.md`.

## Documentation Areas

- `governance/` explains Policy, Directive, source-of-truth, and governance operating model.
- `onboarding/` explains how application repositories consume this baseline.
- `operations/` explains validation, generation, and day-to-day usage.
- `platform/` explains how platform architecture implements baseline controls.
- `pipeline-baseline/` contains reusable CI/CD baseline guidance and related release-facing workflow documentation.
- `releases/` contains published baseline package documentation.

## Repository Model

- `model/` is the machine-readable governance source of truth.
- `generated/` contains rendered documents, reports, and the static status viewer.
- `policies/opa/` contains executable policy rules for automated checks.
- `.github/workflows/` contains repo validation and reusable pipeline workflow automation.
