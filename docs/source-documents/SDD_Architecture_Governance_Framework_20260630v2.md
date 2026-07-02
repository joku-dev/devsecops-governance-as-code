|          |                                                                     |     |
|----------|---------------------------------------------------------------------|-----|
|          |                                                                     |     |
|          |                                                                     |     |
|          |                                                                     |     |
| Project: | sss                                                                 |     |
| Title:   | HENSOLDT Software-Defined Defence Architecture Governance Framework |     |
| Doc. ID: | xxxxx ADO xx1 01                                                    |     |
|          |                                                                     |     |
|          |                                                                     |     |

<span id="_Toc233730385" class="anchor"></span>Table 1: How to read this document

Prepared by:

**HENSOLDT Sensors GmbH**

Registered office:

Willy-Messerschmitt-Strasse 3

82024 Taufkirchen

Germany

<table style="width:100%;">
<caption><p><span id="_Toc233730386" class="anchor"></span>Table 2: BAPO Definition and Use in the SDD Architecture Governance Framework</p></caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 30%" />
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><strong>Name:</strong></th>
<th><strong>Dept.:</strong></th>
<th><strong>Date:</strong></th>
<th><strong>Signature:</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Prepared:<br />
by SDD Enterprise Architect</td>
<td>Dr. Roland Kempter</td>
<td>HTS</td>
<td>xx.xx.2026</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Validated:<br />
by</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Endorsed:<br />
by</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Authorized:<br />
by</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc233730386" class="anchor"></span>Table 2: BAPO Definition and Use in the SDD Architecture Governance Framework

**CHANGE RECORD**

|         |             |                       |                             |                |
|---------|-------------|-----------------------|-----------------------------|----------------|
| Version | Change date | Changed pages/chapter | Brief description of change | Change Request |
| 01      | yy.yy.2026  | All                   | Initial Release             | 111111         |
|         |             |                       |                             |                |
|         |             |                       |                             |                |
|         |             |                       |                             |                |

<span id="_Toc233730387" class="anchor"></span>Table 3: Applicability of The Architecture Governance Framework

**DISTRIBUTION LIST**

A project internal distribution of printouts of this document is not necessary. It is available to every member of the project team electronically via the used configuration management tool (PLM).

|         |      |           |          |               |
|---------|------|-----------|----------|---------------|
| Company | Name | Org.-Unit | Function | No. of copies |
|         |      |           |          | 1             |
|         |      |           |          |               |
|         |      |           |          |               |
|         |      |           |          |               |
|         |      |           |          |               |

<span id="_Toc233730388" class="anchor"></span>Table 4: BAPO questions and architecture interpretation

in electronic form

**TABLE OF CONTENTS**

[1 Purpose and Scope [12](#purpose-and-scope)](#purpose-and-scope)

[1.1 Purpose [12](#purpose)](#purpose)

[1.2 Governing Rule for BAPO [13](#governing-rule-for-bapo)](#governing-rule-for-bapo)

[1.3 Scope [14](#scope)](#scope)

[1.4 Architecture Problem Statement [15](#architecture-problem-statement)](#architecture-problem-statement)

[1.5 Strategic Context [16](#strategic-context)](#strategic-context)

[1.6 Guiding Intent [16](#guiding-intent)](#guiding-intent)

[2 Agile@HENSOLDT Architecture Operating Model [18](#agilehensoldt-architecture-operating-model)](#agilehensoldt-architecture-operating-model)

[2.1 Operating Model Interpretation [18](#operating-model-interpretation)](#operating-model-interpretation)

[2.2 BAPO Alignment Interpretation [21](#bapo-alignment-interpretation)](#bapo-alignment-interpretation)

[2.3 Architecture Flow [24](#architecture-flow)](#architecture-flow)

[2.4 Architecture Work Items [26](#architecture-work-items)](#architecture-work-items)

[2.5 Architecture Events and Decision Points [28](#architecture-events-and-decision-points)](#architecture-events-and-decision-points)

[2.6 Architecture Roles [30](#architecture-roles)](#architecture-roles)

[3 Architecture Governance Levels [33](#architecture-governance-levels)](#architecture-governance-levels)

[3.1 BAPO Structure of Architecture Governance [33](#bapo-structure-of-architecture-governance)](#bapo-structure-of-architecture-governance)

[3.2 Enterprise Level Architecture [35](#enterprise-level-architecture)](#enterprise-level-architecture)

[3.2.1 Purpose [35](#purpose-1)](#purpose-1)

[3.2.2 Enterprise Level Architecture Scope [35](#enterprise-level-architecture-scope)](#enterprise-level-architecture-scope)

[3.2.3 Enterprise Level BAPO Alignment Challenge [36](#enterprise-level-bapo-alignment-challenge)](#enterprise-level-bapo-alignment-challenge)

[3.2.4 Enterprise Level Architecture Decision Rights [37](#enterprise-level-architecture-decision-rights)](#enterprise-level-architecture-decision-rights)

[3.2.5 Enterprise Level Architecture Deliverables [37](#enterprise-level-architecture-deliverables)](#enterprise-level-architecture-deliverables)

[3.2.6 Enterprise Level Architecture Quality Markers [38](#enterprise-level-architecture-quality-markers)](#enterprise-level-architecture-quality-markers)

[3.3 Solution Level Architecture [39](#solution-level-architecture)](#solution-level-architecture)

[3.3.1 Purpose [39](#purpose-2)](#purpose-2)

[3.3.2 Solution Level Architecture Scope [40](#solution-level-architecture-scope)](#solution-level-architecture-scope)

[3.3.3 Solution BAPO Alignment Challenge [40](#solution-bapo-alignment-challenge)](#solution-bapo-alignment-challenge)

[3.3.4 Solution Architecture Decision Rights [41](#solution-architecture-decision-rights)](#solution-architecture-decision-rights)

[3.3.5 Solution Level Architecture Deliverables [41](#solution-level-architecture-deliverables)](#solution-level-architecture-deliverables)

[3.3.6 Solution Release Model [42](#solution-release-model)](#solution-release-model)

[3.3.7 Compatibility Rules for the Solution Level [43](#compatibility-rules-for-the-solution-level)](#compatibility-rules-for-the-solution-level)

[3.3.8 Solution Level Quality Markers [44](#solution-level-quality-markers)](#solution-level-quality-markers)

[3.4 Product Level Architecture [45](#product-level-architecture)](#product-level-architecture)

[3.4.1 Purpose [45](#purpose-3)](#purpose-3)

[3.4.2 Product Level Architecture Scope [46](#product-level-architecture-scope)](#product-level-architecture-scope)

[3.4.3 Product Level BAPO Alignment Challenge [46](#product-level-bapo-alignment-challenge)](#product-level-bapo-alignment-challenge)

[3.4.4 Product Level Architecture Deliverables [47](#product-level-architecture-deliverables)](#product-level-architecture-deliverables)

[3.4.5 Product Level Quality Markers [48](#product-level-quality-markers)](#product-level-quality-markers)

[3.4.6 Cross-Level Traceability Between Enterprise, Solution and Product ArchitectureRelationship between the three Levels [49](#cross-level-traceability-between-enterprise-solution-and-product-architecturerelationship-between-the-three-levels)](#cross-level-traceability-between-enterprise-solution-and-product-architecturerelationship-between-the-three-levels)

[4 Business-Driven Architecture Principles and BAPO Alignment Challenges [52](#business-driven-architecture-principles-and-bapo-alignment-challenges)](#business-driven-architecture-principles-and-bapo-alignment-challenges)

[4.1 Purpose [52](#purpose-4)](#purpose-4)

[4.2 Principle Structure [52](#principle-structure)](#principle-structure)

[4.3 Principle 1: Mission-Driven Architecture [53](#principle-1-mission-driven-architecture)](#principle-1-mission-driven-architecture)

[4.4 Principle 2: Enterprise Alignment with Local Autonomy [53](#principle-2-enterprise-alignment-with-local-autonomy)](#principle-2-enterprise-alignment-with-local-autonomy)

[4.5 Principle 3: Open and Modular Architecture [54](#principle-3-open-and-modular-architecture)](#principle-3-open-and-modular-architecture)

[4.6 Principle 4: Data-Centricity [55](#principle-4-data-centricity)](#principle-4-data-centricity)

[4.7 Principle 5: Interoperability by Design [56](#principle-5-interoperability-by-design)](#principle-5-interoperability-by-design)

[4.8 Principle 6: Security by Design [56](#principle-6-security-by-design)](#principle-6-security-by-design)

[4.9 Principle 7: DevSecOps and Continuous Release Readiness [57](#principle-7-devsecops-and-continuous-release-readiness)](#principle-7-devsecops-and-continuous-release-readiness)

[4.10 Principle 8: Edge / Fog / Cloud Continuum (where Applicable) [58](#principle-8-edge-fog-cloud-continuum-where-applicable)](#principle-8-edge-fog-cloud-continuum-where-applicable)

[4.11 Principle 9: Resilience Under Degraded Conditions (where Applicable) [59](#principle-9-resilience-under-degraded-conditions-where-applicable)](#principle-9-resilience-under-degraded-conditions-where-applicable)

[4.12 Principle 10: Evidence-Based Architecture [60](#principle-10-evidence-based-architecture)](#principle-10-evidence-based-architecture)

[5 Architecture Quality Marker Model [61](#architecture-quality-marker-model)](#architecture-quality-marker-model)

[5.1 Purpose [61](#purpose-5)](#purpose-5)

[5.2 Quality Marker Scoring [61](#quality-marker-scoring)](#quality-marker-scoring)

[5.3 Marker Evidence Types [64](#marker-evidence-types)](#marker-evidence-types)

[5.4 Mandatory BAPO Alignment Markers [65](#mandatory-bapo-alignment-markers)](#mandatory-bapo-alignment-markers)

[5.5 Enterprise Architecture Quality Marker Catalogue [66](#enterprise-architecture-quality-marker-catalogue)](#enterprise-architecture-quality-marker-catalogue)

[5.6 Solution Architecture Quality Marker Catalogue [68](#solution-architecture-quality-marker-catalogue)](#solution-architecture-quality-marker-catalogue)

[5.7 Product Architecture Quality Maker Catalogue [70](#product-architecture-quality-maker-catalogue)](#product-architecture-quality-maker-catalogue)

[5.8 Architecture Quality Marker Reviews [71](#architecture-quality-marker-reviews)](#architecture-quality-marker-reviews)

[5.9 Minimum Acceptance Rule [73](#minimum-acceptance-rule)](#minimum-acceptance-rule)

[6 SDD Enterprise Architecture Guidelines [76](#sdd-enterprise-architecture-guidelines)](#sdd-enterprise-architecture-guidelines)

[6.1 Purpose [76](#purpose-6)](#purpose-6)

[6.2 BAPO Structure of Enterprise Guardrails [77](#bapo-structure-of-enterprise-guardrails)](#bapo-structure-of-enterprise-guardrails)

[6.3 Software-Defined Defence Strategic Alignment [80](#software-defined-defence-strategic-alignment)](#software-defined-defence-strategic-alignment)

[6.4 Enterprise Reference Architecture Catalogue [81](#enterprise-reference-architecture-catalogue)](#enterprise-reference-architecture-catalogue)

[6.5 Technology Radar and Technology Governance [81](#technology-radar-and-technology-governance)](#technology-radar-and-technology-governance)

[6.6 Interface Standards and Interoperability Guardrails [82](#interface-standards-and-interoperability-guardrails)](#interface-standards-and-interoperability-guardrails)

[6.7 Enterprise Data and Semantic Architecture [82](#enterprise-data-and-semantic-architecture)](#enterprise-data-and-semantic-architecture)

[6.8 Security, Safety and Sovereignity Guardrails [83](#security-safety-and-sovereignity-guardrails)](#security-safety-and-sovereignity-guardrails)

[6.9 Runtime, Platform and Edge / Fog / Cloud Guardrails [83](#runtime-platform-and-edge-fog-cloud-guardrails)](#runtime-platform-and-edge-fog-cloud-guardrails)

[6.10 DevSecOps and Continuous Release Guardrails [85](#devsecops-and-continuous-release-guardrails)](#devsecops-and-continuous-release-guardrails)

[6.11 Architecture KPIs [86](#architecture-kpis)](#architecture-kpis)

[6.12 Architecture Exception Process [87](#architecture-exception-process)](#architecture-exception-process)

[7 SDD Solution Architecture Guidelines [89](#sdd-solution-architecture-guidelines)](#sdd-solution-architecture-guidelines)

[7.1 Purpose [89](#purpose-7)](#purpose-7)

[7.2 BAPO Structure oft he Solution Architecture [89](#bapo-structure-oft-he-solution-architecture)](#bapo-structure-oft-he-solution-architecture)

[7.3 Solution Capability and Mission Thread Definition [90](#solution-capability-and-mission-thread-definition)](#solution-capability-and-mission-thread-definition)

[7.4 Product Participation and Capability Allocation [90](#product-participation-and-capability-allocation)](#product-participation-and-capability-allocation)

[7.5 Cross-Product Interface Architecture [92](#cross-product-interface-architecture)](#cross-product-interface-architecture)

[7.6 Solution Data Flow and Semantic Alignment [92](#solution-data-flow-and-semantic-alignment)](#solution-data-flow-and-semantic-alignment)

[7.7 Solution Security and Trust Boundary Architecture [93](#solution-security-and-trust-boundary-architecture)](#solution-security-and-trust-boundary-architecture)

[7.8 Integrated Runtime and Deployment Architecture [94](#integrated-runtime-and-deployment-architecture)](#integrated-runtime-and-deployment-architecture)

[7.9 Solution Release Architecture [95](#solution-release-architecture)](#solution-release-architecture)

[7.10 Independent Product Release Compatibility [98](#independent-product-release-compatibility)](#independent-product-release-compatibility)

[7.11 Integration and Verification Strategy [98](#integration-and-verification-strategy)](#integration-and-verification-strategy)

[7.12 Solution Architecture Runway [99](#solution-architecture-runway)](#solution-architecture-runway)

[7.13 Solution Risk and Technical Debt Governance [101](#solution-risk-and-technical-debt-governance)](#solution-risk-and-technical-debt-governance)

[8 SDD Product Architecture Guidelines [103](#sdd-product-architecture-guidelines)](#sdd-product-architecture-guidelines)

[8.1 Purpose [103](#purpose-8)](#purpose-8)

[8.2 BAPO Structure of the Product Architecture [103](#bapo-structure-of-the-product-architecture)](#bapo-structure-of-the-product-architecture)

[8.3 The Product Business Contribution Statement [106](#the-product-business-contribution-statement)](#the-product-business-contribution-statement)

[8.4 Product Context and Scope [106](#product-context-and-scope)](#product-context-and-scope)

[8.5 Building Block View [106](#building-block-view)](#building-block-view)

[8.6 Runtime View [108](#runtime-view)](#runtime-view)

[8.7 Deployment View [109](#deployment-view)](#deployment-view)

[8.8 Interface and Data Contract Specification [110](#interface-and-data-contract-specification)](#interface-and-data-contract-specification)

[8.9 Architecture Decision Records [111](#architecture-decision-records)](#architecture-decision-records)

[8.10 Product Quality Requirements [113](#product-quality-requirements)](#product-quality-requirements)

[8.11 Product Security Concept [115](#product-security-concept)](#product-security-concept)

[8.12 Product Verification Evidence [116](#product-verification-evidence)](#product-verification-evidence)

[8.13 Product Release Compatibility Declaration [117](#product-release-compatibility-declaration)](#product-release-compatibility-declaration)

[8.14 Product Risk and Technical Debt Register [119](#product-risk-and-technical-debt-register)](#product-risk-and-technical-debt-register)

[9 BAPO Architecture Review and Feedback Process [121](#bapo-architecture-review-and-feedback-process)](#bapo-architecture-review-and-feedback-process)

[9.1 Purpose [121](#purpose-9)](#purpose-9)

[9.2 Review Principles [121](#review-principles)](#review-principles)

[9.3 Enterprise Architecture Review [124](#enterprise-architecture-review)](#enterprise-architecture-review)

[9.4 Solution Architecture Review [125](#solution-architecture-review)](#solution-architecture-review)

[9.5 Product Architecture Review [127](#product-architecture-review)](#product-architecture-review)

[9.6 Release Readiness Review [129](#release-readiness-review)](#release-readiness-review)

[9.7 Architecture Exception Review [131](#architecture-exception-review)](#architecture-exception-review)

[9.8 System Demo and Inspect & Adapt Feedback [133](#system-demo-and-inspect-adapt-feedback)](#system-demo-and-inspect-adapt-feedback)

[10 SDD Architecture Templates and Checklists [135](#sdd-architecture-templates-and-checklists)](#sdd-architecture-templates-and-checklists)

[10.1 Purpose [135](#purpose-10)](#purpose-10)

[10.2 BAPO Architecture Decision Template [135](#bapo-architecture-decision-template)](#bapo-architecture-decision-template)

[10.3 Enterprise Guardrail Template [137](#enterprise-guardrail-template)](#enterprise-guardrail-template)

[10.4 Solution Architecture Template [139](#solution-architecture-template)](#solution-architecture-template)

[10.5 Product Architecture Template [141](#product-architecture-template)](#product-architecture-template)

[10.6 Interface Contract Template [142](#interface-contract-template)](#interface-contract-template)

[10.7 Data Contract Template [144](#data-contract-template)](#data-contract-template)

[10.8 Quality Marker Template [146](#quality-marker-template)](#quality-marker-template)

[10.9 Architecture Exception Template [148](#architecture-exception-template)](#architecture-exception-template)

[10.10 Release Compatibility Declaration Template [150](#release-compatibility-declaration-template)](#release-compatibility-declaration-template)

**LIST OF FIGURES**

[Figure 1: agile@HENSOLDT architecture governance at a glance [11](#_Ref233703209)](#_Ref233703209)

[Figure 2: Architecture responsibilities in the agile@HENSOLDT operating model: [20](#_Ref233703418)](#_Ref233703418)

[Figure 3: BAPO as an additive architecture alignment lens, showing how Business: [23](#_Ref233703593)](#_Ref233703593)

[Figure 4: Enterprise-Solution-Product Architecture Stack [34](#_Ref233703763)](#_Ref233703763)

[Figure 5: Cross-level traceability chain [51](#_Ref233705932)](#_Ref233705932)

[Figure 6: Architecture quality marker maturity model [63](#_Ref233703932)](#_Ref233703932)

[Figure 7: Enterprise guardrail lifecycle [79](#_Ref233704043)](#_Ref233704043)

[Figure 8: Solution release baseline model [97](#_Ref233704145)](#_Ref233704145)

[Figure 9: Product Architecture Evidence Package [105](#_Ref233704287)](#_Ref233704287)

[Figure 10: Architecture review and feedback loop [123](#_Ref233704522)](#_Ref233704522)

**LIST OF TABLES**

[Table 1: How to read this document [9](#_Toc233730385)](#_Toc233730385)

[Table 2: BAPO Definition and Use in the SDD Architecture Governance Framework [13](#_Toc233730386)](#_Toc233730386)

[Table 3: Applicability of The Architecture Governance Framework [15](#_Toc233730387)](#_Toc233730387)

[Table 4: BAPO questions and architecture interpretation [15](#_Toc233730388)](#_Toc233730388)

[Table 5: Anti-patterns and why to avoid them [16](#_Toc233730389)](#_Toc233730389)

[Table 6: The Seven Outcomes of the SDD Architecture Governance Framework [17](#_Toc233730390)](#_Toc233730390)

[Table 7: agile@HENSOLDT operating model and architectural interpretation [18](#_Toc233730391)](#_Toc233730391)

[Table 8: Levels and Architectural assignment [19](#_Toc233730392)](#_Toc233730392)

[Table 9: BAPO elements mapped to elements in agile@HENSOLDT and their resp. Architectural meaning [21](#_Toc233730393)](#_Toc233730393)

[Table 10: Architecture decision flow through the agile@HENSOLDT operating model [25](#_Toc233730394)](#_Toc233730394)

[Table 11: Architecture Work Items [27](#_Toc233730395)](#_Toc233730395)

[Table 12: BAPO Alignment Metadata for architecture work items [27](#_Toc233730396)](#_Toc233730396)

[Table 13: Architecture Events and Decision Points [29](#_Toc233730397)](#_Toc233730397)

[Table 14: Questions for architecture events [29](#_Toc233730398)](#_Toc233730398)

[Table 15: Required architecture roles according tot he ADD Architecture Governance Framework [31](#_Ref233710682)](#_Ref233710682)

[Table 16: BAPO ownership responsibilities [32](#_Ref233710726)](#_Ref233710726)

[Table 17: BAPO Structure of Architecture Governance [33](#_Toc233730401)](#_Toc233730401)

[Table 18: Enterprise Architecture, area and scope [36](#_Toc233730402)](#_Toc233730402)

[Table 19: Enterprise BAPO Alignment Challenge [36](#_Toc233730403)](#_Toc233730403)

[Table 20: Enterprise Architecture Decision Rights [37](#_Toc233730404)](#_Toc233730404)

[Table 21: Mandatory Enterprise Architecture Deliverables [38](#_Toc233730405)](#_Toc233730405)

[Table 22: Enterprise Architecture Quality Markers [39](#_Toc233730406)](#_Toc233730406)

[Table 23: Solution Architecture Scope [40](#_Toc233730407)](#_Toc233730407)

[Table 24: Solution BAPO Alignemnt Challenge [41](#_Toc233730408)](#_Toc233730408)

[Table 25: Solution Architecture Decision Rights [41](#_Toc233730409)](#_Toc233730409)

[Table 26: Mandatory Solution Architecture [42](#_Toc233730410)](#_Toc233730410)

[Table 27: Solution Release Model [43](#_Toc233730411)](#_Toc233730411)

[Table 28: Content required for Solution Release Baselinie [43](#_Toc233730412)](#_Toc233730412)

[Table 29: Required Compatibility Evidence for the Solution Level [44](#_Toc233730413)](#_Toc233730413)

[Table 30: Solution Level Quality Markers [45](#_Toc233730414)](#_Toc233730414)

[Table 31: Product Level Architecture Scope [46](#_Toc233730415)](#_Toc233730415)

[Table 32: Product-Level Architecture Responsibilities for BAPO Alignment [47](#_Toc233730416)](#_Toc233730416)

[Table 33: Mandatory Product Level Architecture Deliverables [48](#_Toc233730417)](#_Toc233730417)

[Table 34: Product Level Architecture Quality Markers [49](#_Toc233730418)](#_Toc233730418)

[Table 35: Traceability Levels, purpose and evidence [49](#_Toc233730419)](#_Toc233730419)

[Table 36: Principles Alignment [52](#_Toc233730420)](#_Toc233730420)

[Table 37: Use Cases and how to apply principles [53](#_Toc233730421)](#_Toc233730421)

[Table 38: Principles of Mission-driven architecture [53](#_Toc233730422)](#_Toc233730422)

[Table 39: Enterprise Alignment with local autonomy [54](#_Toc233730423)](#_Toc233730423)

[Table 40: Architecture Levels and Ownership Elements [54](#_Toc233730424)](#_Toc233730424)

[Table 41: BAPO and open and modular architectures: challenges [54](#_Toc233730425)](#_Toc233730425)

[Table 42: BAPO and data centricity: challenges per level [55](#_Toc233730426)](#_Toc233730426)

[Table 43: BAPO and interoperability by design: challenges per level [56](#_Toc233730427)](#_Toc233730427)

[Table 44: BAPO and security by design: challenges per level [57](#_Toc233730428)](#_Toc233730428)

[Table 45: BAPO, DevSecOps and Continuous Release readiness: challenges per level [58](#_Toc233730429)](#_Toc233730429)

[Table 46: BAPO, Edge / Fog / Cloud continuum: challenges per level [58](#_Toc233730430)](#_Toc233730430)

[Table 47: Resilience under degraded conditions (where applicable): challenges per level [59](#_Toc233730431)](#_Toc233730431)

[Table 48: Evidence-based architecture: challenges per level [60](#_Toc233730432)](#_Toc233730432)

[Table 49: Quality marker scoring [61](#_Toc233730433)](#_Toc233730433)

[Table 50: BAPO scoring rules [62](#_Toc233730434)](#_Toc233730434)

[Table 51: Scoring results and their practical meanng [62](#_Toc233730435)](#_Toc233730435)

[Table 52: Marker evidence types [65](#_Toc233730436)](#_Toc233730436)

[Table 53: Mandatory BAPO alignment markers [66](#_Toc233730437)](#_Toc233730437)

[Table 54: Enterprise architecture quality marker catalogue [68](#_Toc233730438)](#_Toc233730438)

[Table 55: Solution architecture quality marker catalogue [69](#_Toc233730439)](#_Toc233730439)

[Table 56: Product architecture quallity marker catalogue [71](#_Toc233730440)](#_Toc233730440)

[Table 57: Architecture quality markers review points [73](#_Toc233730441)](#_Toc233730441)

[Table 58: Readiness state definitions per architecture level [74](#_Toc233730442)](#_Toc233730442)

[Table 59: BAPO structure of enterprise guardrails [77](#_Toc233730443)](#_Toc233730443)

[Table 60: Questions guardrails must answer [78](#_Toc233730444)](#_Toc233730444)

[Table 61: SDD strategic alignment [80](#_Toc233730445)](#_Toc233730445)

[Table 62: Enterprise Reference Architecture Catalogue [81](#_Toc233730446)](#_Toc233730446)

[Table 63: Technology radar and technology governance [82](#_Toc233730447)](#_Toc233730447)

[Table 64: Interface standards and interoperability guardrails [82](#_Toc233730448)](#_Toc233730448)

[Table 65: Enterprise data and semantic architecture [83](#_Toc233730449)](#_Toc233730449)

[Table 66: Security, safety and sovereignity guardrails [83](#_Toc233730450)](#_Toc233730450)

[Table 67: Runtime, platform and Edge/Fog/Cloud guardrails [84](#_Toc233730451)](#_Toc233730451)

[Table 68: DevSecOps and Continuous Release guardrails [86](#_Toc233730452)](#_Toc233730452)

[Table 69: Architecture KPIs [87](#_Toc233730453)](#_Toc233730453)

[Table 70: Architecture exeption process [88](#_Toc233730454)](#_Toc233730454)

[Table 71: BAPO structure oft he solution architecture [90](#_Toc233730455)](#_Toc233730455)

[Table 72: Solution Capability and mission thread definition [90](#_Toc233730456)](#_Toc233730456)

[Table 73: Product participation and capability allocation [91](#_Toc233730457)](#_Toc233730457)

[Table 74: Cross-product interface architecture [92](#_Toc233730458)](#_Toc233730458)

[Table 75: Solution Data Flow and semantic alignment [92](#_Toc233730459)](#_Toc233730459)

[Table 76: Solution Security and trust boundary architecture [93](#_Toc233730460)](#_Toc233730460)

[Table 77: Integrated runtime and deployment architecture [95](#_Toc233730461)](#_Toc233730461)

[Table 78: Solution release architecture [95](#_Toc233730462)](#_Toc233730462)

[Table 79: Independent product release compatibility [98](#_Toc233730463)](#_Toc233730463)

[Table 80: Integration and verification strategy on solution level [99](#_Toc233730464)](#_Toc233730464)

[Table 81: Solution architecture runway [100](#_Toc233730465)](#_Toc233730465)

[Table 82: Solution risk and technical debt governance [102](#_Toc233730466)](#_Toc233730466)

[Table 83: High level question fort he product architecture [103](#_Toc233730467)](#_Toc233730467)

[Table 84: BAPO structure oft he product level architecture [104](#_Toc233730468)](#_Toc233730468)

[Table 85: Product context and scope [106](#_Toc233730469)](#_Toc233730469)

[Table 86: Building block view, product architecture [107](#_Toc233730470)](#_Toc233730470)

[Table 87: Product architecture: runtime view [108](#_Toc233730471)](#_Toc233730471)

[Table 88: Product architecture: deployment view [109](#_Toc233730472)](#_Toc233730472)

[Table 89: Product architecture: interface and data contract specification [111](#_Toc233730473)](#_Toc233730473)

[Table 90: Product architecture: architecture decision record fields [112](#_Toc233730474)](#_Toc233730474)

[Table 91: Product architecture quality requirements [114](#_Toc233730475)](#_Toc233730475)

[Table 92: Product security concept [115](#_Toc233730476)](#_Toc233730476)

[Table 93: Product verification evidence [117](#_Toc233730477)](#_Toc233730477)

[Table 94: Product release compatibility declaration [118](#_Toc233730478)](#_Toc233730478)

[Table 95: Product risk and technical debt register [120](#_Toc233730479)](#_Toc233730479)

[Table 96: Possible outcomes BAPO architecture review [121](#_Toc233730480)](#_Toc233730480)

[Table 97: BAPO architecture review principles [122](#_Toc233730481)](#_Toc233730481)

[Table 98: Enterprise architecture review questions [125](#_Toc233730482)](#_Toc233730482)

[Table 99: Solution architecture review questions [126](#_Toc233730483)](#_Toc233730483)

[Table 100: Product architecture review questions [128](#_Toc233730484)](#_Toc233730484)

[Table 101: Release readiness review checklist [130](#_Toc233730485)](#_Toc233730485)

[Table 102: Architecture exception review content [132](#_Toc233730486)](#_Toc233730486)

[Table 103: Feedback source versus architectural use [134](#_Toc233730487)](#_Toc233730487)

[Table 104: BAPO Architecture decision template [137](#_Toc233730488)](#_Toc233730488)

[Table 105: Enterprise guardrail template [138](#_Toc233730489)](#_Toc233730489)

[Table 106: Solution architecture template [140](#_Toc233730490)](#_Toc233730490)

[Table 107: Product architecture template [142](#_Toc233730491)](#_Toc233730491)

[Table 108: Interface contract template [144](#_Toc233730492)](#_Toc233730492)

[Table 109: Data contract template [145](#_Toc233730493)](#_Toc233730493)

[Table 110: Quality marker template [147](#_Toc233730494)](#_Toc233730494)

[Table 111: Architecture exception template [149](#_Toc233730495)](#_Toc233730495)

[Table 112: Release compatibility declaration template [151](#_Toc233730496)](#_Toc233730496)

**EXECUTIVE SUMMARY**

The HENSOLDT Software-Defined Defence Architecture Governance Framework defines a practical architecture governance model for aligning Enterprise, Solution, and Product Architecture.

It enables cross-division alignment without removing product autonomy. It supports solution-level integration of multiple products while allowing independent product releases. It defines quality markers so that architecture quality can be reviewed through evidence. It embeds architecture governance into agile@HENSOLDT and uses BAPO as an additive alignment lens.

The framework should be applied iteratively. It should begin with the most important enterprise guardrails, the most critical solution baselines, and the most relevant product architectures. Over time, review findings, system demos, Inspect & Adapt results, release evidence, and operational feedback should improve the framework itself.

The intended result is not more documentation. The intended result is better architectural alignment, faster integration, stronger release readiness, higher interoperability, stronger security, clearer ownership, and more reliable Software-Defined Defence capability delivery.

**How to Read this Document**

This document is structured from general architecture governance to concrete application. Chapters 1 to 5 define the overall framework. Chapters 6 to 8 define the actual guidelines for Enterprise, Solution, and Product Architecture. Chapters 9 and 10 define how architecture is reviewed and documented.

| **Reader**                  | **Most relevant chapters**        | **Why**                                                                                                         |
|-----------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Business Owner / Epic Owner | Chapters 1, 2, 3, 4, 5, 9         | Understand how business intent becomes architecture and how architecture evidence supports investment decisions |
| Enterprise Architect        | Chapters 1, 2, 3, 4, 5, 6, 9, 10  | Define and govern cross-division guardrails                                                                     |
| Solution Architect          | Chapters 2, 3, 4, 5, 7, 9, 10, 11 | Align multiple products into a releasable solution                                                              |
| Product Architect           | Chapters 3, 4, 5, 8, 9, 10, 11    | Produce implementable and verifiable product architecture evidence                                              |
| Product Owner               | Chapters 3, 5, 7, 8, 9            | Understand release compatibility, backlog impact, and evidence expectations                                     |
| Security Architect          | Chapters 4, 5, 6, 7, 8, 9, 10     | Ensure security-by-design across all architecture levels                                                        |
| Data Architect              | Chapters 4, 5, 6, 7, 8, 10        | Govern data models, semantics, metadata, provenance, and data contracts                                         |
| Platform / DevSecOps Owner  | Chapters 4, 5, 6, 7, 8, 9, 10     | Align runtime, deployment, observability, CI/CD, and automation                                                 |
| Architecture Review Board   | Chapters 5, 9, 10                 | Apply quality markers and review evidence                                                                       |

<span id="_Toc233730389" class="anchor"></span>Table 5: Anti-patterns and why to avoid them

**Core Document Rule**

The framework uses the BAPO model only as an **architecture alignment lens**.

BAPO expands the architecture challenge by asking whether business drivers, architecture decisions, delivery processes, and ownership responsibilities are aligned. It does not replace the architecture model, the architecture levels, the architecture quality markers, or the architecture evidence requirements.

- Business drives Architecture.

- Architecture drives Processes.

- Processes drive Organization.

In this framework, BAPO means:

- Business explains why architecture is needed.

- Architecture defines the structural response.

- Process defines the minimum delivery, integration, verification, release, or governance mechanism required.

- Organization defines the ownership needed so that architecture alignment does not break.

Figure 1 provides a one-page overview of the framework. It shows how business and mission drivers are translated through agile@HENSOLDT architecture governance into enterprise guardrails, solution baselines, architecture runway, and product evidence. BAPO and quality markers are shown as cross-cutting alignment mechanisms, while the feedback loop shows how reviews, demos, evidence, and Inspect & Adapt continuously improve the architecture system.

<img src="/workspace/SDD_Architecture_Governance_Framework_20260630v2_media/media/image2.png" style="width:8.96926in;height:5.3535in" />

<span id="_Ref233703209" class="anchor"></span>Figure 1: agile@HENSOLDT architecture governance at a glance, showing how business and mission drivers flow into enterprise guardrails, solution baselines, architecture runway, and product evidence, with BAPO, quality markers, and continuous feedback as cross-cutting alignment mechanisms.

# Purpose and Scope

## Purpose

The purpose of this framework is to define a common architecture governance model for Software-Defined Defence at HENSOLDT.

It provides architecture guidelines, quality markers, review criteria, and mandatory architecture evidence for three levels:

- Enterprise Architecture

- Solution Architecture

- Product Architecture

The framework ensures that software-defined defence capabilities are not developed as isolated products or local solutions, but as part of a coherent, interoperable, secure, scalable, and evolvable HENSOLDT architecture landscape.

The framework is intended to support architectural alignment across HENSOLDT divisions where Software-Defined Defence applies. It defines how technologies, interfaces, data models, security principles, deployment models, runtime platforms, DevSecOps practices, and quality expectations are aligned across the enterprise, while still allowing individual products and solutions to evolve independently.

Architecture governance is necessary because Software-Defined Defence creates dependencies across many parts of the enterprise. A product decision can influence a solution release. A solution interface can become an enterprise standard. A security decision at product level can affect operational trust at solution level. A data model decision can determine whether information can be reused across divisions.

For this reason, the framework separates the architecture landscape into three levels:

- Enterprise Architecture defines the common guardrails.

- Solution Architecture aligns multiple products into releasable capabilities.

- Product Architecture provides implementable and verifiable architecture evidence.

This separation gives each level a clear purpose while maintaining traceability between them. Enterprise Architecture must not become product micromanagement. Product Architecture must not redefine enterprise standards locally. Solution Architecture must act as the integration bridge between enterprise guardrails and product implementation.

The BAPO model is used in this framework only as an architectural alignment lens. It expands the architectural challenge by ensuring that business drivers, architecture decisions, delivery processes, and ownership responsibilities remain traceable across Enterprise, Solution, and Product Architecture. It does not replace the architecture guidelines, quality markers, or architecture evidence model.

## Governing Rule for BAPO

BAPO stands for Business, Architecture, Process and Organization. In this framework, BAPO is applied as an additive alignment model. It is used to check whether architecture decisions are connected to business intent, translated into explicit architecture structures, supported by the required delivery or governance mechanisms, and owned by accountable roles.

BAPO does not replace architecture principles, architecture guidelines, quality markers or technical evidence. It is not a separate process model and it does not turn this framework into an organization handbook. Instead, BAPO provides an alignment lens that makes architecture decisions more complete, traceable and executable.

The four BAPO dimensions are used as follows:

| **BAPO dimension** | **Meaning in this framework**                                                                                   | **Typical question**                                                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Business           | The business, mission, customer, strategic or product-line reason for the architecture decision.                | Why is this architecture decision needed, and which capability, mission outcome or business priority does it support?                        |
| Architecture       | The structural architecture response to the business need.                                                      | What guardrail, solution decision, product architecture decision, interface, data model, security rule, deployment model or ADR is required? |
| Process            | The delivery, verification, release or governance mechanism needed to make the architecture decision effective. | Which review, test, integration step, release rule, DevSecOps mechanism, exception process or feedback loop is required?                     |
| Organization       | The ownership and accountability required to maintain the decision and its consequences.                        | Who owns the decision, evidence, interface, data, security, platform, release compatibility or follow-up action?                             |

<span id="_Toc233730390" class="anchor"></span>Table 6: The Seven Outcomes of the SDD Architecture Governance Framework

The governing rule is that BAPO shall add alignment information without removing, replacing or diluting architecture content. A strong architecture decision must still define the architecture itself. BAPO then ensures that the decision is also linked to business value, executable through process, and owned by accountable roles.

Every relevant enterprise, solution and product architecture decision should therefore answer four questions:

> 1\. What business or mission need does the decision support?
>
> 2\. What architecture response is required?
>
> 3\. What process, verification, release or governance mechanism is needed?
>
> 4\. Who owns the decision, the evidence and the follow-up?

If one of these dimensions is missing, the architecture decision is incomplete. For example, an enterprise guardrail may be technically correct but ineffective if no adoption or exception process exists. A solution baseline may be architecturally sound but risky if product ownership or compatibility evidence is unclear. A product architecture decision may be locally valid but incomplete if it affects a solution interface, data contract, security boundary or release baseline without the required review.

BAPO shall therefore be used consistently across the framework as a cross-cutting traceability mechanism. It connects business intent to architecture decisions, architecture decisions to delivery and governance mechanisms, and those mechanisms to accountable ownership. This ensures that Software-Defined Defence architecture is not only designed, but also executable, reviewable, evidenced and continuously improved.

## Scope

This framework applies to software-defined defence architectures where HENSOLDT products, platforms, sensors, effectors, mission systems, data services, AI components, or integration capabilities must operate as part of a larger digital defence ecosystem.

It applies especially to architectures that involve one or more of the following characteristics:

- Cross-division software architecture alignment

- Multi-product solution integration

- Edge / Fog / Cloud deployment

- Heterogeneous sensors and effectors

- Open APIs and standardized data models

- Mission-critical communication

- Data-centric architecture

- DevSecOps and containerized deployment

- Cybersecurity and zero-trust principles

- Federated systems

- AI-supported data fusion and analysis

- Interoperability with NATO, EU, national, or partner systems

The framework is initially focused on Software-Defined Defence, not on the complete HENSOLDT enterprise architecture landscape. Hardware-only products, mechanical systems, and non-SDD enterprise IT capabilities are outside the initial scope unless they interact with software-defined defence solutions.

The framework should be applied especially when one or more of the following risks exists:

| **Risk**                                                  | **Why the framework is needed**                                                                |
|-----------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Multiple products must work together                      | Solution Architecture is needed to align interfaces, data, security, deployment, and releases  |
| Several divisions make technology decisions independently | Enterprise Architecture is needed to avoid fragmentation                                       |
| Products need independent releases                        | Compatibility rules and release declarations are needed                                        |
| Data must be reused across systems                        | Data contracts, semantic models, and ownership are needed                                      |
| Security spans product boundaries                         | Trust zones, identity, crypto, audit, and monitoring must be aligned                           |
| Runtime environments differ                               | Edge, fog, cloud, containerization, deployment, and observability assumptions must be explicit |
| Integration happens late                                  | Interface standards, contract testing, and architecture runway are needed earlier              |

<span id="_Toc233730391" class="anchor"></span>Table 7: agile@HENSOLDT operating model and architectural interpretation

For all in-scope architecture work, the BAPO chain is used as an alignment check. Architecture decisions, guardrails, quality markers, exceptions, and release criteria should be traceable from business need to architecture decision, from architecture decision to the minimum required delivery or governance process, and from process to ownership.

## Architecture Problem Statement

HENSOLDT’s Software-Defined Defence ambitions require a shift from product-centric architecture to enterprise-aligned, data-centric, interoperable, and continuously releasable architecture.

The key architectural problem is:

> HENSOLDT needs to align multiple divisions, product lines, technologies, interfaces, data models, deployment models, security approaches, and release models without slowing down product innovation.

The BAPO expansion clarifies this problem:

> HENSOLDT must translate Software-Defined Defence business strategy into cross-division enterprise guardrails, multi-product solution architectures, and implementable product architectures, while ensuring that the minimum required processes and ownership responsibilities are identified so that architecture alignment does not break during delivery.

The architecture problem is not only technical. It is a cross-level alignment problem.

At enterprise level, the challenge is to define guardrails that are strong enough to create consistency but flexible enough to allow innovation. At solution level, the challenge is to integrate multiple products into one operational capability while preserving product autonomy. At product level, the challenge is to create concrete, implementable architecture evidence that can be verified during development and release.

BAPO expands this problem by making clear that architecture alignment must remain connected to four questions:

| **BAPO question** | **Architecture interpretation**                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Business          | Why is this architecture needed?                                                       |
| Architecture      | What structural decision or guardrail is required?                                     |
| Process           | Which delivery, integration, verification, release, or governance mechanism is needed? |
| Organization      | Who owns the architecture decision and its evidence?                                   |

<span id="_Toc233730392" class="anchor"></span>Table 8: Levels and Architectural assignment

The framework must therefore prevent the following anti-patterns:

| **Anti-pattern**                 | **Why it is harmful**                                                                           |
|----------------------------------|-------------------------------------------------------------------------------------------------|
| Technology-first architecture    | Technology choices are made before business capability and mission value are clear              |
| Organization-first architecture  | Existing silos define architecture boundaries instead of value streams and mission capabilities |
| Process-first bureaucracy        | Processes are introduced without clear architectural need                                       |
| Product-first local optimization | Products optimize locally but break solution interoperability or enterprise standards           |
| Interface-after-implementation   | Interfaces are discovered too late during integration                                           |
| Security-after-design            | Security is added after architecture decisions are already fixed                                |
| Architecture without evidence    | Architecture claims are not verified by tests, demos, measurements, or release evidence         |

<span id="_Toc233730393" class="anchor"></span>Table 9: BAPO elements mapped to elements in agile@HENSOLDT and their resp. Architectural meaning

## Strategic Context

MDOcore is the primary strategic reference for this framework. MDOcore is HENSOLDTs software suite for Multi-Domain Operations, connecting sensors and command-and-control systems across land, air, sea, cyber, and space to create a unified and resilient real-time operational picture. Furthermore, MDOcore is based on open architectures, enabling rapid integration of HENSOLDT and third-party systems, supporting NATO and EU coalition interoperability, and operating across edge, fog, and cloud environments.

This means that the architecture governance framework must not only define documentation standards. It must enforce the architectural direction needed for MDOcore-like solutions:

- Open architecture

- Modularity

- Interoperability

- Common data models

- Software-defined deployment

- Edge / Fog / Cloud readiness

- Security by design

- Zero-trust and cryptography

- AI and data-science readiness

- Continuous integration, testing, and deployment

- Operational resilience under degraded communication

## Guiding Intent

The SDD Architecture Governance Framework shall achieve seven outcomes:

| **Outcome**                   | **Description**                                                                                                                         |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Business traceability         | Every major architecture decision is linked to a business capability, mission need, strategic theme, value stream, or customer outcome  |
| Enterprise alignment          | SDD-relevant divisions use compatible architecture guardrails for technologies, interfaces, data, security, runtime, and DevSecOps      |
| Solution coherence            | Multiple products can be aligned into one releasable solution capability                                                                |
| Product autonomy              | Products can release independently where compatibility with solution and enterprise guardrails is maintained                            |
| Process enablement            | Architecture identifies the delivery, integration, verification, release, and governance processes needed to make the architecture real |
| Organizational accountability | Architecture-relevant processes have clear ownership through roles, teams, system teams, shared services, or review bodies              |
| Evidence-based quality        | Architecture quality is proven through evidence, not asserted through intention                                                         |

<span id="_Toc233730394" class="anchor"></span>Table 10: Architecture decision flow through the agile@HENSOLDT operating model

# Agile@HENSOLDT Architecture Operating Model

## Operating Model Interpretation

This chapter explains how architecture governance is embedded into agile@HENSOLDT. Architecture must not operate as a separate control layer outside the delivery model. It must be part of portfolio decisions, solution planning, PI planning, system demos, Inspect & Adapt, release readiness, and continuous improvement.

The operating model spans several levels: Portfolio, Large Solution, Program or Agile Release Train, and Team. Each of these levels has a corresponding architecture concern. The framework uses these levels to place architecture decisions where they belong.

The agile@HENSOLDT operating model defines a scaled architecture and delivery structure with four practical levels:

- Portfolio / Enterprise

- Large Solution

- Program / Agile Release Train

- Team / Product

For architecture governance, these levels are interpreted as follows:

| **agile@HENSOLDT level** | **Architecture interpretation** | **Main responsibility**                                                                                                        |
|--------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Portfolio / Enterprise   | Enterprise Architecture         | Strategic guardrails, reference architectures, technology alignment, data architecture, security principles, architecture KPIs |
| Large Solution           | Solution Architecture           | Cross-product alignment, solution integration, solution release architecture, interoperability, shared quality attributes      |
| Program / ART            | Program / System Architecture   | Architecture runway, PI planning, system demos, integration readiness, technical enablers                                      |
| Team / Product           | Product Architecture            | Implementable architecture, product interfaces, ADRs, code-level quality, tests, release evidence                              |

<span id="_Toc233730395" class="anchor"></span>Table 11: Architecture Work Items

This interpretation ensures that architecture is not a separate governance bureaucracy. Architecture work is embedded into portfolio flow, solution train coordination, ART planning, product backlog refinement, system demos, Inspect & Adapt, and built-in quality.

The mapping from agile@HENSOLDT to architecture levels is important because it prevents two common problems.

The first problem is architecture centralization. If all architecture decisions are pushed to enterprise level, product teams lose speed and ownership. The second problem is architecture fragmentation. If all architecture decisions are left to individual products, solutions become difficult to integrate and enterprise alignment is lost.

The operating model solves this by assigning the right architecture responsibility to the right level.

| **Architecture question**                               | **Correct level**          |
|---------------------------------------------------------|----------------------------|
| What strategic guardrails apply across divisions?       | Enterprise Architecture    |
| How do several products become one releasable solution? | Solution Architecture      |
| Which enablers are needed in the next PI?               | Program / ART Architecture |
| How is the product implemented and verified?            | Product Architecture       |

<span id="_Toc233730396" class="anchor"></span>Table 12: BAPO Alignment Metadata for architecture work items

Figure 2 maps architecture responsibilities into the agile@HENSOLDT operating model. It clarifies where architecture work happens across Portfolio / Enterprise, Large Solution, Program / ART, and Team / Product levels, and identifies the key roles, work products, agile events, and outputs at each level.

<img src="/workspace/SDD_Architecture_Governance_Framework_20260630v2_media/media/image3.png" style="width:9.00353in;height:5.49685in" />

<span id="_Ref233703418" class="anchor"></span>Figure 2: Architecture responsibilities in the agile@HENSOLDT operating model, showing the architecture roles, work products, agile events, and outputs across Portfolio / Enterprise, Large Solution, Program / ART, and Team / Product levels.

## BAPO Alignment Interpretation

The agile@HENSOLDT operating model is interpreted as a BAPO alignment system:

- Business drives Architecture.

- Architecture drives Processes.

- Processes drive Organization.

In this framework, BAPO does not replace the agile@HENSOLDT architecture model. It expands the architectural challenge by making alignment needs visible.

| **BAPO element** | **agile@HENSOLDT elements**                                                                                                                                    | **Architecture meaning**                                                                                                               |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Business         | Strategic themes, Business Owners, portfolio canvas, lean budgets, value streams, customer needs, product-line needs, KPIs                                     | Defines why architecture work is needed and which capabilities must be enabled                                                         |
| Architecture     | Enterprise Architect, Solution Architect, System Architect, Product Architect, architecture guardrails, solution backlog, program backlog, architecture runway | Defines structural alignment across interfaces, data, technology, deployment, security, runtime, integration, and release architecture |
| Process          | Portfolio Kanban, PI Planning, solution train planning, system demos, Inspect & Adapt, DevSecOps, release readiness, architecture reviews                      | Defines the minimum planning, integration, verification, governance, and release mechanisms needed to maintain architecture alignment  |
| Organization     | Development Trinities, Solution Train, ARTs, teams, system team, shared services, communities of practice, architecture roles                                  | Defines who owns, builds, integrates, verifies, and evolves the architecture                                                           |

<span id="_Toc233730397" class="anchor"></span>Table 13: Architecture Events and Decision Points

The model must not be interpreted as organization driving architecture. Existing departments, silos, or historical product structures must not become the hidden architecture. Business intent drives architecture; architecture identifies the necessary processes; and those processes identify the required ownership.

The BAPO model should be used carefully. It does not mean that this framework defines the entire business model, process model, or organizational model of HENSOLDT. It means that architecture decisions must be complete enough to identify the business reason, the structural response, the required delivery mechanism, and the accountable owner.

This is especially important for Software-Defined Defence, because many architecture failures are not caused by missing diagrams. They are caused by missing ownership, unclear interface responsibilities, unplanned integration processes, or product releases that are not compatible with solution baselines.

Figure 3 explains how BAPO is used in this framework. BAPO is not treated as a replacement for Enterprise, Solution, or Product Architecture. It is used as an additive alignment lens that makes the business driver, architecture response, process implication, and ownership responsibility visible at every architecture level.

<img src="/workspace/SDD_Architecture_Governance_Framework_20260630v2_media/media/image4.png" style="width:8.59951in;height:5.47707in" />

<span id="_Ref233703593" class="anchor"></span>Figure 3: BAPO as an additive architecture alignment lens, showing how Business, Architecture, Process, and Organization considerations expand the alignment challenge across Enterprise, Solution, and Product Architecture.

## Architecture Flow 

Architecture decisions shall flow through the agile@HENSOLDT operating model in both directions. Top-down flow ensures that strategic themes, portfolio priorities and enterprise guardrails become executable solution and product architecture. Bottom-up flow ensures that implementation constraints, integration findings, technical debt, demo evidence and operational learning improve enterprise guardrails, solution baselines and future investment decisions.

The architecture flow is therefore not a one-way cascade. Enterprise Architecture provides direction and guardrails, Solution Architecture translates these guardrails into cross-product structures and release baselines, and Product Architecture implements and evidences the product-level decisions. At the same time, product implementation and solution integration continuously generate evidence, risks and improvement needs that must flow back upward.

The following table describes the main architecture flows through the agile operating model:

| **Flow type**                  | **Direction**   | **What flows**                                                                                                                                                               | **Governance intent**                                                                                                     | **Typical evidence / trigger**                                                                                         |
|--------------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Strategic-to-architecture flow | Top-down        | Strategic themes, portfolio priorities and business capabilities flow into enterprise guardrails, reference architectures and architecture runway.                           | Ensures that business strategy becomes explicit architecture direction.                                                   | Strategic theme, portfolio epic, capability map, enterprise guardrail, architecture roadmap                            |
| Enterprise-to-solution flow    | Top-down        | Enterprise guardrails flow into solution architecture decisions, product participation, interface standards, data alignment, security expectations and platform assumptions. | Ensures that solutions apply common enterprise expectations without losing necessary solution autonomy.                   | Reference architecture mapping, guardrail mapping, solution context, solution baseline                                 |
| Solution-to-product flow       | Top-down        | Solution architecture decisions flow into product architecture responsibilities, product interfaces, data contracts, compatibility expectations and backlog items.           | Ensures that product teams understand what they must implement, evidence and declare for solution compatibility.          | Product participation map, capability allocation, interface contract, product backlog item, compatibility requirement  |
| Product-to-solution flow       | Bottom-up       | Product constraints, implementation findings, interface issues, verification evidence and product debt flow into solution risk, solution debt and baseline updates.          | Ensures that solution architecture is corrected by real implementation and integration evidence.                          | Product demo result, contract-test finding, product debt item, compatibility declaration, integration issue            |
| Solution-to-enterprise flow    | Bottom-up       | Repeated solution risks, integration patterns, exceptions and shared technical debt flow into enterprise guardrail updates and architecture runway.                          | Ensures that enterprise guidance evolves when solution delivery reveals better patterns or systemic constraints.          | Exception pattern, solution debt trend, integration finding, architecture review action, guardrail improvement request |
| BAPO alignment flow            | Cross-cutting   | Business need is linked to architecture decision, process implication, ownership and evidence.                                                                               | Ensures that every architecture decision has business relevance, executable delivery mechanism and accountable ownership. | BAPO map, review record, RACI, backlog link, evidence link                                                             |
| Feedback and improvement flow  | Continuous loop | Demo evidence, integration findings, Inspect & Adapt actions, operational findings and architecture debt feed back into architecture decisions and portfolio actions.        | Ensures that architecture evolves from evidence rather than assumption.                                                   | System demo result, solution demo finding, Inspect & Adapt item, KPI trend, technical debt item, portfolio decision    |

<span id="_Toc233730398" class="anchor"></span>Table 14: Questions for architecture events

The BAPO model is not a waterfall. Business intent may trigger the initial architecture direction, but product implementation, integration results, system demos, release readiness reviews and operational findings must continuously update architecture guardrails, solution baselines, delivery processes and ownership structures.

The flow through the operating model should therefore be treated as continuous and evidence-driven. Enterprise guardrails must be stable enough to create cross-division alignment, but they must also evolve when product implementation and solution integration reveal better patterns, missing standards, unrealistic assumptions or new constraints.

For example, if several product teams request similar exceptions to an interface standard, this may indicate that the enterprise guardrail is incomplete, too restrictive or outdated. If a solution release repeatedly fails because of incompatible product interfaces, this may indicate that interface ownership, versioning rules or contract testing are not mature enough. If product teams cannot provide required security evidence, this may indicate missing DevSecOps enablement, unclear security guardrails or insufficient security architecture runway.

Architecture flow must therefore be traceable. A strategic theme should be traceable to enterprise guardrails, solution decisions, product architecture decisions, backlog items and evidence. Likewise, a technical debt item or integration finding should be traceable upward to the affected solution baseline, enterprise guardrail, process gap or portfolio decision.

The framework therefore expects architecture feedback to move upward as well as downward. Guardrails flow down. Evidence flows up. BAPO alignment ensures that the connection between business intent, architecture decision, delivery mechanism and ownership remains visible at every level.

## Architecture Work Items

Architecture work shall be represented explicitly in the agile@HENSOLDT operating model. Architecture must not remain hidden as informal design activity, unplanned technical work, or late-stage review feedback. If architecture work affects enterprise guardrails, solution integration, product structure, interfaces, data contracts, security, deployment, release compatibility or technical debt, it shall be visible as an architecture work item.

The purpose of architecture work items is to connect architecture decisions to planning, ownership, implementation and evidence. This ensures that architecture is not only discussed in reviews, but also translated into backlog items, enablers, verification activities, release criteria and improvement actions.

Architecture work items may exist at different levels of the agile operating model:

| **Work item**           | **Primary level**      | **Purpose**                                                                                                 | **Typical result / evidence**                                                                                                                             |
|-------------------------|------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Architecture Epic       | Enterprise / Portfolio | Captures a major architecture initiative with strategic or cross-division impact.                           | Enterprise guardrail, reference architecture, common data model, DevSecOps platform, technology governance decision, portfolio-level architecture roadmap |
| Architecture Capability | Solution               | Captures a cross-product architecture capability needed for one or more releasable solutions.               | Solution-wide identity model, topic model, data flow model, deployment model, integration environment, solution baseline                                  |
| Architecture Feature    | ART / Program          | Captures an implementable architecture increment within an ART or program context.                          | Interface implementation, shared service increment, integration mechanism, security capability, observability capability                                  |
| Architecture Enabler    | ART / Team             | Captures technical work required to enable future features, integration, verification or release readiness. | Architecture runway item, test framework, deployment automation, contract-test capability, simulator, refactoring activity                                |
| Architecture Story      | Product / Team         | Captures concrete product-level implementation work for an architecture decision.                           | Component change, interface update, ADR implementation, schema update, security control, test implementation                                              |
| Architecture Debt Item  | Any level              | Captures a known gap, deviation, risk or limitation that requires mitigation or accepted risk treatment.    | Technical debt record, mitigation plan, exception, risk item, improvement backlog item                                                                    |

<span id="_Ref233710682" class="anchor"></span>Table 15: Required architecture roles according tot he ADD Architecture Governance Framework

Architecture work items should be sized and governed according to their impact. Not every architecture concern requires an epic or capability. However, architecture work that affects multiple products, solution release compatibility, enterprise guardrails, security, data consistency or long-term platform direction should be visible above the team level. Product-internal architecture work may be handled as features, enablers or stories, provided that dependencies, evidence and ownership remain clear.

Each architecture work item should contain BAPO alignment metadata. This metadata ensures that the work item is not treated as a purely technical task. It must be clear why the work exists, what architecture response is required, which delivery or governance mechanism is affected, who owns the work, and what evidence will prove completion.

| **BAPO field**        | **Required content**                                                                                                                                           | **Purpose**                                                                                       |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Business driver       | Strategic theme, business capability, value stream, customer need, mission outcome, product contribution or solution capability                                | Explains why the architecture work is needed and which business or mission value it supports      |
| Architecture response | Enterprise guardrail, reference architecture, interface, data model, security decision, deployment decision, runtime decision, ADR or solution baseline change | Defines the architecture decision or structure that the work item must create, change or evidence |
| Process impact        | Required review, test, integration step, release rule, governance process, exception process, quality gate or DevSecOps pipeline change                        | Shows how the architecture work affects planning, verification, release or governance execution   |
| Organization owner    | Responsible role, team, architect, Product Owner, Product Architect, Solution Architect, System Architect, platform team, community of practice or review body | Clarifies who is accountable for implementation, review, evidence and follow-up                   |
| Evidence              | Document, model, ADR, test result, demo, interface contract, data contract, measurement, review record, release declaration or compatibility evidence          | Defines how completion and architecture quality will be demonstrated                              |

<span id="_Ref233710726" class="anchor"></span>Table 16: BAPO ownership responsibilities

The BAPO metadata should be lightweight but mandatory for architecture-relevant work. It prevents architecture items from becoming vague backlog entries such as “improve architecture” or “align interfaces”. A well-formed architecture work item should explain the business reason, the architecture change, the process consequence, the responsible owner and the evidence required.

Architecture work items should be reviewed at the appropriate agile event. Enterprise-level items should be visible in portfolio and enterprise architecture reviews. Solution-level items should be visible in solution planning, PI planning, integration reviews and release-readiness reviews. Product-level items should be visible in backlog refinement, team planning, product architecture reviews and demos.

If an architecture work item cannot identify its business driver, architecture response, process impact, owner or evidence, it is not yet ready for planning. It should be refined before it is accepted into the relevant backlog or used as the basis for a readiness decision.

## Architecture Events and Decision Points

Architecture governance must be embedded into the existing agile@HENSOLDT events and decision points. The purpose is not to create a parallel meeting structure. The purpose is to ensure that architecture decisions are made early enough, reviewed with the right evidence, translated into backlog work, and verified before product or solution release.

Architecture events should therefore be lightweight, but they must be evidence-based. Each event should clarify which architecture decision is being made or reviewed, which level is affected, which evidence exists or is missing, and which follow-up action is required.

The following events and decision points should be used to connect architecture governance with the agile operating model:

| **Event / decision point**         | **Primary architecture purpose**                                                                                  | **BAPO alignment question**                                                                                                           | **Typical evidence or result**                                                                        |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Portfolio Kanban                   | Evaluate architecture impact of epics, strategic investments and portfolio initiatives.                           | Is the business driver clear, and does the item require enterprise guardrails, architecture runway or strategic architecture funding? | Architecture impact assessment, strategic theme mapping, enterprise guardrail need, architecture epic |
| Portfolio Review                   | Check alignment with enterprise guardrails, SDD strategy, technology direction and investment priorities.         | Are architecture investments linked to value streams, strategic themes and business outcomes?                                         | Portfolio decision, architecture roadmap, technology decision, funding decision, guardrail update     |
| Solution Train Planning            | Align cross-product dependencies, product participation, interfaces, data flows and release architecture.         | Does the solution architecture define the integration, verification and release mechanisms required for the participating products?   | Product participation map, capability allocation, interface catalogue, solution baseline draft        |
| PI Planning                        | Plan architecture runway, enablers, dependencies, integration milestones and risk reduction.                      | Are architecture enablers owned by teams, planned in the backlog and connected to verification evidence?                              | Architecture enablers, PI objectives, dependency map, risk items, owner assignments                   |
| Architecture Review                | Review major architecture decisions, deviations, quality-marker scores and evidence sufficiency.                  | Are business intent, architecture response, process implication and ownership sufficiently clear to proceed?                          | Review record, ADR, quality-marker assessment, exception request, action list                         |
| System / Solution Demo             | Demonstrate architecture claims through integrated behavior and evidence.                                         | Does the demonstrated evidence prove the architecture decision, or does it reveal an architecture gap?                                | Demo result, integration evidence, test result, runtime evidence, follow-up action                    |
| Inspect & Adapt                    | Convert architecture findings, integration issues and recurring risks into improvement actions.                   | Do findings require changes to business priority, architecture, process, ownership or guardrails?                                     | Inspect & Adapt item, technical debt item, architecture runway item, guardrail improvement            |
| Architecture Community of Practice | Harmonize patterns, standards, templates, lessons learned and reusable architecture guidance.                     | Are lessons learned converted into reusable architecture assets or enterprise guardrails?                                             | Pattern, template, reference architecture update, lesson learned, community decision                  |
| Release Readiness Review           | Confirm that product or solution release evidence is complete, current and compatible with the relevant baseline. | Are business, architecture, process, ownership, compatibility and verification evidence complete?                                     | Product compatibility declaration, solution release baseline, release evidence, risk acceptance       |
| Exception Review                   | Decide whether a deviation from a guardrail, baseline or architecture rule is justified and controlled.           | Is the exception justified, owned, time-bounded, risk-assessed and linked to mitigation or feedback?                                  | Exception record, mitigation plan, owner assignment, review date, guardrail feedback                  |

<span id="_Toc233730401" class="anchor"></span>Table 17: BAPO Structure of Architecture Governance

Architecture events should not be treated as isolated architecture meetings. They should be integrated into the existing agile cadence wherever possible. Portfolio events should make enterprise architecture impact visible. Solution and PI planning should turn architecture decisions into enablers, dependencies and backlog items. Demos should provide evidence for architecture claims. Inspect & Adapt should convert findings into architecture improvement actions. Release readiness reviews should confirm that the required evidence is complete before release.

Each architecture-related event should answer three practical questions:

| **Question**                                          | **Purpose**                                                                              | **Typical outcome**                                                                  |
|-------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| What architecture decision is being made or reviewed? | Prevents vague architecture discussions and clarifies the affected architecture level.   | Decision statement, ADR, guardrail, baseline change, interface decision              |
| What evidence exists or is missing?                   | Prevents unverified claims and makes readiness assessable.                               | Test result, review record, demo evidence, quality-marker score, evidence gap        |
| What action is required next?                         | Converts findings into executable work instead of leaving them as observations.          | Backlog item, architecture enabler, technical debt item, exception, review follow-up |
| Who owns the follow-up?                               | Ensures that architecture decisions and findings do not remain unassigned.               | Named owner, responsible team, architect role, review body                           |
| When must it be reviewed again?                       | Keeps architecture risks, exceptions and debt from becoming permanent hidden weaknesses. | Review date, release milestone, PI objective, expiry date                            |

<span id="_Toc233730402" class="anchor"></span>Table 18: Enterprise Architecture, area and scope

The level of review should be proportional to the architecture impact. A local product design decision may only require product-level review and an ADR. A decision that affects several products, a solution baseline, enterprise data rules, security guardrails, platform direction or release compatibility requires broader review and explicit evidence.

The key rule is that architecture governance must create usable decisions, not meeting overhead. A successful architecture event produces one or more concrete outputs: a decision, an owner, an evidence expectation, a backlog item, an exception, a technical debt item, an architecture runway item or a guardrail update.

## Architecture Roles

Architecture governance requires clearly assigned responsibilities across Enterprise, Solution, Program / ART, Product and cross-cutting architecture concerns. The roles described in this section define architecture accountability, not reporting lines. Depending on the organizational context, one person may cover more than one role, or one role may be shared by several people. What matters is that the responsibility is explicit, owned and reviewable.

The architecture roles are required to ensure that guardrails, solution baselines, product decisions, interfaces, data models, security concerns, platform assumptions and quality evidence do not remain implicit. Each role contributes to the architecture flow described in Section 2.3: guardrails flow downward, while evidence, constraints, risks and technical debt flow upward.

The following architecture roles are required:

| **Role**                                 | **Primary level** | **Responsibility**                                                                                                                                                                                                                                                                                                                                                                                    | **Typical outputs / evidence**                                                                                                                                                             |
|------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Enterprise Architect                     | Enterprise        | Defines enterprise guardrails, reference architectures, strategic architecture alignment and cross-division architecture coherence.                                                                                                                                                                                                                                                                   | Enterprise guardrails, reference architectures, technology radar, architecture KPIs, exception decisions                                                                                   |
| Solution Architect                       | Solution          | Defines and governs the cross-product solution architecture and ensures that it can be implemented through architecture runway, enablers, integration planning and release readiness. The Solution Architect owns product participation, capability allocation, interfaces, data flows, security boundaries, deployment assumptions, solution baselines, integration risks and release compatibility. | Solution architecture, product participation map, capability allocation, solution baseline, architecture runway, integration architecture, architecture enablers, compatibility assessment |
| Product Architect                        | Product           | Owns product architecture, design decisions, interfaces, ADRs and product-level quality evidence.                                                                                                                                                                                                                                                                                                     | Product Architecture Document, ADRs, interface specifications, verification evidence, compatibility declaration                                                                            |
| Security Architect                       | Cross-cutting     | Ensures security-by-design, threat modelling, trust boundaries, zero-trust principles, crypto, logging, auditability and compliance alignment.                                                                                                                                                                                                                                                        | Threat models, trust-zone diagrams, security guardrails, security review records, risk treatment                                                                                           |
| Data Architect                           | Cross-cutting     | Owns data models, semantics, metadata, classification, provenance, data ownership and data lifecycle expectations.                                                                                                                                                                                                                                                                                    | Data models, semantic models, metadata rules, data ownership records, provenance rules                                                                                                     |
| Platform Architect                       | Cross-cutting     | Owns runtime, deployment, DevSecOps, observability, automation and platform architecture guardrails.                                                                                                                                                                                                                                                                                                  | Runtime reference architecture, deployment standards, CI/CD guardrails, observability standards                                                                                            |
| Architecture Review Board / Review Forum | Cross-level       | Reviews quality markers, major architecture decisions, deviations, exceptions, risks and cross-level alignment issues.                                                                                                                                                                                                                                                                                | Review records, exception decisions, quality-marker assessments, escalation actions                                                                                                        |
| Architecture Community of Practice       | Cross-level       | Harmonizes architecture patterns, templates, lessons learned and reusable guidance across products, solutions and divisions.                                                                                                                                                                                                                                                                          | Patterns, templates, lessons learned, reference updates, community recommendations                                                                                                         |

<span id="_Toc233730403" class="anchor"></span>Table 19: Enterprise BAPO Alignment Challenge

The role model follows three primary architecture levels. Enterprise Architects define cross-division guardrails and strategic architecture alignment. Solution Architects translate these guardrails into coherent, releasable multi-product solutions and also ensure that the required architecture runway, integration mechanisms, technical dependencies and release evidence exist within the agile delivery model. Product Architects own the detailed architecture, implementation decisions, interfaces, ADRs and product-level evidence for individual products.

The roles in Table 14 define architecture accountability at different decision horizons. The Enterprise Architect is responsible for cross-division coherence and long-term guardrails. The Solution Architect is responsible for cross-product solution coherence and for making the solution architecture executable through architecture runway, enablers, integration planning, system or solution demos and release-readiness evidence. The Product Architect owns the concrete product architecture and the evidence needed for implementation, verification and release readiness.

The cross-cutting architecture roles ensure that security, data, platform, runtime and DevSecOps concerns are not treated as isolated product-level topics. These concerns frequently span several products, ARTs and solutions, and therefore require consistent ownership across architecture levels. The Architecture Review Board or Review Forum provides the cross-level review mechanism for major decisions, deviations, exceptions, risks and quality-marker assessments. The Architecture Community of Practice supports reuse, harmonization and learning, but does not replace formal decision ownership.

These roles should be understood as a collaboration model, not as a rigid hierarchy. Enterprise, Solution and Product Architects must continuously exchange information. Enterprise Architecture provides guardrails and reference direction. Solution Architecture translates them into integration and release structures. Product Architecture implements and evidences the concrete product decisions. Feedback from implementation, demos, integration, operation and technical debt must flow back upward into solution baselines, enterprise guardrails and portfolio decisions.

BAPO adds a second ownership view without turning this framework into an organization handbook. While Table 14 describes architecture roles, Table 16 clarifies how business ownership, architecture ownership, process ownership and organizational ownership work together. This is important because architecture decisions are only effective when the business driver is clear, the structural architecture response is owned, the required delivery or governance mechanisms are executed, and the necessary organizational responsibilities exist.

| **BAPO element** | **Primary ownership**                                                                                    | **Responsibility**                                                                                                                          | **Typical contribution**                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Business         | Business Owners, Epic Owners, Product Management, customer or product-line representatives               | Define capability need, mission value, strategic priority, funding and business acceptance criteria.                                        | Strategic themes, epics, capability priorities, value-stream alignment, product contribution statements           |
| Architecture     | Enterprise, Solution, Product and cross-cutting Architects                                               | Define structural decisions, architecture guardrails, solution baselines, product architecture and cross-cutting architecture expectations. | Guardrails, architecture decisions, ADRs, baselines, interface and data models, quality-marker evidence           |
| Process          | RTE, STE, Product Owners, Scrum Masters / Team Coaches, Quality, DevSecOps, Release Management           | Define and execute the planning, integration, testing, release, governance and improvement mechanisms required by architecture.             | PI planning input, backlog items, test plans, CI/CD evidence, release checks, Inspect & Adapt actions             |
| Organization     | Line management, agile leadership, shared services, platform teams, architecture communities of practice | Ensure that required roles, teams, skills, ownership structures and decision forums exist.                                                  | Role assignments, team ownership, RACI, communities of practice, escalation paths, staffing or capability actions |

<span id="_Toc233730404" class="anchor"></span>Table 20: Enterprise Architecture Decision Rights

Table 15 should be used as an ownership check for architecture decisions and architecture work items. It does not replace the architecture role model in Table 14. Instead, it ensures that architecture decisions are connected to business intent, executable delivery mechanisms and accountable organizational ownership.

If one of the BAPO ownership dimensions is unclear, the architecture decision is incomplete. For example, a technically sound architecture decision may still be weak if the business driver is not clear, if no delivery mechanism exists, if the responsible product or interface owner is missing, or if the required governance forum is not defined. Such gaps should be resolved before the decision is treated as architecture-ready or release-relevant.

# Architecture Governance Levels

## BAPO Structure of Architecture Governance

This chapter is the structural core of the framework. It defines the three architecture governance levels: Enterprise, Solution, and Product. These levels are not optional categories. They are required to prevent architectural concerns from being handled at the wrong level.

Enterprise Architecture provides alignment across divisions. Solution Architecture aligns multiple products into a releasable capability. Product Architecture provides the concrete design and evidence required for implementation and release.

The levels must work together. Enterprise guardrails without solution adoption remain theoretical. Solution architecture without product evidence remains unproven. Product architecture without enterprise and solution alignment creates local optimization and long-term integration risk.

Each architecture level is governed through the same additive BAPO logic.

| **BAPO element** | **Governance question**                                                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Business         | Which business capability, mission outcome, value stream, strategic theme, customer need, or product-line objective is addressed?                                 |
| Architecture     | Which structural architecture decision, guardrail, interface, data model, security model, deployment model, product boundary, or integration pattern is required? |
| Process          | Which delivery, integration, verification, release, governance, or improvement mechanism is required to maintain architecture alignment?                          |
| Organization     | Which role, team, train, community, review body, or owner is accountable for the architecture concern?                                                            |

<span id="_Toc233730405" class="anchor"></span>Table 21: Mandatory Enterprise Architecture Deliverables

Enterprise, Solution, and Product Architecture differ in scope, but not in BAPO alignment logic.

BAPO is used at each architecture level in a different way. At enterprise level, the business concern is strategic alignment. At solution level, the business concern is integrated capability delivery. At product level, the business concern is concrete product contribution.

The architecture response also differs by level. Enterprise Architecture defines guardrails. Solution Architecture defines cross-product structure. Product Architecture defines implementable design.

The same is true for process and ownership. Enterprise-level processes are about governance, standards, and exceptions. Solution-level processes are about integration, verification, and release baselines. Product-level processes are about development, testing, CI/CD, release evidence, and technical debt control.

Figure 4 introduces the three-level architecture governance stack. Enterprise Architecture defines guardrails, Solution Architecture aligns multiple products into releasable capabilities, and Product Architecture provides implementable and verifiable evidence. Guardrails flow downward, while evidence, risks, technical debt, and improvement findings flow upward.

<img src="/workspace/SDD_Architecture_Governance_Framework_20260630v2_media/media/image5.png" style="width:8.67876in;height:5.49587in" />

<span id="_Ref233703763" class="anchor"></span>Figure 4: Enterprise-Solution-Product Architecture Stack, showing the relationship between cross-division enterprise guardrails, multi-product solution architecture, and product-level architecture evidence.

## Enterprise Level Architecture

### Purpose

Enterprise Architecture defines the common architecture direction for Software-Defined Defence across HENSOLDT divisions.

Its purpose is to ensure that all SDD-relevant divisions can build compatible products and solutions by using aligned:

- Architecture principles

- Reference architectures

- Interface standards

- Technology choices

- Data models

- Security principles

- Deployment models

- Runtime assumptions

- DevSecOps practices

- Architecture KPIs

Enterprise Architecture does not design individual products. It defines the guardrails within which product and solution architectures operate.

At enterprise level, BAPO means that business strategy and portfolio priorities define the architecture guardrails. These guardrails define the minimum governance, exception, technology, data, security, and DevSecOps processes needed for alignment. Those processes define the required enterprise architecture roles, communities of practice, and ownership structures.

Enterprise Architecture should be understood as the architecture discipline that protects long-term coherence. It must define the standards and reference models that allow different divisions and product lines to contribute to Software-Defined Defence without creating incompatible islands.

The enterprise level is especially important for decisions that are expensive to change later. Examples include interface standards, data models, identity models, cryptographic principles, deployment models, containerization assumptions, observability expectations, and technology lifecycle decisions.

Enterprise Architecture should therefore be strict where cross-division alignment matters and flexible where local product autonomy does not endanger interoperability, security, maintainability, or release compatibility.

### Enterprise Level Architecture Scope

Enterprise Architecture governs architecture areas that must remain consistent across HENSOLDT divisions where Software-Defined Defence applies. This does not mean that Enterprise Architecture controls all local product or solution design decisions. It means that Enterprise Architecture defines the common guardrails for topics where inconsistent local decisions would create cross-division fragmentation, integration risk, security gaps, data incompatibility, technology divergence, or release incompatibility.

Enterprise Architecture therefore focuses on architecture concerns that have enterprise-wide or cross-solution impact, such as interface standards, data and semantic models, technology choices, security principles, runtime and deployment assumptions, DevSecOps expectations, reference architectures, and architecture KPIs. Product- or solution-specific implementation details remain owned at the Solution and Product Architecture levels unless they affect these shared enterprise concerns.

| **Area**                         | **Enterprise-level responsibility**                                                                           |
|----------------------------------|---------------------------------------------------------------------------------------------------------------|
| Strategic architecture direction | Define the target direction for Software-Defined Defence                                                      |
| Reference architectures          | Define approved patterns such as MDOcore, edge/fog/cloud, DevSecOps, data architecture, security architecture |
| Interface standards              | Define mandatory API, messaging, topic, protocol, and data exchange standards                                 |
| Technology alignment             | Maintain approved, tolerated, deprecated, and forbidden technologies                                          |
| Data architecture                | Define common data models, semantic concepts, metadata, provenance, and lifecycle rules                       |
| Security architecture            | Define zero-trust, crypto, identity, audit, monitoring, and trust-zone principles                             |
| Platform architecture            | Define containerization, runtime, deployment, observability, and CI/CD principles                             |
| Architecture KPIs                | Measure alignment, interoperability, reuse, technical debt, and release readiness                             |

<span id="_Toc233730406" class="anchor"></span>Table 22: Enterprise Architecture Quality Markers

### Enterprise Level BAPO Alignment Challenge

At enterprise level, the BAPO alignment challenge is to translate HENSOLDT’s Software-Defined Defence strategy into architecture guardrails that can be applied consistently across divisions without constraining necessary product and solution autonomy. Business priorities such as interoperability, digital sovereignty, faster capability evolution and product-line reuse must be reflected in enterprise architecture decisions for interfaces, data models, technology standards, security, runtime platforms and DevSecOps.

These architecture decisions must then define the minimum governance processes required to maintain alignment, such as guardrail reviews, exception handling, adoption tracking and KPI monitoring. Clear ownership is required so that enterprise architects, data owners, security owners, platform owners and architecture communities can keep the guardrails current, usable and aligned with evolving business and mission needs.

| **BAPO view** | **Enterprise architecture alignment challenge**                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------------------|
| Business      | Align SDD strategy, value streams, product-line strategy, portfolio priorities, and cross-division capability needs        |
| Architecture  | Define guardrails for interfaces, technologies, data, security, platforms, DevSecOps, and reference architectures          |
| Process       | Ensure guardrails are reviewed, exceptions are managed, technology choices are governed, and architecture KPIs are tracked |
| Organization  | Assign ownership for enterprise standards, data, interfaces, security, platforms, and architecture communities             |

<span id="_Toc233730407" class="anchor"></span>Table 23: Solution Architecture Scope

### Enterprise Level Architecture Decision Rights

Enterprise Architecture owns architecture decisions when the decision has cross-division, cross-solution, or long-term strategic impact. This applies when inconsistent local decisions would reduce interoperability, create duplicated or incompatible technologies, weaken security, fragment data models, complicate integration, or make product and solution releases harder to govern.

Enterprise decision rights therefore apply to shared architecture concerns such as reference architectures, mandatory interface standards, enterprise data and semantic models, technology lifecycle rules, security guardrails, runtime and deployment assumptions, DevSecOps expectations, architecture KPIs, and exception governance. They do not give Enterprise Architecture authority to design every product or solution in detail. Local implementation decisions remain with Solution and Product Architecture unless they affect shared enterprise guardrails or create risk beyond the local product boundary.

| **Decision right**      | **Example**                                                                                |
|-------------------------|--------------------------------------------------------------------------------------------|
| Interface standards     | Which interface standards are mandatory?                                                   |
| Data standards          | Which data models, schemas, metadata, and semantic concepts are approved?                  |
| Technology governance   | Which technologies are strategic, approved, tolerated, deprecated, or forbidden?           |
| Security guardrails     | Which identity, crypto, zero-trust, audit, and monitoring patterns are mandatory?          |
| Reference architectures | Which reference architectures must be reused?                                              |
| Runtime standards       | Which platform, containerization, deployment, and observability assumptions are mandatory? |
| Exception governance    | Which deviations require formal approval and expiration dates?                             |
| Portfolio investment    | Which cross-division architecture gaps require portfolio funding?                          |

<span id="_Toc233730408" class="anchor"></span>Table 24: Solution BAPO Alignemnt Challenge

Enterprise Architecture must avoid over-centralization. It should define guardrails, not micromanage implementation.

### Enterprise Level Architecture Deliverables

The following deliverables define the minimum set of enterprise-level architecture assets required to create cross-division alignment for Software-Defined Defence. These deliverables are not intended as documentation for its own sake. They provide the shared guardrails, standards, reference models and evidence needed by Solution and Product Architecture to make consistent decisions across interfaces, technologies, data, security, runtime, DevSecOps and release compatibility.

Each enterprise deliverable should be owned, versioned, published in a discoverable location and reviewed regularly. Solution and Product Architects must be able to understand which enterprise deliverables apply to their work, how compliance is demonstrated and how deviations are requested. Where a deliverable is not yet mature, this should be made visible as enterprise architecture runway or enterprise technical debt.

| **Deliverable**                             | **Description**                                                                                             |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| SDD Architecture Principles                 | Common principles for Software-Defined Defence                                                              |
| Enterprise Reference Architecture Catalogue | Approved patterns for MDOcore, edge/fog/cloud, data, security, DevSecOps, runtime                           |
| Technology Radar                            | Strategic, approved, tolerated, deprecated, and prohibited technologies                                     |
| Interface Standards Catalogue               | APIs, messaging, topic models, eventing, schema formats, protocol standards                                 |
| Enterprise Data Model / Semantic Model      | Common data concepts, metadata, provenance, information model, and lifecycle rules                          |
| Security Architecture Guardrails            | Identity, crypto, zero-trust, trust zones, audit, monitoring                                                |
| Deployment and Runtime Guardrails           | Containerization, orchestration, service discovery, CI/CD, observability                                    |
| Architecture KPI Dashboard                  | Measurement of alignment, reuse, technical debt, and release readiness                                      |
| Architecture Exception Register             | Approved deviations, rationale, owner, and expiration date                                                  |
| Enterprise BAPO Traceability Map            | Links strategic themes and business capabilities to enterprise guardrails, processes, and owners            |
| Enterprise Process Impact Register          | Identifies which architecture guardrails require new or changed governance, delivery, or release mechanisms |
| Enterprise Ownership Model                  | Defines owners for data, interfaces, platforms, security, DevSecOps, and architecture communities           |

<span id="_Toc233730409" class="anchor"></span>Table 25: Solution Architecture Decision Rights

### Enterprise Level Architecture Quality Markers

Enterprise Architecture quality is achieved when the enterprise guardrails for Software-Defined Defence are not only defined, but also adopted, evidenced and improved across divisions. Quality at this level is therefore measured by how well Enterprise Architecture enables consistent decisions for interfaces, technologies, data models, security principles, runtime platforms, DevSecOps and release compatibility without unnecessarily restricting solution or product autonomy.

The enterprise quality markers below are used to assess whether Enterprise Architecture provides usable and effective alignment mechanisms. They check whether strategic intent is translated into guardrails, whether reference architectures and standards are available, whether solutions and products can apply them, whether deviations are controlled, and whether adoption and technical debt are visible through evidence. A marker is only meaningful if it can be reviewed through concrete artifacts such as catalogues, standards, architecture reviews, KPI dashboards, exception registers, adoption evidence or improvement actions.

| **Marker**                         | **Question**                                                                                                                                    |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| E0 BAPO traceability               | Are enterprise guardrails traceable from business strategy to architecture decision, minimum process requirement, and organizational ownership? |
| E1 Strategic alignment             | Does the architecture support HENSOLDT SDD direction and MDOcore evolution?                                                                     |
| E2 Reference architecture adoption | Are products and solutions using approved reference architectures?                                                                              |
| E3 Interface standardization       | Are common interface standards defined and used?                                                                                                |
| E4 Technology alignment            | Are technology choices governed across divisions?                                                                                               |
| E5 Data model alignment            | Are common data models, semantics, metadata rules, and lifecycle rules defined?                                                                 |
| E6 Security-by-design              | Are zero-trust, cryptography, identity, audit, and monitoring principles defined?                                                               |
| E7 DevSecOps readiness             | Are CI/CD, automated testing, and secure deployment guardrails defined?                                                                         |
| E8 Reuse and modularity            | Are reusable components, services, and platforms encouraged and measured?                                                                       |
| E9 Technical debt transparency     | Is enterprise-level technical debt visible and funded?                                                                                          |
| E10 Release compatibility          | Can solutions and products release without breaking enterprise standards?                                                                       |

<span id="_Toc233730410" class="anchor"></span>Table 26: Mandatory Solution Architecture

## Solution Level Architecture

### Purpose

Solution Architecture aligns multiple products into one coherent releasable solution.

A solution may contain 5–10 single products, each with its own product roadmap, backlog, and release cycle. The solution architecture ensures that these products work together as a system-of-systems.

A solution architecture must enable two release modes:

- Solution Release

- Product Release

A solution release is a coordinated release of multiple products as one integrated solution. A product release is an independent release of one product that remains compatible with the solution architecture.

MDOcore is the primary example of such a solution. HENSOLDT describes MDOcore as a software-centered integration framework that networks sensors, effectors, cognitive systems, weapon systems, and command capabilities across land, air, sea, cyber, and space.

At solution level, BAPO means that the business capability defines the solution architecture. The solution architecture defines the integration, verification, compatibility, and release mechanisms. These mechanisms define the required solution train, system team, product architect alignment, and cross-product ownership model.

Solution Architecture is where the practical complexity of Software-Defined Defence becomes visible. A solution may depend on five to ten products, several ARTs, external systems, suppliers, shared platforms, and cross-domain data flows. Each product may have its own roadmap and release cycle, but the solution must still behave as one coherent operational capability.

For this reason, Solution Architecture must define not only what the solution contains, but also how the products remain compatible over time. A solution release baseline is therefore one of the most important architecture artifacts. It defines which product versions, interface versions, data model versions, security baselines, and deployment configurations work together.

### Solution Level Architecture Scope

Solution Architecture governs the architecture concerns that arise when multiple products must work together as one coherent and releasable solution. It does not replace Product Architecture and does not define every internal product design decision. Instead, it defines the cross-product structure required for integration, interoperability, security, data consistency, deployment alignment and release compatibility.

Solution Architecture therefore focuses on the boundaries and dependencies between products. It defines which products participate in the solution, which capabilities each product contributes, how interfaces and data flows are aligned, how security and trust boundaries span the solution, how the integrated runtime and deployment model works, and how product releases remain compatible with the solution baseline. Product-specific implementation details remain owned by Product Architecture unless they affect the solution boundary, shared interfaces, data contracts, integration behavior or release compatibility.

| **Area**                 | **Solution-level responsibility**                                                                    |
|--------------------------|------------------------------------------------------------------------------------------------------|
| Solution context         | Define participating products, systems, users, suppliers, and external interfaces                    |
| Capability decomposition | Map solution capabilities to products and ARTs                                                       |
| Cross-product interfaces | Define interface contracts, ownership, versions, and compatibility rules                             |
| Data flow architecture   | Define how data moves across products and domains                                                    |
| Security architecture    | Define trust boundaries, identity, access, crypto, logging, and audit across products                |
| Runtime and deployment   | Define integrated deployment topology and runtime dependencies                                       |
| Release architecture     | Define solution release packages and independent product release compatibility                       |
| Integration strategy     | Define test environments, integration sequence, and system demo evidence                             |
| Quality attributes       | Define solution-level performance, resilience, security, scalability, and interoperability scenarios |
| Technical debt           | Track cross-product debt and architecture risks                                                      |

<span id="_Toc233730411" class="anchor"></span>Table 27: Solution Release Model

### Solution BAPO Alignment Challenge

At solution level, the BAPO alignment challenge is to translate a business or mission capability into a coherent architecture that aligns multiple products into one releasable solution. Business needs such as customer value, mission effectiveness, interoperability and release agility must be reflected in solution architecture decisions for product participation, capability allocation, cross-product interfaces, data flows, security boundaries, deployment topology and solution baselines.

These architecture decisions must define the minimum integration, verification and release processes required to keep the products compatible, including contract testing, solution demos, compatibility checks and release planning. Clear ownership is required across the Solution Architect, Product Architects, interface owners, data owners, security owners and system team so that the solution remains integrated, verifiable and releasable while individual products can continue to evolve.

| **BAPO view** | **Solution architecture alignment challenge**                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------------------------------|
| Business      | Deliver one mission/business capability from 5–10 products                                                                         |
| Architecture  | Align product capabilities, interfaces, data contracts, security boundaries, runtime topology, deployment, and release baselines   |
| Process       | Define integration cadence, compatibility checks, contract testing, verification, system demos, and solution release process       |
| Organization  | Assign solution architect, product architects, interface owners, data owners, security owners, system team, and integration owners |

<span id="_Toc233730412" class="anchor"></span>Table 28: Content required for Solution Release Baselinie

### Solution Architecture Decision Rights

Solution Architecture owns architecture decisions when the decision affects how multiple products work together as one integrated and releasable solution. This includes decisions where inconsistent product-level choices would create integration risk, incompatible interfaces, fragmented data flows, unclear security boundaries, deployment conflicts, duplicated solution logic, or release incompatibility.

Solution Architecture decision rights therefore apply to cross-product concerns such as product participation, capability allocation, interface and data contract alignment, solution-level security and trust boundaries, integrated runtime and deployment topology, solution baselines, integration sequencing, verification strategy and release compatibility. They do not give Solution Architecture authority to redesign the internal architecture of each participating product. Product-internal implementation decisions remain with Product Architecture unless they affect shared interfaces, solution behavior, integration evidence, security boundaries or the ability to release the solution as a coherent capability.

| **Decision right**       | **Example**                                                                         |
|--------------------------|-------------------------------------------------------------------------------------|
| Product participation    | Which products are part of the solution?                                            |
| Capability allocation    | Which product owns which solution capability?                                       |
| Cross-product interfaces | Which interfaces are required between products?                                     |
| Data contracts           | Which schemas, topics, data models, and semantic concepts are mandatory?            |
| Release compatibility    | Which product releases are compatible with which solution release?                  |
| Cross-product security   | Which trust boundaries, identities, crypto patterns, and audit rules are mandatory? |
| Solution quality         | Which quality scenarios must be verified at solution level?                         |
| Architecture runway      | Which technical enablers are required before release?                               |

<span id="_Toc233730413" class="anchor"></span>Table 29: Required Compatibility Evidence for the Solution Level

### Solution Level Architecture Deliverables

The following deliverables define the minimum set of solution-level architecture assets required to make multiple products work together as one coherent, integrated and releasable solution. These deliverables are not intended as documentation for its own sake. They define the solution baseline, cross-product interfaces, data flows, security boundaries, deployment assumptions, integration approach, verification evidence and release compatibility expectations needed to govern the solution.

Each solution deliverable should be owned, versioned and aligned with the applicable enterprise guardrails. Product Architects must be able to understand which solution decisions affect their products, which interfaces and data contracts must be implemented, which evidence is required, and how product releases are assessed for compatibility with the solution baseline. Where a deliverable is incomplete or unstable, the gap should be made visible as solution architecture runway, integration risk or solution-level technical debt.

| **Deliverable**                      | **Description**                                                                                                  |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Solution Architecture Document       | Full architecture description of the integrated solution                                                         |
| Product Participation Map            | Products, ARTs, suppliers, and ownership model                                                                   |
| Solution Capability Map              | Capabilities and their allocation to products                                                                    |
| Cross-Product Interface Catalogue    | APIs, topics, schemas, protocols, events, and ownership                                                          |
| Solution Data Flow Model             | Data movement, transformation, storage, and consumption across products                                          |
| Solution Release Model               | Definition of solution releases and compatible product releases                                                  |
| Integrated Deployment View           | Runtime, infrastructure, environment, and deployment topology                                                    |
| Solution Security Concept            | Threat model, trust zones, identity, crypto, logging, monitoring                                                 |
| Solution Quality Attribute Scenarios | Testable scenarios for performance, resilience, interoperability, and security                                   |
| Integration and Verification Matrix  | What must be proven, where, when, and by whom                                                                    |
| Solution Technical Debt Register     | Cross-product risks, gaps, mitigations, and owners                                                               |
| Solution BAPO Map                    | Links solution capability to product architecture decisions, integration processes, and organizational ownership |
| Product Compatibility Matrix         | Shows which product releases are compatible with which solution baseline                                         |
| Cross-Product Ownership Matrix       | Defines interface owners, data owners, security owners, and integration owners                                   |
| Solution Process Model               | Defines integration, verification, solution demo, and release mechanisms required by the solution architecture   |

<span id="_Toc233730414" class="anchor"></span>Table 30: Solution Level Quality Markers

### Solution Release Model

The solution release model defines how independently evolving product releases are combined, verified and governed as one coherent solution release. It must distinguish between product-level release artifacts and solution-level release artifacts, because a product may be technically releasable on its own but still not be compatible with a specific solution baseline.

The purpose of this distinction is to make release readiness explicit. Product releases provide the implemented product version, product evidence and product-level compatibility declaration. The solution release baseline defines which product versions, interface versions, data contract versions, deployment assumptions, security baseline and verification evidence belong together for a specific integrated solution release.

| **Artifact**                 | **Definition**                                                                                                                       |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Solution Baseline            | A defined combination of product versions, interface versions, data model versions, security baseline, and deployment configurations |
| Product Release              | A release of a single product that must remain compatible with one or more solution baselines                                        |
| Solution Release Candidate   | A candidate combination of product releases verified in an integrated environment                                                    |
| Operational Solution Release | A verified, accepted, and deployable solution baseline                                                                               |

<span id="_Toc233730415" class="anchor"></span>Table 31: Product Level Architecture Scope

A solution release baseline is more than a list of product versions. It is an architecture alignment artifact that defines which product releases, interface versions, data contracts, deployment assumptions, security constraints and verification evidence belong together for one coherent solution release.

Its purpose is to make cross-product compatibility explicit. The baseline shows that the participating products do not only work individually, but also fit together at solution level. It therefore provides the architectural evidence needed to assess integration readiness, release compatibility, security consistency, data alignment and compliance with applicable enterprise guardrails.

| **BAPO element** | **Required content for a solution release baseline**                                                                            |
|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Business         | Solution capability, customer value, operational scenario, and release objective                                                |
| Architecture     | Product versions, interface versions, data model versions, runtime configuration, security baseline, and deployment topology    |
| Process          | Integration tests, compatibility checks, system demo, release approval, rollback process, and evidence collection               |
| Organization     | Release owner, solution architect, product owners, product architects, system team, integration owners, and verification owners |

<span id="_Toc233730416" class="anchor"></span>Table 32: Product-Level Architecture Responsibilities for BAPO Alignment

A solution release baseline is the architectural contract for a releasable solution. It defines which product versions, interface versions, data model versions, security assumptions, runtime configurations, and deployment settings are known to work together.

The solution baseline should be maintained as a living artifact. Product teams should know which solution baselines they support. Solution release decisions should be based on verified compatibility, not on assumed compatibility.

### Compatibility Rules for the Solution Level

Every product that participates in a solution must declare compatibility with the applicable solution release baseline. This declaration confirms that the product release is not only internally releasable, but also compatible with the solution-level interface versions, data contracts, security assumptions, deployment model, runtime dependencies and verification expectations defined for that solution.

Compatibility must therefore be assessed against a specific solution baseline, not in isolation. A product can be technically ready for release on its own and still be incompatible with a particular solution if interfaces have changed, data semantics are misaligned, security assumptions differ, deployment constraints are not met, or required integration evidence is missing. The Product Architect is responsible for providing the product-level compatibility declaration and supporting evidence. The Solution Architect is responsible for assessing whether the participating products together form a coherent, integrated and releasable solution.

The compatibility declaration should be updated whenever the product release, solution baseline, interface contract, data contract, security baseline, deployment topology or integration evidence changes.

| **Compatibility evidence**          | **Description**                                                         |
|-------------------------------------|-------------------------------------------------------------------------|
| Supported solution baseline         | Identifies which solution baseline the product release supports         |
| Implemented interface versions      | Lists API, topic, event, protocol, and schema versions                  |
| Implemented data model versions     | Lists data model, semantic model, and metadata compatibility            |
| Supported deployment configurations | Lists runtime, container, infrastructure, and environment assumptions   |
| Security compatibility              | Confirms identity, crypto, trust-zone, logging, and audit compatibility |
| Known limitations                   | Describes limitations, degraded behavior, and restrictions              |
| Migration notes                     | Describes upgrade, downgrade, migration, and rollback considerations    |
| Backward compatibility statement    | States whether older solution baselines remain supported                |
| Test evidence                       | Provides contract, integration, security, and release evidence          |

<span id="_Toc233730417" class="anchor"></span>Table 33: Mandatory Product Level Architecture Deliverables

Independent product releases are a key advantage of modular Software-Defined Defence architectures. They allow products to evolve faster without forcing a full solution release every time. However, this only works if compatibility is governed.

A product release may be independent, but it is not isolated. It must declare which solution baselines it supports, which interface versions it implements, which data model versions it uses, and which limitations apply.

### Solution Level Quality Markers

Solution-level quality markers are used to assess whether the solution architecture is sufficiently coherent, integrated and releasable across all participating products. They focus on the architecture quality that emerges between products, not only inside individual products. This includes cross-product interfaces, data flows, security boundaries, deployment alignment, integration readiness, solution baselines, verification evidence and release compatibility.

The markers below define the initial minimum assessment set for Solution Architecture. They should be used during solution architecture reviews, PI planning, integration reviews, system or solution demos, Inspect & Adapt, and release readiness reviews. A marker should only be considered mature when it is supported by concrete evidence, such as interface contracts, data contracts, baseline records, compatibility declarations, integration test results, security reviews, deployment evidence, risk records or technical debt items.

The initial solution-level quality markers are:

| **Marker**                          | **Question**                                                                                                                                |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| S0 BAPO solution traceability       | Is the solution architecture traceable from business capability to architecture, integration/release process, and organizational ownership? |
| S1 Solution boundary clarity        | Are all participating products, systems, suppliers, external actors, and boundaries identified?                                             |
| S2 Capability allocation            | Is each solution capability allocated to one or more products?                                                                              |
| S3 Cross-product interface maturity | Are interfaces documented, versioned, owned, and tested?                                                                                    |
| S4 Data consistency                 | Are data contracts, schemas, topics, semantics, and ownership aligned across products?                                                      |
| S5 Solution release readiness       | Is the solution release package defined and verified?                                                                                       |
| S6 Product release compatibility    | Can products release independently without breaking the solution?                                                                           |
| S7 Integrated security              | Are cross-product trust zones, identity, access, crypto, logging, and audit defined?                                                        |
| S8 Integration testability          | Can solution behavior be verified in a production-like environment?                                                                         |
| S9 Resilience and degraded modes    | Are degraded cross-product scenarios defined and tested?                                                                                    |
| S10 Architecture runway             | Are required enablers planned before feature delivery depends on them?                                                                      |

<span id="_Toc233730418" class="anchor"></span>Table 34: Product Level Architecture Quality Markers

## Product Level Architecture

### Purpose

Product Architecture defines the implementable architecture of a single product.

A product architecture must be detailed enough for:

- Development

- Integration

- Security assessment

- Verification

- Certification support

- Release readiness

- Maintenance

- Future evolution

Product Architecture must not be generic. It must contain architecture evidence.

MDOcore Qube is a strong initial reference because its architecture document already contains context, scope, building blocks, runtime scenarios, deployment, cross-cutting concepts, ADRs, quality requirements, risks, technical debt, and MDOcore mapping.

At product level, BAPO means that the product’s business contribution defines the product architecture. The product architecture defines the backlog, CI/CD, testing, verification, release, and maintenance mechanisms. These mechanisms define team ownership, product architect responsibility, and quality accountability.

Product Architecture is where architecture becomes implementable. It must be detailed enough that developers can build the product, testers can verify it, security roles can assess it, integrators can connect it, and release owners can decide whether it is ready.

The product architecture is also the main place where architecture evidence is created. Product-level evidence includes interface tests, performance measurements, security test results, deployment manifests, ADRs, runtime scenarios, and technical debt records.

### Product Level Architecture Scope

Product Architecture governs the architecture of an individual product and ensures that the product can participate safely and reliably in one or more solutions. It covers both product-internal design decisions and the product’s externally visible integration responsibilities. Product-internal design includes building blocks, runtime behavior, deployment model, technology choices, quality attributes, security concept and architecture decision records. Product-external integration includes interfaces, data contracts, compatibility declarations, release evidence and alignment with applicable enterprise guardrails and solution baselines.

Product Architecture therefore owns the detailed architecture evidence for a product, but it does not define the complete solution architecture or enterprise guardrails by itself. The Product Architect is responsible for showing how the product is structured, how it behaves, how it is deployed, how it exposes or consumes interfaces, and how it satisfies quality, security and verification expectations. When a product participates in a solution, Product Architecture must provide the evidence needed by Solution Architecture to assess integration readiness and release compatibility.

| **Area**           | **Product-level responsibility**                                                         |
|--------------------|------------------------------------------------------------------------------------------|
| Product context    | Define users, external systems, boundaries, and constraints                              |
| Building blocks    | Define components, responsibilities, and interfaces                                      |
| Runtime behavior   | Define key operational scenarios                                                         |
| Deployment         | Define runtime nodes, containers, infrastructure, and resource assumptions               |
| Interfaces         | Define product APIs, topics, schemas, and protocols                                      |
| Quality attributes | Define measurable non-functional requirements                                            |
| Security           | Define product-level threat model, controls, crypto, logging, and vulnerability handling |
| ADRs               | Document major architecture decisions and rationale                                      |
| Verification       | Define architecture tests and evidence                                                   |
| Technical debt     | Track product-level architecture risks and gaps                                          |

<span id="_Toc233730419" class="anchor"></span>Table 35: Traceability Levels, purpose and evidence

### Product Level BAPO Alignment Challenge

At product level, the BAPO alignment challenge is to ensure that product architecture is connected to business value, delivery execution and accountable ownership. The following table does not describe the BAPO dimensions separately. Instead, it identifies the product-level architecture areas where BAPO alignment must be made explicit. For each area, the Product Architect must ensure that the business relevance is understood, the architecture responsibility is defined, the required delivery and verification mechanisms exist, and ownership is clear.

| **Area**           | **Product-level responsibility**                                                         |
|--------------------|------------------------------------------------------------------------------------------|
| Product context    | Define users, external systems, boundaries, and constraints                              |
| Building blocks    | Define components, responsibilities, and interfaces                                      |
| Runtime behavior   | Define key operational scenarios                                                         |
| Deployment         | Define runtime nodes, containers, infrastructure, and resource assumptions               |
| Interfaces         | Define product APIs, topics, schemas, and protocols                                      |
| Quality attributes | Define measurable non-functional requirements                                            |
| Security           | Define product-level threat model, controls, crypto, logging, and vulnerability handling |
| ADRs               | Document major architecture decisions and rationale                                      |
| Verification       | Define architecture tests and evidence                                                   |
| Technical debt     | Track product-level architecture risks and gaps                                          |

<span id="_Toc233730420" class="anchor"></span>Table 36: Principles Alignment

### Product Level Architecture Deliverables

At product level, architecture deliverables form the minimum evidence package required to understand, govern, integrate, verify and release an individual product. These deliverables show how the product contributes to business or mission value, how it is architected internally, how it exposes or consumes interfaces, how quality and security requirements are addressed, and how compatibility with solution baselines and enterprise guardrails is demonstrated.

The deliverables in the following table do not necessarily have to be separate standalone documents. They may be maintained as sections of a Product Architecture Document, controlled architecture artifacts, backlog-linked evidence, ADRs, registers, model views or tool-based records. What matters is that each deliverable is owned, versioned, reviewable and supported by evidence where required.

The mandatory product-level architecture deliverables are:

| **Deliverable**                           | **Description**                                                                                     |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Product Architecture Document             | Structured architecture description                                                                 |
| Context and Scope                         | Product boundary and external systems                                                               |
| Building Block View                       | Components, modules, and responsibilities                                                           |
| Runtime View                              | Main runtime scenarios                                                                              |
| Deployment View                           | Runtime nodes, containers, hardware assumptions                                                     |
| Interface Specification                   | APIs, topics, schemas, events, and protocols                                                        |
| ADR Register                              | Major decisions with rationale and consequences                                                     |
| Quality Requirement Catalogue             | Measurable product quality attributes                                                               |
| Product Security Concept                  | Threats, controls, crypto, identity, logging                                                        |
| Verification Evidence                     | Test reports, measurements, integration evidence                                                    |
| Risk and Technical Debt Register          | Known gaps, mitigation, owner, and due date                                                         |
| Product Business Contribution Statement   | Explains which business capability, solution capability, or mission outcome the product supports    |
| Product BAPO Map                          | Links product contribution to architecture decisions, development/release mechanisms, and ownership |
| Product Release Compatibility Declaration | Declares compatibility with solution baselines and enterprise guardrails                            |
| Product Process Evidence                  | Shows CI/CD, test, security, release, and debt-management mechanisms required by the architecture   |

<span id="_Toc233730421" class="anchor"></span>Table 37: Use Cases and how to apply principles

### Product Level Quality Markers

Product-level quality markers are used to assess whether an individual product architecture is complete, evidence-based, integration-ready and releasable. They focus on the architecture quality of the product itself, but also on the product’s ability to participate in solution baselines and comply with applicable enterprise guardrails. The markers therefore cover both internal product architecture concerns, such as building blocks, runtime behavior, deployment, security and technical debt, and externally visible concerns, such as interfaces, data contracts, compatibility evidence and release readiness.

The markers in the following table define the initial minimum assessment set for Product Architecture. They should be used during product architecture reviews, backlog refinement, PI planning, implementation reviews, demos, release readiness reviews and Inspect & Adapt. A marker should only be considered mature when it is supported by concrete evidence, such as architecture views, interface specifications, data contracts, ADRs, test results, deployment records, security evidence, observability data, compatibility declarations or technical debt records.

The initial product-level quality markers are:

| **Marker**                     | **Question**                                                                                                                                                   |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P0 Product BAPO traceability   | Is the product architecture traceable from product business contribution to architecture decisions, delivery/release mechanisms, and organizational ownership? |
| P1 Architecture completeness   | Does the product have context, building blocks, runtime, deployment, quality, ADRs, and risks?                                                                 |
| P2 Interface quality           | Are all product interfaces specified, versioned, owned, and tested?                                                                                            |
| P3 Data contract quality       | Are topics, messages, schemas, classifications, and ownership defined?                                                                                         |
| P4 ADR discipline              | Are major architecture decisions documented with rationale and consequences?                                                                                   |
| P5 Determinism and performance | Are latency, throughput, scheduling, and resource budgets defined and measured?                                                                                |
| P6 Security implementation     | Are authentication, authorization, crypto, logging, and vulnerability handling implemented and verified?                                                       |
| P7 Resilience                  | Are restart, failover, degraded operation, and DIL behavior tested?                                                                                            |
| P8 Deployment reproducibility  | Can the product be deployed consistently through automation?                                                                                                   |
| P9 Observability               | Are logs, metrics, traces, events, and health indicators available?                                                                                            |
| P10 Technical debt ownership   | Is product-level debt visible, owned, and actively reduced?                                                                                                    |
| P11 Release Compatibility      | Is compatibility with applicable solution baselines and enterprise guardrails declared, evidenced, and reviewed?                                               |

<span id="_Toc233730422" class="anchor"></span>Table 38: Principles of Mission-driven architecture

### Cross-Level Traceability Between Enterprise, Solution and Product ArchitectureRelationship between the three Levels

Architecture governance across Enterprise, Solution and Product Architecture must be connected by explicit traceability. This ensures that architecture decisions are not isolated at one level and that business intent can be followed through to implementation evidence and release readiness.

The traceability chain connects strategic business or mission needs to enterprise guardrails, solution-level architecture decisions, product-level architecture decisions, implementation evidence, and feedback from reviews, demos, releases and operations.

This traceability is required because Software-Defined Defence architectures depend on cross-level alignment. Enterprise guardrails define the common direction. Solution Architecture translates those guardrails into multi-product baselines and integration decisions. Product Architecture implements and verifies the concrete design. Evidence and feedback then flow back upward to improve solution baselines, architecture runway, enterprise guardrails and portfolio decisions.

| **Traceability level**                   | **Purpose**                                                               | **Typical evidence**                                                                                          |
|------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Strategic theme / business capability    | Defines why architecture work is needed                                   | Strategic theme, epic, business capability, mission thread                                                    |
| Enterprise Architecture guardrail        | Defines the cross-division architecture rule or standard                  | Reference architecture, interface standard, data model, security guardrail, technology radar entry            |
| Solution Architecture decision           | Defines how multiple products are aligned into a releasable solution      | Solution baseline, product participation map, interface model, data flow model, integration architecture      |
| Product Architecture decision / ADR      | Defines how the product implements the required architecture contribution | Product architecture document, ADR, interface specification, data contract, deployment view                   |
| Implementation / test / demo evidence    | Proves that the architecture decision works                               | Contract test, integration test, DIL test, security test, system demo, release evidence                       |
| Release readiness / operational feedback | Confirms readiness or identifies improvement needs                        | Compatibility declaration, release decision, operational finding, technical debt item, Inspect & Adapt action |

<span id="_Toc233730423" class="anchor"></span>Table 39: Enterprise Alignment with local autonomy

The following rule applies:

- Every significant architecture decision must be traceable from business need to architecture decision, from architecture decision to implementation evidence, and from evidence back into architecture improvement.

Traceability should therefore be reviewed during architecture reviews, PI planning, solution planning, system demos, release readiness reviews and Inspect & Adapt events.

Figure 5 illustrates the cross-level traceability chain. It shows how a strategic theme or business capability is translated into enterprise guardrails, solution architecture decisions, product architecture decisions or ADRs, implementation and test evidence, release readiness, and operational feedback. The feedback path ensures that findings from implementation, reviews, demos and releases improve architecture runway, solution baselines, enterprise guardrails and portfolio decisions.

<img src="/workspace/SDD_Architecture_Governance_Framework_20260630v2_media/media/image6.png" style="width:9.18056in;height:5.53125in" />

<span id="_Ref233705932" class="anchor"></span>Figure 5: Cross-level traceability chain from strategic theme or business capability to enterprise guardrail, solution architecture decision, product architecture decision or ADR, implementation evidence, release readiness, and feedback.

# Business-Driven Architecture Principles and BAPO Alignment Challenges

## Purpose

This chapter defines the architecture principles for Software-Defined Defence at HENSOLDT.

The principles apply to Enterprise, Solution, and Product Architecture, but their consequences differ by level.

The principles are business-driven. This means they are not based on technology preference or local design habits. They are based on mission outcomes, customer needs, product-line strategy, interoperability, security, resilience, data-centricity, and the ability to release software-defined capabilities continuously.

The BAPO model expands these principles by showing the architectural alignment challenge across Enterprise, Solution, and Product Architecture. BAPO is not used here to replace the principles. It is used to make visible why each principle matters, how it affects the three architecture levels, and which minimum process or ownership implications must be considered.

## Principle Structure

Each principle is described using the same structure:

| **Section**                     | **Meaning**                                                                       |
|---------------------------------|-----------------------------------------------------------------------------------|
| Principle                       | The architecture rule                                                             |
| Intent                          | Why the principle exists                                                          |
| Enterprise implication          | What must be aligned across divisions                                             |
| Solution implication            | What must be aligned across products                                              |
| Product implication             | What must be implemented and evidenced by products                                |
| Process / ownership implication | Which minimum mechanisms and owners are required to keep the architecture aligned |

<span id="_Toc233730424" class="anchor"></span>Table 40: Architecture Levels and Ownership Elements

Each principle should be used during architecture decisions and reviews. A principle is only useful if it changes decisions. Therefore, each principle must be used to evaluate options, justify trade-offs, detect risks, and identify missing evidence.

For example, the principle “Interoperability by Design” should influence interface standards at enterprise level, cross-product interface contracts at solution level, and API or topic implementation at product level. It should also lead to contract testing, versioning rules, and interface ownership.

The following table explains how principles should be used.

| **Use case**                 | **How principles are applied**                                                      |
|------------------------------|-------------------------------------------------------------------------------------|
| New enterprise guardrail     | Check whether the guardrail supports one or more principles                         |
| Solution architecture review | Check whether the solution applies the principles across products                   |
| Product architecture review  | Check whether product decisions implement the principles with evidence              |
| ADR evaluation               | Use principles to compare alternatives and justify consequences                     |
| Architecture exception       | Explain which principle is violated and why the exception is acceptable             |
| Release readiness            | Verify whether critical principles are proven through tests, demos, or measurements |

<span id="_Toc233730425" class="anchor"></span>Table 41: BAPO and open and modular architectures: challenges

## Principle 1: Mission-Driven Architecture

Architecture shall be derived from mission outcomes, customer value, product-line objectives, and business capabilities, not from technology preference.

| **BAPO alignment view** | **Architecture challenge**                                                                         |
|-------------------------|----------------------------------------------------------------------------------------------------|
| Business                | Define the mission outcome, customer value, operational scenario, or product-line objective        |
| Enterprise Architecture | Define guardrails that enable the strategic mission capability across divisions                    |
| Solution Architecture   | Define the multi-product structure needed to deliver the mission capability                        |
| Product Architecture    | Define the product contribution, product boundaries, and product evidence required for the mission |
| Process / ownership     | Ensure capability mapping, epic review, solution planning, and product ownership are aligned       |

<span id="_Toc233730426" class="anchor"></span>Table 42: BAPO and data centricity: challenges per level

Architecture work must begin with:

- Which business capability must be enabled?

- Which mission thread must be supported?

- Which customer or operational need must be satisfied?

- Which strategic theme does this support?

- Which value stream is affected?

A mission-driven architecture does not mean that every technical decision needs a long business case. It means that important architecture decisions must be traceable to a mission or business purpose. This traceability helps prevent unnecessary complexity and technology-driven design.

At enterprise level, mission-driven architecture ensures that guardrails are created only where they support strategic capability. At solution level, it ensures that product integration is organized around mission threads. At product level, it ensures that implementation effort supports an actual contribution to operational value.

## Principle 2: Enterprise Alignment with Local Autonomy

Products and solutions shall follow common enterprise guardrails while retaining local design autonomy where there is no cross-division impact.

| **BAPO alignment view** | **Architecture challenge**                                                                               |
|-------------------------|----------------------------------------------------------------------------------------------------------|
| Business                | Enable cross-division alignment without blocking innovation                                              |
| Enterprise Architecture | Define mandatory standards for interfaces, data, technology, security, runtime, and DevSecOps            |
| Solution Architecture   | Apply enterprise guardrails while solving cross-product integration needs                                |
| Product Architecture    | Make local design decisions within enterprise and solution constraints                                   |
| Process / ownership     | Use lightweight review, exception handling, and architecture ownership to balance alignment and autonomy |

<span id="_Toc233730427" class="anchor"></span>Table 43: BAPO and interoperability by design: challenges per level

This principle separates decision rights:

| **Level**  | **Owns**                                                                    |
|------------|-----------------------------------------------------------------------------|
| Enterprise | Guardrails, standards, reference architectures, exception rules             |
| Solution   | Cross-product architecture, release compatibility, integration architecture |
| Product    | Implementable design, ADRs, component structure, local technical evidence   |

<span id="_Toc233730428" class="anchor"></span>Table 44: BAPO and security by design: challenges per level

The framework therefore uses the following rule:

- Enterprise controls what must be common.

- Solution controls what must work together.

- Product controls what can be implemented locally.

## Principle 3: Open and Modular Architecture

Architectures shall be modular, replaceable, and extensible.

For example, MDOcore is based on open architectures and modular software, supporting rapid integration of HENSOLDT and third-party systems, flexible interfaces, interoperability with NATO and EU coalitions, and operation across edge, fog, and cloud environments.

| **BAPO alignment view** | **Architecture challenge**                                                                            |
|-------------------------|-------------------------------------------------------------------------------------------------------|
| Business                | Enable faster modernization, supplier integration, customer-specific variants, and product-line reuse |
| Enterprise Architecture | Define modularity guardrails, open interface standards, and reusable reference architectures          |
| Solution Architecture   | Define product boundaries, replaceable components, compatibility rules, and integration contracts     |
| Product Architecture    | Implement loose coupling, stable interfaces, component boundaries, and versioned APIs                 |
| Process / ownership     | Require interface governance, contract testing, component ownership, and exception handling           |

<span id="_Toc233730429" class="anchor"></span>Table 45: BAPO, DevSecOps and Continuous Release readiness: challenges per level

Architecture implication:

- Avoid tightly coupled product integrations.

- Prefer stable contracts over direct dependencies.

- Design modules so they can be replaced, upgraded, or relocated.

Modularity shall be evaluated through evidence. A product or solution is not modular because it uses microservices, containers, or APIs. It is modular when components can be changed, replaced, tested, deployed, or reused without uncontrolled impact.

For this reason, modularity must be visible in architecture artifacts. The building block view should show responsibilities. The interface catalogue should show contracts. ADRs should explain major decomposition decisions. Tests should prove that components interact through defined boundaries.

## Principle 4: Data-Centricity

Data shall be treated as a strategic architecture asset.

Architecture shall define:

- Data model

- Semantic meaning

- Metadata

- Classification

- Source of origin (Provenance)

- Lifecycle

- Access control

- Quality rules

- Retention rules

| **BAPO alignment view** | **Architecture challenge**                                                                                |
|-------------------------|-----------------------------------------------------------------------------------------------------------|
| Business                | Create trusted, timely, mission-relevant information for decision superiority                             |
| Enterprise Architecture | Define common data models, semantic rules, metadata, provenance, classification, and lifecycle guardrails |
| Solution Architecture   | Define solution data flows, cross-product data contracts, semantic mappings, and data ownership           |
| Product Architecture    | Implement product schemas, topics, messages, classifications, validation, and data quality checks         |
| Process / ownership     | Require data governance, schema review, data quality checks, data owners, and data architecture community |

<span id="_Toc233730430" class="anchor"></span>Table 46: BAPO, Edge / Fog / Cloud continuum: challenges per level

Data-centricity changes the role of architecture. Data is not merely exchanged between components. It must be understood, governed, protected, and reused. This requires explicit architecture decisions about meaning, structure, ownership, classification, provenance, quality, and lifecycle.

Without these decisions, solutions may transport data successfully but still fail to create trusted operational information. For Software-Defined Defence, this is not sufficient. The architecture must support the transformation from data movement to information value.

## Principle 5: Interoperability by Design

Interoperability shall be designed from the beginning, not repaired during integration.

Architectures shall use:

- Standardized interfaces

- Open APIs

- Common data models

- Versioned schemas

- Explicit compatibility rules

- Integration test environments

For example, HENSOLDT identifies standardized interfaces and common data models as key SDD requirements for compatibility between NATO, EU, and national systems.

| **BAPO alignment view** | **Architecture challenge**                                                                                      |
|-------------------------|-----------------------------------------------------------------------------------------------------------------|
| Business                | Achieve cross-division, customer, partner, NATO/EU, and multi-domain interoperability                           |
| Enterprise Architecture | Define mandatory interface standards, common data models, and interoperability guardrails                       |
| Solution Architecture   | Define cross-product interface contracts, compatibility rules, and integration architecture                     |
| Product Architecture    | Implement and test product APIs, topics, messages, schemas, and protocol behavior                               |
| Process / ownership     | Require interface review, contract testing, versioning process, interface ownership, and compatibility evidence |

<span id="_Toc233730431" class="anchor"></span>Table 47: Resilience under degraded conditions (where applicable): challenges per level

nteroperability must be designed before integration starts. Late interoperability usually produces temporary adapters, duplicated transformations, unclear ownership, and fragile releases.

The framework therefore treats interfaces and data contracts as architecture governance boundaries. They define not only technical communication, but also release compatibility, ownership, security expectations, semantic meaning, and test obligations.

## Principle 6: Security by Design

Security shall be built into architecture, not added afterwards.

Every architecture shall define:

- Trust boundaries

- Identity model

- Authentication

- Authorization

- Crypto approach

- Key management

- Logging and audit

- Monitoring

- Vulnerability handling

- Secure update approach

For Example: HENSOLDT identifies zero-trust architecture, cryptography, and continuous monitoring as SDD security requirements for protection, traceability, and integrity in operational environments.

| **BAPO alignment view** | **Architecture challenge**                                                                                                   |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Business                | Enable trustworthy, sovereign, compliant, and mission-safe operation                                                         |
| Enterprise Architecture | Define security guardrails, zero-trust principles, crypto standards, identity rules, audit, and monitoring                   |
| Solution Architecture   | Define cross-product trust zones, identity propagation, crypto boundaries, and security evidence                             |
| Product Architecture    | Implement authentication, authorization, crypto, secure logging, secure update, and vulnerability handling                   |
| Process / ownership     | Require threat modelling, security testing, vulnerability management, product security owners, and security architect review |

<span id="_Toc233730432" class="anchor"></span>Table 48: Evidence-based architecture: challenges per level

Security by design means that security decisions are part of the architecture baseline. They are not optional implementation details. Every relevant architecture description should show trust boundaries, identities, access rules, cryptographic mechanisms, logging, audit, monitoring, update mechanisms, and vulnerability handling.

At solution level, security must be considered across product boundaries. At product level, security must be verified through evidence. A security concept without test evidence is not sufficient for release readiness.

## Principle 7: DevSecOps and Continuous Release Readiness

Architecture shall support continuous integration, automated testing, secure deployment, and controlled release.

For example, HENSOLDT understands SDD as using open architectures, modular software components, and continuous development cycles that shorten modernization processes from years to weeks. HENSOLDT also identifies DevSecOps methods, containerized microservices, and automated deployment as SDD agility requirements.

| **BAPO alignment view** | **Architecture challenge**                                                                              |
|-------------------------|---------------------------------------------------------------------------------------------------------|
| Business                | Enable faster modernization, operational adaptability, and continuous readiness                         |
| Enterprise Architecture | Define CI/CD, automated testing, secure deployment, pipeline, and observability guardrails              |
| Solution Architecture   | Define solution integration pipelines, compatibility checks, release baseline process, and system demos |
| Product Architecture    | Implement build, test, scan, deploy, monitor, and release evidence generation                           |
| Process / ownership     | Require DevSecOps process, platform team ownership, release governance, and automated verification      |

<span id="_Toc233730433" class="anchor"></span>Table 49: Quality marker scoring

Architecture implication:

- No architecture is complete unless it can be built, tested, deployed, monitored, and updated.

DevSecOps is not only a pipeline concern. It is an architecture concern because architecture determines whether a system can be built, tested, deployed, monitored, and updated reliably.

If a product architecture cannot be deployed reproducibly, it is not release-ready. If a solution architecture cannot be integrated repeatedly, it is not solution-ready. If enterprise guardrails do not support automation, they will slow down delivery.

## Principle 8: Edge / Fog / Cloud Continuum (where Applicable)

Architectures shall support distribution of capabilities across Edge, Fog, and Cloud where applicable.

For example, HENSOLDT positions MDOcore as operating across edge, fog, and cloud environments, from tactical edge systems to national cloud-based command-and-control structures.

| **BAPO alignment view** | **Architecture challenge**                                                                           |
|-------------------------|------------------------------------------------------------------------------------------------------|
| Business                | Enable tactical autonomy, scalable processing, and mission flexibility                               |
| Enterprise Architecture | Define edge/fog/cloud reference architecture, deployment guardrails, and runtime assumptions         |
| Solution Architecture   | Define integrated runtime topology, placement rules, synchronization, and deployment variants        |
| Product Architecture    | Define product deployment nodes, containers, resource budgets, and runtime assumptions               |
| Process / ownership     | Require deployment validation, runtime monitoring, environment qualification, and platform ownership |

<span id="_Toc233730434" class="anchor"></span>Table 50: BAPO scoring rules

Architecture shall define:

- What runs at the edge

- What runs in fog environments

- What can run in cloud environments

- How data, control, security, observability, and lifecycle work across all three

Edge, fog, and cloud placement decisions must be explicit because they affect latency, resilience, bandwidth, security, data lifecycle, compute capacity, deployment complexity, and operational autonomy.

A product architecture shall define where its components run. A solution architecture shall define how distributed products interact across environments. Enterprise Architecture shall define the guardrails that make this distribution consistent and secure.

## Principle 9: Resilience Under Degraded Conditions (where Applicable)

Architectures shall assume contested, degraded, denied, intermittent, or limited communication.

For example.MDOcore is positioned as robust in contested environments with degraded communications, dynamically prioritizing available resources and providing mission-relevant information

| **BAPO alignment view** | **Architecture challenge**                                                                                       |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| Business                | Preserve mission capability under degraded communication, cyberattack, high data load, or partial system failure |
| Enterprise Architecture | Define resilience guardrails, degraded-mode principles, and availability expectations                            |
| Solution Architecture   | Define cross-product degraded modes, fallback behavior, continuity, and recovery scenarios                       |
| Product Architecture    | Implement restart, retry, buffering, store-and-forward, failover, graceful degradation, and recovery behavior    |
| Process / ownership     | Require failure-mode testing, degraded-mode demos, resilience evidence, and reliability ownership                |

<span id="_Toc233730435" class="anchor"></span>Table 51: Scoring results and their practical meanng

Architectures must define:

- Degraded modes

- Fallback behavior

- Store-and-forward

- Graceful degradation

- Offline behavior

- Recovery behavior

- Prioritization under constraint

Resilience must be described through scenarios, not only through general statements. A useful architecture should explain what happens when connectivity is degraded, a node is unavailable, a product restarts, bandwidth is limited, a queue overflows, data arrives late, or a security check fails.

This is especially important for mission-critical Software-Defined Defence systems, where degraded conditions may be normal operating conditions rather than rare exceptions.

## Principle 10: Evidence-Based Architecture

Architecture quality shall be proven through evidence.

- Accepted evidence includes:

- Architecture documents

- ADRs

- Interface contracts

- Automated tests

- Integration tests

- Security test results

- Performance measurements

- System demo results

- Release compatibility evidence

- Risk and debt registers

- Operational monitoring

| **BAPO alignment view** | **Architecture challenge**                                                                                   |
|-------------------------|--------------------------------------------------------------------------------------------------------------|
| Business                | Prove that architecture supports the intended capability and mission outcome                                 |
| Enterprise Architecture | Prove guardrail adoption, exception control, technology alignment, and enterprise KPIs                       |
| Solution Architecture   | Prove cross-product behavior, solution release readiness, and integration quality                            |
| Product Architecture    | Prove product design, interfaces, runtime behavior, security, quality, and release compatibility             |
| Process / ownership     | Require architecture reviews, system demos, release readiness checks, evidence ownership, and feedback loops |

<span id="_Toc233730436" class="anchor"></span>Table 52: Marker evidence types

Architecture claims without evidence are not accepted.

Evidence-based architecture is the discipline that keeps architecture connected to reality. It prevents architecture from becoming only diagrams and intentions.

Evidence may come from documents, ADRs, tests, measurements, demos, scans, logs, dashboards, reviews, and operational feedback. The right evidence depends on the quality marker. For example, an interface quality marker requires interface contracts and contract tests. A resilience marker requires degraded-mode scenarios and failure-mode evidence. A security marker requires threat models and verification evidence.

# Architecture Quality Marker Model

## Purpose

This chapter defines how architecture quality is evaluated. The purpose of the quality marker model is to make architecture quality visible, comparable, and evidence-based.

A quality marker is not a general statement of intent. It is a reviewable expectation that connects an architecture claim to evidence. This is important because Software-Defined Defence architectures are complex, distributed, security-sensitive, and release-driven. Claims such as “secure”, “scalable”, “modular”, or “interoperable” are not sufficient unless they are supported by concrete evidence.

The BAPO alignment markers expand the quality model. They check whether the architecture item is connected to business value, aligned across levels, supported by the required process, owned by accountable roles, and improved through feedback.

Bad marker:

- The solution is scalable.

Good marker:

- The solution has documented scalability scenarios, quantified capacity assumptions, a deployment model, tested scaling behavior, monitoring metrics, and an owner for scalability risks.

In a BAPO-expanded framework, a quality marker must evaluate not only the technical architecture, but also the architecture alignment challenge: why the architecture is needed, how it aligns across levels, which minimum delivery or governance mechanism is required, and who owns it.

## Quality Marker Scoring

All markers use the same maturity scale:

| **Score** | **Meaning**                        | **Interpretation**                                                      |
|-----------|------------------------------------|-------------------------------------------------------------------------|
| 0         | Missing                            | No evidence exists                                                      |
| 1         | Mentioned                          | Topic is named but not described                                        |
| 2         | Described                          | Architecture description exists                                         |
| 3         | Designed and owned                 | Design, owner, and responsibility are clear                             |
| 4         | Verified                           | Evidence exists through review, test, integration, demo, or measurement |
| 5         | Continuously measured and improved | Marker is monitored and improved over time                              |

<span id="_Toc233730437" class="anchor"></span>Table 53: Mandatory BAPO alignment markers

Note that BAPO does not replace the technical score. BAPO adds alignment markers!

| **Scoring rule**                          | **Meaning**                                                                                                       |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Technical marker score remains valid      | A product can be technically strong even if BAPO alignment needs improvement                                      |
| BAPO markers are evaluated separately     | Business traceability, cross-level alignment, process implication, ownership, and feedback are checked explicitly |
| Release decisions consider both           | Release readiness requires technical evidence and sufficient alignment evidence                                   |
| BAPO does not dilute architecture quality | It expands the alignment challenge without replacing technical evaluation                                         |

<span id="_Toc233730438" class="anchor"></span>Table 54: Enterprise architecture quality marker catalogue

The scoring model should be used consistently across Enterprise, Solution, and Product Architecture. A score of 3 means that the architecture topic is designed and owned, but not yet fully verified. A score of 4 means that evidence exists. A score of 5 means that the quality is not only verified once, but continuously measured and improved.

This distinction is important for release decisions. A marker may be acceptable for early architecture readiness at score 3, but a release decision usually requires score 4 for critical quality markers. Operationally mature systems should move toward score 5 for the most critical markers.

| **Score** | **Practical meaning in review**                                             |
|-----------|-----------------------------------------------------------------------------|
| 0         | The topic is missing and creates immediate architecture risk                |
| 1         | The topic is known but not yet usable for decision-making                   |
| 2         | The topic is described but ownership or implementation detail is still weak |
| 3         | The design is clear enough to plan and assign work                          |
| 4         | Evidence proves that the design works as intended                           |
| 5         | Evidence is continuously collected and used for improvement                 |

<span id="_Toc233730439" class="anchor"></span>Table 55: Solution architecture quality marker catalogue

Figure 6 visualizes the quality-marker maturity scale used throughout the framework. The scale separates missing or merely described architecture topics from architecture that is owned, verified, and continuously improved.

<img src="/workspace/SDD_Architecture_Governance_Framework_20260630v2_media/media/image7.png" style="width:8.78125in;height:5.45833in" />

<span id="_Ref233703932" class="anchor"></span>Figure 6: Architecture quality marker maturity model, showing the progression from missing evidence to continuously measured and improved architecture quality.

## Marker Evidence Types

Each quality marker must define which evidence is acceptable to assess the marker. Evidence is required because architecture quality shall not be based on opinion, informal claims, or undocumented assumptions. A marker can only be reviewed reliably when the supporting evidence shows what was decided, why it was decided, who owns it, how it was implemented or verified, and whether the result is still valid.

Evidence does not always have to be a formal document. Depending on the marker, stronger evidence may come from architecture models, ADRs, automated tests, contract tests, security scans, runtime metrics, release records, system demos, Inspect & Adapt findings, or named ownership records. The purpose of evidence is to make architecture quality reviewable and traceable, not to create unnecessary documentation.

The following evidence types may be used to support architecture quality marker assessments:

| **Evidence type**     | **What it demonstrates**                                                                                           | **Examples**                                                                                                                             |
|-----------------------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Business evidence     | The architecture concern is linked to business, mission, customer, or strategic value.                             | Strategic theme, epic, value-stream map, business capability map, customer requirement, mission thread                                   |
| Architecture evidence | The architecture structure or design intent is described and understandable.                                       | Architecture document, architecture model, context diagram, building block view, runtime view, deployment view, reference architecture   |
| Decision evidence     | Major architecture choices and trade-offs are documented and justified.                                            | ADR, trade-off analysis, option assessment, exception approval, design rationale                                                         |
| Interface evidence    | Interfaces are specified, versioned, owned, and testable.                                                          | API contract, topic model, schema, ICD, protocol specification, versioning rule                                                          |
| Data evidence         | Data meaning, structure, ownership, classification, and lifecycle are defined.                                     | Data model, semantic model, metadata model, classification rules, provenance rules, data ownership record                                |
| Test evidence         | Architecture assumptions or requirements have been verified through testing.                                       | Automated test, integration test, contract test, performance test, resilience test, failure-mode test                                    |
| Security evidence     | Security decisions, controls, and risks have been analysed and verified.                                           | Threat model, vulnerability scan, crypto review, penetration test, security architecture review, risk treatment                          |
| Runtime evidence      | The system is observable and behaves as expected in execution.                                                     | Logs, metrics, traces, health indicators, monitoring dashboard, operational measurement                                                  |
| Release evidence      | The architecture is compatible with release, deployment, and integration expectations.                             | Release compatibility matrix, deployment manifest, release declaration, solution baseline, compatibility declaration                     |
| Governance evidence   | The architecture concern has been reviewed, approved, tracked, or escalated.                                       | Review record, risk register, technical debt register, exception register, architecture board decision                                   |
| Process evidence      | The required delivery, integration, test, release, or governance process exists and is used.                       | Integration process, release process, test process, governance workflow, DevSecOps pipeline, quality gate                                |
| Organization evidence | Ownership, accountability, and required roles are clear.                                                           | RACI, named owner, role assignment, team ownership, architecture board mandate, community-of-practice ownership                          |
| Feedback evidence     | Learning from implementation, demos, operation, or review has been captured and converted into improvement action. | System demo result, solution demo finding, Inspect & Adapt action, architecture debt item, operational finding, improvement backlog item |

<span id="_Toc233730440" class="anchor"></span>Table 56: Product architecture quallity marker catalogue

Evidence should be selected according to the marker and the maturity level being assessed. Not every marker requires the same type or amount of evidence. For example, enterprise technology alignment may be evidenced through a technology radar, adoption dashboard and exception register. Cross-product interface maturity may be evidenced through interface contracts, versioning rules and contract tests. Product resilience may be evidenced through failure-mode tests, recovery measurements and operational findings.

The review should therefore apply an evidence sufficiency principle. Evidence is sufficient when it is concrete, current, traceable to the marker, owned by an accountable role, and strong enough to justify the assessed maturity score. Descriptive evidence may be sufficient for lower maturity levels, but higher maturity levels require stronger proof such as verification results, runtime measurements, adoption data, release evidence or continuous improvement records.

The review should avoid two extremes. It should not accept architecture claims without evidence. At the same time, it should not demand unnecessary documentation where automated tests, demos, runtime metrics or tool-generated records provide stronger proof. The preferred evidence is the evidence that most directly demonstrates that the architecture concern is defined, owned, implemented, verified and improved.

## Mandatory BAPO Alignment Markers

BAPO alignment markers are mandatory cross-cutting markers that apply to Enterprise, Solution and Product Architecture items. They ensure that architecture quality is not assessed only as a technical design question. Each relevant architecture item must also be traceable to business intent, aligned across architecture levels, connected to delivery and governance mechanisms, assigned to clear ownership, and linked to a feedback loop.

The BAPO markers should be applied as an alignment overlay. They do not replace the Enterprise, Solution or Product quality markers. Instead, they make visible whether an architecture item is complete from a Business, Architecture, Process and Organization perspective. An architecture item may be technically well designed, but still incomplete if its business driver is unclear, its cross-level alignment is missing, its process implications are not defined, ownership is ambiguous, or findings do not flow back into architecture improvement.

The following mandatory BAPO alignment markers apply to relevant architecture items across all three architecture levels:

| **ID** | **Marker**                         | **Review question**                                                                                                                                              | **Typical evidence**                                                                                                                           |
|--------|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| B1     | Business traceability              | Is the architecture item linked to a business capability, mission outcome, value stream, strategic theme, customer need, or product contribution?                | Strategic theme, epic, capability map, value-stream map, portfolio item, customer requirement, product business contribution statement         |
| B2     | Cross-level architecture alignment | Is the architecture item aligned with the relevant Enterprise, Solution and Product Architecture decisions, guardrails and constraints?                          | Traceability map, reference architecture mapping, enterprise guardrail mapping, solution baseline mapping, product architecture mapping        |
| B3     | Process implication                | Are the required planning, integration, verification, release, security, or governance mechanisms identified and executable?                                     | Process description, review checklist, pipeline evidence, quality gate, integration plan, test plan, release process, governance workflow      |
| B4     | Ownership clarity                  | Are the responsible architecture owners, interface owners, data owners, security owners, platform owners, product owners, or governance bodies clearly assigned? | RACI, owner list, role assignment, review record, architecture board decision, team ownership record                                           |
| B5     | Feedback loop                      | Is there a mechanism to feed findings from implementation, review, demo, integration, release, or operation back into architecture improvement?                  | System demo result, solution demo finding, Inspect & Adapt item, technical debt item, KPI trend, operational finding, improvement backlog item |

<span id="_Toc233730441" class="anchor"></span>Table 57: Architecture quality markers review points

The BAPO alignment markers should be scored separately from the technical architecture quality markers. This separation is important because different weaknesses require different improvement actions. A product may have a strong internal architecture but weak business traceability. A solution may have a convincing business case but unclear interface ownership. An enterprise guardrail may be strategically correct but ineffective because the required adoption process, exception process or feedback mechanism is missing.

By scoring the BAPO markers separately, the framework makes these alignment gaps visible without hiding the technical assessment. The result is a more balanced view of architecture maturity: technical quality shows whether the architecture is well designed, while BAPO alignment shows whether the architecture is connected to business value, executable through process, owned by accountable roles, and improved through feedback.

A BAPO marker should only be considered mature when the evidence is concrete, current, owned and reviewable. For lower maturity levels, a description or mapping may be sufficient. For higher maturity levels, the evidence should show that the alignment mechanism is actively used, verified, measured or improved.

## Enterprise Architecture Quality Marker Catalogue

Enterprise Architecture quality markers are used to assess whether enterprise-level architecture guidance for Software-Defined Defence is defined, usable, adopted and continuously improved across divisions. They focus on the architecture concerns that must be consistent beyond individual products or solutions, such as strategic alignment, reference architectures, interface standards, data models, security guardrails, technology governance, platform alignment, DevSecOps expectations, reuse and enterprise technical debt.

The markers in the following table define the minimum enterprise-level assessment catalogue. They should be used during enterprise architecture reviews, guardrail reviews, technology governance reviews, portfolio alignment discussions, exception reviews and architecture KPI reviews. A marker should only be considered mature when the required evidence is available, owned, versioned, communicated to Solution and Product Architecture, and reviewed through an appropriate governance mechanism.

| **ID** | **Marker**                          | **Review question**                                                                                                                    | **Required enterprise evidence**                                                                                                                |
|--------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| E0     | Enterprise BAPO traceability        | Are strategic business drivers translated into enterprise architecture guardrails, governance mechanisms and accountable ownership?    | Strategic themes mapped to enterprise guardrails, governance mechanisms, ownership records, BAPO traceability map                               |
| E1     | Strategic SDD alignment             | Are enterprise architecture decisions aligned with the Software-Defined Defence strategy and relevant strategic capability priorities? | Architecture principles, strategic themes, SDD alignment record, MDOcore alignment, portfolio architecture rationale                            |
| E2     | Reference architecture availability | Are relevant enterprise reference architectures published, understandable and applicable by solutions and products?                    | Published reference architectures, adoption rules, usage guidance, review records, applicability criteria                                       |
| E3     | Interface standardization           | Are enterprise-level interface principles, standards and versioning expectations defined and governed?                                 | Enterprise interface standards catalogue, interface governance rules, versioning rules, exception records                                       |
| E4     | Technology governance               | Are technology choices governed across lifecycle, adoption, exception and retirement decisions?                                        | Technology radar, approved technology catalogue, lifecycle rules, exception process, retirement plan                                            |
| E5     | Data architecture alignment         | Are enterprise data, semantic, metadata, classification and provenance expectations defined consistently?                              | Enterprise data model, semantic model, metadata rules, classification rules, provenance rules, data ownership records                           |
| E6     | Security guardrails                 | Are enterprise security principles and mandatory controls defined for Software-Defined Defence architecture?                           | Zero-trust principles, identity rules, crypto rules, monitoring and audit expectations, trust-zone principles, security architecture guardrails |
| E7     | DevSecOps guardrails                | Are common DevSecOps expectations defined for build, test, security, deployment and release evidence?                                  | CI/CD standards, automated test expectations, secure deployment standards, pipeline controls, quality gates                                     |
| E8     | Platform alignment                  | Are runtime, deployment, orchestration, containerization and observability expectations aligned across relevant platforms?             | Runtime standards, containerization rules, deployment standards, orchestration guidance, observability standards                                |
| E9     | Reuse and modularity                | Are reuse and modularity principles defined so that products and services can be shared safely across solutions?                       | Reuse catalogue, modularity rules, platform/service catalogue, reuse criteria, ownership and lifecycle rules                                    |
| E10    | Enterprise technical debt           | Is enterprise-level architecture debt visible, owned, prioritized and linked to funding or improvement actions?                        | Enterprise technical debt register, debt ownership, mitigation plan, funding model, improvement backlog                                         |

<span id="_Toc233730442" class="anchor"></span>Table 58: Readiness state definitions per architecture level

The enterprise markers should be scored using the common maturity scale defined in Chapter 5.2. A low score does not necessarily mean that the enterprise direction is wrong. It may mean that the guardrail is not yet published, not sufficiently adopted, not supported by evidence, not governed through an exception process, or not measured through architecture KPIs.

Enterprise Architecture reviews should therefore distinguish between three questions. First, is the enterprise architecture guidance itself correct and aligned with strategy? Second, is it usable by Solution and Product Architecture? Third, is there evidence that it is actually adopted, governed and improved across divisions? This distinction prevents enterprise architecture from becoming a static document set and turns it into an active alignment mechanism for Software-Defined Defence.

Where an enterprise marker scores low, the resulting action should be captured as enterprise architecture runway, enterprise technical debt, a guardrail improvement, a governance-process improvement, or a portfolio-level decision.

## Solution Architecture Quality Marker Catalogue

Solution Architecture quality markers are used to assess whether multiple products can work together as one coherent, integrated and releasable solution. They focus on architecture quality at the boundaries between products, where integration risk, interface inconsistency, data misalignment, security gaps, deployment conflicts and release incompatibility typically emerge.  
  
The markers in the following table define the minimum solution-level assessment catalogue. They should be used during solution architecture reviews, PI planning, integration planning, system or solution demos, release readiness reviews and Inspect & Adapt. A marker should only be considered mature when the required evidence is available, owned, versioned, aligned with applicable enterprise guardrails, and usable by the participating Product Architects.

| **ID** | **Marker**                       | **Review question**                                                                                                                             | **Required solution evidence**                                                                                                                     |
|--------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| S0     | Solution BAPO traceability       | Is the solution capability traceable to product architecture decisions, integration and release mechanisms, and accountable ownership?          | Solution capability map, solution BAPO map, product participation map, architecture ownership records, integration and release governance evidence |
| S1     | Solution boundary clarity        | Is the solution boundary clear, including participating products, external systems, interfaces, assumptions and constraints?                    | Solution context diagram, product participation map, external system map, scope statement, boundary assumptions                                    |
| S2     | Capability allocation            | Are solution capabilities allocated clearly to participating products and product owners?                                                       | Capability-to-product mapping, responsibility allocation, product contribution statements, backlog or epic mapping                                 |
| S3     | Cross-product interface maturity | Are cross-product interfaces specified, versioned, owned, tested and aligned with enterprise interface guardrails?                              | Interface catalogue, ICDs, API contracts, topic definitions, version records, interface owners, contract test results                              |
| S4     | Data flow consistency            | Are cross-product data flows, schemas, topics, semantic mappings and data ownership defined consistently?                                       | Data flow model, schemas, topic catalogue, semantic mapping, data ownership records, classification and provenance rules                           |
| S5     | Integrated security              | Are solution-level security boundaries, trust zones, identities, crypto assumptions and controls defined and verified?                          | Solution threat model, trust-zone model, security architecture review, crypto assumptions, identity model, security evidence                       |
| S6     | Release architecture             | Is the solution release baseline defined, including compatible product releases, interface versions, data contracts and deployment assumptions? | Solution release baseline, product compatibility matrix, interface version matrix, deployment manifest, release declaration                        |
| S7     | Integration readiness            | Is the solution ready for integration, verification and demonstration across participating products?                                            | Integration environment, integration plan, system or solution demo plan, verification matrix, integration test results                             |
| S8     | Resilience                       | Are degraded-mode, failover, recovery and DIL scenarios defined and evidenced at solution level?                                                | Degraded-mode scenarios, resilience test results, recovery evidence, operational assumptions, DIL behavior evidence                                |
| S9     | Architecture runway              | Are solution-level architecture enablers identified and planned before they become delivery blockers?                                           | Architecture enablers in backlog, runway roadmap, dependency map, risk records, PI objectives or planning evidence                                 |
| S10    | Solution technical debt          | Is shared solution-level technical debt visible, owned, prioritized and linked to mitigation actions?                                           | Shared technical debt register, mitigation plan, owner list, due dates, risk assessment, improvement backlog                                       |

<span id="_Toc233730443" class="anchor"></span>Table 59: BAPO structure of enterprise guardrails

The solution markers should be scored using the common maturity scale defined in Chapter 5.2. A low score does not necessarily mean that the solution concept is wrong. It may mean that the solution boundary is unclear, product participation is not sufficiently defined, interface ownership is missing, integration evidence is incomplete, release compatibility is not yet proven, or solution-level debt has not been made visible.

Solution Architecture reviews should therefore distinguish between three questions. First, is the intended solution capability clearly understood? Second, are the participating products architecturally aligned so that they can work together? Third, is there sufficient evidence that the solution can be integrated, verified, released and improved as one coherent capability?

Where a solution marker scores low, the resulting action should be captured as solution architecture runway, solution technical debt, an integration-risk item, a product-level follow-up, a guardrail clarification request, or a release-readiness improvement action.

## Product Architecture Quality Maker Catalogue

Product Architecture quality markers are used to assess whether an individual product architecture is complete, evidence-based, implementation-ready, integration-ready and releasable. They focus on the architecture quality of the product itself, including context, building blocks, runtime behavior, deployment, interfaces, ADRs, security, performance, resilience, observability and technical debt. They also assess whether the product can participate in solution baselines and comply with applicable enterprise guardrails.

The markers in the following table define the minimum product-level assessment catalogue. They should be used during product architecture reviews, backlog refinement, PI planning, implementation reviews, product demos, release readiness reviews and Inspect & Adapt. A marker should only be considered mature when the required evidence is available, owned, versioned, reviewable and connected to the relevant backlog, verification, release or governance mechanism.

| **ID** | **Marker**                          | **Review question**                                                                                                                 | **Required product evidence**                                                                                                                     |
|--------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| P0     | Product BAPO traceability           | Is the product contribution traceable to architecture decisions, delivery mechanisms, release mechanisms and accountable ownership? | Product business contribution statement, product BAPO map, backlog mapping, test/release evidence, owner records                                  |
| P1     | Architecture completeness           | Does the product architecture contain the minimum required views, decisions, quality requirements, risks and evidence?              | Product Architecture Document, architecture view set, quality catalogue, ADR register, risk and debt register                                     |
| P2     | Context and boundary clarity        | Are product users, external systems, boundaries, constraints and external dependencies clearly defined?                             | System context diagram, external interface model, scope statement, dependency map, boundary assumptions                                           |
| P3     | Building block quality              | Are product components, modules, responsibilities and internal interfaces clearly structured and owned?                             | Component model, building block view, responsibility mapping, internal interface description                                                      |
| P4     | Runtime behavior                    | Are key runtime scenarios, interactions, sequences and operational behavior described and understood?                               | Runtime view, sequence descriptions, scenario descriptions, event flows, operational assumptions                                                  |
| P5     | Deployment reproducibility          | Can the product be deployed consistently across defined runtime environments through controlled and repeatable mechanisms?          | Deployment view, deployment manifests, infrastructure assumptions, container/runtime configuration, automation evidence                           |
| P6     | Interface and data contract quality | Are product APIs, topics, schemas, events, protocols and data contracts specified, versioned, owned and tested?                     | API contracts, topic definitions, schema contracts, ICDs, protocol specifications, version records, contract test results                         |
| P7     | ADR discipline                      | Are major product architecture decisions documented with rationale, alternatives, consequences and ownership?                       | ADR register, decision records, trade-off analysis, option assessment, exception records                                                          |
| P8     | Security implementation             | Are product-level security controls, identity assumptions, crypto usage, logging and vulnerability handling defined and verified?   | Product security concept, threat model, security controls, crypto review, vulnerability scan, security test evidence                              |
| P9     | Performance and determinism         | Are latency, throughput, scheduling, resource budgets and deterministic behavior defined and measured where required?               | Performance budgets, measurement results, load tests, timing analysis, resource measurements, determinism evidence                                |
| P10    | Resilience                          | Are failure, restart, failover, degraded-mode, DIL and recovery behaviors defined and tested?                                       | Failure-mode tests, restart tests, recovery evidence, degraded-mode scenarios, DIL test evidence                                                  |
| P11    | Observability                       | Are logs, metrics, traces, health indicators and operational diagnostics available and usable?                                      | Logging concept, metrics, traces, health indicators, monitoring dashboard, operational evidence                                                   |
| P12    | Technical debt                      | Is product-level architecture debt visible, owned, prioritized and actively reduced?                                                | Risk and technical debt register, mitigation plan, owner list, due dates, backlog items, improvement evidence                                     |
| P13    | Release compatibility               | Is compatibility with applicable solution baselines and enterprise guardrails declared, evidenced and reviewed?                     | Product Release Compatibility Declaration, solution baseline mapping, enterprise guardrail mapping, compatibility evidence, release review record |

<span id="_Toc233730444" class="anchor"></span>Table 60: Questions guardrails must answer

The product markers should be scored using the common maturity scale defined in Section 5.2. A low score does not necessarily mean that the product implementation is poor. It may mean that architecture evidence is incomplete, ownership is unclear, interfaces are not sufficiently specified, verification evidence is missing, deployment is not reproducible, or release compatibility with a solution baseline has not yet been demonstrated.

Product Architecture reviews should therefore distinguish between three questions. First, is the product architecture internally coherent and sufficiently documented? Second, is there evidence that the architecture has been implemented, verified and made observable? Third, can the product safely participate in the relevant solution baselines and comply with applicable enterprise guardrails?

Where a product marker scores low, the resulting action should be captured as product architecture runway, product technical debt, a backlog enabler, an interface clarification, a verification action, a security action, a deployment improvement, or a release-readiness follow-up.

## Architecture Quality Marker Reviews

Architecture quality markers shall be reviewed at the points in the agile@HENSOLDT lifecycle where architecture-relevant decisions are made, planned, implemented, demonstrated, released or improved. The purpose of these reviews is not to create an additional approval bureaucracy. The purpose is to ensure that architecture quality is assessed with the right evidence at the right decision point.

The review model is therefore event-driven and evidence-driven. Early lifecycle reviews focus on business traceability, strategic alignment, architecture impact and required enablers. Planning reviews focus on ownership, dependencies, integration risks and architecture runway. Demos and verification events provide evidence that architecture claims are actually valid. Release readiness reviews assess whether product and solution baselines are compatible, evidenced and governed. Inspect & Adapt ensures that findings are converted into technical debt, architecture runway, guardrail updates or portfolio decisions.

The following review points should be used to assess the relevant Enterprise, Solution, Product and BAPO quality markers:

| **Review point**                 | **Primary marker focus**                                                                                    | **Mandatory BAPO alignment check**                                                                                                             | **Typical evidence or review result**                                                                                    |
|----------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Epic review                      | Enterprise alignment, strategic architecture impact, required architecture work                             | Is the business driver clear, and does the epic require architecture guardrails, runway, standards, or cross-level alignment?                  | Strategic theme, epic, capability map, initial architecture impact assessment, enterprise marker pre-check               |
| Enterprise guardrail review      | Enterprise standards, reference architectures, technology governance, data, security and platform alignment | Are the business need, architecture guardrail, governance mechanism and accountable owner clear?                                               | Guardrail record, reference architecture, technology radar entry, exception rule, owner assignment                       |
| Solution planning                | Cross-product interfaces, solution boundary, capability allocation, solution release architecture           | Does the solution architecture define the integration, verification and release mechanisms needed for the solution?                            | Solution context, product participation map, capability allocation, interface catalogue, solution baseline draft         |
| PI planning                      | Architecture runway, enablers, dependencies, integration risks and product-level responsibilities           | Are architecture enablers owned, planned and connected to delivery teams, owners and verification mechanisms?                                  | Architecture enablers, backlog items, dependency map, PI objectives, risk records, owner assignments                     |
| Architecture review              | Major architecture decisions, deviations, quality-marker scores and evidence sufficiency                    | Are the business reason, cross-level alignment, process implications and ownership clear enough to proceed?                                    | Review record, ADRs, quality-marker assessment, decision log, exception request, action list                             |
| Product / system / solution demo | Verified architecture behavior, integration evidence and observable system behavior                         | Does the demonstrated evidence prove the architecture claim, or does it reveal a gap in business priority, architecture, process or ownership? | Demo result, integration evidence, test results, runtime metrics, findings, follow-up actions                            |
| Inspect & Adapt                  | Architecture findings, technical debt, recurring risks and improvement actions                              | Does feedback require a change to business priority, architecture guardrails, delivery process or ownership?                                   | Inspect & Adapt item, technical debt item, KPI trend, operational finding, improvement backlog                           |
| Product release readiness        | Product architecture evidence, interface quality, verification evidence and release compatibility           | Are product ownership, compatibility declarations, verification evidence and required process evidence complete?                               | Product evidence package, compatibility declaration, test evidence, security evidence, deployment evidence               |
| Solution release readiness       | Integrated evidence, solution baseline, product compatibility and release governance                        | Is the solution baseline technically, architecturally and organizationally releasable?                                                         | Solution release baseline, product compatibility matrix, integration test evidence, release declaration, risk acceptance |
| Exception review                 | Deviations from enterprise guardrails, solution baselines or product architecture requirements              | Is the exception justified, owned, time-bounded, risk-assessed and linked to mitigation or debt reduction?                                     | Exception record, risk assessment, mitigation plan, owner, expiry date, review decision                                  |

<span id="_Toc233730446" class="anchor"></span>Table 62: Enterprise Reference Architecture Catalogue

Quality marker reviews should be integrated into existing agile events wherever possible. Portfolio and epic reviews should use Enterprise Architecture and BAPO markers to clarify business traceability and strategic architecture impact. Solution planning should use Solution Architecture markers to assess cross-product integration, release architecture and capability allocation. PI planning should make architecture runway, enablers, dependencies and ownership visible. Product and system demos should provide evidence for markers that require implemented or integrated behavior.

Release readiness reviews should use Product and Solution Architecture markers to assess whether the required evidence is complete and whether the relevant product or solution baseline is releasable. Inspect & Adapt should be used to convert architecture findings into improvement actions, such as technical debt items, architecture runway, guardrail updates, process changes or portfolio decisions.

The review depth should be proportional to the architecture risk and decision impact. Not every marker requires a full review at every event. However, every relevant marker should have a clear review point, acceptable evidence, an accountable owner and a mechanism for follow-up. A marker score should not be treated as final if the required evidence is missing, outdated, unowned or not traceable to the architecture decision being assessed.

## Minimum Acceptance Rule

The minimum acceptance rule defines when an enterprise, solution or product architecture item may be considered architecture-ready, release-ready or operationally mature. The rule prevents architecture readiness from being claimed when critical markers are still missing, only mentioned, insufficiently owned or not supported by evidence.

A product, solution or enterprise architecture item shall not be considered architecture-ready unless all applicable critical markers have reached at least score 3 on the maturity scale defined in Section 5.2. Score 3 means that the architecture concern is designed, owned and connected to the required responsibilities and delivery mechanisms. At this stage, the architecture does not yet have to be fully verified, but it must be sufficiently clear, traceable and actionable to guide implementation, planning or governance.

For release readiness, all applicable critical release markers must reach at least score 4. This higher threshold is required because release decisions must be based on verified evidence, not only on architecture descriptions or assigned ownership. A product or solution can only be considered release-ready when the relevant architecture claims have been verified through suitable evidence such as tests, reviews, integration results, security evidence, release baselines, compatibility declarations, deployment evidence or runtime measurements.

Critical markers are those whose failure could create significant risk for business value, cross-level alignment, integration, security, data compatibility, release compatibility, compliance, operational resilience or mission effectiveness. The set of critical markers shall be defined for each review context and recorded in the review result. Non-critical markers may remain below the target score only if the gap is visible, owned, risk-assessed and tracked as architecture runway, technical debt or an improvement action.

| **Readiness state**  | **Minimum acceptance rule**                                                           | **Definition**                                                                                                                                                                  | **Typical evidence**                                                                                                                                                    |
|----------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Architecture-ready   | All applicable critical markers score at least 3                                      | The architecture item is designed, owned, traceable and process-aware. It is sufficiently clear to guide implementation, planning or governance.                                | Architecture views, ADRs, BAPO map, ownership records, backlog enablers, review record, applicable guardrail or baseline mapping                                        |
| Release-ready        | All applicable critical release markers score at least 4                              | The architecture item is verified with evidence, compatible with required baselines and owned by accountable roles. It is sufficiently evidenced to support a release decision. | Verification evidence, integration evidence, security evidence, release compatibility matrix, product compatibility declaration, solution baseline, deployment evidence |
| Operationally mature | Relevant operational and feedback markers show continuous measurement and improvement | The architecture item is measured in operation, improved through feedback and connected to architecture, process and business decisions.                                        | Runtime metrics, monitoring dashboards, KPI trends, operational findings, Inspect & Adapt actions, technical debt reduction, guardrail updates, improvement backlog     |

<span id="_Toc233730447" class="anchor"></span>Table 63: Technology radar and technology governance

The minimum acceptance rule separates architecture readiness from release readiness. Architecture-ready means that the architecture is sufficiently defined and owned to proceed with implementation, planning or governance. Release-ready means that the architecture has been verified sufficiently to support a release decision. Operational maturity means that architecture quality is no longer assessed only at review points, but is continuously measured, improved and fed back into future architecture and business decisions.

A marker below the required threshold shall block the corresponding readiness claim unless a formal exception is approved. Such an exception must identify the risk, owner, mitigation, due date and follow-up review point. Exceptions must not be used to hide missing architecture work. They are controlled risk decisions and shall be visible in the relevant exception register, technical debt register or release readiness record.

The rule should be applied proportionally. Not every marker is critical for every architecture item, and not every review requires the same evidence depth. However, every readiness claim must be backed by explicit marker scores, reviewable evidence, accountable ownership and a clear record of remaining risks or gaps.

# SDD Enterprise Architecture Guidelines

## Purpose

This chapter defines the Enterprise Architecture Guidelines for Software-Defined Defence. These guidelines establish the guardrails that enable cross-division architectural alignment while preserving product and solution autonomy.

Enterprise Architecture is responsible for the architecture decisions that must be consistent across divisions, product lines, solutions, and long-term technology evolution. It defines the standards, reference architectures, technology rules, interface expectations, data principles, security guardrails, runtime assumptions, DevSecOps expectations, and architecture KPIs that allow HENSOLDT Software-Defined Defence capabilities to evolve coherently.

The chapter should be read as a guardrail catalogue. It does not tell product teams exactly how to implement every component. Instead, it defines the architecture constraints that must be respected whenever products and solutions need to interoperate, share data, reuse platforms, comply with security expectations, or release into a common solution baseline.

The goal is alignment, not central micromanagement.

Enterprise Architecture shall ensure that SDD-relevant divisions can develop interoperable solutions and products using consistent standards for:

- Interfaces

- Data

- Technologies

- Security

- Runtime

- Deployment

- DevSecOps

- Architecture quality

- Architecture evidence

The enterprise level is where long-term architectural coherence is protected. Without enterprise guardrails, products and solutions may choose incompatible technologies, define different data meanings, use inconsistent interface patterns, or implement different security assumptions. These differences may not be visible during early product development, but they become expensive during integration and release.

Enterprise Architecture should therefore focus on decisions that are difficult to reverse:

- Interface standards

- Data and semantic models

- Technology lifecycle decisions

- Security and trust principles

- Runtime and deployment assumptions

- DevSecOps and observability requirements

- Architecture evidence expectations

## BAPO Structure of Enterprise Guardrails

Enterprise guardrails shall be written in a consistent BAPO structure so that they are usable across Enterprise, Solution and Product Architecture. The purpose of this structure is to ensure that every guardrail has a clear business reason, a precise architecture statement, an executable process implication, accountable ownership and reviewable evidence.

A guardrail is not only a rule or recommendation. It is an enterprise architecture asset that connects strategic intent to concrete architecture decisions and delivery mechanisms. Without this structure, guardrails risk becoming either too abstract to influence implementation or too detailed to preserve solution and product autonomy.

Every enterprise guardrail shall therefore use the following structure:

| **Element**            | **Required content**                                                                                                                              | **Purpose**                                                                         |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Business driver        | Strategic theme, value stream, capability need, customer need, sovereignty need, interoperability need, security need, or product-line objective  | Explains why the guardrail exists and which business or mission outcome it supports |
| Architecture guardrail | Reference architecture, standard, technology decision, data rule, security rule, runtime rule, interoperability rule, or DevSecOps rule           | Defines the architecture expectation that must be applied consistently              |
| Process requirement    | Review mechanism, governance workflow, exception process, test requirement, KPI tracking, release rule, or compliance check                       | Defines how the guardrail is applied, verified, governed and improved               |
| Ownership requirement  | Enterprise Architect, data owner, interface owner, security owner, platform owner, DevSecOps owner, product-line owner, or architecture community | Clarifies who owns, maintains, reviews and evolves the guardrail                    |
| Evidence               | Published standard, reference architecture, catalogue, review record, exception register, adoption evidence, KPI dashboard, or release evidence   | Makes application of the guardrail visible, measurable and reviewable               |

<span id="_Toc233730448" class="anchor"></span>Table 64: Interface standards and interoperability guardrails

Each enterprise guardrail must be written so that Solution and Product Architects can apply it in practice. A guardrail that is too abstract will not guide architecture decisions. A guardrail that is too detailed will slow delivery, create unnecessary central control and reduce local product autonomy. The right level of detail defines what must be consistent while leaving room for local implementation choices where variation does not create enterprise risk.

A good enterprise guardrail must therefore answer the following questions:

| **Question**                    | **Purpose**                                                                                                          |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Why does this guardrail exist?  | Connects the guardrail to business, mission, customer, sovereignty, security or product-line value                   |
| Where does it apply?            | Defines scope and prevents over-application or under-application                                                     |
| What is mandatory?              | Creates clear enterprise alignment expectations                                                                      |
| What can be decided locally?    | Preserves solution and product autonomy where local variation is acceptable                                          |
| Who owns the guardrail?         | Ensures that the guardrail can be maintained, reviewed and evolved                                                   |
| How is compliance demonstrated? | Makes application of the guardrail reviewable through evidence                                                       |
| How are exceptions handled?     | Enables controlled deviation without weakening governance                                                            |
| How is feedback used?           | Ensures that adoption findings, exceptions, KPIs and architecture community learning improve the guardrail over time |

<span id="_Toc233730449" class="anchor"></span>Table 65: Enterprise data and semantic architecture

Figure 7 shows the lifecycle of enterprise architecture guardrails. Guardrails are not static rules that are published once and then forgotten. They are living architecture assets that start from strategic or business need, are translated into reference architectures, standards or rules, are applied by Solution and Product Architecture, are assessed through evidence and KPIs, and are improved through exceptions, adoption feedback, technical debt, architecture reviews and architecture community learning.

The lifecycle view is important because enterprise guardrails must remain both stable and adaptive. They must provide enough consistency to enable Software-Defined Defence across divisions, but they must also evolve when solution integration, product implementation, technology change or operational evidence shows that the guardrail needs to be clarified, strengthened, relaxed or retired.

<img src="/workspace/SDD_Architecture_Governance_Framework_20260630v2_media/media/image8.png" style="width:8.64583in;height:5.27083in" />

<span id="_Ref233704043" class="anchor"></span>Figure 7: Enterprise guardrail lifecycle, showing how guardrails evolve from business or strategic need through definition, publication, adoption, evidence collection, exception handling, improvement, and eventual update or retirement.

## Software-Defined Defence Strategic Alignment

Software-Defined Defence strategic alignment ensures that enterprise architecture guardrails actively support HENSOLDT’s shift toward adaptable, software-enabled and continuously evolvable defence capabilities. The purpose of this guideline is to translate the strategic intent of Software-Defined Defence into architecture expectations that can be applied consistently across divisions, solutions and products.

Strategic alignment does not mean that every product or solution must use the same implementation approach. It means that architecture decisions shall be assessed against the enterprise concerns that are critical for Software-Defined Defence, including openness, modularity, interoperability, security, digital sovereignty, DevSecOps readiness, data alignment and edge/fog/cloud deployment readiness.

The following guideline defines how Software-Defined Defence strategic alignment shall be governed:

| **Guideline element**  | **Content**                                                                                                                                                                                                                                                                             | **Governance intent**                                                                                                      |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Business driver        | HENSOLDT must enable adaptable, software-based defence capabilities and reduce dependency on rigid hardware-bound modernization cycles.                                                                                                                                                 | Connects architecture governance to strategic business and mission value.                                                  |
| Architecture guardrail | All relevant SDD architectures shall be assessed against open architecture, modularity, interoperability, DevSecOps, security, digital sovereignty, data alignment and edge/fog/cloud readiness.                                                                                        | Ensures that architecture decisions support long-term adaptability, integration and sovereign capability evolution.        |
| Process requirement    | Portfolio architecture review shall check whether epics, initiatives, solution concepts and major product investments align with the applicable SDD guardrails.                                                                                                                         | Embeds SDD alignment into portfolio and architecture decision points instead of treating it as a separate document review. |
| Ownership requirement  | Enterprise Architecture owns the SDD architecture principles and guardrails. Business Owners own strategic priority and investment intent. Product Management owns value-stream and capability alignment. Solution and Product Architects provide implementation and evidence feedback. | Clarifies that SDD alignment requires shared ownership across business, architecture and delivery roles.                   |
| Evidence               | Strategic theme mapping, SDD alignment checklist, architecture review record, guardrail mapping, portfolio decision record, exception record, adoption evidence and improvement actions.                                                                                                | Makes SDD alignment visible, reviewable and improvable.                                                                    |

<span id="_Toc233730450" class="anchor"></span>Table 66: Security, safety and sovereignity guardrails

<span id="_Toc233730445" class="anchor"></span>**Table 61:** SDD strategic alignment

This guideline should be used whenever a portfolio epic, solution initiative, product-line investment, platform decision or major architecture decision claims relevance for Software-Defined Defence. The review should ask whether the proposed architecture improves adaptability, interoperability, reuse, security, deployability, data consistency or digital sovereignty. If the answer is unclear, the architecture item should either be refined, linked to a clearer business driver, or treated as an architecture risk.

The SDD alignment check should also remain proportional. Not every product decision requires a full enterprise-level review. However, decisions that affect cross-division interoperability, solution integration, enterprise data models, platform direction, DevSecOps capability, security posture or long-term technology dependency should be assessed against the SDD guardrails.

Where an architecture item does not fully meet the SDD guardrails, the deviation shall be documented through the architecture exception process. The exception should explain the reason, affected scope, risk, owner, mitigation, review date and expected path back to alignment. This ensures that local delivery needs can be handled without weakening the long-term Software-Defined Defence architecture direction.

## Enterprise Reference Architecture Catalogue

Reference architectures should be treated as reusable architectural assets. They should include not only diagrams, but also principles, applicability rules, quality expectations, required interfaces, security assumptions, deployment patterns, and known trade-offs.

A reference architecture becomes useful when Solution and Product Architects can apply it directly. Therefore, each reference architecture should include examples, mandatory elements, optional elements, allowed variations, and evidence expectations.

| **Guideline element**  | **Content**                                                                                                                                                             |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Business driver        | Cross-division reuse and interoperability require common reference patterns                                                                                             |
| Architecture guardrail | Enterprise Architecture shall maintain approved reference architectures for MDOcore, edge/fog/cloud, DevSecOps, data, security, runtime, observability, and integration |
| Process requirement    | Solution and product architectures shall declare which reference architectures they use or why they deviate                                                             |
| Ownership requirement  | Enterprise Architect owns catalogue; Solution Architects and Product Architects apply it                                                                                |
| Evidence               | Reference architecture catalogue, adoption matrix, deviation ADRs                                                                                                       |

<span id="_Toc233730451" class="anchor"></span>Table 67: Runtime, platform and Edge/Fog/Cloud guardrails

## Technology Radar and Technology Governance

Technology governance should not be used to block innovation. Its purpose is to manage risk and alignment. A technology radar helps teams understand which technologies are strategic, which are allowed, which are temporary, and which are no longer acceptable.

A technology can be locally useful but strategically harmful if it creates long-term maintenance risk, supplier lock-in, security exposure, licensing risk, deployment incompatibility, or integration complexity. The technology radar makes these trade-offs explicit.

| **Guideline element**  | **Content**                                                                                                       |
|------------------------|-------------------------------------------------------------------------------------------------------------------|
| Business driver        | Technology choices must support long-term maintainability, interoperability, security, and product-line evolution |
| Architecture guardrail | Technologies shall be classified as strategic, approved, tolerated, deprecated, or prohibited                     |
| Process requirement    | New technologies require architecture review; deprecated technologies require migration plans                     |
| Ownership requirement  | Enterprise Architect owns radar; Product Architects own product-level technology declarations                     |
| Evidence               | Technology radar, exception register, migration backlog                                                           |

<span id="_Toc233730452" class="anchor"></span>Table 68: DevSecOps and Continuous Release guardrails

## Interface Standards and Interoperability Guardrails

Interface standards are among the most important enterprise guardrails. They determine whether products can be integrated reliably, whether solution releases can be verified, and whether products can release independently without breaking solution baselines.

Enterprise interface standards should therefore define not only technical formats, but also ownership, versioning, deprecation, compatibility, security, testing, and documentation expectations.

| **Guideline element**  | **Content**                                                                                                                      |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Business driver        | Cross-division interoperability, partner integration, and independent product releases require stable interface standards        |
| Architecture guardrail | Mandatory interface standards shall define API styles, messaging, topics, schemas, versioning, compatibility, and error handling |
| Process requirement    | Interfaces require review, contract testing, schema validation, and compatibility checks                                         |
| Ownership requirement  | Interface owners are mandatory for enterprise-level and solution-level interfaces                                                |
| Evidence               | Interface standards catalogue, API contracts, topic catalogue, contract test results                                             |

<span id="_Toc233730453" class="anchor"></span>Table 69: Architecture KPIs

## Enterprise Data and Semantic Architecture

Enterprise data architecture is essential for moving from data transport to information value. Without common data models and semantic rules, products may exchange data but interpret it differently. This can lead to inconsistent operational pictures, duplicated transformations, and unreliable AI or analytics.

The enterprise data architecture should define the common language used across SDD solutions. It should also define who owns data definitions, how schemas evolve, how metadata and provenance are handled, and how data quality is measured.

| **Guideline element**  | **Content**                                                                                                                             |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Business driver        | Information superiority requires trusted, consistent, and mission-relevant data across products and domains                             |
| Architecture guardrail | Enterprise shall define common data models, semantic concepts, metadata, provenance, classification, quality rules, and lifecycle rules |
| Process requirement    | Data contracts require review, schema validation, quality checks, and lifecycle governance                                              |
| Ownership requirement  | Data Architect owns data architecture; data owners own domain data definitions                                                          |
| Evidence               | Enterprise data model, semantic model, metadata catalogue, data ownership matrix                                                        |

<span id="_Toc233730454" class="anchor"></span>Table 70: Architecture exeption process

## Security, Safety and Sovereignity Guardrails

Security, safety, and sovereignty must be treated as architecture constraints. They are not late-stage approval activities. Enterprise guardrails should ensure that trust boundaries, identity, cryptography, monitoring, audit, vulnerability handling, secure updates, and data classification are considered early enough to influence design.

Where defence-specific safety, compliance, classification, or export-control constraints apply, these must be connected to architecture evidence and release readiness criteria.

| **Guideline element**  | **Content**                                                                                                                                                                                     |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Business driver        | Defence systems require trustworthy, sovereign, secure, and mission-safe operation                                                                                                              |
| Architecture guardrail | Enterprise shall define zero-trust principles, identity, authentication, authorization, cryptography, key management, trust zones, audit, monitoring, secure update, and vulnerability handling |
| Process requirement    | Threat modelling, security review, vulnerability management, and security test evidence are mandatory for applicable systems                                                                    |
| Ownership requirement  | Security Architect owns guardrails; product security owners own implementation evidence                                                                                                         |
| Evidence               | Security guardrail catalogue, threat model template, security review record, vulnerability register                                                                                             |

<span id="_Toc233730455" class="anchor"></span>Table 71: BAPO structure oft he solution architecture

## Runtime, Platform and Edge / Fog / Cloud Guardrails

Runtime, platform and Edge/Fog/Cloud guardrails ensure that Software-Defined Defence capabilities can be deployed, operated, observed, updated and recovered across different execution environments. These environments may range from resource-constrained tactical edge nodes to fog-level mission infrastructure and cloud-based services. The guardrails are therefore required to prevent each product or solution from making incompatible runtime, deployment, observability, update or configuration decisions.

The purpose of this guideline is not to prescribe one single platform for all use cases. Instead, Enterprise Architecture shall define the minimum runtime and platform expectations that solutions and products must consider when they are intended to operate across edge, fog or cloud environments. This includes deployment reproducibility, environment compatibility, service discovery, configuration, observability, update mechanisms, security controls, resource assumptions and resilience under degraded connectivity.

| **Guideline element**  | **Content**                                                                                                                                                                                                                                                     | **Governance intent**                                                                                                                           |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Business driver        | SDD capabilities must operate across tactical edge, fog and cloud environments while remaining deployable, observable, secure and maintainable.                                                                                                                 | Connects runtime and platform architecture to mission adaptability, operational availability and long-term capability evolution.                |
| Architecture guardrail | Enterprise Architecture shall define runtime, containerization, orchestration, deployment, observability, service discovery, configuration, update, rollback and environment-compatibility principles.                                                          | Ensures that products and solutions can be deployed consistently across target environments without creating incompatible platform assumptions. |
| Process requirement    | Deployment configurations, update mechanisms and environment assumptions must be tested and declared release-compatible for the relevant solution baseline.                                                                                                     | Makes deployment readiness, runtime compatibility and operational resilience verifiable before release.                                         |
| Ownership requirement  | The Platform Architect owns runtime and platform guardrails. Solution Architects own solution-level deployment alignment. Product teams own product deployment implementation and evidence. Security Architects own runtime security controls where applicable. | Clarifies shared responsibility between enterprise platform guidance, solution deployment alignment and product-level evidence.                 |
| Evidence               | Runtime reference architecture, deployment manifest, environment compatibility matrix, deployment pipeline evidence, observability dashboard, update and rollback evidence, resource measurements, DIL or degraded-connectivity test evidence.                  | Makes runtime and platform alignment visible, testable and reviewable.                                                                          |

<span id="_Toc233730456" class="anchor"></span>Table 72: Solution Capability and mission thread definition

This guideline should be used whenever a product or solution is expected to run in more than one operational environment, or where deployment location, connectivity, resource constraints, security classification, latency, observability or updateability materially affect the architecture. The review should ask whether the architecture defines where workloads run, how they are configured, how services discover each other, how operational health is monitored, how updates are performed, how rollback works, and how the deployment remains compatible with the relevant solution baseline.

The guardrail should also make environment assumptions explicit. A product that works in a cloud environment may not automatically be suitable for tactical edge deployment. Edge environments may have limited compute resources, intermittent connectivity, stricter update windows, local security constraints or degraded operating modes. Conversely, cloud or fog environments may introduce different scalability, observability, data-protection and dependency-management requirements. These differences must be visible in the architecture evidence.

Where a product or solution cannot fully comply with the runtime and platform guardrails, the deviation shall be handled through the architecture exception process. The exception should identify the affected environment, the reason for the deviation, the operational risk, the owner, the mitigation and the follow-up review point. This ensures that local deployment needs can be supported without creating uncontrolled runtime fragmentation across Software-Defined Defence solutions.

## DevSecOps and Continuous Release Guardrails

DevSecOps and continuous release guardrails ensure that Software-Defined Defence capabilities can be built, tested, secured, deployed and released in a repeatable and evidence-based way. The purpose of this guideline is to prevent release readiness from depending on manual interpretation, undocumented test results or inconsistent product-level delivery practices.  
  
Enterprise Architecture shall define the minimum DevSecOps expectations that products and solutions must satisfy when they contribute to Software-Defined Defence capabilities. These expectations include automated build and test mechanisms, security scans, deployment automation, traceable release evidence, compatibility checks, monitoring, vulnerability handling and feedback from operation into architecture improvement.  
  
The goal is not to enforce one identical pipeline for every product. The goal is to ensure that every relevant product and solution can demonstrate how architecture decisions are implemented, verified, secured, deployed and released through reliable delivery mechanisms.

| **Guideline element**  | **Content**                                                                                                                                                                                                                                                                                         | **Governance intent**                                                                                                               |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Business driver        | HENSOLDT needs faster modernization, secure delivery and continuous release readiness for software-defined capabilities.                                                                                                                                                                            | Connects DevSecOps architecture to business agility, mission adaptability, security and release confidence.                         |
| Architecture guardrail | Products and solutions shall support CI/CD, automated testing, security scanning, deployment automation, monitoring, vulnerability handling and traceable release evidence.                                                                                                                         | Ensures that architecture quality can be verified through repeatable engineering mechanisms instead of manual claims.               |
| Process requirement    | Release readiness shall include automated build evidence, test evidence, security evidence, deployment evidence, compatibility evidence and release declaration evidence.                                                                                                                           | Makes product and solution release decisions evidence-based and reviewable.                                                         |
| Ownership requirement  | Platform teams own pipeline enablement and shared DevSecOps capabilities. Product teams own pipeline usage, product-level evidence and remediation. Solution Architects own solution-level compatibility expectations. Security Architects own security verification expectations where applicable. | Clarifies shared responsibility between platform enablement, product execution, solution release governance and security assurance. |
| Evidence               | CI/CD pipeline records, automated test results, contract test results, security scan results, deployment manifests, release compatibility matrix, release declaration, monitoring evidence and vulnerability remediation records.                                                                   | Makes delivery, security, deployment and release readiness visible, measurable and auditable.                                       |

<span id="_Toc233730457" class="anchor"></span>Table 73: Product participation and capability allocation

This guideline should be used whenever a product or solution is expected to contribute to a releasable Software-Defined Defence capability. The review should ask whether the architecture can be built reproducibly, tested automatically, scanned for security risks, deployed consistently, monitored in operation and linked to release evidence. Where the answer depends on manual steps or undocumented assumptions, the gap should be treated as architecture runway, process debt or product-level technical debt.

Continuous release readiness does not mean that every product is released continuously into operation. It means that the product or solution maintains the technical and evidential capability to support controlled, secure and repeatable release decisions. This is especially important when independently evolving products must remain compatible with a solution baseline.

DevSecOps evidence should also feed back into architecture governance. Failed tests, recurring security findings, deployment failures, compatibility issues, observability gaps or operational incidents may indicate that architecture guardrails, product architecture decisions, platform assumptions or release processes need to be improved. These findings should be captured through Inspect & Adapt, technical debt registers, architecture runway or guardrail updates.

Where a product or solution cannot fully comply with the DevSecOps and continuous release guardrails, the deviation shall be handled through the architecture exception process. The exception should identify the missing capability, release risk, security or integration impact, owner, mitigation and follow-up review point.

## Architecture KPIs

Architecture KPIs shall be used to improve the architecture system, not to punish teams. Their purpose is to reveal whether enterprise guardrails are working. If a KPI shows low adoption of a reference architecture, the reason may be insufficient communication, poor usability, missing tooling, or a reference architecture that no longer fits product needs.

KPIs should therefore be reviewed as feedback into architecture governance.

| **KPI**                              | **Purpose**                                                    |
|--------------------------------------|----------------------------------------------------------------|
| Reference architecture adoption rate | Measures use of approved patterns                              |
| Interface standard compliance        | Measures adherence to enterprise interface standards           |
| Data model adoption                  | Measures use of common data and semantic models                |
| Technology radar compliance          | Measures approved versus deviating technologies                |
| Security evidence completeness       | Measures security-by-design maturity                           |
| DevSecOps automation rate            | Measures build/test/deploy automation                          |
| Technical debt trend                 | Measures debt growth or reduction                              |
| Release compatibility rate           | Measures successful product and solution release compatibility |
| Reuse rate                           | Measures reuse of components, services, platforms, or patterns |
| Architecture exception aging         | Measures whether exceptions are temporary and actively managed |

<span id="_Toc233730458" class="anchor"></span>Table 74: Cross-product interface architecture

## Architecture Exception Process

The architecture exception process provides a controlled way to handle justified deviations from enterprise guardrails. Its purpose is not to block delivery, but to ensure that deviations are visible, risk-assessed, owned, time-bounded and fed back into architecture governance.

An exception may be required when a product, solution or initiative cannot fully comply with an enterprise guardrail because of customer constraints, mission needs, legacy dependencies, technology limitations, delivery timing, security constraints or integration realities. Such deviations shall not remain informal. They must be documented as explicit architecture decisions with clear rationale, impact, ownership, mitigation and review date.

An architecture exception is therefore a controlled risk decision, not a silent waiver. It must explain why the deviation is needed, what risk it creates, who accepts or mitigates the risk, how long the exception is valid, and whether the guardrail itself needs to be clarified or improved.

| **Step**                 | **Description**                                                                                                                                                   | **Required content / evidence**                                                                              |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Identify deviation       | A team, architect or governance body identifies a deviation from an enterprise guardrail, reference architecture, standard or mandatory architecture expectation. | Affected guardrail, affected product or solution, deviation description, discovery source                    |
| Document rationale       | The deviation is documented with a clear business and architecture rationale.                                                                                     | Business reason, mission/customer constraint, architecture reason, alternatives considered, rejected options |
| Assess impact            | The deviation is assessed for enterprise, solution and product impact.                                                                                            | Integration impact, security impact, data impact, release impact, operational impact, technical debt impact  |
| Assess BAPO implications | The deviation is checked against Business, Architecture, Process and Organization consequences.                                                                   | Business priority, architecture risk, required process change, responsible owner or governance body          |
| Decide exception         | The Architecture Review Board or responsible architecture owner approves, rejects or requests rework.                                                             | Decision record, approval status, conditions, required mitigation, escalation if required                    |
| Assign owner             | An accountable owner is assigned for mitigation, monitoring, follow-up and expiration.                                                                            | Named owner, affected team, responsible architect, mitigation backlog item                                   |
| Define validity          | The exception receives a review date, expiry date and expected path to closure or renewal.                                                                        | Review date, expiry date, closure criteria, target guardrail alignment or accepted long-term deviation       |
| Track and report         | The exception is tracked in the exception register and reviewed until closure.                                                                                    | Exception register entry, status, risk level, mitigation progress, review history                            |
| Feed back                | Repeated or high-impact exceptions trigger guardrail review, architecture runway, technical debt or portfolio action.                                             | Guardrail update, architecture debt item, improvement backlog, KPI trend, portfolio decision                 |

<span id="_Toc233730459" class="anchor"></span>Table 75: Solution Data Flow and semantic alignment

The exception process should be applied proportionally. Minor local deviations may be handled by the responsible architect if they do not affect enterprise alignment, solution integration, security, data compatibility or release readiness. Major deviations that affect multiple products, multiple solutions, enterprise guardrails, security posture, customer commitments or long-term technology direction should be reviewed by the Architecture Review Board or the responsible enterprise architecture governance body.

Every approved exception must remain visible until it is closed, expired or renewed. Exceptions should not become permanent undocumented alternatives to the guardrails. Where an exception remains necessary over multiple review cycles, the governance body should decide whether the guardrail is still correct, whether a controlled variant should be added, or whether the deviation represents enterprise technical debt that requires funding or remediation.

Repeated exceptions are especially important. If several products or solutions request similar deviations, this may indicate that the enterprise guardrail is unclear, too restrictive, outdated or not supported by the required platform or process capabilities. In such cases, the feedback should trigger guardrail improvement rather than repeated isolated approvals.

# SDD Solution Architecture Guidelines

## Purpose

This chapter defines how Solution Architecture shall be performed for Software-Defined Defence capabilities. Solution Architecture is the bridge between enterprise guardrails and product implementation.

The solution level is where cross-product complexity becomes visible. A solution may include any number of products, each with its own backlog, roadmap, release cycle, and technical constraints. The Solution Architect must align these products so that they deliver one coherent business or mission capability.

The chapter is especially important for MDOcore-like solutions. HENSOLDT positions MDOcore as a software suite for Multi-Domain Operations that connects sensors and command-and-control systems across domains, provides a unified resilient operational picture, supports interoperability, and operates across edge, fog, and cloud environments.

Solution Architecture Guidelines define how multiple products are aligned into one coherent, releasable software-defined defence solution.

A solution architecture is required when:

- Any number of products must work together

- Cross-product interfaces are needed

- Solution-level releases are required

- Product-level releases must remain compatible

- Shared quality attributes must be verified

- Integrated security and data flows span multiple products

The Solution Architecture exists because products alone do not deliver the full capability. A product may be technically strong, but if it uses incompatible interfaces, inconsistent data models, or unsupported security assumptions, the solution will fail during integration.

The solution level must therefore define:

- Which products participate

- Which capabilities each product contributes

- Which interfaces connect the products

- Which data contracts are shared

- Which security assumptions apply across products

- Which runtime and deployment topology is used

- Which product versions form the solution baseline

- Which tests prove integrated behavior

## BAPO Structure oft he Solution Architecture

The solution BAPO view should remain focused on architecture. It does not define the entire organization or delivery model. It identifies only the process and ownership mechanisms required to keep the solution architecture aligned.

For example, if the solution architecture depends on a stable cross-product interface, then the required process is interface review and contract testing, and the required ownership is an interface owner. If the solution architecture depends on a shared data model, then the required process is data contract validation, and the required ownership is a data owner.

| **Element**                    | **Required content**                                                                                                   |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Business capability            | Customer-facing or mission-facing capability delivered by the solution                                                 |
| Solution architecture decision | Product participation, capability allocation, interfaces, data flows, runtime, security, deployment, and release model |
| Process requirement            | Integration cadence, contract testing, solution demo, verification, release approval, compatibility checks             |
| Ownership requirement          | Solution architect, product architects, interface owners, data owners, security owners, system team                    |
| Evidence                       | Solution architecture document, interface catalogue, product compatibility matrix, integration test results            |

<span id="_Toc233730460" class="anchor"></span>Table 76: Solution Security and trust boundary architecture

## Solution Capability and Mission Thread Definition

Mission threads are one of the most useful tools for solution architecture. They show how value flows through multiple products. They help identify interfaces, data dependencies, runtime dependencies, security boundaries, and verification scenarios.

A solution architecture should define enough mission threads to prove the critical behavior of the solution. These mission threads should later become integration test scenarios and system demo scenarios.

| **Guideline element** | **Content**                                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------------------------|
| Business driver       | The solution must deliver an end-to-end mission or business capability                                           |
| Architecture response | Define mission threads, operational scenarios, system context, participating products, and capability allocation |
| Process requirement   | Mission threads shall be used for integration tests and solution demos                                           |
| Ownership requirement | Solution Architect owns capability architecture; Product Management owns capability priority                     |
| Evidence              | Capability map, mission thread model, solution context diagram                                                   |

<span id="_Toc233730461" class="anchor"></span>Table 77: Integrated runtime and deployment architecture

## Product Participation and Capability Allocation

Product participation and capability allocation define which products contribute to a solution and which solution capabilities each product is responsible for. This is a core Solution Architecture activity because a solution is not created by listing products next to each other. A solution becomes governable only when product roles, capability ownership, interface responsibilities and release dependencies are explicit.

The purpose of this guideline is to avoid unclear product boundaries, duplicated functionality, missing ownership, hidden dependencies and integration risk. Solution Architecture must show how the required business or mission capability is decomposed into product contributions and how these contributions are integrated into one coherent solution baseline.

| **Guideline element** | **Content**                                                                                                                                                                                                                                      | **Governance intent**                                                                                                                           |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Business driver       | Multiple products must contribute coherently to one solution capability or mission outcome.                                                                                                                                                      | Ensures that product participation is driven by solution value, not by organizational convenience or historical product boundaries.             |
| Architecture response | Define which products participate in the solution, which capability each product contributes, which product owns which interfaces, and which dependencies exist between products.                                                                | Creates a clear solution structure and prevents duplicated, missing or conflicting product responsibilities.                                    |
| Process requirement   | Product participation and capability allocation must be reviewed during solution planning, PI planning, integration planning and release planning. Changes must be reflected in the solution baseline.                                           | Ensures that capability allocation is not a static diagram, but remains aligned with planning, integration, verification and release decisions. |
| Ownership requirement | The Solution Architect owns the overall capability allocation and product participation map. Product Architects own the architecture evidence for their product contribution. Product Management and Business Owners confirm value and priority. | Clarifies shared responsibility between solution-level coherence and product-level implementation ownership.                                    |
| Evidence              | Product participation map, capability-to-product matrix, interface ownership map, dependency map, solution baseline, product contribution statements, compatibility declarations and review records.                                             | Makes product contribution, ownership and release compatibility visible and reviewable.                                                         |

<span id="_Toc233730462" class="anchor"></span>Table 78: Solution release architecture

The product participation map should identify all products that contribute to the solution, the capabilities they provide, the interfaces they expose or consume, and the dependencies that affect integration and release compatibility. The capability-to-product matrix should make clear whether a capability is owned by one product, shared across several products, or still unresolved.

Capability allocation should also identify architecture risks. A capability may be at risk if ownership is unclear, if several products provide overlapping functionality, if a required interface is not yet specified, if data ownership is missing, or if a product release is not compatible with the intended solution baseline. These risks should be captured as solution architecture runway, integration risks or solution-level technical debt.

Where several products could provide the same capability, the Solution Architect should document the allocation rationale. This should include the reason for the selected product, rejected alternatives where relevant, expected integration impact, required interface or data contracts, and consequences for future product autonomy. This makes the solution architecture decision traceable and prevents later ambiguity.

Product participation and capability allocation must be updated whenever the solution scope, product contribution, interface ownership, release baseline or capability priority changes. A solution release baseline should not be considered complete unless the participating products and their allocated capabilities are clear, owned, evidenced and compatible.

## Cross-Product Interface Architecture

Cross-product interfaces must be treated as first-class architecture elements. They should not be left to individual teams to negotiate informally. A cross-product interface affects multiple product backlogs, test environments, release compatibility, security, and operational behavior.

Every cross-product interface should have an owner, version, contract, test strategy, compatibility rule, and deprecation rule. Without these elements, independent product releases become risky.

| **Guideline element** | **Content**                                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------------------------|
| Business driver       | Products must integrate reliably and release independently without breaking the solution                        |
| Architecture response | Define cross-product APIs, topics, messages, schemas, protocols, ownership, versioning, and compatibility rules |
| Process requirement   | Contract testing, interface review, compatibility testing, and schema validation are required                   |
| Ownership requirement | Interface owners are mandatory for all cross-product interfaces                                                 |
| Evidence              | Cross-product interface catalogue, contract tests, compatibility matrix                                         |

<span id="_Toc233730463" class="anchor"></span>Table 79: Independent product release compatibility

## Solution Data Flow and Semantic Alignment

Solution data flow architecture should show how data moves from source to consumer across products. It should also show where data is transformed, enriched, filtered, stored, classified, or exposed as a service.

Semantic alignment is especially important when products from different divisions or suppliers contribute to one solution. If the meaning of data is not aligned, technical integration may still produce incorrect operational interpretation.

| **Guideline element** | **Content**                                                                                                   |
|-----------------------|---------------------------------------------------------------------------------------------------------------|
| Business driver       | The solution must turn product-level data into mission-relevant information                                   |
| Architecture response | Define data flows, data contracts, semantic mapping, metadata, provenance, classification, and data lifecycle |
| Process requirement   | Data contracts require validation, review, and integration test evidence                                      |
| Ownership requirement | Data Architect and solution data owners are required                                                          |
| Evidence              | Solution data flow model, semantic mapping, data contract catalogue                                           |

<span id="_Toc233730464" class="anchor"></span>Table 80: Integration and verification strategy on solution level

## Solution Security and Trust Boundary Architecture

Solution security and trust boundary architecture define how security is governed across multiple products that operate together as one solution. This is required because security cannot be assessed only at the product level when identities, data flows, interfaces, deployment zones, operational roles and audit responsibilities span several products.

The purpose of this guideline is to make the solution-level security structure explicit. Solution Architecture must show where trust zones begin and end, which identities and access rules apply, where data crosses security boundaries, which cryptographic protections are required, how logging and audit evidence are collected, and how security assumptions remain compatible across the participating products.

| **Guideline element** | **Content**                                                                                                                                                                                                                                                    | **Governance intent**                                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Business driver       | Cross-product operation requires consistent trust, protection, auditability and compliance across the complete solution.                                                                                                                                       | Ensures that security is treated as a solution-level architecture concern, not only as separate product implementation detail. |
| Architecture response | Define solution trust zones, identities, access rules, authorization boundaries, crypto boundaries, secure communication paths, logging, audit, monitoring and security-relevant data flows.                                                                   | Creates a clear security architecture for the integrated solution and prevents inconsistent product-level assumptions.         |
| Process requirement   | Solution-level threat modelling, security architecture review, security verification and release-readiness checks are required.                                                                                                                                | Ensures that security assumptions are reviewed, verified and evidenced before the solution is released.                        |
| Ownership requirement | The Security Architect owns the solution security concept and trust-boundary model. The Solution Architect ensures integration with the overall solution architecture. Product Security Owners and Product Architects provide product-level security evidence. | Clarifies responsibility between solution-level security design and product-level security implementation evidence.            |
| Evidence              | Solution threat model, trust-zone diagram, identity and access model, crypto assumptions, security requirements, security test evidence, vulnerability findings, audit/logging evidence and product security declarations.                                     | Makes solution security reviewable, testable and traceable across products.                                                    |

<span id="_Toc233730465" class="anchor"></span>Table 81: Solution architecture runway

The trust-boundary model should identify all relevant security zones, participating products, external systems, communication paths, identity providers, authorization points, crypto boundaries, logging responsibilities and audit-relevant events. It should also show where data crosses boundaries between products, domains, classifications, runtime environments or operational responsibilities.

Solution-level security review should verify that the participating products share compatible security assumptions. A product may be secure in isolation but still create solution-level risk if identity handling, authorization logic, crypto configuration, logging, monitoring, data classification or vulnerability handling is inconsistent with the solution security concept.

Security evidence must therefore be collected at both levels. Product teams provide evidence that their product implements the required controls. Solution Architecture and Security Architecture assess whether these controls work together across the full solution. Gaps should be captured as solution security risks, product follow-up actions, architecture runway, technical debt or release-readiness blockers.

Where a product or solution cannot fully satisfy the solution security and trust-boundary expectations, the deviation shall be handled through the architecture exception process. The exception must identify the affected security boundary, the risk, the owner, the mitigation, the review date and the impact on release readiness.

## Integrated Runtime and Deployment Architecture

Integrated runtime and deployment architecture defines how the participating products of a solution are deployed, configured, connected, observed and operated as one coherent solution. This is required because a solution may be architecturally correct on paper, but still fail in practice if runtime dependencies, deployment topology, infrastructure assumptions, configuration rules or environment constraints are not aligned.

The purpose of this guideline is to make the operational execution model of the solution explicit. Solution Architecture must show where solution components run, how products are distributed across edge, fog and cloud environments, which runtime dependencies exist, how configuration is managed, how services discover and communicate with each other, how observability is provided, and how deployment compatibility is verified before release.

| **Guideline element** | **Content**                                                                                                                                                                                                                                                                    | **Governance intent**                                                                                                                       |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Business driver       | The solution must be deployable and operable in realistic mission, customer and operational environments.                                                                                                                                                                      | Ensures that deployment architecture is driven by real operational constraints, not only by development or laboratory assumptions.          |
| Architecture response | Define the integrated deployment topology, runtime dependencies, edge/fog/cloud placement, infrastructure assumptions, configuration model, service discovery, observability, update and rollback assumptions.                                                                 | Creates a clear runtime model for the complete solution and prevents incompatible product-level deployment assumptions.                     |
| Process requirement   | Deployment verification, environment compatibility checks, configuration validation and release-baseline alignment are required.                                                                                                                                               | Ensures that deployment readiness is verified before the solution is declared release-compatible.                                           |
| Ownership requirement | The Solution Architect owns the integrated deployment architecture. The Platform Architect owns platform and runtime guardrails. Product Architects own product-level deployment evidence. DevSecOps and operations roles support automation, monitoring and release evidence. | Clarifies shared responsibility between solution-level deployment coherence, platform enablement and product-level implementation evidence. |
| Evidence              | Solution deployment view, runtime configuration, environment compatibility matrix, deployment manifests, infrastructure assumptions, observability evidence, deployment pipeline evidence, update/rollback evidence and resource measurements.                                 | Makes runtime and deployment readiness visible, testable and reviewable.                                                                    |

<span id="_Toc233730466" class="anchor"></span>Table 82: Solution risk and technical debt governance

The integrated deployment view should show all relevant runtime nodes, containers, services, products, infrastructure dependencies, network zones, communication paths and operational environments. It should also identify which parts of the solution are deployed at the tactical edge, in fog-level mission infrastructure, in cloud environments or in hybrid configurations.

Deployment architecture must also make assumptions explicit. This includes resource constraints, latency expectations, connectivity limitations, security zones, configuration dependencies, data locality, update windows, observability requirements and degraded-connectivity behavior. A product that is deployable in isolation may still create solution-level risk if its runtime assumptions are incompatible with the intended solution environment.

Solution-level deployment verification should confirm that the participating products can be deployed together, configured consistently, monitored effectively and operated within the intended environment constraints. Evidence may come from deployment tests, environment compatibility checks, infrastructure-as-code records, runtime configuration validation, monitoring dashboards, update and rollback tests, or operational rehearsal results.

Where runtime or deployment gaps are identified, they should be captured as solution architecture runway, deployment risk, product follow-up action, platform improvement or solution-level technical debt. A solution release baseline should not be considered complete unless the deployment topology, runtime dependencies, configuration assumptions and environment compatibility are sufficiently defined, owned and evidenced.

## Solution Release Architecture

A solution release baseline is the architectural contract for a releasable solution. It defines which product versions, interface versions, data model versions, security assumptions, runtime configurations, and deployment settings are known to work together.

The solution baseline should be maintained as a living artifact. Product teams should know which solution baselines they support. Solution release decisions should be based on verified compatibility, not on assumed compatibility.

| **Element**  | **Required content**                                                                                   |
|--------------|--------------------------------------------------------------------------------------------------------|
| Business     | Release objective, customer value, mission capability, operational scenario                            |
| Architecture | Product versions, interface versions, data model versions, runtime configuration, security baseline    |
| Process      | Integration tests, compatibility checks, system demo, release approval, rollback                       |
| Organization | Release owner, solution architect, product owners, product architects, system team, verification owner |
| Evidence     | Solution baseline, release notes, verification matrix, compatibility declaration                       |

<span id="_Toc233730467" class="anchor"></span>Table 83: High level question fort he product architecture

Figure 8 illustrates the solution release baseline model. A solution release baseline is not just a set of product versions. It is an architecture alignment artifact that combines product versions, interface versions, data model versions, security baseline, runtime configuration, verification evidence, and release compatibility rules.

<img src="/workspace/SDD_Architecture_Governance_Framework_20260630v2_media/media/image9.png" style="width:8.53125in;height:5.4375in" />

<span id="_Ref233704145" class="anchor"></span>Figure 8: Solution release baseline model, showing how multiple compatible product releases, interface versions, data model versions, security baseline, runtime configuration, and verification evidence form one releasable solution baseline.

## Independent Product Release Compatibility

Independent product releases are a key advantage of modular Software-Defined Defence architectures. They allow products to evolve faster without forcing a full solution release every time. However, this only works if compatibility is governed.

A product release may be independent, but it is not isolated. It must declare which solution baselines it supports, which interface versions it implements, which data model versions it uses, and which limitations apply.

| **Rule**               | **Description**                                                                          |
|------------------------|------------------------------------------------------------------------------------------|
| Backward compatibility | Product releases shall not break supported solution baselines unless explicitly approved |
| Interface versioning   | Interfaces shall use defined versioning and deprecation rules                            |
| Contract testing       | Product releases shall pass contract tests for supported solution baselines              |
| Release declaration    | Products shall publish compatibility declarations                                        |
| Migration support      | Breaking changes require migration, rollback, or transition strategy                     |

<span id="_Toc233730468" class="anchor"></span>Table 84: BAPO structure oft he product level architecture

## Integration and Verification Strategy

The integration and verification strategy defines how the solution architecture is proven across all participating products. A solution is not sufficiently governed when each product is verified only in isolation. Solution-level verification must demonstrate that interfaces, data flows, security assumptions, runtime dependencies, deployment configuration, performance behavior, resilience and release compatibility work together as one coherent solution.

The purpose of this guideline is to make integration evidence explicit before release readiness is claimed. The Solution Architect must define which architecture assumptions require verification, which products are involved, which environments are needed, which evidence is acceptable, and how findings are converted into follow-up actions, technical debt, architecture runway or release blockers.

The following verification areas define the minimum solution-level integration and verification scope:

| **Verification area** | **Verification intent**                                                                                                 | **Required evidence**                                                                                                           |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Interface integration | Verify that cross-product interfaces are compatible, versioned, implemented and usable by the participating products.   | Contract test results, interface validation, ICD review, API/topic/schema compatibility evidence, interface owner sign-off      |
| Data consistency      | Verify that data structures, schemas, topics, semantics, classifications and ownership are aligned across the solution. | Schema validation, semantic mapping tests, data flow review, topic validation, data ownership evidence, classification evidence |
| Security              | Verify that the solution-level security concept works across product boundaries, trust zones and runtime environments.  | Threat model evidence, vulnerability results, crypto verification, identity/access validation, logging and audit evidence       |
| Performance           | Verify that the integrated solution satisfies latency, throughput, load, scheduling and resource expectations.          | Latency measurements, throughput results, load test evidence, resource measurements, performance budget validation              |
| Resilience            | Verify that the solution can tolerate failures, degraded operation, DIL conditions and recovery scenarios.              | Failure-mode tests, degraded-mode tests, DIL test evidence, restart/failover tests, recovery measurements                       |
| Deployment            | Verify that the solution can be deployed, configured, observed and updated in the intended environments.                | Deployment automation evidence, environment validation, deployment manifest, observability checks, update and rollback evidence |
| Release compatibility | Verify that the participating product releases form one compatible solution release baseline.                           | Product compatibility matrix, solution release baseline, release declaration, integration test evidence, unresolved risk record |

<span id="_Toc233730469" class="anchor"></span>Table 85: Product context and scope

The integration and verification strategy should be defined early enough to influence solution planning, PI planning, architecture runway and product backlog priorities. Verification must not be postponed until release readiness if the required evidence depends on missing environments, unavailable product releases, undefined interfaces or unresolved security assumptions.

Solution-level verification should also distinguish between product evidence and integration evidence. Product evidence shows that a product satisfies its own architecture and quality requirements. Integration evidence shows that the participating products work together according to the solution architecture. Both are required for release readiness, but they answer different questions.

Findings from integration and verification activities must be fed back into architecture governance. Failed contract tests, inconsistent schemas, security gaps, deployment failures, performance deviations or resilience weaknesses should be captured as product follow-up actions, solution technical debt, architecture runway, release-readiness risks or guardrail improvement requests.

A solution release baseline should not be considered release-ready unless the required integration and verification evidence is available, current, owned and traceable to the relevant solution architecture decisions.

## Solution Architecture Runway

The Solution Architecture runway defines the architecture preparation needed before integration, verification or release becomes blocked. It captures cross-product enablers that must be available early enough for participating products to implement compatible interfaces, data flows, security mechanisms, deployment assumptions and verification evidence.

The purpose of solution architecture runway is not to create speculative architecture work. It is to identify the structural capabilities, shared decisions, technical foundations and integration mechanisms that are required for the solution to evolve safely. Runway items should therefore be linked to concrete solution capabilities, integration risks, release dependencies or quality-marker gaps.

| **Runway item**    | **Purpose**                                                                           | **Example runway content**                                                                                                          |
|--------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Interface runway   | Prepare the shared interface foundations required for cross-product integration.      | Shared API standards, topic model, interface versioning rules, compatibility test framework, ICD templates                          |
| Data runway        | Prepare common data structures, semantics and validation mechanisms.                  | Common data model, semantic mapping, schema validation, data classification rules, metadata conventions                             |
| Security runway    | Prepare the solution-level security mechanisms required across product boundaries.    | Identity model, crypto assumptions, trust-zone model, audit logging, access-control patterns, security verification approach        |
| Platform runway    | Prepare the runtime and deployment foundations required for the solution environment. | Runtime architecture, deployment automation, observability model, configuration approach, environment compatibility checks          |
| Integration runway | Prepare the technical and organizational basis for integration and demonstration.     | Integration environment, simulators, test harnesses, system demo capability, integration sequencing, dependency map                 |
| Resilience runway  | Prepare the mechanisms needed to verify degraded operation and recovery.              | DIL test setup, degraded-mode scenarios, failover concept, recovery automation, resilience test evidence                            |
| Release runway     | Prepare the evidence and structures needed for solution release readiness.            | Solution baseline structure, product compatibility matrix, release evidence template, release declaration, unresolved-risk tracking |

<span id="_Toc233730470" class="anchor"></span>Table 86: Building block view, product architecture

Solution architecture runway should be reviewed during solution planning, PI planning, integration planning and release-readiness preparation. Each runway item should have a clear owner, affected products, expected delivery horizon, related quality markers and evidence expectation. If a runway item is required for integration or release but is not planned, it should be treated as a solution architecture risk.

Runway items should also be connected to the backlog. They may appear as architecture enablers, integration enablers, platform enablers, security enablers, verification enablers or product follow-up items. The Solution Architect is responsible for ensuring that the runway is visible and sufficient at solution level. Product Architects are responsible for implementing the product-level architecture work required by the runway. Platform, Security and Data Architects provide cross-cutting support where needed.

The solution architecture runway must remain focused. It should not become a general wish list of future improvements. A valid runway item should explain which future capability, integration milestone, release baseline, quality marker or risk reduction it enables. Where the benefit is unclear, the item should either be refined, linked to a concrete dependency, or moved to technical debt or the improvement backlog.

A solution release baseline should not be considered robust if critical runway items remain unresolved. Missing interface runway may create integration failure. Missing data runway may create semantic inconsistency. Missing security runway may create release blockers. Missing deployment runway may prevent realistic environment validation. Missing resilience runway may leave degraded operation unproven. Therefore, runway status should be visible in solution architecture reviews and release-readiness assessments.

## Solution Risk and Technical Debt Governance

Solution risk and technical debt governance ensures that architecture risks affecting the integrated solution are visible, owned and actively managed. Solution-level debt shall be tracked separately from product-level technical debt because it affects the relationships between products, not only the internal architecture of one product.

Product debt affects one product. Solution debt affects integration, release compatibility, interoperability, security, data consistency, shared runtime behavior, deployment alignment or verification across multiple products. A product may therefore appear technically healthy in isolation while the solution still carries significant architecture debt at the interfaces, data flows, security boundaries, deployment model or release baseline.

Solution debt should be reviewed during solution planning, PI planning, integration planning, release readiness and Inspect & Adapt. If solution debt is not visible early, it will usually appear later as integration delay, release risk, security exception, operational instability or unplanned rework.

| **Debt / risk type**       | **What it affects**                                    | **Examples**                                                                                                  | **Typical evidence or follow-up**                                                            |
|----------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Interface debt             | Cross-product communication and interoperability       | Temporary undocumented interface, missing versioning, incomplete ICD, missing contract test                   | Interface debt item, interface owner, contract-test backlog item, versioning plan            |
| Data debt                  | Cross-product data consistency and semantic alignment  | Incomplete semantic mapping, missing metadata, inconsistent schema, unclear data ownership                    | Data debt item, semantic mapping action, schema alignment task, data-owner assignment        |
| Security debt              | Solution-level trust, protection, audit and compliance | Missing solution threat model, incomplete logging, temporary crypto exception, inconsistent identity handling | Security risk record, exception, mitigation plan, security review follow-up                  |
| Deployment debt            | Integrated runtime and environment compatibility       | Manual deployment, environment-specific configuration, missing rollback, incomplete observability             | Deployment improvement item, automation task, environment compatibility check, rollback plan |
| Integration debt           | Integration readiness and verification                 | Missing test environment, late integration, unavailable simulator, unverified product compatibility           | Integration risk item, integration environment backlog item, system demo follow-up           |
| Release compatibility debt | Ability to form a coherent solution release baseline   | Missing product compatibility declaration, outdated product version matrix, unresolved baseline conflict      | Release-readiness action, product compatibility matrix update, solution baseline correction  |
| Architecture runway debt   | Future integration, release or capability evolution    | Enabler not funded before dependent features are planned, missing shared platform capability                  | Architecture runway item, PI planning dependency, portfolio escalation, funding decision     |
| Ownership or process debt  | Accountability and execution of solution governance    | Missing interface owner, unclear release responsibility, no review point, no escalation path                  | RACI update, owner assignment, governance workflow action, review decision                   |
| Resilience debt            | Degraded operation, recovery and mission continuity    | DIL behavior untested, failover not proven, recovery automation missing                                       | Resilience test action, degraded-mode scenario, recovery evidence, operational risk record   |

<span id="_Toc233730471" class="anchor"></span>Table 87: Product architecture: runtime view

Every solution debt item should identify the affected products, affected solution baseline, architecture impact, risk level, accountable owner, mitigation action, due date and review point. A debt item without ownership or follow-up is not governed debt; it is only a known weakness.

Solution debt should also be connected to the appropriate improvement mechanism. Some items belong in the solution architecture runway because they must be resolved before future integration or release work can proceed. Some items belong in the technical debt register because they represent known structural weakness. Others may require a product backlog action, guardrail clarification, platform improvement, security exception or portfolio-level funding decision.

The Solution Architect is responsible for making solution-level debt visible and for ensuring that it is reviewed at the right planning and governance points. Product Architects are responsible for resolving the product-level actions required to reduce the solution debt. Platform, Security and Data Architects provide cross-cutting support where the debt affects shared runtime, trust, data or technology assumptions.

Repeated or long-lived solution debt should trigger architecture review. If the same debt pattern appears across several solutions, it may indicate that an enterprise guardrail is missing, a platform capability is insufficient, an interface standard is unclear, or the architecture runway is not funded early enough.

# SDD Product Architecture Guidelines

## Purpose

This chapter defines the required structure and evidence for Product Architecture. Product Architecture is where the framework becomes concrete. It describes how a single product is structured, how it behaves, how it is deployed, how it is secured, how it integrates, and how its quality is verified.

A product architecture must be useful for engineering. It should help teams build, test, integrate, release, and maintain the product. It should not be written only for review. It must be accurate enough to support implementation and stable enough to support future evolution.

The product architecture also provides evidence to the solution level. A solution release can only be trusted if participating products provide reliable evidence about their interfaces, data contracts, security mechanisms, deployment assumptions, quality attributes, and release compatibility.

Product Architecture Guidelines define the required structure and evidence for a single software-defined defence product.

The product architecture must be implementable, testable, securable, deployable, releasable, maintainable, and compatible with solution and enterprise architecture constraints.

A product architecture should answer four practical questions:

| **Question**                               | **Purpose**                                       |
|--------------------------------------------|---------------------------------------------------|
| What is the product responsible for?       | Defines scope and prevents unclear boundaries     |
| How is the product structured?             | Enables development, testing, and maintainability |
| How does the product integrate?            | Enables solution compatibility                    |
| What evidence proves the product is ready? | Enables release decisions                         |

<span id="_Toc233730472" class="anchor"></span>Table 88: Product architecture: deployment view

A product architecture shall be updated when significant design decisions change, when interfaces change, when deployment assumptions change, when security assumptions change, or when product technical debt affects solution compatibility.

## BAPO Structure of the Product Architecture

At product level, BAPO is used to keep the product architecture connected to its contribution. The product should not only describe its internal components. It should also explain why the product exists, which solution capability it supports, which enterprise and solution guardrails apply, which processes are required to verify it, and who owns the critical architecture elements.

This is especially important for products that participate in a larger solution such as MDOcore. A product can be released independently only if it remains compatible with the solution baseline.

| **Element**                   | **Required content**                                                                                               |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Product business contribution | Product mission, product-line objective, solution contribution, customer value                                     |
| Product architecture decision | Context, building blocks, interfaces, runtime, deployment, quality attributes, security mechanisms, ADRs           |
| Process requirement           | Backlog refinement, CI/CD, architecture review, testing, security verification, release readiness, debt management |
| Ownership requirement         | Product architect, product owner, development team, test owner, security owner, interface owner                    |
| Evidence                      | Product architecture document, ADRs, tests, release declaration, technical debt register                           |

<span id="_Toc233730473" class="anchor"></span>Table 89: Product architecture: interface and data contract specification

Figure 9 summarizes the required product architecture evidence package. The package acts as the product-level source of truth for architecture design, integration, quality, security, verification, release compatibility, and technical debt.

<img src="/workspace/SDD_Architecture_Governance_Framework_20260630v2_media/media/image10.png" style="width:10.13636in;height:5.5454in" />

<span id="_Ref233704287" class="anchor"></span>Figure 9: Product Architecture Evidence Package, showing the required evidence elements for a single software-defined defence product, including context, building blocks, runtime, deployment, interfaces, ADRs, quality requirements, security concept, verification evidence, release compatibility, and technical debt.

## The Product Business Contribution Statement

The Product Business Contribution Statement should be short but clear. It should not become a marketing description. It should explain the product’s architectural role in business and solution terms.

For example, for MDOcore Qube, the contribution can be stated as:

- MDOcore Qube contributes to MDOcore by providing deterministic,semantic, secure, and resilient communication control between Edge and Fog nodes. Its business contribution is not merely data transport, but enabling mission-reliable information flow under constrained and degraded communication conditions.

## Product Context and Scope

A clear context and scope section prevents integration misunderstandings. It should define what the product owns and what it does not own. It should also identify all external systems and actors that influence product behavior.

Out-of-scope statements are as important as in-scope statements. They prevent false expectations and help Solution Architects understand where additional products, platforms, or services are required.

| **Required element** | **Description**                                                                                |
|----------------------|------------------------------------------------------------------------------------------------|
| System boundary      | Defines what is inside and outside the product                                                 |
| External actors      | Users, operators, systems, suppliers, platforms                                                |
| External systems     | Sensors, mission systems, C2 systems, runtime platforms, security infrastructure               |
| Interfaces           | APIs, topics, protocols, messages, files, events                                               |
| Constraints          | Resource, safety, security, deployment, operational, regulatory, and environmental constraints |
| Assumptions          | Assumed infrastructure, data sources, runtime environment, communication conditions            |

<span id="_Toc233730474" class="anchor"></span>Table 90: Product architecture: architecture decision record fields

## Building Block View

The Building Block View describes the static structure of the product architecture. It shall show more than components, modules or services. It must also explain what each building block is responsible for, which interfaces it provides or consumes, which dependencies it has, which quality attributes it supports, and who owns it.

A component diagram without responsibility descriptions is not sufficient. The purpose of the Building Block View is to make the product architecture understandable, reviewable and maintainable. Each building block should have a clear purpose, clear boundaries, clear interfaces, clear ownership and a clear relationship to the product’s quality requirements.

The Building Block View should also show where architecture-relevant quality attributes are implemented. For example, if a product claims resilience, the architecture should show which building blocks implement retry, buffering, failover, monitoring, recovery or degraded-mode behavior. If a product claims security, the architecture should show where authentication, authorization, crypto, logging or audit responsibilities are implemented.

| **Required element**         | **Purpose**                                                                     | **Required content / evidence**                                                                                  |
|------------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Component model              | Shows the main structural elements of the product.                              | Components, modules, services, libraries, adapters, external-facing building blocks                              |
| Responsibility mapping       | Explains what each building block is accountable for.                           | Purpose, responsibilities, boundaries, owned functions, excluded responsibilities                                |
| Dependency model             | Shows how building blocks depend on each other and on external systems.         | Internal dependencies, external dependencies, platform dependencies, library dependencies, service dependencies  |
| Interface ownership          | Clarifies which building block owns, exposes or consumes which interface.       | Provided interfaces, consumed interfaces, API ownership, topic ownership, schema ownership, protocol assumptions |
| Quality attribute allocation | Shows where important quality requirements are implemented in the architecture. | Resilience mechanisms, performance-critical components, security controls, observability points, recovery logic  |
| Modularity assessment        | Assesses whether the structure supports maintainability and change.             | Coupling, cohesion, replaceability, testability, separation of concerns, dependency direction                    |
| Reuse assessment             | Shows where existing assets or reusable patterns are used.                      | Reused platform, service, framework, pattern, library, component or reference architecture                       |
| Ownership and lifecycle      | Clarifies who maintains each relevant building block and how it evolves.        | Component owner, team ownership, lifecycle status, replacement plan, technical debt link                         |

<span id="_Toc233730475" class="anchor"></span>Table 91: Product architecture quality requirements

The Building Block View should focus on architecture-relevant building blocks, not on every implementation detail. The level of detail is sufficient when a reviewer can understand how the product is structured, where responsibilities are located, how dependencies are managed, and where important quality attributes are realized.

The Building Block View should be consistent with the Runtime View, Deployment View, Interface Specification, ADR Register and Quality Requirement Catalogue. If a building block exposes an interface, this interface should also appear in the interface specification. If a building block implements an important runtime behavior, this should be reflected in the runtime view. If a building block exists because of a major architecture decision, the rationale should be traceable to an ADR.

Where responsibilities, ownership, dependencies or quality allocations are unclear, the gap should be captured as product architecture debt. A product architecture should not be considered complete if the building blocks are visible as boxes but their responsibilities, interfaces, dependencies and ownership remain ambiguous.

## Runtime View

The runtime view describes how the product behaves during execution. While the building block view shows the static structure of the product, the runtime view shows how the product actually operates in relevant scenarios. It explains how components interact, how messages and events flow, how state changes over time, how errors are handled, and how the product behaves under normal, degraded and failure conditions.

The runtime view is required because many architecture risks only become visible during execution. A product may have a reasonable component structure but still fail to meet latency, determinism, resilience, security, observability or recovery expectations. The runtime view therefore connects product architecture to measurable behavior and verification evidence.

| **Required element**   | **Purpose**                                                                        | **Required content / evidence**                                                                                       |
|------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Runtime scenarios      | Define the most important execution situations the product must support.           | Main operational scenarios, failure scenarios, degraded scenarios, DIL scenarios, startup and shutdown scenarios      |
| Sequence behavior      | Show how components, services, interfaces and external systems interact over time. | Message flow, event flow, control flow, command flow, error handling, timeout behavior                                |
| State behavior         | Explain relevant product, session, connection or mission states.                   | State machines, session state, lifecycle state, degraded state, recovery state, invalid or exceptional states         |
| Performance behavior   | Show whether runtime behavior can meet timing and resource expectations.           | Latency, throughput, scheduling, resource use, timing constraints, performance budgets and measurements               |
| Security behavior      | Show how security controls operate during runtime interactions.                    | Authentication, authorization, crypto usage, logging, audit behavior, access checks, security-relevant event handling |
| Recovery behavior      | Define how the product reacts to failure and returns to a controlled state.        | Restart, failover, retry, store-and-forward, rollback, recovery sequence, data consistency after recovery             |
| Observability behavior | Show how runtime behavior can be monitored, diagnosed and reviewed.                | Logs, metrics, traces, health indicators, alerts, diagnostic events and monitoring dashboards                         |

<span id="_Toc233730476" class="anchor"></span>Table 92: Product security concept

The runtime view should be based on the scenarios that matter most for the product’s business contribution, solution participation and quality requirements. It should not attempt to describe every possible execution path. Instead, it should focus on the runtime behavior that is architecture-relevant, risk-relevant or required for integration, verification and release readiness.

Each runtime scenario should identify the involved building blocks, external systems, interfaces, data exchanges, state changes, timing assumptions, error conditions and expected evidence. Where the product participates in a solution, the runtime view must also show the externally visible behavior needed by Solution Architecture to assess integration readiness and release compatibility.

The runtime view should be maintained together with the building block view, deployment view, interface specifications, quality requirements, security concept and verification evidence. If runtime behavior changes, the affected ADRs, tests, interface contracts, deployment assumptions and release compatibility declarations should be reviewed as well.

## Deployment View

The Deployment View describes where and how the product runs in its intended operational environments. While the Runtime View explains the product’s execution behavior, the Deployment View explains the physical, virtual and platform context in which that behavior is executed. It shows deployment nodes, infrastructure assumptions, runtime dependencies, resource constraints, configuration mechanisms, observability, update behavior and rollback options.

The Deployment View is required because deployment assumptions directly affect product quality, release readiness and solution compatibility. A product may work correctly in a development environment but still fail in a realistic edge, fog, cloud or customer environment if resource limits, network assumptions, container runtime, configuration, storage, security controls or update mechanisms are not understood and verified.

| **Required element**      | **Purpose**                                                                | **Required content / evidence**                                                                                                 |
|---------------------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Deployment nodes          | Shows where product elements are deployed and executed.                    | Edge nodes, fog nodes, cloud services, platform services, containers, devices, servers, gateways, external runtime dependencies |
| Runtime assumptions       | Defines the technical environment required to execute the product.         | Operating system, container runtime, orchestration, network assumptions, storage assumptions, middleware, platform services     |
| Resource budgets          | Makes operational constraints explicit and measurable.                     | CPU, memory, bandwidth, storage, energy, thermal constraints, timing constraints, scaling assumptions                           |
| Configuration model       | Explains how the product is configured for different environments.         | Configuration files, environment variables, secrets handling, feature flags, parameter sets, environment-specific settings      |
| Deployment automation     | Shows how deployment is made repeatable and controlled.                    | Scripts, manifests, infrastructure-as-code, pipeline records, deployment templates, configuration automation                    |
| Observability             | Shows how the deployed product can be monitored and diagnosed.             | Logs, metrics, traces, health checks, alerts, dashboards, operational diagnostics                                               |
| Update and rollback       | Defines how the product is updated and restored safely.                    | Update mechanism, compatibility checks, rollback strategy, versioning rules, migration steps, recovery procedure                |
| Environment compatibility | Demonstrates that the product can run in the intended target environments. | Environment compatibility matrix, deployment test evidence, platform compatibility evidence, edge/fog/cloud validation          |

<span id="_Toc233730477" class="anchor"></span>Table 93: Product verification evidence

The Deployment View should focus on deployment aspects that are architecture-relevant, release-relevant or risk-relevant. It does not need to describe every operational detail, but it must provide enough information to understand whether the product can be deployed, configured, observed, updated and recovered in the environments for which it is intended.

The Deployment View should be consistent with the Runtime View, Interface Specification, Product Security Concept, Quality Requirement Catalogue and Product Release Compatibility Declaration. If the product depends on a specific runtime, network condition, platform service, container configuration, storage model or security control, this dependency should be visible in the Deployment View and verified through suitable evidence.

Where a product participates in a solution, the Deployment View must also support Solution Architecture. It should show whether the product’s deployment assumptions are compatible with the solution deployment topology, runtime environment, observability model, security boundaries and release baseline. If deployment assumptions differ between product and solution level, the gap should be captured as product technical debt, solution deployment risk or architecture runway.

A product should not be considered deployment-ready if deployment is manual, undocumented, environment-specific, untested or not reproducible. Missing deployment automation, unclear configuration, insufficient observability, missing rollback strategy or unverified environment compatibility should be treated as release-readiness risks.

## Interface and Data Contract Specification

Interface and data contract specifications define how the product communicates with other products, platforms, users and external systems. They are one of the most important connections between Product Architecture and Solution Architecture, because cross-product integration depends on interfaces and data contracts that are explicit, versioned, owned, tested and compatible with the relevant solution baseline.

A product should not release an interface or data contract change without understanding the solution-level impact. Even a technically correct product change can create solution-level risk if it changes APIs, topics, schemas, events, protocols, field semantics, timing behavior, security assumptions or compatibility rules used by other products.

Each interface and data contract shall therefore be treated as a managed architecture artifact. It must have a clear purpose, owner, version, compatibility rule, schema, semantics, security assumptions, error-handling behavior and verification evidence.

| **Required element** | **Purpose**                                                                        | **Required content / evidence**                                                                                    |
|----------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Interface name       | Provides a unique and understandable reference for the interface or data contract. | Unique name, purpose, consuming systems, providing system, related capability or solution baseline                 |
| Owner                | Clarifies who is accountable for maintaining the interface or data contract.       | Product, team, role, interface owner, data owner, escalation contact                                               |
| Type                 | Defines the technical communication or exchange pattern.                           | API, topic, event, file, stream, message, protocol, command, query, notification                                   |
| Version              | Makes compatibility and change control explicit.                                   | Current version, previous version, versioning rule, compatibility rule, deprecation rule, migration expectation    |
| Schema               | Defines the structural format of exchanged information.                            | Request schema, response schema, payload schema, message schema, event schema, topic schema, validation rule       |
| Semantics            | Defines the meaning of exchanged information.                                      | Field meaning, event meaning, status definitions, command semantics, units, timing assumptions, state implications |
| Security             | Defines how the interface or data exchange is protected.                           | Authentication, authorization, crypto, classification, trust zone, audit requirement, logging requirement          |
| Error handling       | Defines how failures and exceptional conditions are handled.                       | Error codes, retries, timeouts, fallback behavior, idempotency, compensation behavior, degraded-mode behavior      |
| Tests                | Demonstrates that the interface or data contract is implemented and compatible.    | Contract tests, schema validation, integration tests, compatibility tests, negative tests, regression evidence     |
| Change control       | Defines how changes are reviewed, communicated and released.                       | Change record, impact assessment, consumer notification, release note, solution compatibility assessment           |

<span id="_Toc233730478" class="anchor"></span>Table 94: Product release compatibility declaration

The specification should be detailed enough for another product team to implement, consume, test and verify the interface without relying on informal knowledge. It should describe not only the technical structure of the interface, but also its meaning, ownership, compatibility expectations, security assumptions and operational behavior.

Interface and data contract changes must be assessed against the relevant solution baseline. A change may be acceptable at product level but still create solution-level incompatibility if consumers are not ready, schemas are no longer compatible, semantic meaning changes, security assumptions differ, or required contract tests are missing. Such changes should be reviewed with the Solution Architect before release.

Where interfaces or data contracts are incomplete, unowned, unversioned, untested or semantically unclear, the gap should be captured as product architecture debt or solution integration risk. A product should not be considered release-ready if externally visible interfaces or data contracts required by the solution baseline are not specified, versioned, owned and verified.

## Architecture Decision Records

Architecture Decision Records preserve the reasoning behind important product architecture decisions. They explain not only what was built, but why it was built that way, which alternatives were considered, which trade-offs were accepted, and which consequences must be managed over time.

ADRs are required because future teams, reviewers and solution architects need to understand the rationale behind major product decisions. Without ADRs, architecture knowledge becomes implicit, person-dependent and difficult to review. This creates risk when products evolve, teams change, interfaces are reused, solution baselines change, or technical debt needs to be assessed.

In this framework, ADRs are not only technical notes. They are product architecture governance records. Each relevant ADR should connect the business driver, architecture decision, process implication, ownership implication, affected quality markers and verification evidence. This makes the decision traceable from intent to implementation, review and release readiness.

| **ADR field**            | **Purpose**                                                                               | **Required content**                                                                                                  |
|--------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Title                    | Provides a short and recognizable decision reference.                                     | Short decision title                                                                                                  |
| Status                   | Shows whether the decision is still valid.                                                | Proposed, accepted, deprecated, superseded, rejected                                                                  |
| Affected scope           | Clarifies where the decision applies.                                                     | Product, component, interface, data contract, runtime behavior, deployment model, security concept, solution baseline |
| Business driver          | Explains why the decision is needed from a business, mission or capability perspective.   | Capability, mission, customer, solution, product-line or strategic reason                                             |
| Context                  | Describes the situation in which the decision was made.                                   | Technical context, architecture constraints, dependencies, assumptions, relevant guardrails or solution baseline      |
| Decision                 | States the chosen architecture decision clearly.                                          | Selected architecture option, pattern, technology, structure, interface approach or design rule                       |
| Alternatives             | Shows which options were considered and why they were not selected.                       | Options considered, rejected alternatives, trade-off analysis, selection rationale                                    |
| Consequences             | Makes benefits, trade-offs and risks visible.                                             | Benefits, limitations, risks, constraints, future impact, technical debt implications                                 |
| Process implication      | Defines what must happen in delivery, verification or governance because of the decision. | Required tests, reviews, release rules, pipeline changes, governance steps, documentation updates                     |
| Ownership implication    | Clarifies who is accountable for maintaining the decision and its consequences.           | Owner, affected teams, interface owner, data owner, security owner, platform owner                                    |
| Quality markers affected | Links the decision to architecture quality assessment.                                    | Relevant enterprise, solution or product quality markers, BAPO markers, expected marker impact                        |
| Verification evidence    | Shows how the decision will be proven or reviewed.                                        | Tests, measurements, reviews, demos, integration evidence, security evidence, runtime evidence                        |
| Review date              | Defines when the decision should be reassessed.                                           | Review date, trigger condition, expiry condition, supersession link if applicable                                     |

<span id="_Toc233730479" class="anchor"></span>Table 95: Product risk and technical debt register

ADRs should be created for decisions that materially affect product structure, interfaces, data contracts, runtime behavior, deployment assumptions, security controls, quality attributes, technology choices, solution compatibility or alignment with enterprise guardrails. They are especially important where the decision creates a dependency for other products or influences a solution release baseline.

Not every implementation detail requires an ADR. The ADR discipline should focus on decisions that would be difficult, risky or costly to reverse, or decisions that future teams would not be able to understand from the implementation alone. The test is simple: if a future reviewer would ask “why was this done this way?”, an ADR is likely required.

ADRs should remain linked to the Product Architecture Document, Interface Specification, Data Contract Specification, Quality Requirement Catalogue, Product Security Concept, Verification Evidence and Product Release Compatibility Declaration. If an ADR affects a solution-level interface, data flow, deployment model or security boundary, it should also be visible to the Solution Architect.

An ADR should not be treated as final forever. Decisions may be superseded when technology changes, enterprise guardrails evolve, solution baselines change, operational evidence reveals weaknesses, or technical debt becomes unacceptable. Deprecated or superseded ADRs should remain available so that the architecture history remains traceable.

## Product Quality Requirements

Product quality requirements define the measurable non-functional expectations that the product architecture must satisfy. They translate architecture claims such as performance, resilience, security, interoperability or deployability into concrete requirements that can be designed, implemented, verified and reviewed.

Quality requirements must not remain generic statements. A product should not only claim to be “secure”, “performant” or “resilient”. The architecture must define what this means for the product, where the requirement is implemented, which evidence proves it, and who owns the requirement. Product quality requirements therefore connect architecture design to verification evidence, release readiness and technical debt management.

The following quality attributes define the minimum product-level quality requirement set:

| **Quality attribute** | **Purpose**                                                                                               | **Required content / evidence**                                                                                          |
|-----------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Determinism           | Ensures predictable timing and behavior where required by mission or system constraints.                  | Scheduling rules, prioritization, timing assumptions, deterministic execution constraints, timing analysis, test results |
| Performance           | Ensures that the product meets required latency, throughput and resource expectations.                    | Latency budgets, throughput targets, resource budgets, load tests, performance measurements                              |
| Availability          | Ensures that the product can remain available or recover within defined limits.                           | Availability assumptions, restart behavior, failover concept, recovery evidence, availability measurements               |
| Resilience            | Ensures that the product can handle degraded, disconnected, intermittent or limited operating conditions. | Degraded-mode scenarios, DIL behavior, retry logic, buffering, store-and-forward tests, recovery tests                   |
| Security              | Ensures that product-level protection mechanisms are defined and verified.                                | Threat model, crypto assumptions, identity and access model, logging, audit behavior, vulnerability evidence             |
| Maintainability       | Ensures that the product can be changed, extended and maintained safely over time.                        | Modularity assessment, ADRs, code quality evidence, dependency management, technical debt records                        |
| Interoperability      | Ensures that the product can exchange information and interact correctly with other products or systems.  | Interface contracts, schema validation, semantic mapping, integration tests, compatibility evidence                      |
| Scalability           | Ensures that the product can handle expected growth in users, data, messages, load or deployment scale.   | Capacity assumptions, scaling model, deployment scaling evidence, performance tests, resource measurements               |
| Observability         | Ensures that product behavior can be monitored, diagnosed and reviewed during operation.                  | Logs, metrics, traces, health checks, alerts, dashboards, operational diagnostics                                        |
| Deployability         | Ensures that the product can be deployed consistently and safely in the intended environments.            | Automated deployment, configuration evidence, deployment manifests, environment validation, rollback evidence            |
| Compatibility         | Ensures that the product remains compatible with applicable solution baselines and enterprise guardrails. | Product Release Compatibility Declaration, solution baseline mapping, interface version evidence, release review record  |

<span id="_Toc233730480" class="anchor"></span>Table 96: Possible outcomes BAPO architecture review

Each quality requirement should be measurable or otherwise reviewable. Where a numeric threshold is meaningful, it should be stated explicitly, for example latency, throughput, recovery time, resource usage or availability target. Where a numeric threshold is not sufficient, the requirement should define observable behavior, acceptance criteria, test approach or review evidence.

Product quality requirements should be linked to the relevant architecture views. Performance and determinism should be reflected in the Runtime View. Deployability should be reflected in the Deployment View. Interoperability should be reflected in the Interface and Data Contract Specification. Security requirements should be reflected in the Product Security Concept. Maintainability and major trade-offs should be traceable to ADRs.

Quality requirements should also be linked to verification evidence. A product should not be considered release-ready if important quality attributes are only described but not verified. Missing or weak evidence should be captured as product technical debt, architecture runway, verification backlog or release-readiness risk.

The Product Architect is responsible for ensuring that quality requirements are architecturally defined and traceable. Product teams are responsible for implementation and evidence. Security, Platform, Data and Solution Architects should be involved where the quality requirement affects cross-cutting concerns, deployment environments, data contracts or solution-level compatibility.

## Product Security Concept

The Product Security Concept defines how the product protects data, functions, interfaces, runtime behavior and operational evidence against relevant threats. It translates security expectations into concrete product-level architecture decisions, controls, ownership and verification evidence.

The security concept is required because security cannot be treated as an implementation detail added after the architecture has been defined. Security decisions affect interfaces, data contracts, runtime behavior, deployment assumptions, logging, auditability, update mechanisms, vulnerability handling and release readiness. Where the product participates in a solution, the Product Security Concept must also align with the applicable solution trust-boundary model and enterprise security guardrails.

The following elements define the minimum content of the Product Security Concept:

| **Required element**   | **Purpose**                                                                                       | **Required content / evidence**                                                                                |
|------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Threat model           | Identifies relevant threats, attack surfaces and trust boundaries.                                | Threats, attack surfaces, misuse cases, trust boundaries, assets, assumptions, risk ratings                    |
| Identity               | Defines how users, systems, services and components are authenticated.                            | Authentication model, certificates, tokens, keys, credential model, identity provider assumptions              |
| Authorization          | Defines how access to functions, data and interfaces is controlled.                               | Access rights, roles, policies, permission model, privilege boundaries, enforcement points                     |
| Cryptography           | Defines how confidentiality, integrity and authenticity are protected.                            | Encryption, integrity protection, signing, key management, crypto lifecycle, approved algorithms               |
| Logging and audit      | Defines which security-relevant events are recorded and how auditability is preserved.            | Security events, audit trail, tamper resistance, log retention, audit responsibilities, monitoring linkage     |
| Vulnerability handling | Defines how vulnerabilities are detected, triaged, remediated and tracked.                        | Scanning, triage process, remediation workflow, disclosure handling, vulnerability register, owner assignment  |
| Secure update          | Defines how product updates are protected and recoverable.                                        | Update package, signing, verification, compatibility check, rollback strategy, update audit evidence           |
| Security tests         | Demonstrates that security controls have been verified.                                           | Static analysis, dynamic analysis, penetration test, crypto review, vulnerability scan, security test evidence |
| Security ownership     | Clarifies who owns security decisions, evidence and remediation actions.                          | Product Security Owner, Product Architect, Security Architect, responsible team, escalation path               |
| Solution alignment     | Shows how product security aligns with solution-level trust boundaries and enterprise guardrails. | Solution trust-zone mapping, security baseline mapping, exception record, compatibility declaration            |

<span id="_Toc233730481" class="anchor"></span>Table 97: BAPO architecture review principles

The Product Security Concept should be specific to the product and its operational context. Generic security statements are not sufficient. The concept should explain which threats are relevant, which controls are implemented, where those controls are located in the architecture, how they are verified, and who is responsible for maintaining them.

Security evidence should be connected to the relevant architecture views. Trust boundaries and secure communication paths should be reflected in the Runtime View and Interface Specification. Deployment-related security assumptions should be reflected in the Deployment View. Major security trade-offs should be documented through ADRs. Security verification results should be linked to the Verification Evidence and release readiness assessment.

Where the product participates in a solution, product-level security must be compatible with the solution security architecture. A product may implement strong security controls in isolation but still create solution-level risk if identity handling, authorization logic, crypto assumptions, logging, audit behavior or vulnerability handling differ from the solution trust-boundary model.

Missing or incomplete security evidence should be treated as product technical debt, security risk or release-readiness blocker, depending on severity. A product should not be considered release-ready if required security controls are only described but not implemented, verified, owned or aligned with the applicable solution and enterprise security expectations.

## Product Verification Evidence

Product Verification Evidence defines how product architecture claims are proven. Verification evidence should be planned together with architecture decisions, not collected only at the end of delivery. A product should not wait until release readiness to discover that an architecture claim cannot be demonstrated, measured or reviewed.

For every critical architecture decision and quality attribute, Product Architecture should define which evidence is required, how the evidence will be produced, who owns it and where it will be reviewed. This is especially important for claims related to determinism, performance, security, resilience, deployment reproducibility, interface compatibility and release readiness.

Verification evidence connects the Product Architecture Document, ADRs, quality requirements, interface specifications, security concept, deployment view and release compatibility declaration. It turns architecture from a description into a reviewable and evidence-based product baseline.

| **Evidence area**              | **Verification intent**                                                                                                                                  | **Required evidence**                                                                                                                           |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Architecture conformance       | Verify that the implemented product architecture conforms to the documented architecture decisions and required quality markers.                         | Architecture review record, conformance checklist, quality-marker score, ADR review, architecture deviation record                              |
| Interface and data conformance | Verify that product interfaces and data contracts are implemented, versioned and compatible with consumers and solution baselines.                       | Contract tests, schema validation, interoperability tests, API/topic/schema test results, interface compatibility evidence                      |
| Quality attributes             | Verify that critical product quality requirements are satisfied through suitable tests or measurements.                                                  | Performance tests, resilience tests, security tests, reliability tests, scalability tests, determinism evidence                                 |
| Runtime behavior               | Verify that the product behaves correctly in relevant operational, failure and degraded scenarios.                                                       | Scenario tests, sequence tests, failure tests, degraded-mode tests, DIL behavior evidence, recovery evidence                                    |
| Deployment                     | Verify that the product can be deployed, configured, observed, updated and rolled back in the intended environments.                                     | Automated deployment result, deployment manifest, environment validation, observability evidence, update and rollback evidence                  |
| Security                       | Verify that product-level security controls are implemented, effective and aligned with security expectations.                                           | Threat model review, vulnerability scan result, penetration test, crypto evidence, security test evidence, audit/logging evidence               |
| Release compatibility          | Verify that the product release is compatible with the applicable solution baseline and enterprise guardrails.                                           | Product Release Compatibility Declaration, solution baseline mapping, enterprise guardrail mapping, compatibility matrix, release review record |
| Technical debt                 | Verify that known architecture gaps, residual risks and mitigation actions are visible and owned.                                                        | Risk and technical debt register, mitigation plan, owner assignment, due date, residual risk acceptance, improvement backlog item               |
| Traceability                   | Verify that evidence can be traced back to the architecture decision, quality requirement, interface, security control or release criterion it supports. | Evidence traceability matrix, linked ADR, linked requirement, test reference, review record, backlog link                                       |

<span id="_Toc233730482" class="anchor"></span>Table 98: Enterprise architecture review questions

Verification evidence should be defined early enough to influence backlog planning, test strategy, architecture runway and release-readiness preparation. If evidence depends on missing test environments, unavailable simulators, undefined interfaces, incomplete deployment automation or unclear security assumptions, the gap should be treated as product architecture runway, technical debt or release-readiness risk.

The Product Architect is responsible for defining which architecture claims require evidence. Product teams are responsible for producing the implementation and test evidence. Security, Platform, Data and Solution Architects should be involved where the evidence affects security controls, deployment environments, data contracts, cross-product interfaces or solution baseline compatibility.

The strength of evidence should match the criticality of the architecture claim. A descriptive review may be sufficient for a low-risk design detail. Critical claims, however, require stronger evidence such as automated tests, contract tests, performance measurements, security scans, integration results, deployment records or runtime metrics.

A product should not be considered release-ready if critical architecture claims are unsupported, outdated, unowned or not traceable to verification evidence. Missing evidence should be recorded explicitly and handled through technical debt, release risk, architecture exception or follow-up action.

## Product Release Compatibility Declaration

The Product Release Compatibility Declaration states whether a specific product release is compatible with one or more defined solution release baselines. It is required because a product can be internally complete, tested and releasable on its own, while still being incompatible with a particular solution because of interface versions, data contracts, security assumptions, deployment configuration or missing integration evidence.

The declaration is therefore not a general product release note. It is product-level architecture evidence for solution-level release readiness. It shows which product version is being declared, which solution baseline it supports, which interface and data versions are implemented, which security and deployment assumptions apply, which limitations are known, and which evidence proves compatibility.

The following fields define the minimum content of the Product Release Compatibility Declaration:

| **Field**                   | **Purpose**                                                                      | **Required content**                                                                                                               |
|-----------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Product version             | Identifies the exact product release being assessed.                             | Product release version, build identifier, release date, relevant configuration or variant                                         |
| Supported solution baseline | Defines which solution release baseline the product release is compatible with.  | Compatible solution baseline or baselines, baseline version, solution name, release context                                        |
| Interface versions          | Shows which externally visible interface versions are implemented.               | Implemented API versions, topic versions, schema versions, event versions, protocol versions, ICD references                       |
| Data model versions         | Shows which data and semantic models are supported.                              | Implemented data model versions, semantic model versions, metadata rules, classification rules, schema references                  |
| Security baseline           | Confirms compatibility with solution-level and enterprise security expectations. | Identity assumptions, crypto configuration, logging and audit behavior, trust-zone compatibility, security exceptions              |
| Deployment configurations   | Defines the environments and runtime assumptions supported by the release.       | Supported environments, runtime assumptions, container/runtime versions, configuration profiles, platform dependencies             |
| Known limitations           | Makes remaining constraints and deviations explicit.                             | Deviations, constraints, degraded modes, unsupported scenarios, accepted risks, open technical debt                                |
| Migration notes             | Explains what is required to move from earlier versions or configurations.       | Required migration steps, rollback steps, transition constraints, data migration, compatibility notes                              |
| Verification evidence       | Provides proof that compatibility has been assessed.                             | Contract test results, schema validation, integration test evidence, deployment evidence, security evidence, release review record |
| Owner approval              | Confirms accountable ownership for the declaration.                              | Product Owner approval, Product Architect approval, Product Security Owner approval if required, review date                       |

<span id="_Toc233730483" class="anchor"></span>Table 99: Solution architecture review questions

The declaration should be created or updated whenever a product release is intended to participate in a solution release baseline. It should also be updated when interfaces, data contracts, deployment assumptions, security controls, runtime dependencies or compatibility rules change. A stale compatibility declaration should not be used as release evidence.

The Product Architect is responsible for ensuring that the declaration is architecturally correct and supported by evidence. The Product Owner confirms release intent and business readiness. The Solution Architect uses the declaration to assess whether all participating product releases together form a coherent solution release baseline.

Compatibility must always be declared against a specific baseline. A product release should not simply claim to be “compatible” in general. It must state which solution baseline, interface versions, data model versions, security assumptions and deployment configurations it supports.

Where compatibility cannot be fully declared, the limitation must be made explicit. Depending on severity, the gap should be handled as product technical debt, solution integration risk, architecture exception, release-readiness blocker or planned follow-up action. A solution release baseline should not be considered release-ready unless all participating products have current, owned and evidenced compatibility declarations.

## Product Risk and Technical Debt Register

The Product Risk and Technical Debt Register makes product-level architecture gaps, limitations, risks and accepted compromises visible and governable. It is required because architecture debt is often created intentionally during delivery, but becomes dangerous when it is not documented, owned, reviewed or connected to mitigation actions.

Product technical debt may affect product-internal design, interfaces, data contracts, deployment, security, verification evidence, quality attributes, maintainability or compatibility with a solution baseline. Some product-level debt may also create solution-level or enterprise-level impact. The register must therefore show not only what the debt is, but also why it exists, what it affects, who owns it, how it will be mitigated and whether any residual risk remains.

The Product Risk and Technical Debt Register should be reviewed during product architecture reviews, backlog refinement, PI planning, release readiness and Inspect & Adapt. Open debt items that affect release compatibility, security, integration or mission-critical quality attributes must be explicitly assessed before release.

| **Field**              | **Purpose**                                                             | **Required content**                                                                                                      |
|------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Debt item              | Provides a short, recognizable name for the risk or debt item.          | Short name or identifier                                                                                                  |
| Description            | Explains the architecture risk, gap, limitation or accepted compromise. | Architecture risk, missing evidence, design gap, implementation limitation, unresolved dependency                         |
| Level                  | Shows whether the debt is product-internal or has wider impact.         | Product, solution, enterprise, or cross-level impact                                                                      |
| Affected scope         | Clarifies what part of the architecture is affected.                    | Component, interface, data contract, runtime behavior, deployment, security control, quality attribute, solution baseline |
| Cause                  | Explains why the debt exists.                                           | Delivery constraint, legacy dependency, missing runway, technology limitation, customer constraint, temporary workaround  |
| Impact                 | Describes the consequence if the debt is not resolved.                  | Business, architecture, quality, security, release, integration, operational or maintenance impact                        |
| Severity / priority    | Indicates how urgently the item must be addressed.                      | Risk rating, priority, release relevance, affected milestone, escalation need                                             |
| Mitigation             | Defines the planned action to reduce or remove the debt.                | Planned remediation, backlog item, architecture runway, test action, refactoring, guardrail clarification, exception      |
| Owner                  | Assigns accountability for resolution and follow-up.                    | Responsible person, product team, Product Architect, Product Owner, Security Owner, Interface Owner                       |
| Due date               | Defines when the mitigation should be completed or reviewed.            | Planned resolution date, review date, release milestone, expiry date                                                      |
| Residual risk          | Describes the risk that remains after mitigation or accepted deviation. | Remaining risk, accepted limitation, open dependency, release condition                                                   |
| Status                 | Shows the current lifecycle state of the item.                          | Open, accepted, mitigated, closed, escalated, deferred                                                                    |
| Evidence / review link | Connects the item to reviewable evidence and governance records.        | ADR, review record, test result, exception record, release-readiness decision, backlog link                               |

<span id="_Toc233730484" class="anchor"></span>Table 100: Product architecture review questions

A debt item without a named owner, mitigation action and review date should not be considered governed. It is only a known weakness. The register should therefore be used as an active management tool, not as a passive list of problems.

Product-level debt should be distinguished from solution-level debt. Product debt affects the internal architecture, evidence or release readiness of one product. Solution debt affects the integration, interoperability, release compatibility, shared runtime behavior, security boundary or data consistency across multiple products. If a product debt item creates solution-level impact, it should be visible to the Solution Architect and linked to the relevant solution risk or release-readiness record.

Not every debt item blocks release. Some debt may be accepted temporarily if the impact is understood, the residual risk is documented, and the mitigation is planned. However, debt that affects critical security controls, release compatibility, integration evidence, safety-relevant behavior, mission-critical resilience or mandatory enterprise guardrails shall require explicit review and approval before release.

Repeated or long-lived product debt should trigger architecture review. If the same debt pattern appears repeatedly, it may indicate missing architecture runway, insufficient platform support, unclear enterprise guardrails, weak interface governance, or structural underinvestment. In such cases, the debt should be escalated beyond the product backlog and considered in solution or enterprise architecture governance.

# BAPO Architecture Review and Feedback Process

## Purpose

This chapter defines how architecture is reviewed and improved. The review process is not intended to create bureaucracy. Its purpose is to make sure that architecture decisions are traceable, aligned, owned, and verified.

Architecture reviews should be understood as quality and feedback mechanisms. They help identify missing evidence, unclear ownership, integration risks, security gaps, release incompatibilities, and technical debt before these issues become expensive.

The review process applies to all three architecture levels. Enterprise reviews focus on guardrails and strategic alignment. Solution reviews focus on cross-product coherence and release baselines. Product reviews focus on implementable architecture and verification evidence.

Architecture reviews are evidence-based decision and feedback points. They are not intended to create bureaucracy or slideware.

- The review process shall verify:

- Business relevance

- Architecture quality

- Cross-level alignment

- Process readiness

- Ownership clarity

- Evidence completeness

- Feedback into improvement backlog

Each review should be practical and decision-oriented. A review that does not produce a decision, finding, action, or accepted risk is not useful.

The outcome of a review should be one of the following:

| **Review outcome**     | **Meaning**                                                          |
|------------------------|----------------------------------------------------------------------|
| Accepted               | Evidence is sufficient and no blocking issue remains                 |
| Accepted with actions  | Architecture is acceptable but improvement actions are required      |
| Conditionally accepted | A risk or gap must be resolved before a defined milestone            |
| Rejected               | Architecture is not acceptable in its current form                   |
| Deferred               | Decision cannot be made because evidence is missing                  |
| Escalated              | Decision requires higher-level architecture or portfolio involvement |

<span id="_Toc233730485" class="anchor"></span>Table 101: Release readiness review checklist

## Review Principles

Evidence over presentation is the most important review principle. A polished diagram is not enough. The review must check whether architecture claims are supported by real artifacts.

For example, a claim of interoperability should be supported by interface contracts and integration tests. A claim of security should be supported by threat models and verification evidence. A claim of release compatibility should be supported by a product compatibility matrix and release baseline.

| **Principle**              | **Description**                                                                              |
|----------------------------|----------------------------------------------------------------------------------------------|
| Evidence over presentation | Claims must be proven through documents, tests, demos, measurements, or operational evidence |
| Lightweight but mandatory  | Reviews should be efficient, but critical architecture markers cannot be skipped             |
| Cross-level alignment      | Enterprise, Solution, and Product implications must be visible                               |
| Early review               | Critical architecture issues should be reviewed before implementation becomes expensive      |
| Continuous feedback        | System demos, Inspect & Adapt, and operational findings must update architecture             |
| Exception transparency     | Deviations are allowed only when documented, owned, time-bounded, and risk-assessed          |

<span id="_Toc233730486" class="anchor"></span>Table 102: Architecture exception review content

Figure 10 shows the architecture review and feedback loop. Architecture governance is not a one-time gate. Architecture decisions are reviewed, implemented through backlog items and enablers, demonstrated through product, system, or solution demos, verified through evidence, and improved through Inspect & Adapt, technical debt, architecture runway, guardrail updates, and portfolio decisions.

<img src="/workspace/SDD_Architecture_Governance_Framework_20260630v2_media/media/image11.png" style="width:9.77653in;height:5.69589in" />

<span id="_Ref233704522" class="anchor"></span>Figure 10: Architecture review and feedback loop, showing how architecture decisions move through review, implementation, demos, evidence, Inspect & Adapt, technical debt, architecture runway, guardrail updates, and portfolio improvement.

## Enterprise Architecture Review

The Enterprise Architecture Review assesses whether an architecture item has cross-division, cross-solution or long-term strategic impact and therefore requires enterprise-level guidance, guardrails or governance. It is used for strategic themes, portfolio epics, major technology decisions, reference architectures, enterprise standards, repeated solution-level issues, significant exceptions and architecture risks that cannot be resolved within a single product or solution.

The purpose of the review is not to centralize all architecture decisions. Its purpose is to determine which decisions must be consistent across divisions and which decisions can remain local to Solution or Product Architecture. The review must therefore clarify the business driver, enterprise architecture relevance, affected guardrails, required process mechanisms, ownership, evidence and follow-up actions.

| **Review question**                                                      | **Purpose**                                                                                                                           | **Required evidence or output**                                                                                                  |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Is the business driver or strategic theme clear?                         | Ensures that the enterprise architecture item is connected to business, mission, customer, sovereignty or product-line value.         | Strategic theme, epic, portfolio canvas, capability map, value-stream mapping                                                    |
| Does the item have enterprise-level impact?                              | Determines whether the decision affects more than one division, solution, product line, platform, data model or technology direction. | Architecture impact analysis, affected-scope assessment, cross-division dependency map                                           |
| Is an enterprise guardrail required?                                     | Clarifies whether the issue requires a common rule, standard, reference architecture or governance mechanism.                         | Guardrail proposal, architecture impact analysis, exception pattern, risk assessment                                             |
| Does a reference architecture or standard already exist?                 | Prevents duplication and ensures reuse of existing enterprise guidance.                                                               | Reference architecture catalogue, standards catalogue, technology radar, existing guardrail mapping                              |
| Are interface, data, security, runtime and DevSecOps impacts identified? | Ensures that cross-cutting enterprise concerns are visible before local implementation decisions diverge.                             | Enterprise alignment checklist, interface impact assessment, data impact assessment, security review, platform impact assessment |
| Are process implications defined?                                        | Ensures that the guardrail can be applied, reviewed, tested, governed and improved.                                                   | Review process, exception process, KPI tracking, release rule, quality gate, DevSecOps requirement                               |
| Is ownership assigned?                                                   | Ensures that the architecture item can be maintained, communicated and evolved.                                                       | RACI, owner list, named Enterprise Architect, data owner, interface owner, security owner, platform owner                        |
| Is the required evidence defined?                                        | Makes enterprise alignment reviewable instead of assumption-based.                                                                    | Evidence checklist, adoption evidence, review record, KPI dashboard, exception register                                          |
| Are exceptions or deviations documented?                                 | Ensures that local deviations are visible, risk-assessed and time-bounded.                                                            | Exception register, risk assessment, mitigation plan, review date, expiry date                                                   |
| Is feedback from solutions and products considered?                      | Ensures that enterprise guardrails evolve from implementation evidence, integration findings and repeated exception patterns.         | Solution review findings, product feedback, Inspect & Adapt actions, technical debt trends, operational findings                 |
| What follow-up action is required?                                       | Converts the review into executable governance, backlog or improvement action.                                                        | Guardrail update, architecture runway item, portfolio action, exception decision, technical debt item, owner assignment          |

<span id="_Toc233730487" class="anchor"></span>Table 103: Feedback source versus architectural use

The Enterprise Architecture Review should produce a clear decision or follow-up action. Typical outcomes include approval of an enterprise guardrail, creation or update of a reference architecture, a technology governance decision, an exception decision, an enterprise architecture runway item, an enterprise technical debt item, or escalation to portfolio decision-making.

The review should also apply the BAPO alignment markers. The business reason must be explicit, the architecture response must be defined, the required process mechanism must be executable, and ownership must be assigned. If one of these dimensions is unclear, the enterprise architecture item is not yet ready for adoption.

An Enterprise Architecture Review should not block local delivery without reason. If a topic does not create cross-division, cross-solution, security, data, platform, interoperability or strategic risk, it should remain within Solution or Product Architecture. Enterprise Architecture should focus on the decisions where inconsistency would create fragmentation, integration risk, duplicated investment, security gaps or long-term architectural debt.

## Solution Architecture Review

The Solution Architecture Review assesses whether multiple products can work together as one coherent, integrated and releasable solution. It focuses on the architecture concerns that emerge between products, including product participation, capability allocation, cross-product interfaces, data flows, security boundaries, deployment assumptions, integration strategy, release compatibility, risks and solution-level technical debt.

Solution reviews must be held early enough to influence product backlogs, architecture runway and PI planning. If a solution review happens only shortly before release, it is usually too late to resolve major interface, data, security, deployment or compatibility issues without causing delay or rework.

The review should therefore be connected to solution planning, PI planning, integration planning, product / system / solution demos and release readiness. Early reviews focus on solution structure, completeness, risks and required enablers. Later reviews focus on verification evidence, compatibility declarations, solution baselines and release readiness.

| **Review question**                           | **Purpose**                                                                                                                                       | **Required evidence or output**                                                                               |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Is the solution capability clear?             | Ensures that the solution architecture is linked to a business capability, mission outcome or customer value.                                     | Capability map, mission thread, business objective, solution context, value-stream mapping                    |
| Are participating products identified?        | Clarifies which products contribute to the solution and which products are affected by integration and release decisions.                         | Product participation map, product contribution statements, affected product list                             |
| Is capability allocation clear?               | Ensures that each solution capability is assigned to one or more responsible products.                                                            | Capability-to-product matrix, ownership mapping, backlog or epic mapping                                      |
| Are cross-product interfaces defined?         | Ensures that product interactions are explicit, owned, versioned and testable.                                                                    | Interface catalogue, ICDs, API contracts, topic definitions, schema references, interface owner list          |
| Are data flows and semantic mappings defined? | Ensures that exchanged data is consistent across products and meaningful at solution level.                                                       | Data flow model, data contracts, semantic mapping, metadata rules, data ownership records                     |
| Is solution security defined?                 | Ensures that security is governed across product boundaries, trust zones and deployment environments.                                             | Solution threat model, trust-zone diagram, identity model, crypto assumptions, logging and audit expectations |
| Is integrated runtime and deployment defined? | Ensures that the solution can be deployed, configured, observed and operated in the intended environments.                                        | Deployment view, runtime configuration, environment compatibility matrix, observability evidence              |
| Is release compatibility defined?             | Ensures that independently evolving product releases can form one coherent solution release baseline.                                             | Solution release baseline, product compatibility matrix, product release compatibility declarations           |
| Is integrated verification planned?           | Ensures that architecture claims can be proven before release readiness is claimed.                                                               | Verification matrix, integration plan, contract test plan, system / solution demo plan                        |
| Are architecture runway items identified?     | Ensures that required enablers are planned before they become integration or release blockers.                                                    | Architecture runway, enabler backlog, dependency map, PI planning input                                       |
| Are risks and debt visible?                   | Ensures that integration, interface, data, security, deployment and release risks are tracked and owned.                                          | Solution risk register, solution technical debt register, mitigation plan, owner list                         |
| Are BAPO responsibilities clear?              | Ensures that the solution architecture has business relevance, owned architecture decisions, executable process mechanisms and accountable roles. | Solution BAPO map, RACI, owner assignments, review record                                                     |
| What follow-up action is required?            | Converts review findings into executable work instead of leaving them as observations.                                                            | Product backlog item, solution enabler, technical debt item, exception request, release-readiness action      |

<span id="_Toc233730488" class="anchor"></span>Table 104: BAPO Architecture decision template

The Solution Architecture Review should produce a clear review result. Typical outcomes include approval of the solution architecture, a required update to the solution baseline, product-level follow-up actions, interface or data contract clarification, architecture runway items, integration-risk items, technical debt items, exception requests or release-readiness blockers.

The Solution Architect owns the review from a solution-coherence perspective. Product Architects provide product-level architecture evidence, interface evidence, data contract evidence, deployment assumptions and compatibility declarations. Security, Data and Platform Architects should be involved where the solution review affects trust boundaries, semantic alignment, runtime environments, DevSecOps or deployment architecture.

The review should apply the BAPO alignment markers in addition to the solution quality markers. The business capability must be clear, the solution architecture response must be defined, the required integration and release mechanisms must be executable, and ownership must be assigned across the participating products.

A solution should not be considered architecture-ready if product participation, capability allocation, interfaces, data flows, security boundaries, deployment assumptions or integration evidence are still unclear. A solution should not be considered release-ready unless the required product compatibility declarations, solution baseline, integration evidence, security evidence and release risks are current, owned and reviewable.

## Product Architecture Review

The Product Architecture Review assesses whether an individual product architecture is complete, owned, evidence-based, implementation-ready and compatible with the relevant solution and enterprise architecture expectations. It focuses on the architecture of one product, including context, building blocks, runtime behavior, deployment, interfaces, data contracts, ADRs, quality requirements, security, verification evidence and technical debt.

Product architecture reviews should be staged across the lifecycle. Early reviews may accept maturity score 3 for relevant markers if the design, rationale, ownership and delivery mechanisms are clear. Release readiness reviews require stronger evidence, especially for critical interfaces, data contracts, security controls, deployment reproducibility, resilience, performance, observability and compatibility with solution baselines.

Product reviews must also check whether product-level architecture changes affect solution compatibility. A product-level ADR may require solution-level review if it changes an externally visible interface, data model, security assumption, runtime dependency, deployment assumption, compatibility declaration or release baseline.

| **Review question**                                     | **Purpose**                                                                                                                    | **Required evidence or output**                                                                                                   |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Is the product business contribution clear?             | Ensures that the product architecture is linked to business capability, mission value, customer need or solution contribution. | Product Business Contribution Statement, product BAPO map, capability mapping                                                     |
| Is context and scope defined?                           | Clarifies product boundaries, users, external systems, constraints and dependencies.                                           | Context diagram, boundary description, external system map, dependency map                                                        |
| Are building blocks and responsibilities clear?         | Ensures that the product structure is understandable, owned and maintainable.                                                  | Building Block View, responsibility mapping, component ownership, dependency model                                                |
| Are runtime scenarios defined?                          | Verifies that relevant operational, failure, degraded and recovery scenarios are understood.                                   | Runtime View, sequence descriptions, state behavior, failure scenarios, degraded-mode scenarios                                   |
| Is deployment reproducible?                             | Ensures that the product can be deployed, configured, observed, updated and rolled back consistently.                          | Deployment View, deployment manifests, pipeline evidence, environment compatibility matrix, rollback evidence                     |
| Are interfaces and data contracts specified and tested? | Ensures that externally visible integration points are versioned, owned, semantically clear and compatible.                    | Interface contracts, data contracts, schemas, ICDs, contract tests, schema validation, interoperability tests                     |
| Are ADRs complete and current?                          | Ensures that major product architecture decisions are documented with rationale, alternatives and consequences.                | ADR register, decision records, trade-off analysis, supersession or review records                                                |
| Are quality attributes measurable and evidenced?        | Ensures that performance, determinism, resilience, observability, maintainability and deployability claims can be verified.    | Quality Requirement Catalogue, test results, measurements, runtime evidence, observability evidence                               |
| Is security implemented and verified?                   | Ensures that product-level security controls are defined, implemented, tested and aligned with solution trust boundaries.      | Product Security Concept, threat model, security test evidence, vulnerability scan results, crypto review, logging/audit evidence |
| Is product verification evidence available?             | Confirms that critical architecture claims are supported by concrete evidence.                                                 | Verification Evidence, test reports, review records, demo evidence, marker scores                                                 |
| Is release compatibility declared?                      | Ensures that the product release is compatible with the relevant solution baseline and enterprise guardrails.                  | Product Release Compatibility Declaration, solution baseline mapping, enterprise guardrail mapping, compatibility evidence        |
| Is technical debt visible and owned?                    | Ensures that known product architecture gaps, risks and limitations are tracked and governed.                                  | Product Risk and Technical Debt Register, mitigation plan, owner assignment, due date, residual risk record                       |
| Does the product change affect solution architecture?   | Determines whether a product-level change requires solution-level review.                                                      | ADR impact assessment, interface change record, data contract change, security impact, runtime or deployment impact               |
| What follow-up action is required?                      | Converts review findings into executable backlog, evidence or governance actions.                                              | Product backlog item, architecture enabler, technical debt item, exception request, solution review request                       |

<span id="_Toc233730489" class="anchor"></span>Table 105: Enterprise guardrail template

The Product Architect owns the product architecture review from a product-coherence perspective. Product teams provide implementation and verification evidence. Security, Data and Platform Architects should be involved where the review affects security controls, data contracts, deployment environments, DevSecOps, observability or runtime assumptions. The Solution Architect should be involved whenever product architecture changes affect solution interfaces, data flows, deployment topology, security boundaries, solution baselines or release compatibility.

The review should apply the Product Architecture quality markers together with the mandatory BAPO alignment markers. The business contribution must be clear, the product architecture response must be defined, the required delivery and verification mechanisms must exist, and ownership must be assigned. A product architecture should not be considered architecture-ready if these dimensions are unclear.

The review depth should match the lifecycle stage and risk. During early product architecture review, the main question is whether the architecture is designed, owned, traceable and executable. During release readiness, the main question is whether the architecture is verified, compatible, evidenced and releasable. Critical markers that affect security, interfaces, data contracts, deployment, resilience, performance or solution compatibility require stronger evidence before release.

A product architecture review should produce a clear result: approval, conditional approval, required rework, a technical debt item, an architecture enabler, an exception request, a release-readiness blocker or a solution-level escalation. Review findings must not remain informal observations. They should be assigned to owners and tracked through backlog items, debt registers, release-readiness records or architecture review actions.

## Release Readiness Review

The Release Readiness Review confirms whether a product release or solution release is sufficiently evidenced, compatible, owned and risk-assessed to support a release decision. It is not only a project-management checkpoint. It is an architecture governance checkpoint that verifies whether the required architecture evidence is complete and whether remaining risks are visible and accepted.

The review must distinguish between product release readiness and solution release readiness. Product release readiness confirms that an individual product release is architecturally current, verified, deployable and compatible with applicable guardrails and baselines. Solution release readiness confirms that multiple independently evolving product releases form one coherent, integrated and releasable solution baseline.

A product may be release-ready on its own but still not be compatible with a specific solution release baseline. Therefore, product compatibility declarations, interface versions, data contract versions, security assumptions, deployment configurations and verification evidence must be assessed against the relevant solution baseline.

| **Review area**                  | **Product release readiness**                                                                  | **Solution release readiness**                                                           | **Typical evidence / decision**                                                                                             |
|----------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Business objective               | Product contribution is confirmed.                                                             | Solution capability or mission outcome is confirmed.                                     | Product Business Contribution Statement, solution capability map, release scope, business acceptance criteria               |
| Architecture baseline            | Product architecture is current, reviewed and consistent with implemented release.             | Solution release baseline is defined, current and aligned with participating products.   | Product Architecture Document, ADR register, solution baseline, product participation map, capability allocation            |
| Interface compatibility          | Product interface contracts are specified, versioned and verified.                             | Cross-product interface versions are compatible across the solution baseline.            | Interface contracts, ICDs, API/topic/schema versions, contract test results, compatibility matrix                           |
| Data compatibility               | Product data contracts and schemas are verified.                                               | Solution data flows, semantic mappings and data model versions are compatible.           | Data contracts, schema validation, semantic mapping, data flow model, data ownership evidence                               |
| Security evidence                | Product security evidence is complete and product-level exceptions are documented.             | Cross-product security evidence, trust boundaries and security assumptions are complete. | Product Security Concept, threat model, vulnerability results, crypto review, trust-zone diagram, security exception record |
| Deployment evidence              | Product deployment is reproducible and verified in supported environments.                     | Integrated deployment is verified for the intended solution runtime environment.         | Deployment manifests, pipeline evidence, environment compatibility matrix, runtime configuration, observability evidence    |
| Test and verification evidence   | Product tests and critical quality evidence are complete.                                      | Integration, system or solution tests prove cross-product behavior.                      | Automated tests, performance results, resilience tests, integration tests, system demo evidence, verification matrix        |
| Release compatibility            | Product compatibility with applicable solution baseline and enterprise guardrails is declared. | All participating product releases are compatible with the solution release baseline.    | Product Release Compatibility Declaration, solution release baseline, product compatibility matrix                          |
| Technical debt and residual risk | Product-level debt is visible, owned and accepted or mitigated.                                | Solution-level debt and integration risks are visible, owned and accepted or mitigated.  | Product debt register, solution debt register, risk acceptance, mitigation plan, review date                                |
| Ownership and approval           | Product Owner and Product Architect approve the product release evidence.                      | Solution Owner and Solution Architect approve the integrated solution release evidence.  | Approval record, review minutes, named owners, release decision                                                             |
| Exceptions                       | Product-level deviations are documented, time-bounded and approved.                            | Solution-level or enterprise guardrail deviations are documented and approved.           | Exception register, risk assessment, expiry date, mitigation owner                                                          |
| Follow-up actions                | Product follow-up actions are assigned and tracked.                                            | Solution follow-up actions are assigned and tracked across products.                     | Backlog items, architecture enablers, technical debt items, improvement actions                                             |

<span id="_Toc233730490" class="anchor"></span>Table 106: Solution architecture template

The Release Readiness Review should not be the first point at which missing evidence is discovered. Critical evidence should be planned during architecture reviews, PI planning, integration planning and verification activities. The release review should confirm readiness, identify remaining risks and decide whether the release can proceed, not create the architecture baseline from scratch.

For product releases, the review focuses on whether the product architecture is current, whether critical interfaces and data contracts are tested, whether deployment is reproducible, whether security and quality evidence are complete, and whether compatibility with the relevant solution baseline is declared.

For solution releases, the review focuses on whether the participating product releases together form a coherent solution release baseline. This includes cross-product interfaces, data flows, security boundaries, runtime configuration, deployment topology, integration evidence and unresolved solution-level risks.

A release should not be approved if critical architecture evidence is missing, outdated, unowned or not traceable to the relevant product or solution baseline. If release proceeds with known gaps, those gaps must be documented as accepted residual risk, architecture exception, technical debt or follow-up action with a named owner and review date.

## Architecture Exception Review

The Architecture Exception Review assesses whether a deviation from an architecture guardrail, standard, marker, baseline, interface rule, data rule, technology decision, security expectation or runtime assumption is justified and controlled. An exception is not a silent waiver. It is an explicit architecture risk decision that must be documented, assessed, owned, time-bounded and reviewed.

The purpose of the review is to support delivery where justified deviations are necessary, while preventing uncontrolled fragmentation of the architecture. Exceptions may be appropriate because of customer constraints, legacy dependencies, mission urgency, technology limitations, integration realities, delivery timing or operational constraints. However, each exception must explain why the deviation is needed, what impact it creates, how the risk is mitigated, who owns it and when it will be reviewed again.

The following content shall be provided for an Architecture Exception Review:

| **Field**                | **Purpose**                                                                                                  | **Required content**                                                                                                                                                          |
|--------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exception target         | Identifies what the exception applies to.                                                                    | Guardrail, standard, quality marker, interface, technology, data rule, security rule, runtime rule, deployment assumption, solution baseline or product architecture decision |
| Affected scope           | Clarifies where the exception has impact.                                                                    | Enterprise, solution, product, ART, product line, interface, data model, security boundary, deployment environment or release baseline                                        |
| Business reason          | Explains why the deviation is needed.                                                                        | Customer constraint, mission need, delivery urgency, business priority, legacy dependency, contractual requirement or product-line reason                                     |
| Architecture impact      | Describes the architectural consequence of the deviation.                                                    | Enterprise impact, solution impact, product impact, interface impact, data impact, platform impact, runtime impact                                                            |
| BAPO implications        | Shows whether the deviation affects business intent, architecture alignment, process execution or ownership. | Business priority, architecture risk, required process change, affected owner, governance implication                                                                         |
| Risk                     | Makes the risk explicit and reviewable.                                                                      | Security, safety, interoperability, maintainability, release, compliance, operational, technical debt or integration risk                                                     |
| Alternatives             | Demonstrates that other options were considered.                                                             | Options considered, rejected alternatives, trade-offs, reason why standard alignment is not feasible                                                                          |
| Mitigation               | Defines how the risk will be controlled.                                                                     | Mitigation action, compensating control, workaround, additional test, monitoring, time limit, migration plan                                                                  |
| Evidence                 | Provides proof for the assessment and decision.                                                              | Impact analysis, test evidence, security review, interface analysis, compatibility assessment, risk assessment, review record                                                 |
| Owner                    | Assigns accountability for the exception.                                                                    | Responsible owner, architect, team, product owner, security owner, interface owner, data owner or platform owner                                                              |
| Expiration / review date | Prevents the exception from becoming permanent by default.                                                   | Review date, end date, expiry condition, closure criterion, renewal condition                                                                                                 |
| Decision                 | Records the outcome of the review.                                                                           | Approved, rejected, conditionally approved, escalated, deferred or returned for rework                                                                                        |
| Follow-up action         | Converts the exception into managed work or governance feedback.                                             | Backlog item, technical debt item, architecture runway item, guardrail update, release condition or portfolio decision                                                        |

<span id="_Toc233730491" class="anchor"></span>Table 107: Product architecture template

The Architecture Exception Review should determine whether the deviation is acceptable for the affected scope and timeframe. Minor local deviations may be approved by the responsible architect if they do not affect solution compatibility, enterprise guardrails, security, data consistency, release readiness or cross-product integration. Major deviations should be reviewed by the Architecture Review Board or the responsible enterprise architecture governance body.

An approved exception must always remain visible until it is closed, expired or renewed. It should be recorded in the relevant exception register and linked to any affected technical debt item, release-readiness decision, product compatibility declaration, solution baseline or enterprise guardrail. The exception record should make clear whether the deviation is temporary, conditionally accepted or a candidate for future guardrail improvement.

Conditional approvals should define explicit conditions. These may include additional verification evidence, security review, contract testing, migration before a future release, mitigation before deployment, or review at a defined milestone. If the conditions are not met, the exception should not be treated as valid release evidence.

Repeated exceptions are architecture feedback. If multiple products or solutions request similar deviations, the review should not only approve or reject the individual case. It should also ask whether the underlying enterprise guardrail, solution baseline, platform capability, interface standard or process expectation is incomplete, outdated, too restrictive or insufficiently supported. In such cases, the exception should trigger guardrail review, architecture runway, technical debt reduction or portfolio-level improvement action.

## System Demo and Inspect & Adapt Feedback

System demos, solution demos and product demos are among the strongest forms of architecture evidence because they show whether architecture decisions work in implemented behavior. Documents, diagrams and reviews can describe the intended architecture, but demos can reveal whether interfaces, data flows, runtime behavior, deployment assumptions, security controls, observability and degraded-mode behavior actually work together.

The purpose of architecture feedback is not only to identify defects. It is to convert implementation, integration, demo and operational findings into architecture improvement actions. These actions may become product backlog items, solution architecture enablers, enterprise guardrail updates, technical debt items, architecture runway, exception reviews or portfolio investment decisions.

Inspect & Adapt provides the mechanism to turn evidence into improvement. If a demo reveals repeated interface issues, the response may be stronger interface ownership or contract testing. If deployment is difficult, the response may be deployment automation or platform runway. If security evidence is missing, the response may be a DevSecOps or security architecture improvement. If several teams encounter the same problem, the feedback may require enterprise guardrail clarification or portfolio funding.

| **Feedback source**       | **Architecture use**                                                                                                                                | **Typical evidence**                                                                                  | **Typical follow-up action**                                                                     |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Product demo              | Proves product-level architecture behavior, such as runtime scenarios, deployment behavior, observability, security controls or quality attributes. | Product demo result, test evidence, runtime evidence, product findings                                | Product backlog item, ADR update, verification action, product technical debt                    |
| System demo               | Proves integrated behavior within an ART or system context and reveals integration, timing, interface, deployment or observability issues.          | System demo result, integration evidence, contract-test result, runtime finding                       | Architecture enabler, integration action, technical debt item, PI planning input                 |
| Solution demo             | Proves multi-product solution behavior and release capability across participating products.                                                        | Solution demo result, product compatibility evidence, solution baseline evidence, integration finding | Solution enabler, solution debt item, baseline update, release-readiness action                  |
| Inspect & Adapt           | Converts demo, integration and delivery findings into structured improvement actions.                                                               | Inspect & Adapt item, root-cause analysis, improvement backlog item, KPI trend                        | Architecture runway, technical debt reduction, process improvement, guardrail update             |
| Operational monitoring    | Identifies runtime architecture gaps that appear under real or realistic operating conditions.                                                      | Logs, metrics, traces, health indicators, monitoring dashboards, operational findings                 | Observability improvement, resilience action, runtime guardrail update, product or solution debt |
| Incident analysis         | Identifies architecture weaknesses related to security, resilience, performance, deployment or process gaps.                                        | Incident report, root-cause analysis, security finding, recovery evidence                             | Security action, resilience improvement, process change, exception review, architecture debt     |
| Technical debt review     | Makes architecture gaps visible and updates priorities for mitigation.                                                                              | Debt register, mitigation status, residual risk, owner list                                           | Debt reduction backlog, architecture runway, portfolio escalation, release condition             |
| Exception review feedback | Identifies whether repeated deviations indicate a weak or outdated guardrail.                                                                       | Exception trend, repeated deviation pattern, risk assessment                                          | Guardrail clarification, controlled variant, enterprise debt item, portfolio action              |

<span id="_Toc233730492" class="anchor"></span>Table 108: Interface contract template

Demo and feedback findings should be treated as architecture evidence when they reveal whether architecture assumptions are valid. A successful demo can confirm that a marker is sufficiently evidenced. A failed or partial demo can show that an architecture decision, interface contract, data contract, deployment assumption, security control or quality requirement is incomplete.

Each relevant finding should be assessed against the architecture quality markers and BAPO alignment markers. The review should ask whether the finding affects business value, architecture structure, delivery or governance process, or ownership. This prevents findings from being treated only as local defects when they actually indicate architecture or governance weakness.

Feedback must result in clear ownership. A finding without an owner, action and review point is not governed feedback. Every architecture-relevant finding should therefore be converted into one of the following: a backlog item, architecture enabler, technical debt item, exception, guardrail update, solution baseline update, product compatibility action or portfolio decision.

The feedback loop is essential to the framework. Architecture governance is not complete when a decision is documented or approved. It is complete only when decisions are implemented, demonstrated, evidenced, reviewed and improved through feedback from delivery and operation.

# SDD Architecture Templates and Checklists

## Purpose

This chapter provides templates and checklists for applying the SDD Architecture Governance Framework consistently across Enterprise, Solution and Product Architecture. The templates are not intended to create unnecessary paperwork. They exist to make architecture information reusable, reviewable, comparable and traceable across teams, products, solutions and architecture levels.

The templates should be used pragmatically and proportionally. A small product, early concept or local architecture decision may require only a lightweight version of the template. A major solution release, enterprise guardrail, cross-product interface, data contract, security decision or release compatibility declaration requires stronger evidence and more complete documentation. The level of detail should therefore reflect architecture impact, integration risk, release relevance, security criticality and expected reuse.

Regardless of tailoring, the core information should remain consistent. Architecture artifacts should explain the business driver, the architecture decision or structure, the process implication, the accountable ownership, the required evidence and the affected quality markers. This ensures that architecture decisions are not treated as isolated technical statements, but as governed decisions connected to business value, delivery execution and reviewable evidence.

The templates also support cross-level alignment. Enterprise guardrails define what must be consistent. Solution architecture artifacts define how multiple products work together as one releasable solution. Product architecture artifacts define how individual products are designed, implemented, verified and made compatible with applicable solution baselines and enterprise guardrails.

The templates in this chapter should be used as living architecture artifacts. They should be updated when architecture decisions change, interfaces or data contracts evolve, solution baselines are revised, evidence becomes available, risks are accepted or mitigated, or feedback from demos, release readiness reviews, operation or Inspect & Adapt requires improvement.

A template should be considered useful only if it supports better architecture decisions, clearer ownership, stronger evidence or faster review. Templates should not be completed mechanically. They should help architects, product teams, solution teams and governance bodies answer the essential question: is the architecture decision clear, owned, executable, evidenced and aligned with the relevant business, solution and product context?

## BAPO Architecture Decision Template

The BAPO Architecture Decision Template shall be used for architecture decisions that affect more than one component, product, solution, ART, division or architecture level. It is especially relevant for decisions concerning interfaces, data models, security mechanisms, runtime platforms, deployment models, technology choices, enterprise guardrails, solution baselines and release compatibility.

The purpose of the template is to ensure that architecture decisions are not documented only as technical choices. Every significant architecture decision must explain the business reason, the architecture response, the process implications, the ownership model, the affected quality markers and the evidence required to verify the decision.

For small local implementation decisions, a lightweight ADR may be sufficient. For decisions with cross-product, solution-level or enterprise-level impact, the full BAPO decision template should be used. The template may also be used as an extended ADR format where stronger governance traceability is required.

The following fields define the minimum content of a BAPO architecture decision:

| **Field**                | **Purpose**                                                                                                   | **Required content**                                                                                                                          |
|--------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Decision title           | Provides a short and recognizable name for the decision.                                                      | Short decision title, identifier, affected product or solution where useful                                                                   |
| Decision status          | Shows the current lifecycle state of the decision.                                                            | Proposed, accepted, rejected, superseded, deprecated, under review                                                                            |
| Level                    | Clarifies the primary architecture level affected by the decision.                                            | Enterprise, solution, product, or cross-level                                                                                                 |
| Affected scope           | Defines where the decision applies and who is impacted.                                                       | Component, product, solution, ART, platform, interface, data model, security boundary, deployment environment, solution baseline              |
| Business driver          | Explains why the decision is needed.                                                                          | Capability, mission outcome, customer need, strategic theme, product-line objective, value-stream need, sovereignty or security driver        |
| Architecture decision    | States the actual architecture decision clearly.                                                              | Structural decision, guardrail, pattern, interface, data model, deployment decision, runtime decision, security decision, technology choice   |
| Alternatives             | Shows that relevant options were considered.                                                                  | Options considered, rejected alternatives, trade-offs, reason for selection                                                                   |
| Process implication      | Explains what must happen in planning, delivery, verification, release or governance because of the decision. | Required review, test, integration step, release rule, governance process, exception process, quality gate, DevSecOps pipeline change         |
| Ownership implication    | Defines who is accountable for the decision and its consequences.                                             | Responsible architect, product owner, team, interface owner, data owner, security owner, platform owner, community of practice, review body   |
| Quality markers affected | Links the decision to architecture quality assessment.                                                        | Relevant Enterprise, Solution, Product and BAPO markers, expected marker impact, critical marker indication                                   |
| Evidence                 | Defines how the decision will be verified or reviewed.                                                        | Documents, architecture models, ADRs, tests, demos, measurements, review records, compatibility declarations, release evidence                |
| Compatibility impact     | Identifies whether the decision affects product or solution compatibility.                                    | Interface version impact, data contract impact, security baseline impact, runtime dependency, deployment assumption, solution baseline impact |
| Consequences             | Makes the benefits, trade-offs and risks explicit.                                                            | Benefits, constraints, risks, technical debt, migration impact, operational impact, maintenance impact                                        |
| Follow-up actions        | Converts the decision into executable work.                                                                   | Backlog item, architecture enabler, technical debt item, exception, test action, release-readiness action, guardrail update                   |
| Review date              | Defines when or under which condition the decision must be reassessed.                                        | Review date, expiry condition, trigger event, next release, solution baseline change, guardrail update                                        |

<span id="_Toc233730494" class="anchor"></span>Table 110: Quality marker template

The template should be completed with enough detail to make the decision understandable, reviewable and actionable. It should not become a long report for every minor design choice. The level of detail should be proportional to the impact of the decision. A cross-product interface decision, for example, requires stronger evidence and ownership than a product-internal implementation detail.

The decision should be linked to the relevant architecture artifacts. Enterprise-impacting decisions should reference applicable guardrails or reference architectures. Solution-impacting decisions should reference the solution baseline, product participation map, interface catalogue or data flow model. Product-impacting decisions should reference the Product Architecture Document, ADR Register, Interface Specification, Product Security Concept or Verification Evidence.

A BAPO architecture decision is not complete unless all four BAPO dimensions are addressed. The business driver explains why the decision matters. The architecture decision explains what structural choice is being made. The process implication explains how the decision will be implemented, verified, released or governed. The ownership implication explains who is accountable for maintaining the decision and handling its consequences.

Where the decision creates risk, deviation or incomplete evidence, this must be made visible. The follow-up may be an architecture enabler, technical debt item, exception request, additional verification action, solution review or enterprise guardrail update. The decision should not be treated as accepted architecture if critical ownership, process or evidence gaps remain unresolved.

## Enterprise Guardrail Template

Enterprise guardrails shall be written so that Solution and Product Architects can apply them without needing interpretation from the original author. A guardrail must clearly state why it exists, where it applies, what is mandatory, what can still be decided locally, which evidence is required, who owns it and how exceptions are handled.

The purpose of an enterprise guardrail is not to centralize all architecture decisions. Its purpose is to define the minimum architecture alignment required where inconsistent local decisions would create cross-division fragmentation, integration risk, security gaps, data incompatibility, technology divergence, platform fragmentation or release incompatibility.

Every enterprise guardrail shall have a clear owner and review mechanism. Without ownership, guardrails become static documents and will eventually become outdated. A guardrail must therefore be treated as a living architecture asset that is versioned, communicated, applied, measured and improved through feedback from solutions and products.

The following fields define the minimum content of an enterprise guardrail:

| **Field**           | **Purpose**                                                                                 | **Required content**                                                                                                                 |
|---------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Guardrail name      | Provides a clear and recognizable reference for the guardrail.                              | Name, short identifier, version, status                                                                                              |
| Business driver     | Explains why the guardrail is needed.                                                       | Strategic theme, business capability, mission need, customer need, sovereignty need, security need, product-line objective           |
| Scope               | Defines where the guardrail applies.                                                        | Divisions, solutions, products, systems, platforms, interfaces, data domains or runtime environments affected                        |
| Architecture rule   | States the mandatory or recommended architecture guidance.                                  | Required standard, reference architecture, interface rule, data rule, technology rule, security rule, runtime rule or DevSecOps rule |
| Applicability       | Clarifies whether the guardrail is mandatory in all cases or only under defined conditions. | Mandatory, recommended, conditional, optional with justification, applicability criteria                                             |
| Local autonomy      | Defines what can still be decided locally by Solution or Product Architecture.              | Allowed local decisions, variation points, tailoring rules, product-specific options                                                 |
| Process requirement | Defines how the guardrail is applied, verified and governed.                                | Required review, checklist, test, KPI, release rule, governance step, quality gate or DevSecOps pipeline evidence                    |
| Owner               | Assigns accountability for maintenance and evolution.                                       | Enterprise owner, responsible architect, data owner, interface owner, security owner, platform owner or architecture community       |
| Evidence            | Defines how application of the guardrail is demonstrated.                                   | Standard, catalogue, reference architecture, review record, adoption evidence, KPI dashboard, test result, release evidence          |
| Exception rule      | Defines how deviations are requested, assessed and approved.                                | Exception process, approval authority, risk assessment, mitigation, expiry date, review date                                         |
| Review cadence      | Ensures that the guardrail remains current.                                                 | Review interval, review trigger, lifecycle status, update responsibility                                                             |
| Feedback mechanism  | Defines how findings from solutions and products improve the guardrail.                     | Exception trends, solution feedback, product findings, technical debt, Inspect & Adapt actions, KPI trends                           |

<span id="_Toc233730495" class="anchor"></span>Table 111: Architecture exception template

A well-written enterprise guardrail should be specific enough to guide architecture decisions, but not so detailed that it unnecessarily constrains product or solution autonomy. It should define what must be common while leaving local design freedom where variation does not create enterprise risk.

The guardrail should also be testable or reviewable. If architects cannot determine whether a solution or product follows the guardrail, the guardrail is not precise enough. Evidence expectations should therefore be stated explicitly. Depending on the guardrail, evidence may include architecture mappings, interface contracts, data models, security reviews, deployment manifests, pipeline evidence, KPI dashboards, exception records or release declarations.

The exception rule is part of the guardrail, not an afterthought. Controlled deviations are sometimes necessary because of customer constraints, legacy dependencies, mission needs, technology limitations or delivery timing. However, deviations must be visible, risk-assessed, owned and time-bounded. Repeated exceptions should trigger a review of the guardrail itself.

An enterprise guardrail should not be considered ready for publication unless the business driver, architecture rule, applicability, ownership, evidence expectation and exception process are clear. If these elements are missing, the guardrail may create confusion rather than alignment.

## Solution Architecture Template

The Solution Architecture Template shall be used whenever several products must be aligned into one coherent, integrated and releasable solution. The template ensures that Solution Architecture does not only describe the participating products, but also defines how these products work together, how they are verified, how they are deployed, how they are secured, and how their releases remain compatible with the solution baseline.

The solution architecture document is the primary architecture record for cross-product coherence. It connects the business or mission capability to product participation, capability allocation, interface and data contracts, security boundaries, runtime and deployment assumptions, integration evidence, release compatibility, architecture runway, risks and technical debt.

A solution architecture document shall be updated whenever the solution scope, product participation, capability allocation, interface architecture, data model, security baseline, deployment topology, integration strategy or solution release baseline changes.

| **Section**                           | **Purpose**                                                                                 | **Required content**                                                                                                        |
|---------------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Solution business capability          | Explains why the solution exists and which business, customer or mission value it provides. | Mission capability, customer capability, business objective, value stream, strategic theme, success criteria                |
| Solution context                      | Defines the solution boundary and its environment.                                          | Participating products, external systems, users, actors, suppliers, operational context, assumptions and constraints        |
| Product participation                 | Identifies which products contribute to the solution.                                       | Product participation map, product contribution statements, product owners, Product Architects, affected teams              |
| Capability allocation                 | Shows which product is responsible for which solution capability.                           | Capability-to-product mapping, responsibility allocation, shared capability ownership, unresolved allocation gaps           |
| Interface architecture                | Defines how products communicate and integrate.                                             | Cross-product APIs, topics, schemas, events, protocols, ICDs, interface owners, versioning and compatibility rules          |
| Data architecture                     | Defines how data flows and remains semantically consistent across products.                 | Data flows, data contracts, semantic mapping, metadata rules, classification, provenance, data ownership                    |
| Security architecture                 | Defines the solution-level security and trust model.                                        | Trust zones, identity model, access rules, crypto assumptions, logging, audit, monitoring, solution threat model            |
| Runtime and deployment                | Defines how the integrated solution is deployed and operated.                               | Deployment topology, edge/fog/cloud placement, runtime dependencies, configuration, observability, environment assumptions  |
| Release architecture                  | Defines how product releases form one solution release baseline.                            | Solution release baseline, product compatibility matrix, interface versions, data model versions, deployment configurations |
| Integration and verification strategy | Defines how solution-level architecture claims are proven.                                  | Integration tests, contract tests, system or solution demos, verification matrix, quality scenarios, evidence expectations  |
| Architecture runway                   | Identifies architecture enablers required before integration or release is blocked.         | Interface runway, data runway, security runway, platform runway, integration runway, resilience runway                      |
| Risks and technical debt              | Makes cross-product risks and architecture debt visible.                                    | Solution risk register, solution technical debt register, mitigation actions, owners, due dates, residual risks             |
| BAPO map                              | Connects business intent, architecture response, delivery mechanisms and ownership.         | Business driver, architecture decisions, process implications, organizational ownership, evidence links                     |
| Governance and review record          | Shows how the solution architecture is reviewed and maintained.                             | Review history, decision records, exceptions, quality-marker scores, approvals, follow-up actions                           |

<span id="_Toc233730496" class="anchor"></span>Table 112: Release compatibility declaration template

The level of detail should be proportional to the solution’s complexity and risk. A small solution may describe some sections briefly, while a large multi-product solution requires detailed interface, data, security, deployment, release and verification evidence. However, no section should be omitted if it affects integration, release compatibility, security, data consistency or operational readiness.

The Solution Architect owns the solution architecture document and is responsible for keeping it aligned with the solution baseline. Product Architects provide the product-level architecture evidence required by the solution, including interface specifications, data contracts, deployment assumptions, security evidence and product release compatibility declarations.

The template should not be treated as a static document. It is a living architecture artifact that must be updated through solution planning, PI planning, integration reviews, demos, release readiness reviews and Inspect & Adapt. Changes to participating products, interface versions, data semantics, security assumptions, deployment configuration or verification evidence must be reflected in the solution architecture.

A solution architecture should not be considered architecture-ready if product participation, capability allocation, cross-product interfaces, data flows, security boundaries, deployment assumptions or ownership are unclear. It should not be considered release-ready unless the solution release baseline, product compatibility declarations, integration evidence, security evidence and unresolved risks are current, owned and reviewable.

## Product Architecture Template

The Product Architecture Template shall be used as the standard structure for product-level architecture descriptions. It defines the minimum architecture evidence required to understand, review, implement, verify and release an individual product. The template may be tailored to product size, maturity and criticality, but the essential evidence categories should remain present.

The Product Architecture Document should not duplicate low-level design unnecessarily. It should focus on architecture-relevant decisions: product contribution, boundaries, building blocks, runtime behavior, deployment assumptions, interfaces, data contracts, quality attributes, security, verification evidence, release compatibility and technical debt.

The product architecture document is also the main evidence source for Product Architecture reviews and product release readiness. It must therefore be current, owned, versioned and aligned with applicable enterprise guardrails and solution baselines.

| **Section**                               | **Purpose**                                                                                 | **Required content**                                                                                                                |
|-------------------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Product business contribution             | Explains why the product exists and which business, mission or solution value it supports.  | Product value, mission contribution, customer need, supported solution capability, product-line relevance                           |
| Context and scope                         | Defines the product boundary and its external environment.                                  | Boundary, actors, users, external systems, suppliers, constraints, assumptions, dependencies                                        |
| Building Block View                       | Describes the static product structure and responsibilities.                                | Components, modules, services, responsibilities, dependencies, ownership, quality attribute allocation                              |
| Runtime View                              | Describes how the product behaves during execution.                                         | Runtime scenarios, message flows, event flows, state behavior, failure behavior, recovery behavior                                  |
| Deployment View                           | Describes where and how the product runs.                                                   | Nodes, containers, runtime assumptions, environment constraints, configuration, observability, update and rollback                  |
| Interface and Data Contract Specification | Defines externally visible integration points and exchanged data.                           | APIs, topics, schemas, messages, events, protocols, versions, semantics, owners, contract tests                                     |
| ADR Register                              | Preserves major architecture decisions and their rationale.                                 | Architecture decisions, alternatives, trade-offs, consequences, affected quality markers, review dates                              |
| Quality Requirement Catalogue             | Defines measurable non-functional requirements.                                             | Performance, determinism, resilience, security, interoperability, deployability, observability, maintainability                     |
| Product Security Concept                  | Defines product-level security architecture and evidence.                                   | Threat model, trust boundaries, identity, authorization, crypto, logging, audit, vulnerability handling, secure update              |
| Verification Evidence                     | Shows how architecture claims are proven.                                                   | Test results, review evidence, contract tests, security evidence, performance measurements, deployment evidence                     |
| Product Release Compatibility Declaration | Declares compatibility with relevant solution baselines and enterprise guardrails.          | Supported solution baseline, product version, interface versions, data model versions, security baseline, deployment configurations |
| Product Risk and Technical Debt Register  | Makes known architecture gaps and risks visible and governable.                             | Risks, debt items, causes, impact, mitigation, owner, due date, residual risk, status                                               |
| Product Process Evidence                  | Shows that required delivery, test, security, release and debt-management mechanisms exist. | CI/CD evidence, test process, release process, security scans, review records, debt-management process                              |
| Product BAPO Map                          | Connects product value, architecture decisions, delivery mechanisms and ownership.          | Business driver, architecture response, process implications, organizational ownership, evidence links                              |
| Governance and review record              | Shows how the product architecture is maintained and reviewed.                              | Review history, marker scores, approvals, exceptions, follow-up actions, update history                                             |

The level of detail should be proportional to product complexity, criticality and integration impact. A small product may use a compact architecture document, while a product that participates in several solution baselines, exposes critical interfaces, handles sensitive data or supports mission-critical behavior requires stronger evidence.

The Product Architect owns the Product Architecture Document and is responsible for keeping it consistent with implementation, ADRs, interfaces, data contracts, deployment assumptions, security evidence and release compatibility declarations. Product teams provide implementation and verification evidence. Security, Data and Platform Architects should contribute where the product affects cross-cutting concerns.

The Product Architecture Document should be treated as a living artifact. It must be updated when major architecture decisions, interfaces, data contracts, security assumptions, deployment models, quality requirements, technical debt or release compatibility change.

A product architecture should not be considered architecture-ready if the business contribution, context, building blocks, runtime behavior, deployment assumptions, interfaces, quality requirements, security concept or ownership are unclear. It should not be considered release-ready unless the required verification evidence, compatibility declaration, security evidence, deployment evidence and open risks are current, owned and reviewable.

## Interface Contract Template

Interface contracts shall be treated as living architecture artifacts. They define how products, systems, services or components interact, and they are therefore critical for product autonomy, solution compatibility and release readiness. An interface contract must be versioned, owned, tested and linked to the relevant product and solution baselines.

The purpose of the Interface Contract Template is to make externally visible behavior explicit. The contract must describe not only the technical structure of an API, topic, event, stream, file or protocol, but also its purpose, provider, consumers, semantics, security assumptions, compatibility rules, error behavior and verification evidence.

When an interface changes, the affected product architecture, solution architecture and release baselines must be reviewed. For critical interfaces, the contract should be supported by automated contract tests so that product teams can release independently while maintaining solution-level compatibility.

The following fields define the minimum content of an interface contract:

| **Field**            | **Purpose**                                                                    | **Required content**                                                                                              |
|----------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Interface name       | Provides a unique and recognizable reference.                                  | Unique name, short identifier, related product, related solution or capability                                    |
| Interface purpose    | Explains why the interface exists and what capability it supports.             | Business or mission purpose, supported product function, supported solution capability                            |
| Owner                | Assigns accountability for maintaining the interface.                          | Responsible product, team, role, Product Architect, interface owner or service owner                              |
| Provider             | Identifies the system or product that exposes the interface.                   | Providing product, component, service, system or platform                                                         |
| Consumer             | Identifies known or intended consumers of the interface.                       | Consuming product, solution, component, external system, customer system or platform                              |
| Type                 | Defines the technical interaction pattern.                                     | API, topic, event, stream, file, protocol, command, query, message or notification                                |
| Version              | Makes interface evolution and compatibility explicit.                          | Current version, previous version, versioning rule, release baseline mapping                                      |
| Schema               | Defines the structural format of exchanged information.                        | Request schema, response schema, payload schema, message schema, event schema, topic schema                       |
| Semantics            | Defines the meaning and expected behavior of the interface.                    | Field meaning, event meaning, command behavior, status values, units, timing assumptions, state implications      |
| Security             | Defines how the interface is protected.                                        | Authentication, authorization, crypto, classification, trust zone, logging, audit and access rules                |
| Error handling       | Defines behavior under failure or exceptional conditions.                      | Error codes, retries, timeouts, fallback behavior, idempotency, compensation behavior, degraded-mode behavior     |
| Compatibility        | Defines how changes are handled without breaking consumers.                    | Backward compatibility rule, deprecation rule, migration rule, supported versions, breaking-change criteria       |
| Quality expectations | Defines relevant non-functional expectations for the interface.                | Latency, throughput, availability, reliability, ordering, delivery guarantees, resource assumptions               |
| Tests                | Demonstrates that the interface works as specified.                            | Contract tests, schema validation, interoperability tests, regression tests, negative tests, integration evidence |
| Change control       | Defines how changes are reviewed, communicated and released.                   | Change request, impact assessment, consumer notification, review record, release note, approval                   |
| Baseline impact      | Shows whether the interface affects product or solution release compatibility. | Product release mapping, solution baseline mapping, compatibility declaration, affected products or consumers     |

The interface contract should be detailed enough for another team to implement, consume, test and verify the interface without relying on informal knowledge. The contract should therefore describe both the technical exchange format and the expected behavior. A schema alone is not sufficient if the meaning of fields, events, commands, timing assumptions or error behavior remains unclear.

Interface contracts must be aligned with the Product Architecture Document and the Solution Architecture Document. At product level, they define externally visible product behavior. At solution level, they provide the evidence needed to assess cross-product compatibility. If an interface is part of a solution baseline, its version and compatibility rule must be reflected in the solution release baseline and product release compatibility declarations.

For critical interfaces, automated contract tests should be mandatory. Contract tests allow providers and consumers to evolve independently while detecting breaking changes early. Where automated tests are not yet available, the missing evidence should be captured as product technical debt, solution integration risk or architecture runway.

An interface change should not be treated as a local product decision if it affects another product, a solution baseline, a data contract, a security boundary, deployment behavior or release compatibility. Such changes require impact assessment and, where necessary, Solution Architecture review before release.

An interface contract should not be considered mature if it is unowned, unversioned, untested, semantically unclear or disconnected from compatibility rules. These gaps should be made visible during product architecture reviews, solution architecture reviews and release readiness reviews.

## Data Contract Template

Data contracts shall be treated as living architecture artifacts. They define how data is produced, interpreted, consumed, protected, validated and governed across products and solutions. A data contract must therefore define not only structure, but also meaning, ownership, classification, provenance, quality expectations, lifecycle rules and permitted use.

A schema without semantics is not sufficient for data-centric architecture. The data contract must explain what the data represents, who owns it, where it comes from, how it was derived, how it may be used, how quality is measured, and which consumers depend on it. This is especially important for AI, data fusion, sensor integration, command-and-control functions and multi-domain operational pictures, where incorrect or ambiguous data meaning can create mission, safety, security or interoperability risk.

When a data contract changes, the affected product architecture, solution architecture, data flows, interface contracts and release baselines must be reviewed. A product may produce technically valid data, but still create solution-level incompatibility if semantics, classification, provenance, quality rules or lifecycle assumptions differ from the solution baseline.

The following fields define the minimum content of a data contract:

| **Field**          | **Purpose**                                                                                 | **Required content**                                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Data contract name | Provides a unique and recognizable reference.                                               | Unique name, short identifier, related product, related solution, related capability or data domain                    |
| Data purpose       | Explains why the data exists and what business, mission or solution capability it supports. | Business purpose, mission purpose, supported function, supported decision, operational use case                        |
| Data owner         | Assigns accountability for data meaning, quality and lifecycle.                             | Responsible data owner, product owner, domain owner, governance contact, escalation path                               |
| Producer           | Identifies the system or product that creates or publishes the data.                        | Producing system, product, component, sensor, service, external source or platform                                     |
| Consumer           | Identifies known or intended consumers of the data.                                         | Consuming product, solution, service, external system, AI model, analytics function or operational user                |
| Data model         | Defines the structural representation of the data.                                          | Schema, entity model, topic model, object model, message structure, field definitions, version                         |
| Semantics          | Defines the meaning of the data and prevents ambiguous interpretation.                      | Meaning of entities, fields, events, status values, units, coordinate systems, time references, assumptions            |
| Metadata           | Defines the additional information required to interpret and govern the data.               | Timestamp, source identifier, classification, quality indicator, confidence value, version, processing state           |
| Classification     | Defines security, handling and access restrictions.                                         | Security classification, handling caveats, releasability, access rules, need-to-know constraints, audit requirements   |
| Provenance         | Defines where the data comes from and how it was derived.                                   | Source system, sensor source, transformation chain, derivation rules, aggregation logic, lineage information           |
| Quality rules      | Defines how data quality is assessed and evidenced.                                         | Completeness, timeliness, accuracy, consistency, validity, confidence, freshness, error tolerance                      |
| Lifecycle          | Defines how the data is created, updated, retained and removed.                             | Retention, deletion, archival, update rules, expiration, versioning, correction and invalidation rules                 |
| Usage constraints  | Defines how the data may or may not be used.                                                | Permitted use, prohibited use, AI/analytics constraints, operational limitations, decision-support restrictions        |
| Tests              | Demonstrates that the data contract is implemented and valid.                               | Schema validation, semantic validation, data quality evidence, contract tests, consumer validation, regression tests   |
| Change control     | Defines how changes are reviewed, communicated and released.                                | Change record, impact assessment, consumer notification, migration rule, deprecation rule, approval                    |
| Baseline impact    | Shows whether the data contract affects product or solution compatibility.                  | Product release mapping, solution baseline mapping, affected interfaces, affected consumers, compatibility declaration |

<span id="_Toc233730493" class="anchor"></span>**Table 109:** Data contract template

A data contract should be detailed enough for another team to consume, validate and interpret the data without relying on informal knowledge. The contract should therefore describe both the technical structure and the operational meaning of the data. Field names and schemas are not sufficient if units, status values, timestamps, coordinate systems, classifications, confidence values or provenance rules remain unclear.

Data contracts must be aligned with the Product Architecture Document and the Solution Architecture Document. At product level, they define the data a product produces or consumes. At solution level, they provide the evidence needed to assess cross-product data consistency, semantic alignment and release compatibility. If a data contract is part of a solution baseline, its version and compatibility rule must be reflected in the solution release baseline and product release compatibility declarations.

For critical data contracts, validation should be automated where possible. Schema validation proves structural correctness, but semantic and quality validation are also required where incorrect meaning, stale data, missing provenance or poor confidence could affect mission outcome, AI behavior, sensor fusion, operational picture quality or release readiness.

A data contract change should not be treated as a local product decision if it affects another product, a solution baseline, a data flow, a security classification, an AI model, an operational picture or release compatibility. Such changes require impact assessment and, where necessary, Solution Architecture and Data Architecture review before release.

A data contract should not be considered mature if it is unowned, unversioned, semantically unclear, unclassified, untested, missing provenance, or disconnected from lifecycle and compatibility rules. These gaps should be made visible during product architecture reviews, solution architecture reviews and release readiness reviews.

## Quality Marker Template

The Quality Marker Template shall be used to define, assess and track Enterprise, Solution, Product and BAPO quality markers. Its purpose is to make architecture quality reviewable, evidence-based and comparable across architecture levels.

A quality marker is not only a checklist item. It defines a specific architecture concern, the review question used to assess it, the evidence required at different maturity levels, the accountable owner, the review point, the current score, the findings and the improvement actions required to raise maturity.

The following fields define the minimum content of a quality marker:

| **Field**                     | **Purpose**                                                                                 | **Required content**                                                                                                      |
|-------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Marker ID                     | Provides a unique reference for the marker.                                                 | Unique marker ID, for example E1, S4, P8 or B2                                                                            |
| Marker name                   | Provides a short understandable marker name.                                                | Short name describing the architecture concern                                                                            |
| Level                         | Defines where the marker applies.                                                           | Enterprise, Solution, Product or BAPO                                                                                     |
| Applicable scope              | Clarifies where the marker is relevant.                                                     | Guardrail, solution baseline, product architecture, interface, data contract, release, security concept, deployment model |
| Review question               | Defines what the reviewer must assess.                                                      | Clear review question that can be answered through evidence                                                               |
| Criticality                   | Indicates whether the marker is required for architecture readiness or release readiness.   | Critical, release-critical, recommended or informational                                                                  |
| Required evidence for score 3 | Defines what evidence is needed to consider the concern designed and owned.                 | Architecture description, owner assignment, ADR, mapping, review record, planned process or backlog item                  |
| Required evidence for score 4 | Defines what evidence is needed to consider the concern verified.                           | Test result, integration evidence, security evidence, release evidence, deployment evidence, compatibility declaration    |
| Required evidence for score 5 | Defines what evidence is needed to consider the concern continuously measured and improved. | KPI trend, runtime metric, operational evidence, repeated review result, improvement action, feedback loop                |
| Owner                         | Assigns accountability for the marker.                                                      | Responsible architect, product owner, interface owner, data owner, security owner, platform owner or review body          |
| Review point                  | Defines when the marker is assessed.                                                        | Epic review, solution planning, PI planning, architecture review, demo, release readiness, Inspect & Adapt or operation   |
| Score                         | Records the current maturity score.                                                         | Score from 0 to 5 according to the maturity scale in Section 5.2                                                          |
| Score rationale               | Explains why the score was assigned.                                                        | Short justification linked to available evidence and identified gaps                                                      |
| Findings                      | Captures review observations.                                                               | Strengths, gaps, risks, missing evidence, unclear ownership or process weaknesses                                         |
| Actions                       | Converts findings into improvement work.                                                    | Backlog item, architecture enabler, technical debt item, exception, review follow-up, guardrail update                    |
| Follow-up owner and due date  | Ensures improvement actions are owned and tracked.                                          | Named owner, responsible team, target date, review date                                                                   |
| Status                        | Shows the lifecycle state of the marker assessment.                                         | Open, in progress, accepted, blocked, mitigated, closed                                                                   |
| Review history                | Preserves traceability over time.                                                           | Review date, reviewer, previous score, decision, evidence link, change history                                            |

A quality marker should be written so that different reviewers can apply it consistently. The review question must be specific enough to avoid subjective interpretation, and the evidence requirements must make clear what is needed for score 3, score 4 and score 5. This prevents marker scoring from becoming a matter of opinion.

The difference between the maturity levels is important. Score 3 means that the architecture concern is designed, owned and process-aware. Score 4 means that it has been verified with suitable evidence. Score 5 means that it is continuously measured, improved and fed back into architecture decisions. A marker should not receive a higher score unless the evidence supports that maturity level.

Quality marker assessments should always lead to action when gaps are found. A low score is not only a finding; it should trigger an architecture enabler, technical debt item, verification action, exception request, guardrail update or release-readiness follow-up. Without an owner and follow-up action, the marker assessment does not create governance value.

The template should be used consistently across Enterprise, Solution, Product and BAPO markers. This allows architecture maturity to be reviewed across levels while still preserving the specific evidence expectations of each marker type.

## Architecture Exception Template

The Architecture Exception Template shall be used whenever a product, solution, initiative or architecture decision deviates from an approved enterprise guardrail, standard, reference architecture, solution baseline, interface rule, data rule, security expectation, runtime assumption or quality marker requirement.

An exception is not a silent waiver and not proof of compliance. It is a controlled architecture risk decision. The template must therefore make clear what is being deviated from, why the deviation is needed, what impact it creates, who owns the risk, how the risk is mitigated, how long the exception is valid, and when it must be reviewed again.

The following fields define the minimum content of an architecture exception:

| **Field**                  | **Purpose**                                                                                                 | **Required content**                                                                                                                                            |
|----------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exception ID               | Provides a unique reference for the exception.                                                              | Unique ID, version, status                                                                                                                                      |
| Exception title            | Provides a short understandable name.                                                                       | Short title describing the deviation                                                                                                                            |
| Requested by               | Identifies who requests the exception.                                                                      | Requesting role, team, product, solution or initiative                                                                                                          |
| Exception target           | Identifies what the exception applies to.                                                                   | Guardrail, standard, reference architecture, quality marker, interface rule, data rule, security rule, runtime rule, deployment assumption or solution baseline |
| Affected scope             | Clarifies where the exception has impact.                                                                   | Enterprise, solution, product, ART, product line, interface, data contract, security boundary, deployment environment or release baseline                       |
| Business reason            | Explains why the exception is needed.                                                                       | Customer constraint, mission need, delivery urgency, legacy dependency, contractual requirement, technology limitation or product-line reason                   |
| Architecture impact        | Describes the architectural consequence of the deviation.                                                   | Enterprise impact, solution impact, product impact, interface impact, data impact, security impact, platform impact or runtime impact                           |
| BAPO implications          | Shows whether the deviation affects business intent, architecture alignment, delivery process or ownership. | Business priority, architecture risk, required process change, affected owner, governance implication                                                           |
| Risk                       | Makes the risk explicit and reviewable.                                                                     | Security, safety, interoperability, maintainability, release, compliance, operational, integration or technical debt risk                                       |
| Alternatives considered    | Demonstrates that other options were evaluated.                                                             | Options considered, rejected alternatives, trade-offs, reason why standard alignment is not feasible                                                            |
| Mitigation                 | Defines how the risk will be controlled.                                                                    | Mitigation plan, compensating control, additional test, monitoring, migration path, temporary workaround                                                        |
| Owner                      | Assigns accountability for the exception.                                                                   | Exception owner, responsible architect, product owner, team, security owner, interface owner, data owner or platform owner                                      |
| Validity / expiration date | Prevents the exception from becoming permanent by default.                                                  | Review date, expiry date, release milestone, closure criterion or renewal condition                                                                             |
| Decision                   | Records the outcome of the review.                                                                          | Approved, rejected, conditionally approved, escalated, deferred or returned for rework                                                                          |
| Approval authority         | Identifies who made the decision.                                                                           | Responsible architect, Architecture Review Board, enterprise governance body, security authority or release authority                                           |
| Conditions                 | Defines additional requirements attached to the approval.                                                   | Required evidence, mitigation before release, additional review, migration before next baseline, monitoring requirement                                         |
| Evidence                   | Provides supporting material for the decision.                                                              | Review record, impact analysis, risk assessment, test evidence, security review, compatibility assessment, supporting documents                                 |
| Follow-up action           | Converts the exception into managed work or governance feedback.                                            | Backlog item, technical debt item, architecture runway item, guardrail update, release condition or portfolio action                                            |

The exception template should be completed with enough detail to allow the decision to be reviewed later without relying on informal knowledge. A reviewer should be able to understand what was approved, why it was approved, which risk was accepted, which mitigation was required, who owns the follow-up and when the exception expires.

Approved exceptions must remain visible until they are closed, expired or renewed. They should be linked to the relevant exception register, technical debt register, release-readiness record, product compatibility declaration, solution baseline or enterprise guardrail. An exception without an owner, mitigation and review date should not be considered governed.

Conditional approvals must state the conditions explicitly. These may include additional verification evidence, contract testing, security review, migration before a future release, mitigation before deployment or review at a defined milestone. If the conditions are not met, the exception should not be used as valid release evidence.

Repeated exceptions should be treated as architecture feedback. If several products or solutions request similar deviations, the issue may not be the individual product or solution. It may indicate that the enterprise guardrail is unclear, outdated, too restrictive, insufficiently supported by platform capabilities, or missing an accepted variant. In such cases, the exception should trigger guardrail review, architecture runway, technical debt reduction or portfolio-level improvement action.

## Release Compatibility Declaration Template

The Release Compatibility Declaration is one of the most important artifacts for independent product releases. It allows products to evolve independently while ensuring that they do not break the solution baselines in which they participate. The declaration makes explicit which product or solution release is being assessed, which baseline it supports, which interface and data versions are implemented, which security and deployment assumptions apply, and which evidence proves compatibility.

The declaration is primarily used for product releases that participate in a solution baseline. It may also be used at solution level to declare compatibility with enterprise guardrails, runtime assumptions, security baselines or deployment environments. In both cases, compatibility must be declared against a specific baseline. A release should not simply claim to be “compatible” in general.

A product release should not be accepted into a solution release baseline unless its compatibility declaration is complete, current, owned and verified with evidence.

| **Field**                 | **Purpose**                                                                 | **Required content**                                                                                                        |
|---------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Declaration name          | Provides a clear reference for the declaration.                             | Product or solution name, declaration title, identifier                                                                     |
| Declaration type          | Clarifies whether the declaration applies to a product or solution release. | Product release compatibility, solution release compatibility, enterprise baseline compatibility                            |
| Release version           | Identifies the exact release being assessed.                                | Product version, solution version, build identifier, release date, variant or configuration                                 |
| Supported baseline        | Defines the baseline against which compatibility is declared.               | Solution baseline, enterprise baseline, security baseline, platform baseline, deployment baseline                           |
| Baseline version          | Makes the compatibility target precise.                                     | Baseline name, version, release candidate, date, applicable scope                                                           |
| Interface versions        | Shows which externally visible interfaces are supported.                    | API versions, topic versions, event versions, schema versions, protocol versions, ICD references                            |
| Data model versions       | Shows which data structures and semantics are supported.                    | Data model versions, semantic model versions, metadata rules, classification rules, provenance assumptions                  |
| Security baseline         | Confirms alignment with required security assumptions.                      | Identity model, authentication, authorization, crypto, logging, audit, trust-zone compatibility, security exceptions        |
| Deployment configurations | Defines the environments in which the release is compatible.                | Supported environments, runtime assumptions, container/runtime versions, configuration profiles, edge/fog/cloud placement   |
| Tests passed              | Provides evidence that compatibility has been verified.                     | Contract tests, integration tests, schema validation, security tests, performance tests, deployment tests, regression tests |
| Verification evidence     | Links the declaration to reviewable proof.                                  | Test reports, review records, demo evidence, compatibility matrix, deployment evidence, security evidence                   |
| Known limitations         | Makes restrictions, unresolved issues and accepted gaps explicit.           | Restrictions, unsupported scenarios, open defects, degraded modes, residual risks, technical debt                           |
| Migration notes           | Explains how the release can be introduced safely.                          | Upgrade steps, downgrade steps, rollback procedure, data migration, compatibility transition, deprecation notes             |
| Exceptions                | Documents approved deviations from baselines or guardrails.                 | Exception ID, affected rule, risk, mitigation, expiry date, review date                                                     |
| Approval                  | Confirms accountable ownership and acceptance.                              | Product Owner, Product Architect, Solution Architect, Security Architect where required, approval date                      |
| Follow-up actions         | Captures remaining work after declaration.                                  | Backlog items, technical debt items, release conditions, mitigation actions, next review point                              |

The declaration should be created or updated whenever a release changes externally visible interfaces, data contracts, deployment assumptions, security behavior, runtime dependencies, compatibility rules or baseline participation. A stale declaration should not be accepted as release evidence.

For product releases, the Product Architect is responsible for the architectural correctness of the declaration. The Product Owner confirms release intent and product readiness. The Solution Architect uses the declaration to assess whether all participating product releases together form a coherent solution release baseline.

For solution releases, the Solution Architect is responsible for confirming that the solution baseline is complete and that all participating product releases are compatible with it. This includes interface compatibility, data compatibility, security consistency, deployment compatibility, integration evidence and unresolved risk acceptance.

A declaration should not be considered complete if it lacks baseline version, interface version, data model version, security assumption, deployment configuration, verification evidence, known limitations or accountable approval. Missing or incomplete compatibility evidence should be treated as a release-readiness risk, technical debt item, architecture exception or release blocker, depending on severity.
