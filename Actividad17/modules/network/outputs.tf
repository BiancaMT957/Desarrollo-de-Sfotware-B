output "vpc_id" {
  value       = local.vpc.id
  description = "Simulated VPC id"
}

output "public_subnets" {
  value       = local.public_subnets
  description = "List of public subnets with id and cidr"
}

output "private_subnets" {
  value       = local.private_subnets
  description = "List of private subnets with id and cidr"
}