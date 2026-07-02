# App Architecture Evidence Templates

## Purpose

Application repositories can add structured architecture evidence under:

```text
.governance/architecture/
```

The architecture governance collector reads these files and uses them to raise marker maturity from "described" to "verified" when evidence is approved.

## Files

| File | Evidence type | Typical effect |
|---|---|---|
| `solution-baseline.json` | `solution_baseline` | Satisfies solution baseline presence. |
| `release-compatibility-declaration.json` | `release_compatibility_declaration` | Satisfies release compatibility declaration presence and approval when `status` is `approved`. |
| `security-evidence.json` | `security_evidence` | Strengthens E6, S5 and P8 security marker scores. |
| `resilience-evidence.json` | `resilience_evidence` | Strengthens S8 and P10 resilience marker scores. |
| `operation-evidence.json` | `operation_evidence` | Strengthens P11 observability marker score. |
| `feedback-evidence.json` | `feedback_evidence` | Strengthens B5 feedback-loop marker score. |

## Status Semantics

| Status | Meaning |
|---|---|
| `draft` | Evidence exists but is not verified. |
| `reviewed` | Evidence has been reviewed but is not yet approved for gate satisfaction. |
| `approved` | Evidence is accepted for gate satisfaction. |

## Usage

Copy the `.governance/architecture/` folder into the application repository and update owners, baseline names, evidence references, limitations and follow-up actions.

For demo purposes, keep files in `draft` to show findings. Change selected files to `approved` to demonstrate how findings are reduced through evidence.
