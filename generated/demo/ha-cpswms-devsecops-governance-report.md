# DevSecOps Governance Report

## Target

- Repository: `/workspace/ha-CPsWMS`
- Commit: `002db4e`
- Release ID: `ha-CPsWMS-demo`

## Gate Summary

| Gate | Status | Findings |
|---|---:|---:|
| DevSecOps Release Readiness | FINDINGS | 8 |

## Findings

- DSCB-L1-REQ-006: Release candidates require an SBOM.
- DSCB-L1-REQ-009: Release candidates require vulnerability scan evidence.
- DSCB-L1-REQ-011: Releasable artifacts require checksum, digest, or signature evidence.
- DSCB-L2-REQ-006: Dependency ha-sync/requirements.txt is not retrieved from an approved source.
- DSCB-L2-REQ-006: Dependency query-api/requirements.txt is not retrieved from an approved source.
- DSCB-L2-REQ-006: Dependency semantic-enrichment/requirements.txt is not retrieved from an approved source.
- DSCB-L2-REQ-006: Dependency world-model-chat/requirements.txt is not retrieved from an approved source.
- DSCB-L2-REQ-011: DevSecOps pipelines must enforce security gates.
