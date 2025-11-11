output "buckets" {
  value       = { for b in local.buckets : b.name => b }
  description = "Map of bucket name -> metadata"
}