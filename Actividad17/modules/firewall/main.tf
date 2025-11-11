locals {
  # canonical policy structure
  policy_object = {
    version = "2025-1"
    rules   = var.rules
  }

  policy_json = jsonencode(local.policy_object)
}