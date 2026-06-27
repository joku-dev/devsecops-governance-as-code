# Control Evaluation Report

Input File: `demo/inputs/release-candidate-green.json`
Required Platform Level: `PRA-Level 2`
Release Candidate: `true`

## Summary

- Total controls: `46`
- Applicable controls: `30`
- Tested controls: `20`
- Passed: `20`
- Failed: `0`
- Not tested: `10`
- Not applicable: `16`

## Control Decisions

| Control | Level | Method | Status | Message |
| --- | --- | --- | --- | --- |
| `DSCB-GOV-REQ-001` | `GOV` | `hybrid` | `not_applicable` | Governance-board-level controls are not directly evaluated by this repository pipeline run. |
| `DSCB-GOV-REQ-002` | `GOV` | `hybrid` | `not_applicable` | Governance-board-level controls are not directly evaluated by this repository pipeline run. |
| `DSCB-GOV-REQ-003` | `GOV` | `hybrid` | `not_applicable` | Governance-board-level controls are not directly evaluated by this repository pipeline run. |
| `DSCB-GOV-REQ-004` | `GOV` | `hybrid` | `not_applicable` | Governance-board-level controls are not directly evaluated by this repository pipeline run. |
| `DSCB-GOV-REQ-005` | `GOV` | `hybrid` | `not_applicable` | Governance-board-level controls are not directly evaluated by this repository pipeline run. |
| `DSCB-L1-REQ-001` | `L1` | `hybrid` | `not_tested` | This control expects manual or hybrid evidence that is not fully represented in the current machine-readable pipeline input. |
| `DSCB-L1-REQ-002` | `L1` | `automated` | `not_tested` | The input does not explicitly prove approved version control usage and author traceability. |
| `DSCB-L1-REQ-003` | `L1` | `automated` | `pass` | Mapped policy `branch_protection` returned 0 deny messages. |
| `DSCB-L1-REQ-004` | `L1` | `hybrid` | `not_tested` | This control expects manual or hybrid evidence that is not fully represented in the current machine-readable pipeline input. |
| `DSCB-L1-REQ-005` | `L1` | `automated` | `pass` | Dependencies are treated as documented when the input includes a dependency list and an SBOM. |
| `DSCB-L1-REQ-006` | `L1` | `automated` | `pass` | Mapped policy `sbom` returned 0 deny messages. |
| `DSCB-L1-REQ-007` | `L1` | `automated` | `pass` | The run is treated as pipeline-executed when structured pipeline metadata is present. |
| `DSCB-L1-REQ-008` | `L1` | `automated` | `pass` | Artifact uniqueness is inferred from digest presence or explicit artifact version metadata. |
| `DSCB-L1-REQ-009` | `L1` | `automated` | `pass` | Mapped policy `vulnerability_gate` returned 0 deny messages. |
| `DSCB-L1-REQ-010` | `L1` | `automated` | `pass` | Mapped policy `vulnerability_gate` returned 0 deny messages. |
| `DSCB-L1-REQ-011` | `L1` | `automated` | `pass` | Mapped policy `artifact_integrity` returned 0 deny messages. |
| `DSCB-L1-REQ-012` | `L1` | `automated` | `pass` | Artifact identity is inferred from digest linkage to the evaluated artifact. |
| `DSCB-L1-REQ-013` | `L1` | `hybrid` | `not_tested` | This control expects manual or hybrid evidence that is not fully represented in the current machine-readable pipeline input. |
| `DSCB-L1-REQ-014` | `L1` | `hybrid` | `not_tested` | This control expects manual or hybrid evidence that is not fully represented in the current machine-readable pipeline input. |
| `DSCB-L1-REQ-015` | `L1` | `automated` | `pass` | Machine-readable evidence generation is inferred from structured pipeline execution data. |
| `DSCB-L1-REQ-016` | `L1` | `hybrid` | `not_tested` | This control expects manual or hybrid evidence that is not fully represented in the current machine-readable pipeline input. |
| `DSCB-L2-REQ-001` | `L2` | `hybrid` | `not_tested` | This control expects manual or hybrid evidence that is not fully represented in the current machine-readable pipeline input. |
| `DSCB-L2-REQ-002` | `L2` | `hybrid` | `not_tested` | This control expects manual or hybrid evidence that is not fully represented in the current machine-readable pipeline input. |
| `DSCB-L2-REQ-003` | `L2` | `automated` | `pass` | Central identity management is taken directly from the evaluated platform metadata. |
| `DSCB-L2-REQ-004` | `L2` | `automated` | `pass` | Mapped policy `access_control` returned 0 deny messages. |
| `DSCB-L2-REQ-005` | `L2` | `automated` | `pass` | Dependency repository approval is inferred from the source_approved flag on all declared dependencies. |
| `DSCB-L2-REQ-006` | `L2` | `automated` | `pass` | Mapped policy `dependency_source_control` returned 0 deny messages. |
| `DSCB-L2-REQ-007` | `L2` | `automated` | `pass` | Mapped policy `artifact_signing` returned 0 deny messages. |
| `DSCB-L2-REQ-008` | `L2` | `automated` | `pass` | Signing key protection is taken from the signing metadata in the run input. |
| `DSCB-L2-REQ-009` | `L2` | `hybrid` | `pass` | Mapped policy `iac` returned 0 deny messages. |
| `DSCB-L2-REQ-010` | `L2` | `hybrid` | `pass` | Infrastructure version control is inferred from the IaC repository metadata. |
| `DSCB-L2-REQ-011` | `L2` | `automated` | `pass` | Mapped policy `pipeline_security_gates` returned 0 deny messages. |
| `DSCB-L2-REQ-012` | `L2` | `automated` | `pass` | Mapped policy `pipeline_security_gates` returned 0 deny messages. |
| `DSCB-L2-REQ-013` | `L2` | `automated` | `not_tested` | This control expects manual or hybrid evidence that is not fully represented in the current machine-readable pipeline input. |
| `DSCB-L2-REQ-014` | `L2` | `automated` | `not_tested` | This control expects manual or hybrid evidence that is not fully represented in the current machine-readable pipeline input. |
| `DSCB-L3-REQ-001` | `L3` | `hybrid` | `not_applicable` | Control requires PRA-Level 3, but the evaluated run declares PRA-Level 2. |
| `DSCB-L3-REQ-002` | `L3` | `hybrid` | `not_applicable` | Control requires PRA-Level 3, but the evaluated run declares PRA-Level 2. |
| `DSCB-L3-REQ-003` | `L3` | `automated` | `not_applicable` | Control requires PRA-Level 3, but the evaluated run declares PRA-Level 2. |
| `DSCB-L3-REQ-004` | `L3` | `automated` | `not_applicable` | Control requires PRA-Level 3, but the evaluated run declares PRA-Level 2. |
| `DSCB-L3-REQ-005` | `L3` | `hybrid` | `not_applicable` | Control requires PRA-Level 3, but the evaluated run declares PRA-Level 2. |
| `DSCB-L3-REQ-006` | `L3` | `hybrid` | `not_applicable` | Control requires PRA-Level 3, but the evaluated run declares PRA-Level 2. |
| `DSCB-L3-REQ-007` | `L3` | `automated` | `not_applicable` | Control requires PRA-Level 3, but the evaluated run declares PRA-Level 2. |
| `DSCB-L3-REQ-008` | `L3` | `automated` | `not_applicable` | Control requires PRA-Level 3, but the evaluated run declares PRA-Level 2. |
| `DSCB-L3-REQ-009` | `L3` | `hybrid` | `not_applicable` | Control requires PRA-Level 3, but the evaluated run declares PRA-Level 2. |
| `DSCB-L3-REQ-010` | `L3` | `automated` | `not_applicable` | Control requires PRA-Level 3, but the evaluated run declares PRA-Level 2. |
| `DSCB-L3-REQ-011` | `L3` | `automated` | `not_applicable` | Control requires PRA-Level 3, but the evaluated run declares PRA-Level 2. |
