# End-to-End Governance Demo

## Purpose

This demo shows how the governance repository can be used to evaluate a real application repository against two governance domains:

1. Architecture Runtime Governance
2. DevSecOps Release Governance

The target application repository is:

```text
/workspace/ha-CPsWMS
```

The governance repository is:

```text
/workspace/devsecops-governance-as-code
```

## Demo Message

The demo story is:

> Governance is no longer only a document or review meeting. The application repository provides machine-readable evidence. The governance repository collects that evidence, evaluates policy-as-code rules, and generates reports that show whether the repository is ready from an architecture and DevSecOps perspective.

The important point is not only that the final result is green. The important point is that findings can be traced back to missing or immature evidence, and that adding approved evidence changes the governance result.

## Repositories And Branches

Use these branches for the demo:

| Repository | Branch | Purpose |
|---|---|---|
| `devsecops-governance-as-code` | `codex/runtime-governance-addendum` | Contains policies, collectors, schemas, reports and templates. |
| `ha-CPsWMS` | `codex/architecture-governance-workflow` | Contains GitHub Actions workflows and application evidence. |

Why this matters:

- The governance repository is the reusable governance engine.
- The application repository remains the source of product evidence.
- The app repo does not copy policy logic; it references the governance repo.

## Prerequisites

Required local tools:

```bash
python3
opa
git
```

Optional but useful:

```bash
gh
```

Check the tools:

```bash
python3 --version
opa version
git --version
```

## Step 1: Validate The Governance Repository

Run this in the governance repository:

```bash
cd /workspace/devsecops-governance-as-code
python3 scripts/validate_runtime_governance.py
python3 scripts/validate_governance_repo.py
```

Why:

- `validate_runtime_governance.py` checks the architecture runtime governance model, schemas, marker catalogue, generated reports and OPA policies.
- `validate_governance_repo.py` checks the existing DevSecOps control baseline, traceability, pipeline placement and governance requirements.

Expected result:

```text
Runtime governance validation passed
Validation passed
```

Interpretation:

- The governance repository itself is internally consistent.
- This does not validate the application repository yet.

## Step 2: Inspect Application Evidence

Run this in the application repository:

```bash
cd /workspace/ha-CPsWMS
find .governance -maxdepth 4 -type f | sort
```

Expected architecture evidence:

```text
.governance/architecture/feedback-evidence.json
.governance/architecture/operation-evidence.json
.governance/architecture/release-compatibility-declaration.json
.governance/architecture/resilience-evidence.json
.governance/architecture/security-evidence.json
.governance/architecture/solution-baseline.json
```

Expected DevSecOps evidence:

```text
.governance/devsecops/release-evidence.json
```

Why:

- These files are the machine-readable evidence supplied by the application repository.
- They represent baseline, compatibility, security, resilience, runtime, feedback and DevSecOps release evidence.

Interpretation:

- If these files are missing, the governance checks still run, but they should produce findings.
- If the files exist and are approved, the collector can treat them as verified evidence.

## Step 3: Generate Architecture Governance Input

Run this in the governance repository:

```bash
cd /workspace/devsecops-governance-as-code
python3 scripts/collect_architecture_release_input.py \
  --repo /workspace/ha-CPsWMS \
  --output generated/demo/ha-cpswms-architecture-release-input.json \
  --release-id ha-CPsWMS-demo \
  --baseline ha-CPsWMS-demo-baseline
```

Why:

- This converts observable repository evidence into a policy input JSON.
- It reads application documents, schemas, deployment files, benchmark reports and `.governance/architecture/*.json`.

Generated output:

```text
generated/demo/ha-cpswms-architecture-release-input.json
```

Interpretation:

- This file is the machine-readable architecture governance input.
- It contains marker assessments, evidence links, baseline information, compatibility declaration, runtime evidence and exceptions.

## Step 4: Generate Architecture Governance Report

Run:

```bash
python3 scripts/generate_architecture_governance_report.py \
  --input generated/demo/ha-cpswms-architecture-release-input.json \
  --output-json generated/demo/ha-cpswms-architecture-governance-report.json \
  --output-md generated/demo/ha-cpswms-architecture-governance-report.md
```

Why:

- This evaluates all architecture OPA gates.
- It generates both machine-readable JSON and human-readable Markdown.

The architecture gates are:

| Gate | Meaning |
|---|---|
| Architecture Readiness | Is minimum architecture evidence present and owned? |
| Integration Readiness | Are interfaces, data, tests and deployment evidence sufficient? |
| Operation Readiness | Is runtime and feedback evidence mature enough? |
| Release Readiness | Is architecture evidence sufficient for governed release? |

View the report:

```bash
sed -n '1,160p' generated/demo/ha-cpswms-architecture-governance-report.md
```

Expected result:

```text
Architecture Readiness | PASS | 0
Integration Readiness  | PASS | 0
Operation Readiness    | PASS | 0
Release Readiness      | PASS | 0
```

Interpretation:

- The application repository currently satisfies the demo architecture governance gates.
- This means approved architecture evidence is present and accepted by the current policies.
- It does not mean formal certification; it means the current governance-as-code checks pass.

## Step 5: Generate DevSecOps Governance Input

Run:

```bash
python3 scripts/collect_devsecops_release_input.py \
  --repo /workspace/ha-CPsWMS \
  --output generated/demo/ha-cpswms-devsecops-release-input.json \
  --release-id ha-CPsWMS-demo
```

Why:

