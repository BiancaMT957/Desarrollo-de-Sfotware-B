output "instance_ids" {
  value       = [for i in local.instances : i.id]
  description = "Simulated instance ids"
}

output "instance_private_ips" {
  value       = [for i in local.instances : i.ip]
  description = "Simulated instance private IPs"
}