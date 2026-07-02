# DevSecOps Governance as Code

This repository is the starting structure for transforming the DevSecOps Control Baseline and DevSecOps Platform Reference Architecture into a Doc-as-Code and Policy-as-Code operating model.

## Purpose

The repository separates four concerns:

| Area | Purpose |
|---|---|
| `docs/source-documents` | Approved or working DOCX source documents brought into the repository for traceable migration. |
| `controls` | Structured DevSecOps control baseline requirements. |
| `platform` | Platform Reference Architecture levels and platform capabilities. |
| `traceability` | Mapping between controls, platform capabilities, evidence, and policy candidates. |
| `policies/opa` | Executable policy-as-code rules for automated checks. |
| `evidence` | Evidence type definitions expected from pipelines and platforms. |
| `waivers` | Waiver model and approval authority structure. |
| `schemas` | JSON Schemas for validating structured governance data. |
| `generated` | Generated DOCX, PDF, HTML, and XLSX outputs. |
| `architecture` | Runtime governance addendum data derived from the SDD Architecture Governance Framework. |

## Target Model

The long-term target is that structured sources become the controlled master data for DevSecOps governance. Word and PDF remain important output formats for BMS, reviews, and audits, but they should be generated from the structured source where feasible.

```mermaid
flowchart TD
    A["Control Library YAML"] --> B["Generated Word/PDF"]
    A --> C["Traceability Matrix"]
    A --> D["Policy-as-Code Rules"]
    D --> E["CI/CD and Platform Checks"]
    E --> F["Machine Evidence"]
```

## Initial Scope

The initial scope is based on:

- DevSecOps Control Baseline Standard aligned with Platform Levels
- DevSecOps Platform Reference Architecture Standard aligned with Control Baseline

The first implementation should focus on:

- Level 1 controls as complete structured data
- Platform Reference Architecture levels 1 to 3
- Traceability from control requirement to platform capability and expected evidence
- Initial automated checks for branch protection, SBOM, vulnerability evidence, artifact integrity, dependency source control, IaC, and waiver validity

## Runtime Governance Addendum

The repository now includes a first runtime governance addendum for the SDD Architecture Governance Framework:

- `docs/runtime-governance-addendum.md`
- `architecture/quality-markers.yaml`
- `architecture/guardrails.yaml`
- `architecture/review-gates.yaml`
- `architecture/arch-l1.yaml`
- `architecture/arch-l2.yaml`
- `architecture/arch-l3.yaml`
- `architecture/arch-gov.yaml`
- `policies/opa/architecture_readiness.rego`
- `policies/opa/architecture_integration_readiness.rego`
- `policies/opa/architecture_release_readiness.rego`

The addendum keeps the original framework document as the normative reference and adds machine-readable marker, guardrail, gate and policy artifacts for executable governance.

## Recommended Workflow

1. Maintain structured control and platform data in YAML.
2. Validate YAML against JSON Schemas.
3. Generate traceability views and documents from YAML.
4. Implement policy-as-code only for controls that can be objectively checked.
5. Store generated evidence from pipelines and platform checks.
6. Use waivers only as controlled, time-limited exceptions.

## Local Commands

Validate repository consistency:

```bash
python scripts/validate_governance_repo.py
```

Generate the first traceability CSV:

```bash
python scripts/generate_traceability_csv.py
```

Generate Policy/Directive governance traceability:

```bash
python scripts/generate_governance_traceability_csv.py
```

Generate the automation coverage report:

```bash
python scripts/generate_automation_report.py
```

Generate the CI/CD pipeline baseline report:

```bash
python scripts/generate_pipeline_baseline_report.py
```

Generate the architecture runtime traceability CSV:

```bash
python3 scripts/generate_architecture_traceability_csv.py
```

Validate the runtime governance addendum:

```bash
python3 scripts/validate_runtime_governance.py
```

Generate a demo architecture release-readiness input for `ha-CPsWMS`:

```bash
python3 scripts/collect_architecture_release_input.py \
  --repo /workspace/ha-CPsWMS \
  --output generated/demo/ha-cpswms-architecture-release-input.json \
  --release-id ha-CPsWMS-demo \
  --baseline ha-CPsWMS-demo-baseline
```

## Important Principle

Not every requirement should become executable policy. Some requirements are governance obligations, some are evidence obligations, and some are enforceable technical gates. The repository keeps these concerns connected but distinct.
