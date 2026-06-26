package devsecops.artifact_integrity

deny[msg] {
  input.release_candidate == true
  not input.artifact.digest.exists
  not input.artifact.signature.exists
  msg := "DSCB-L1-REQ-011: Releasable artifacts require checksum, digest, or signature evidence."
}

deny[msg] {
  input.release_candidate == true
  input.artifact.digest.exists
  not input.artifact.digest.linked_to_artifact
  msg := "DSCB-L1-REQ-011: Artifact digest must be linked to the releasable artifact."
}
