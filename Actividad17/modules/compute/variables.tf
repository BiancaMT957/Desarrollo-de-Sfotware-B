variable "instance_count" {
  type        = number
  description = "Number of instances"
  default     = 1
  validation {
    condition     = var.instance_count > 0
    error_message = "instance_count must be greater than 0"
  }
}

variable "instance_type" {
  type        = string
  description = "Type of instance (simulated)"
  default     = "small"
}

variable "subnet_cidrs" {
  type        = list(string)
  description = "List of subnet CIDRs to place instances in (used to derive IPs locally)"
  default     = ["10.0.1.0/24"]
}