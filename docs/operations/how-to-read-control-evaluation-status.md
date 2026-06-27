# How To Read Control Evaluation Status

## Purpose

This document explains why the current green control evaluation report shows:

- `20` tested controls
- `0` failed controls
- `10` `not_tested`
- `16` `not_applicable`

It is intended to help readers understand that the control report is not a simple yes/no checklist.  
Instead, it distinguishes between:

- controls that were actually machine-evaluated
- controls that are relevant but not yet fully machine-provable
- controls that do not apply to the evaluated run context

## The Four Status Values

### `pass`

The control was evaluated by the current machine-readable logic and passed.

Typical reasons:

- a mapped OPA policy returned no deny messages
- the input evidence contained the required machine-readable proof
- the evaluator could infer the expected condition from the run metadata

Examples from the current green report:

- `DSCB-L1-REQ-003`
- `DSCB-L1-REQ-006`
- `DSCB-L1-REQ-009`
- `DSCB-L2-REQ-004`
- `DSCB-L2-REQ-011`

### `fail`

The control was evaluated by the current machine-readable logic and failed.

This would happen for example if:

- branch protection was not effective
- the SBOM was missing
- vulnerability thresholds were exceeded
- artifact signing was required but missing

In the current green example, there are:

- `0` failed controls

### `not_tested`

The control is relevant for the evaluated baseline and run scope, but the current run input does not provide enough machine-readable evidence to assert `pass` or `fail` safely.

This is important:

- `not_tested` does **not** mean the control is wrong
- `not_tested` means the current evaluator does not yet have enough structured proof

Typical reasons:

- the control expects manual review evidence
- the control is defined as `hybrid`
- the current input JSON does not include the required approval or traceability details

### `not_applicable`

The control does not apply directly to this evaluated run context.

Typical reasons:

- the control belongs to `GOV` and is not directly evaluated by a normal pipeline run
- the control requires a higher platform level than the current run declares

In the current green example:

- the input declares `PRA-Level 2`
- therefore all `L3` controls are currently `not_applicable`

## How The Current Green Report Is Counted

The current report summary is:

- Total controls: `46`
- Applicable controls: `30`
- Tested controls: `20`
- Passed: `20`
- Failed: `0`
- Not tested: `10`
- Not applicable: `16`

The key formula is:

- `tested_controls = pass + fail`

So in the current green report:

- `20 tested = 20 pass + 0 fail`

That means:

- `20` controls were really evaluated
- `10` controls were in scope but did not have enough machine-readable proof
- `16` controls were outside the direct run scope

## Why `16` Controls Are `not_applicable`

The current green input declares:

- `required_platform_level: PRA-Level 2`

That means:

- `L1` controls are applicable
- `L2` controls are applicable
- `L3` controls are not applicable in this run

Also, the repository currently treats `GOV` controls as not directly pipeline-testable in this report type.

### Breakdown

#### `5` `GOV` controls

These are:

- `DSCB-GOV-REQ-001`
- `DSCB-GOV-REQ-002`
- `DSCB-GOV-REQ-003`
- `DSCB-GOV-REQ-004`
- `DSCB-GOV-REQ-005`

Reason:

- they are governance-board or deviation-management controls
- they are not directly evaluated by a normal application pipeline run

#### `11` `L3` controls

These are:

- `DSCB-L3-REQ-001`
- `DSCB-L3-REQ-002`
- `DSCB-L3-REQ-003`
- `DSCB-L3-REQ-004`
- `DSCB-L3-REQ-005`
- `DSCB-L3-REQ-006`
- `DSCB-L3-REQ-007`
- `DSCB-L3-REQ-008`
- `DSCB-L3-REQ-009`
- `DSCB-L3-REQ-010`
- `DSCB-L3-REQ-011`

Reason:

- they require `PRA-Level 3`
- the evaluated run declares `PRA-Level 2`

So:

- `5 GOV + 11 L3 = 16 not_applicable`

## Why `10` Controls Are `not_tested`

These controls are applicable, but the current machine-readable run input does not fully prove them.

### Current `not_tested` controls

