variable "vpc_cidr" {
  type        = string
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
  validation {
    condition     = can(regex("^([0-9]{1,3}\\.){3}[0-9]{1,3}/(\\d|[12]\\d|3[0-2])$", var.vpc_cidr))
    error_message = "vpc_cidr must be a valid IPv4 CIDR (e.g. 10.0.0.0/16)"
  }
}

variable "public_subnets" {
  type        = list(string)
  description = "List of public subnet CIDRs"
  default     = ["10.0.1.0/24"]
}

variable "private_subnets" {
  type        = list(string)
  description = "List of private subnet CIDRs"
  default     = ["10.0.2.0/24"]
}

variable "azs" {
  type        = list(string)
  description = "Availability zones (simulated)"
  default     = ["az1", "az2", "az3"]
}