# Source of Truth Decision Record

## Current State

The current authoritative content exists in DOCX documents:

- `docs/governance/source-documents/DevSecOps-Control-Baseline-Standard_aligned_with_Platform_Levels.docx`
- `docs/governance/source-documents/DevSecOps-Platform-Reference-Architecture-Standard_aligned_with_Control_Baseline.docx`

The repository now also contains working draft representations for:

- `docs/governance/devsecops-policy.md`
- `docs/governance/devsecops-directive.md`

These are not yet the formal master documents, but they allow the repository to model governance intent and execution semantics above the standards layer.

## Pilot Decision

For the pilot, the structured YAML files should become the working governance data model. The DOCX documents remain comparison and review inputs.

## Target Decision

After the pilot, the organization should decide whether:

1. DOCX remains the formal master and YAML is generated or manually synchronized.
2. YAML becomes the formal master and DOCX/PDF are generated outputs.
3. A BMS system remains the formal master and YAML is synchronized through a controlled export/import process.

## Recommendation

For DevSecOps and Software Defined Defence, option 2 is the strongest long-term model:

> Structured governance data is the master source. Documents, traceability matrices, policy rules, and evidence dashboards are generated views.

This enables stronger consistency between standards, platform capabilities, pipeline enforcement, and audit evidence.
