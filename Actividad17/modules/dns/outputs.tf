output "policy_json" {
  value       = local.policy_json
  description = "Firewall policy serialized as JSON"
}

output "rules_count" {
  value       = length(var.rules)
  description = "Number of firewall rules"
}