# Governance Change Request

## Summary

Provide 2-5 bullets describing the proposed governance change.

- 

## Change ID

```text
GCR-YYYY-NNN
```

## Source Document Intake

| Question | Answer |
|---|---|
| New or updated source document? |  |
| Source document path | `docs/governance/source-documents/...` |
| Register updated? | yes/no |
| Supersedes existing source? | yes/no, source ID |
| Source status | draft/intake/review/approved/superseded/retired |

## Why This Change Is Needed

Explain the governance, platform, audit, architecture or downstream consumer reason.

## Impact Analysis

| Area | Impact |
|---|---|
| Policy or directive |  |
| DevSecOps controls |  |
| Platform model |  |
| Architecture governance |  |
| OPA policies |  |
| Schemas and evidence contracts |  |
| Viewer, status indexes or intake |  |
| Release package or baseline |  |
| Downstream repositories |  |

## Derived Artifacts

List expected or changed derived artifacts.

- 

## Governance Behavior

Choose one:

- [ ] Documentation-only
- [ ] Report-only governance behavior
- [ ] Blocking governance behavior
- [ ] Release packaging only

Notes:

- 

## Release Decision

Choose one:

- [ ] No release required
- [ ] Release candidate required
- [ ] Patch baseline release required
- [ ] Minor baseline release required
- [ ] Major baseline release required

Release notes:

- 

## Validation Plan

Confirm what must pass before merge.

- [ ] `python3 scripts/validate_runtime_governance.py`
- [ ] `python3 scripts/validate_governance_repo.py`
- [ ] `python3 -m unittest discover -s tests`
- [ ] Source lineage regenerated or confirmed unchanged
- [ ] Viewer regenerated if status or presentation changed
- [ ] Downstream example checked if consumer behavior changed

## Reviewer Notes

List open decisions, assumptions or review focus.

- 
