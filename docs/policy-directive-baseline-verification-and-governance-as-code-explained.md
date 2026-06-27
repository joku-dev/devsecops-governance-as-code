# Policy, Directive, Baseline, Verification und Governance as Code

## Zweck dieses Dokuments

Dieses Dokument erklärt den fachlichen und operativen Zusammenhang zwischen:

- **Policy**
- **Directive**
- **Baseline / Standard**
- **Anforderungen**
- **Verifikationsmethoden**
- **Governance-Ausführung als Code**

Es dient als Orientierungsdokument für Governance Owner, Plattform-Verantwortliche, Security Engineers, Auditoren und anbindende Application-Repositories.

## Kurzfassung

Die drei wichtigsten Dokumentebenen haben unterschiedliche Rollen:

1. **Policy** sagt, **was verbindlich ist und wer verantwortlich ist**.
2. **Directive** sagt, **wie diese Verbindlichkeit organisatorisch und operativ ausgeführt werden muss**.
3. **Baseline / Standards** sagen, **welche konkreten Anforderungen technisch und fachlich erfüllt werden müssen**.

Governance as Code ist dann die ausführbare Umsetzung ausgewählter Teile dieser Anforderungen in:

- strukturierte Daten,
- Traceability,
- Evidence-Modelle,
- Policy-as-Code,
- CI/CD-Gates,
- maschinenlesbare Compliance-Evidence.

## Die Dokumentenhierarchie im Governance-Stack

### 1. Policy

Die Policy ist die oberste normative Ebene in diesem Modell.

Sie beantwortet vor allem die Fragen:

- Was ist verpflichtend?
- Für wen gilt es?
- Welche Grundprinzipien gelten?
- Wer trägt die Verantwortung?

Die Policy ist also **nicht** das operative Arbeitsdokument für die tägliche Pipeline-Entscheidung, sondern das Dokument, das die grundlegende Verbindlichkeit herstellt.

Im Repository liegt die aktuelle Arbeitsfassung hier:

- `docs/policy/devsecops-policy.md`

### 2. Directive

Die Directive ist die operative Governance-Ebene unterhalb der Policy.

Sie beantwortet vor allem die Fragen:

- Wie wird die Policy praktisch ausgeführt?
- Wer entscheidet bei Abweichungen?
- Wie funktioniert Waiver- und Eskalationsmanagement?
- Wie wird Compliance überwacht und berichtet?

Die Directive übersetzt also den normativen Willen der Policy in bindende organisatorische und prozedurale Ausführung.

Im Repository liegt die aktuelle Arbeitsfassung hier:

- `docs/directive/devsecops-directive.md`

### 3. Baseline / Standards

Die Baseline beziehungsweise die Standards sind die konkrete normative Anforderungsebene.

Sie beantworten vor allem die Fragen:

- Welche Controls müssen auf L1, L2, L3 oder GOV erfüllt werden?
- Welche Plattformfähigkeiten werden dafür benötigt?
- Welche technischen oder prozessualen Nachweise werden erwartet?

In diesem Repository sind die importierten Ursprungsdokumente derzeit:

- `docs/source-documents/DevSecOps-Control-Baseline-Standard_aligned_with_Platform_Levels.docx`
- `docs/source-documents/DevSecOps-Platform-Reference-Architecture-Standard_aligned_with_Control_Baseline.docx`

Zusätzlich liegt die strukturierte Repräsentation der Anforderungen in YAML-Dateien, insbesondere unter:

- `controls/`
- `platform/`
- `traceability/`
- `evidence/`

## Der fachliche Zusammenhang zwischen Policy, Directive und Baseline

Die Beziehung lässt sich so ausdrücken:

- **Policy** legitimiert und verpflichtet.
- **Directive** operationalisiert und regelt die Governance-Ausführung.
- **Baseline** konkretisiert die zu erfüllenden Anforderungen.

Oder anders formuliert:

- Die **Policy** sagt: _DevSecOps ist verpflichtend._
- Die **Directive** sagt: _So wird diese Verpflichtung gesteuert, überwacht und bei Abweichungen behandelt._
- Die **Baseline** sagt: _Diese konkreten Controls und Anforderungen müssen erfüllt oder nachweisbar behandelt werden._

## Der Zusammenhang zwischen Dokumenten und Anforderungen

Nicht jede Anforderung steht direkt in der Policy oder Directive selbst.

Die typische Struktur ist:

1. **Policy** definiert die Pflicht und Verantwortlichkeit.
2. **Directive** definiert die Ausführungs- und Entscheidungslogik.
3. **Standards/Baseline** enthalten die einzelnen technischen und organisatorischen Anforderungen.
4. **Structured YAML** modelliert diese Anforderungen in maschinenverarbeitbarer Form.

