# Operational Governance Enforcement Options

## Goal

If this repository becomes the enterprise governance baseline, other software repositories must not only know about it, but must actually use it in their CI/CD pipelines.

## Recommended Enforcement Layers

### 1. Shared Pipeline Template

The strongest operational pattern is to provide a central CI template and require teams to import it.

Examples:

- `templates/ci/github-actions-governance-check.yml`
- `templates/ci/gitlab-ci-governance-check.yml`

### 2. Standardized Compliance Artifact

Each target repository should produce a machine-readable result file such as:

- `governance-compliance-result.json`

The schema for that result is defined in:

- `schemas/governance-compliance-result.schema.json`

An example is provided in:

- `docs/governance-compliance-result.example.json`
- `docs/governance-compliance-result.extended.example.json`

An extended result can be generated with:

```bash
python3 scripts/generate_governance_compliance_result.py \
  --target-repo /path/to/target-repo \
  --input-file /path/to/release-candidate.json \
  --output-file governance-compliance-result.json
```

### 3. Integration Scanner

This repository provides a scanner script that can check whether a target repository appears to use the governance pipeline integration:

```bash
python3 scripts/check_repo_governance_integration.py \
  --target-repo /path/to/target-repo \
  --output-file governance-compliance-result.json
```

### 4. Required Status Checks

If GitHub or GitLab is used, the governance job should be configured as a required merge condition.

That means:

- no merge to `main` without a successful governance check
- no silent bypass of the governance stage

## Practical Rollout Sequence

1. publish the central pipeline template
2. make target repositories consume the template
3. make target repositories produce a standardized compliance result
4. make the governance check a required merge gate
5. later build central compliance monitoring across repositories
