package devsecops.sbom

deny[msg] {
  input.release_candidate == true
  not input.evidence.sbom.exists
  msg := "DSCB-L1-REQ-006: Release candidates require an SBOM."
}

deny[msg] {
  input.release_candidate == true
  input.evidence.sbom.exists
  not input.evidence.sbom.linked_to_artifact
  msg := "DSCB-L1-REQ-006: SBOM must be linked to the releasable artifact."
}
