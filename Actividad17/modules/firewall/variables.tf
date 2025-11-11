variable "rules" {
  description = "List of firewall rules (port, cidr, proto)"
  type = list(object({
    port = number
    cidr = string
    proto = string
  }))
  default = [
    { port = 22, cidr = "0.0.0.0/0", proto = "tcp" }
  ]

  validation {
    condition = alltrue([
      for r in var.rules : (
        r.port > 0 && r.port <= 65535 &&
        can(regex("^([0-9]{1,3}\\.){3}[0-9]{1,3}/(\\d|[12]\\d|3[0-2])$", r.cidr)) &&
        contains(["tcp", "udp", "icmp"], lower(r.proto))
      )
    ])
    error_message = "Each rule must have port 1-65535, a valid CIDR and proto in [tcp, udp, icmp]."
  }
}