Die Zuordnung der Governance-Dokumente zu Controls wird im Repository explizit modelliert, insbesondere in:

- `documents/governance-documents.yaml`
- `traceability/document-to-control.yaml`

Dadurch ist nachvollziehbar:

- welches Dokument welche Anforderungen autorisiert,
- welche Controls auf welche Dokumente zurückgehen,
- welche Baseline-Level durch welche Governance-Artefakte gestützt werden.

## Der Zusammenhang zwischen Anforderungen und Verifikationsmethoden

Eine Anforderung allein reicht operativ nicht aus. Sie muss auch verifizierbar sein.

Deshalb braucht jede relevante Anforderung eine oder mehrere Verifikationsmethoden.

Typische Verifikationsmethoden sind:

- Dokumentenprüfung
- Konfigurationsprüfung
- Pipeline-Prüfung
- Repository-Prüfung
- Policy-as-Code-Auswertung
- Evidence-Prüfung gegen strukturierte Kriterien
- manuelle Governance- oder Auditfreigabe

Im Governance-as-Code-Modell bedeutet das:

- Eine Anforderung wird nicht nur textuell beschrieben,
- sondern idealerweise mit erwarteter Evidence und möglicher Prüfmechanik verknüpft.

Diese Verknüpfung wird im Repository über Evidence-Definitionen und Traceability modelliert, insbesondere in:

- `evidence/evidence-types.yaml`
- `traceability/`
- `controls/`

## Der Zusammenhang zwischen Anforderungen und Evidence

Eine Verifikationsmethode braucht in der Regel einen Nachweis.

Dieser Nachweis ist die **Evidence**.

Beispiele:

- SBOM-Datei
- Vulnerability-Scan-Report
- Branch-Protection-Konfiguration
- Review-Historie
- Build-Logs
- Pipeline-Execution-Logs
- Artifact-Digest
- Signatur-Nachweis
- Approval-Records

Im Repository wird modelliert:

- welche Evidence-Typen existieren,
- wer sie erzeugt,
- in welchem Format sie vorliegen,
- welche Anforderungen sie unterstützen.

Das ist wichtig, weil Governance as Code nicht nur Regeln ausführt, sondern auch festlegt, **welcher Nachweis für welche Anforderung gilt**.

## Der Zusammenhang zwischen Verifikationsmethode und Governance-Ausführung als Code

Governance-Ausführung als Code bedeutet nicht einfach nur „ein paar Regeln in einer Pipeline“.

Vielmehr umfasst sie mehrere Ebenen:

1. **Strukturierte Modellierung**
   - Anforderungen, Dokumente, Evidence und Traceability liegen maschinenlesbar vor.

2. **Validierung**
   - Schemas und Konsistenzprüfungen stellen sicher, dass das Governance-Modell intern korrekt ist.

3. **Ausführbare Regeln**
   - ausgewählte Anforderungen werden als Policy-as-Code oder Gate-Logik implementiert.

4. **Evidence-Erzeugung**
   - Pipelines und Plattformen erzeugen maschinenlesbare Nachweise.

5. **Evidence-Auswertung**
   - die erzeugte Evidence wird gegen die Governance-Anforderungen geprüft.

6. **Compliance-Ergebnis**
   - das Ergebnis wird als maschinenlesbare Governance-Evidence gespeichert.

## Was Governance as Code in diesem Repository konkret bedeutet

In diesem Repository wird Governance as Code durch mehrere Bausteine umgesetzt:

### 1. Strukturierte Governance-Daten

Zum Beispiel:

- `controls/`
- `documents/`
- `platform/`
- `traceability/`
- `evidence/`
- `waivers/`

### 2. Validierung der Governance-Struktur

Zum Beispiel:

- `scripts/validate_governance_repo.py`
- Schemas unter `schemas/`
- Tests unter `tests/`

### 3. Policy-as-Code

Zum Beispiel:

- `policies/opa/`

Hier werden ausgewählte objektiv prüfbare Anforderungen in ausführbare Rego-Regeln übersetzt.

### 4. Generierung von Review- und Audit-Artefakten

Zum Beispiel:

- Traceability-Matrizen
- Document-Control-Matrix
- Open-Gap-Reports
- gerenderte Policy- und Directive-Dokumente

### 5. Wiederverwendbare Governance-Ausführung in CI/CD

Zum Beispiel:

- `.github/workflows/devsecops-baseline-reusable.yml`

