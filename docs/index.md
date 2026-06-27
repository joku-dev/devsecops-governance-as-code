# DevSecOps Governance as Code

This documentation space separates governance content into a few clear areas so teams can find the right entry point quickly.

## Start Here

- If you want the official entrypoint overview, read `official-entrypoints.md`.
- If you are new, begin with `onboarding/application-repo-onboarding.md`.
- If you want the operational flow, read `operations/beginner-step-by-step-operations-guide.md`.
- If you want the documentation publishing flow, read `operations/mkdocs-and-github-pages-step-by-step.md`.
- If you want the governance logic, read `governance/policy-directive-baseline-verification-and-governance-as-code-explained.md`.
- If you want the platform relationship, read `platform/control-baseline-and-platform-architecture-relationship-explained.md`.

## Documentation Areas

- `governance/` explains Policy, Directive, source-of-truth, and governance operating model.
- `onboarding/` explains how application repositories consume this baseline.
- `operations/` explains validation, generation, and day-to-day usage.
- `platform/` explains how platform architecture implements baseline controls.
- `pipeline-baseline/` is the intended home for reusable CI/CD baseline guidance.
- `releases/` is the intended home for published baseline package documentation.

## Repository Model

- `model/` is the machine-readable governance source of truth.
- `generated/` contains rendered documents, reports, and the static status viewer.
- `policies/opa/` contains executable policy rules for automated checks.
- `.github/workflows/` contains repo validation and reusable pipeline workflow automation.
