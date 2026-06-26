# Migration Status

## Completed

| Area | Status |
|---|---|
| Source DOCX documents imported | Complete |
| Policy source DOCX imported | Complete |
| Directive source DOCX imported | Complete |
| L1 control requirements | 16 / 16 complete |
| L2 control requirements | 14 / 14 complete |
| L3 control requirements | 11 / 11 complete |
| Governance requirements | 5 / 5 complete |
| Policy requirements | 21 / 21 complete |
| Directive requirements | 22 / 22 complete |
| Control-to-platform traceability | 46 / 46 complete |
| Policy/Directive-to-Control traceability | 43 / 43 complete |
| Initial evidence catalog | Complete |
| Initial platform capability catalog | Complete |
| Governance operating model YAML | Complete |
| CI/CD Pipeline Control Baseline | Complete |
| Control-to-pipeline-stage mapping | 46 / 46 complete |
| Initial policy-as-code candidates | 14 candidates |
| Automation classification | 46 / 46 complete |
| Verification requirements | 46 / 46 complete |
| BMS-visible Control Baseline DOCX | Complete |
| BMS-visible Platform Architecture DOCX | Complete |
| Repository validation script | Complete |
| Traceability CSV generator | Complete |
| Automation coverage report | Complete |

## Automation Classification Result

| Category | Count |
|---|---:|
| Blocking gates | 15 |
| Evidence checks | 30 |
| Review checks | 1 |
| Warning gates | 0 |

| Maturity | Count |
|---|---:|
| Immediate | 19 |
| Tool integration required | 22 |
| Future | 5 |

## Verification Readiness

Each requirement now contains:

- the original normative requirement
- a `verification_requirement` describing the machine-checkable evidence or decision expectation
- an `automation.check_type` describing how the requirement can be checked
- `automation.machine_readable_evidence_required` to state whether evidence should be machine-readable

Check type distribution:

| Check Type | Count |
|---|---:|
| Configuration | 14 |
| Presence | 10 |
| Linkage | 8 |
| Integrity | 5 |
| Approval | 4 |
| Threshold | 2 |
| Provenance | 2 |
| Review | 1 |

Interpretation:

- 15 requirements are candidates for hard automated gates.
- 30 further requirements can be checked through automated evidence presence, linkage, completeness, or freshness checks.
- 1 requirement remains primarily review-led.
- The high automation-supported count does not mean all controls should become release blockers. It means the repository can automatically support the control through gates or evidence checks.

## Still To Refine

The current model is a complete MVP, not yet a fully approved enterprise baseline. The following items should be refined during expert review:

- final evidence naming conventions
- exact verification frequency per control
- exact waiver authority per control
- formatting and pagination review of the generated BMS DOCX files in Microsoft Word
- mapping to concrete tool integrations such as GitLab, GitHub Enterprise, Artifactory, Nexus, SonarQube, Dependency-Track, DefectDojo, or ALM systems
- executable policy input model per selected platform
- generated DOCX/PDF production pipeline