Dieser wiederverwendbare Workflow ermöglicht es, dass andere Repositories zentral definierte Governance-Logik auf ihre eigene Pipeline-Evidence anwenden.

## Wie der operative Fluss aussieht

Der operative Zusammenhang lässt sich in einer Kette darstellen:

1. **Policy** macht DevSecOps verbindlich.
2. **Directive** definiert Governance, Rollen, Waiver und Reporting.
3. **Baseline/Standards** definieren konkrete Anforderungen.
4. **Structured Controls und Evidence-Modelle** übersetzen diese Anforderungen in maschinenlesbare Form.
5. **Application-Repositories und Plattformen** erzeugen Evidence.
6. **Governance-as-Code-Workflows und Policy-as-Code-Regeln** prüfen die Evidence.
7. **Maschinenlesbare Governance-Ergebnisse** dokumentieren, ob Anforderungen erfüllt, verletzt oder per Waiver behandelt wurden.

## Was nicht alles automatisiert werden kann

Ein wichtiger Grundsatz dieses Repositories ist:

> Nicht jede Governance-Anforderung sollte oder kann als Code ausgeführt werden.

Es gibt drei verschiedene Typen von Anforderungen:

### 1. Rein normative Anforderungen

Beispiel:

- ein Governance Board muss eingerichtet werden
- Verantwortlichkeiten müssen formal zugewiesen sein

Diese Anforderungen sind wichtig, aber oft nicht vollständig technisch prüfbar.

### 2. Evidence-basierte Anforderungen

Beispiel:

- ein SBOM muss vorliegen
- ein Vulnerability-Scan muss nachweisbar sein

Diese Anforderungen sind gut für Governance as Code geeignet.

### 3. Technische Gate-Anforderungen

Beispiel:

- Artifact-Digest muss vorhanden sein
- Severity-Threshold darf nicht überschritten sein
- Signatur muss vorhanden sein

Diese Anforderungen lassen sich besonders gut als automatisierte Gates ausführen.

## Warum dieser Zusammenhang wichtig ist

Ohne diese Trennung entstehen typische Probleme:

- Controls sind da, aber niemand weiß, welches Dokument sie autorisiert
- Evidence wird erzeugt, aber niemand weiß, gegen welche Anforderung sie geprüft wird
- Pipeline-Gates laufen, aber sie sind nicht sauber auf die Governance-Dokumente zurückführbar
- Auditoren sehen technische Checks, aber nicht die normative Grundlage

Dieses Repository adressiert genau diese Lücke:

- **Policy** liefert die normative Legitimation
- **Directive** liefert die Governance-Ausführung und Entscheidungslogik
- **Baseline** liefert die konkret zu verifizierenden Anforderungen
- **Evidence** liefert den Nachweis
- **Governance as Code** liefert die ausführbare Prüfung

## Praktische Lesart für unterschiedliche Zielgruppen

### Für Management

Die Policy ist die verbindliche Aussage, dass DevSecOps eingehalten werden muss.

### Für Governance und Compliance

Die Directive regelt, wie die Einhaltung organisatorisch gesteuert, berichtet und bei Abweichungen behandelt wird.

### Für Plattform- und Security-Teams

Die Baseline enthält die konkreten Anforderungen, die technisch oder prozessual umgesetzt werden müssen.

### Für CI/CD und Application-Repositories

Governance as Code ist die operative Ausführung ausgewählter Anforderungen gegen maschinenlesbare Evidence.

## Repository-Dateien mit zentraler Bedeutung

Für diesen Zusammenhang sind insbesondere diese Dateien wichtig:

- `docs/policy/devsecops-policy.md`
- `docs/directive/devsecops-directive.md`
- `docs/source-documents/DevSecOps-Control-Baseline-Standard_aligned_with_Platform_Levels.docx`
- `docs/source-documents/DevSecOps-Platform-Reference-Architecture-Standard_aligned_with_Control_Baseline.docx`
- `documents/governance-documents.yaml`
- `traceability/document-to-control.yaml`
- `evidence/evidence-types.yaml`
- `docs/source-of-truth.md`
- `docs/governance-document-hierarchy.md`
- `.github/workflows/devsecops-baseline-reusable.yml`

## Kernaussage

Der Gesamtzusammenhang lautet:

> Die Policy macht DevSecOps verbindlich, die Directive regelt die bindende Ausführung, die Baseline definiert die konkreten Anforderungen, die Verifikationsmethoden bestimmen, wie diese Anforderungen geprüft werden, und Governance as Code führt ausgewählte Teile dieser Prüfung automatisiert auf Basis maschinenlesbarer Evidence aus.
