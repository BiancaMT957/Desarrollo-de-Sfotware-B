locals {
  instances = [
    for i in range(var.instance_count) : {
      id  = "inst-${i}-${var.instance_type}"
      ip  = cidrhost(element(var.subnet_cidrs, i % length(var.subnet_cidrs)), 10 + i)
      meta = {
        instance_type = var.instance_type
        name          = "inst-${i}"
      }
    }
  ]
}