- `DSCB-L1-REQ-001`
- `DSCB-L1-REQ-002`
- `DSCB-L1-REQ-004`
- `DSCB-L1-REQ-013`
- `DSCB-L1-REQ-014`
- `DSCB-L1-REQ-016`
- `DSCB-L2-REQ-001`
- `DSCB-L2-REQ-002`
- `DSCB-L2-REQ-013`
- `DSCB-L2-REQ-014`

### Why these land in `not_tested`

#### Traceability and review-style controls

Examples:

- `DSCB-L1-REQ-001`
- `DSCB-L1-REQ-004`

Reason:

- they expect traceability records, review records, or hybrid proof
- the current input file does not contain a rich traceability evidence structure for those checks

#### Source code governance detail not explicitly present

Example:

- `DSCB-L1-REQ-002`

Reason:

- the current input does not explicitly prove approved version control usage and author traceability

#### Release approval controls

Examples:

- `DSCB-L1-REQ-013`
- `DSCB-L1-REQ-014`

Reason:

- these require stronger approval and approved-artifact evidence
- the current green input does not carry a dedicated approval record structure that the evaluator can verify

#### Operational and monitoring controls

Examples:

- `DSCB-L1-REQ-016`
- `DSCB-L2-REQ-013`
- `DSCB-L2-REQ-014`

Reason:

- they expect operational logs, monitoring records, or forwarded event evidence
- those are not yet present in the current machine-readable demo input

#### Environment baseline controls

Examples:

- `DSCB-L2-REQ-001`
- `DSCB-L2-REQ-002`

Reason:

- they expect richer environment configuration and configuration baseline evidence
- this evidence is not represented in the current input JSON

## Why `20` Controls Are `pass`

These controls are currently machine-evaluable with the present rule set and input structure.

### Typical `pass` patterns

#### OPA-mapped controls

Examples:

- `DSCB-L1-REQ-003` via branch protection
- `DSCB-L1-REQ-006` via SBOM
- `DSCB-L1-REQ-009` and `DSCB-L1-REQ-010` via vulnerability gate
- `DSCB-L1-REQ-011` via artifact integrity
- `DSCB-L2-REQ-004` via access control
- `DSCB-L2-REQ-006` via dependency source control
- `DSCB-L2-REQ-007` via artifact signing
- `DSCB-L2-REQ-009` via IaC
- `DSCB-L2-REQ-011` and `DSCB-L2-REQ-012` via pipeline security gates

These are strong machine-evaluable controls because:

- there is a direct mapping from control to policy
- the input JSON exposes the required facts

#### Evidence-inference controls

Examples:

- `DSCB-L1-REQ-005`
- `DSCB-L1-REQ-007`
- `DSCB-L1-REQ-008`
- `DSCB-L1-REQ-012`
- `DSCB-L1-REQ-015`
- `DSCB-L2-REQ-003`
- `DSCB-L2-REQ-005`
- `DSCB-L2-REQ-008`
- `DSCB-L2-REQ-010`

These pass because the evaluator can infer them from structured fields such as:

- SBOM existence
- dependency list
- pipeline metadata
- digest linkage
- signing metadata
- IaC repository metadata

## Why This Distinction Is Important

If the report forced every control into only:

- `pass`
- `fail`

then the output would be misleading.

It would hide the difference between:

- controls that were actually tested
- controls that still need manual review
- controls that were not in scope for this run

The current four-state model is therefore more honest and more useful operationally.

## How To Improve The Report Over Time

If you want fewer `not_tested` results in the future, the next step is not to weaken the logic.

The better step is to increase the machine-readable evidence available to the evaluator.

Examples:

- add explicit approval records for release authorization controls
- add structured traceability evidence
- add environment baseline evidence
- add operational monitoring evidence

Then more controls can move from:

- `not_tested`

to:

- `pass`
- or `fail`

based on real proof.

## Practical Reading Rule

When reading a control evaluation report, use this interpretation:

- `pass` = proven by the current machine-readable evaluation
- `fail` = disproven by the current machine-readable evaluation
- `not_tested` = relevant, but not yet sufficiently machine-proven
- `not_applicable` = outside the direct scope of this evaluated run

## Related Files

- `generated/control-evaluation-report.json`
- `generated/control-evaluation-report.md`
- `generated/governance-compliance-result.json`
- `generated/viewer/status-viewer.html`
- `scripts/control_evaluation.py`
- `scripts/generate_control_evaluation_report.py`
