package devsecops.waiver_validity

deny[msg] {
  waiver := input.waivers[_]
  waiver.status == "approved"
  waiver.expired == true
  msg := sprintf("DSCB-GOV-REQ-005: Waiver %s is expired and must not be used.", [waiver.id])
}

deny[msg] {
  waiver := input.waivers[_]
  waiver.status == "approved"
  not waiver.risk_classification
  msg := sprintf("DSCB-GOV-REQ-005: Waiver %s requires risk classification.", [waiver.id])
}

deny[msg] {
  waiver := input.waivers[_]
  waiver.status == "approved"
  not waiver.compensating_controls
  msg := sprintf("DSCB-GOV-REQ-005: Waiver %s requires compensating controls.", [waiver.id])
}
