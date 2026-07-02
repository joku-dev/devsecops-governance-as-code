# Demo: ha-CPsWMS Architecture Runtime Governance

## Purpose

This demo shows how the governance repository can evaluate architecture runtime governance evidence from a real target repository.

Target repository:

```text
/workspace/ha-CPsWMS
```

The demo does not require changing the target repository. The governance repository reads observable signals such as architecture documentation, deployment documentation, Dockerfiles, schemas, tests and benchmark reports, then generates a policy input for architecture release readiness.

## Demo Flow

1. Collect architecture release-readiness input from `ha-CPsWMS`.
2. Validate the generated JSON against the architecture release candidate schema.
3. Run the OPA architecture release-readiness policy.
4. Review the governance findings.

## Generate Input

```bash
python3 scripts/collect_architecture_release_input.py \
  --repo /workspace/ha-CPsWMS \
  --output generated/demo/ha-cpswms-architecture-release-input.json \
  --release-id ha-CPsWMS-demo \
  --baseline ha-CPsWMS-demo-baseline
```

Generated file:

```text
generated/demo/ha-cpswms-architecture-release-input.json
```

## Validate Input Schema

```bash
python3 - <<'PY'
from pathlib import Path
import json
import jsonschema

schema = json.loads(Path("schemas/architecture-release-candidate.schema.json").read_text())
data = json.loads(Path("generated/demo/ha-cpswms-architecture-release-input.json").read_text())
jsonschema.validate(data, schema)
print("ha-CPsWMS architecture input validates against schema")
PY
```

## Run OPA Release Readiness

Architecture readiness:

```bash
opa eval \
  --data policies/opa/architecture_readiness.rego \
  --input generated/demo/ha-cpswms-architecture-release-input.json \
  'data.architecture.readiness.deny'
```

Current expected result: no findings. The target repository has enough architecture documentation, component structure and deployment/process evidence to pass the initial architecture-readiness gate.

Integration readiness:

```bash
opa eval \
  --data policies/opa/architecture_integration_readiness.rego \
  --input generated/demo/ha-cpswms-architecture-release-input.json \
  'data.architecture.integration_readiness.deny'
```

Current expected result: no findings. The target repository has enough interface, schema, test and deployment evidence to pass the initial integration-readiness gate.

Operation readiness:

```bash
opa eval \
  --data policies/opa/architecture_operation_readiness.rego \
  --input generated/demo/ha-cpswms-architecture-release-input.json \
  'data.architecture.operation_readiness.deny'
```

Current expected result: findings. Runtime and feedback evidence can be detected, but the operation-readiness markers are not yet verified at score 4.

Release readiness:

```bash
opa eval \
  --data policies/opa/architecture_release_readiness.rego \
  --input generated/demo/ha-cpswms-architecture-release-input.json \
  'data.architecture.release_readiness.deny'
```

## Current Demo Findings

The current `ha-CPsWMS` demo input is expected to pass architecture readiness and integration readiness, then produce release-readiness findings. That is useful for the demo because it shows staged governance: a repository can be good enough to continue architecture and integration work, but not yet ready for governed release.

Expected finding categories:

| Area | Why it is flagged |
|---|---|
| Release compatibility declaration | No explicit approved release compatibility declaration is detected. |
| Solution baseline | No explicit solution baseline artifact is detected. |
| Security markers | Security notes exist, but stronger verified security evidence is not detected. |
| Resilience markers | Deployment restart behavior exists, but verified resilience or degraded-mode evidence is not detected. |
| Release architecture markers | Architecture and deployment evidence exist, but release baseline and compatibility evidence are incomplete. |
| Operation readiness | Runtime and feedback evidence exist, but observability and feedback-loop maturity are not verified at score 4. |

## Demo Message

The governance repository can now show three things:

1. Architecture governance concepts from the SDD framework are represented as machine-readable markers, guardrails and levels.
2. A target repository can be converted into a release-readiness policy input.
3. OPA can produce concrete, reviewable architecture governance findings.

This is the bridge from document-based governance to runtime governance as code.
