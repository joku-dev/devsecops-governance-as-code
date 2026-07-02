# Architecture Runtime Governance Report

## Target

- Repository: `/workspace/ha-CPsWMS`
- Commit: `3babb93`
- Release ID: `ha-CPsWMS-demo`
- Detected services: `5`

## Gate Summary

| Gate | Status | Findings |
|---|---:|---:|
| Architecture Readiness | PASS | 0 |
| Integration Readiness | PASS | 0 |
| Operation Readiness | FINDINGS | 2 |
| Release Readiness | FINDINGS | 9 |

## Findings

### Architecture Readiness

No findings.

### Integration Readiness

No findings.

### Operation Readiness

- RG-OPERATION-READY: Operation-readiness marker B5 requires score 4 or a valid exception; current score is 3.
- RG-OPERATION-READY: Operation-readiness marker P11 requires score 4 or a valid exception; current score is 3.

Recommended actions:
- **Strengthen architecture feedback loop**: Link operational findings, demo findings or benchmark trends to owned improvement actions, technical debt items or architecture runway.
  Evidence: `operational_finding`, `improvement_backlog_item`, `technical_debt_item`
- **Verify observability evidence**: Add runtime metrics, health indicators, monitoring dashboard evidence or operational diagnostics that prove observability works.
  Evidence: `monitoring_dashboard`, `runtime_metric`, `health_indicator`

### Release Readiness

- RG-RELEASE-READY: Release candidate requires a release compatibility declaration.
- RG-RELEASE-READY: Release candidate requires a solution baseline.
- RG-RELEASE-READY: Release-critical architecture marker E6 requires score 4 or a valid exception; current score is 3.
- RG-RELEASE-READY: Release-critical architecture marker P10 requires score 4 or a valid exception; current score is 3.
- RG-RELEASE-READY: Release-critical architecture marker P13 requires score 4 or a valid exception; current score is 1.
- RG-RELEASE-READY: Release-critical architecture marker P8 requires score 4 or a valid exception; current score is 3.
- RG-RELEASE-READY: Release-critical architecture marker S5 requires score 4 or a valid exception; current score is 3.
- RG-RELEASE-READY: Release-critical architecture marker S6 requires score 4 or a valid exception; current score is 1.
- RG-RELEASE-READY: Release-critical architecture marker S8 requires score 4 or a valid exception; current score is 3.

Recommended actions:
- **Create release compatibility declaration**: Create and approve a release compatibility declaration that identifies the supported solution baseline, interface versions, data versions, deployment assumptions, security assumptions, known limitations and approval roles.
  Evidence: `release_compatibility_declaration`, `product_compatibility_matrix`, `approval_record`
- **Define solution baseline**: Define a solution baseline that lists participating product versions, interface versions, data contract versions, security baseline and deployment configuration.
  Evidence: `solution_release_baseline`, `product_participation_map`, `compatibility_matrix`
- **Verify enterprise security guardrail evidence**: Add verified security evidence such as threat model review, vulnerability scan result, crypto/security review or security architecture review.
  Evidence: `security_architecture_review`, `vulnerability_scan_result`, `security_test_evidence`
- **Verify product resilience behavior**: Add failure-mode, restart, recovery, degraded-mode or DIL behavior tests.
  Evidence: `failure_mode_test`, `recovery_test_result`, `degraded_mode_evidence`
- **Declare product release compatibility**: Add a product release compatibility declaration showing supported baselines, interface versions, data versions, deployment assumptions, exceptions and approvals.
  Evidence: `product_release_compatibility_declaration`, `compatibility_evidence`, `release_review_record`
- **Verify product security implementation**: Add product-level security verification evidence for authentication, authorization, crypto usage, logging and vulnerability handling.
  Evidence: `product_security_concept`, `vulnerability_scan_result`, `security_test_evidence`
- **Verify solution security evidence**: Define and verify solution trust zones, identity assumptions, crypto assumptions, logging/audit expectations and product security declarations.
  Evidence: `solution_threat_model`, `trust_zone_model`, `security_test_evidence`
- **Complete release architecture evidence**: Link the solution baseline to compatible product releases, interface versions, data contracts and deployment assumptions.
  Evidence: `solution_release_baseline`, `product_compatibility_matrix`, `release_declaration`
- **Verify solution resilience scenarios**: Add tested degraded-mode, failover, recovery or disconnected/intermittent/limited connectivity scenarios.
  Evidence: `degraded_mode_scenario`, `resilience_test_result`, `recovery_evidence`
