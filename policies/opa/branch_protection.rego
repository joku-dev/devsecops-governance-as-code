package devsecops.branch_protection

deny[msg] {
  input.repository.protected_branch == true
  input.repository.direct_push_allowed == true
  msg := "DSCB-L1-REQ-003: Direct modification of protected branches is prohibited."
}

deny[msg] {
  input.repository.protected_branch == true
  not input.repository.review_required
  msg := "DSCB-L1-REQ-003: Protected branch integration requires review."
}
