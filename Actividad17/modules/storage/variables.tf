variable "bucket_names" {
  type        = list(string)
  description = "List of bucket names"
  default     = ["app-data"]
  validation {
    condition     = length(var.bucket_names) > 0
    error_message = "At least one bucket name is required"
  }
}