- This converts application DevSecOps evidence into a policy input JSON.
- It reads `.governance/devsecops/release-evidence.json`, CI workflow evidence, dependency files and deployment/IaC signals.

Generated output:

```text
generated/demo/ha-cpswms-devsecops-release-input.json
```

Interpretation:

- This file is the machine-readable DevSecOps governance input.
- It contains branch/review posture, SBOM evidence, vulnerability scan evidence, artifact integrity evidence, dependency source approval, IaC presence and pipeline security gate state.

## Step 6: Generate DevSecOps Governance Report

Run:

```bash
python3 scripts/generate_devsecops_governance_report.py \
  --input generated/demo/ha-cpswms-devsecops-release-input.json \
  --output-json generated/demo/ha-cpswms-devsecops-governance-report.json \
  --output-md generated/demo/ha-cpswms-devsecops-governance-report.md
```

View the report:

```bash
sed -n '1,120p' generated/demo/ha-cpswms-devsecops-governance-report.md
```

Expected result:

```text
DevSecOps Release Readiness | PASS | 0
```

Interpretation:

- The app repository currently satisfies the demo DevSecOps release governance gate.
- The result depends on approved DevSecOps evidence in `.governance/devsecops/release-evidence.json`.
- The local command is report-only by default. Add `--fail-on-findings` when a manual run should behave as a blocking gate.

## Step 7: Generate Combined End-To-End Report

Run:

```bash
python3 scripts/generate_end_to_end_governance_report.py \
  --architecture-json generated/demo/ha-cpswms-architecture-governance-report.json \
  --devsecops-json generated/demo/ha-cpswms-devsecops-governance-report.json \
  --output-json generated/demo/ha-cpswms-end-to-end-governance-report.json \
  --output-md generated/demo/ha-cpswms-end-to-end-governance-report.md
```

View the report:

```bash
sed -n '1,180p' generated/demo/ha-cpswms-end-to-end-governance-report.md
```

Expected result:

```text
Architecture Runtime Governance | PASS | 0
DevSecOps Governance            | PASS | 0
Overall                         | PASS | 0
```

Interpretation:

- The demo target passes both governance domains.
- The result is supported by machine-readable evidence in the application repository.
- The governance repository produces repeatable evidence, policy output and reports.

## Step 8: Run GitHub Actions In The App Repo

In GitHub, open the `ha-CPsWMS` repository on branch:

```text
codex/architecture-governance-workflow
```

Run these workflows manually:

```text
Architecture Runtime Governance
DevSecOps Governance
```

Why:

- This shows that the same checks work in CI, not only locally.
- The application repository checks out the governance repository as tooling.

Expected GitHub Actions outputs:

| Workflow | Expected step summary |
|---|---|
| Architecture Runtime Governance | Architecture gates all PASS |
| DevSecOps Governance | DevSecOps Release Readiness PASS |

Expected artifacts:

```text
architecture-governance-evidence
devsecops-governance-evidence
```

Interpretation:

- The application repository can run governance checks without copying the governance policy logic.
- Governance logic remains centrally maintained in the governance repository.
- Evidence remains close to the application repository.

## Before / After Demo Option

To show the value more clearly, demonstrate two states:

### Before

Temporarily remove or rename:

```text
/workspace/ha-CPsWMS/.governance/architecture
/workspace/ha-CPsWMS/.governance/devsecops
```

Then rerun the collectors and reports.

Expected result:

- Architecture has operation/release findings.
- DevSecOps has release findings.

### After

Restore the `.governance` folders and rerun the collectors and reports.

Expected result:

- Architecture PASS
- DevSecOps PASS
- Overall PASS

Interpretation:

- Governance findings are not arbitrary.
- Findings disappear when the application repository provides approved, machine-readable evidence.
- This demonstrates a practical path from document-based governance to runtime governance as code.

## What The Demo Proves

The demo proves that:

1. Governance requirements can be represented as structured data and OPA policies.
2. Application repositories can provide evidence in a repeatable format.
3. Collectors can translate repository state into policy input.
4. OPA can evaluate architecture and DevSecOps readiness.
5. Reports can be generated for humans and machines.
6. GitHub Actions can run the same process in CI.

## What The Demo Does Not Yet Prove

The demo does not yet prove:

- formal production approval
- complete security certification
- full compliance with every enterprise process
- real SBOM/vulnerability tool integration
- real artifact signing infrastructure
- live operational monitoring integration

These are future hardening steps. The demo shows the operating model and the technical governance loop.

## Troubleshooting

### OPA Not Found

Install OPA or use the GitHub Actions workflow, which installs OPA automatically.

### Schema Validation Fails

Check that evidence files follow:

```text
schemas/app-architecture-evidence.schema.json
schemas/app-devsecops-evidence.schema.json
schemas/architecture-release-candidate.schema.json
```

### Architecture Findings Remain

Open:

```text
generated/demo/ha-cpswms-architecture-governance-report.md
```

Read the finding and recommended action. Then update the relevant file under:

```text
/workspace/ha-CPsWMS/.governance/architecture/
```

### DevSecOps Findings Remain

Open:

```text
generated/demo/ha-cpswms-devsecops-governance-report.md
```

Then update:

```text
/workspace/ha-CPsWMS/.governance/devsecops/release-evidence.json
```

### GitHub Actions Cannot Checkout Governance Repo

Check the workflow uses the correct governance repository and branch:

```text
joku-dev/devsecops-governance-as-code
codex/runtime-governance-addendum
```

For production usage, replace the branch with a version tag or pinned commit SHA.
