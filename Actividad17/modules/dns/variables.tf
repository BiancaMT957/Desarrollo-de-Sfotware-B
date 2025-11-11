variable "hosts" {
  description = "Map of hostname -> IP"
  type = map(string)
  default = {
    "app" = "10.0.1.10"
  }

  validation {
    condition = alltrue([
      for k, v in var.hosts : (
        can(regex("^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$", k)) &&
        can(regex("^([0-9]{1,3}\\.){3}[0-9]{1,3}$", v))
      )
    ])
    error_message = "Hostnames must be lowercase labels (RFC-like) and values must be IPv4 addresses."
  }
}