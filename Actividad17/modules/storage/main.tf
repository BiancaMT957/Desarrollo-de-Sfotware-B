locals {
  buckets = [
    for name in var.bucket_names : {
      name = name
      arn  = "arn:local:storage::${name}"
    }
  ]
}