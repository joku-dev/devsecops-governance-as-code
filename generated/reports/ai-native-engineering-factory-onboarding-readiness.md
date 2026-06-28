# joku-dev/ai-native-engineering-factory Governance Onboarding Readiness

- Status: `ready_with_gaps`
- Generated: `2026-06-28T07:20:20Z`
- Target path: `/workspace/ai-native-engineering-factory`
- Recommended next step: Create a report-only central L1 baseline branch run.

## Summary

| Checks | Pass | Warn | Fail |
| --- | ---: | ---: | ---: |
| 5 | 4 | 1 | 0 |

## Checks

| Check | Status | Evidence | Recommendation |
| --- | --- | --- | --- |
| `repository_shape` Repository has discoverable project structure | `pass` | README.md<br>pyproject.toml<br>155 source/script files<br>138 test files | Keep README, setup instructions, source layout, and test entrypoints stable before wiring central governance. |
| `local_quality_gates` Local CI already covers tests, lint, typing, and governance freshness | `pass` | .github/workflows/quality-gates.yml<br>.gitlab-ci.yml<br>pytest=True<br>ruff=True<br>mypy=True<br>governance_evidence_check=True<br>agent_execution_gate=True | Preserve existing local quality gates and add the central L1 baseline as a separate report-only job first. |
| `governance_evidence_surface` Repository already contains governance and execution evidence | `pass` | 52 governance docs<br>137 agent execution records<br>128 slice candidate records<br>17 generated governance examples | Map this repository-native evidence into the central L1 evidence contract instead of duplicating it manually. |
| `supply_chain_and_security_evidence` Security and supply-chain evidence is present or planned | `pass` | .factory/security/90-day-pilot-readiness.example.json<br>.factory/security/assurance-runtime-policy.json<br>.factory/security/authorization-dry-run-observations.example.json<br>.factory/security/authorized_keys.example<br>.factory/security/factory-execution-authorization.json<br>security_docs=True<br>ci_supply_chain_script=True<br>secrets_scan_support=True<br>sbom_or_vulnerability_artifact=True | Before mainline enforcement, provide concrete SBOM and vulnerability scan artifacts for central intake. |
| `central_baseline_integration` Central governance baseline workflow is wired | `warn` | scanner_status=fail<br>governance_ci_file_present: pass<br>governance_reference_present: fail<br>governance_commands_present: fail | Add the reusable L1 workflow pinned to l1-baseline-v1.1.3 in report-only mode, then record the first branch run. |
