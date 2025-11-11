locals {
  # Simulación de recursos de red basados en variables de entrada
  vpc = {
    cidr = var.vpc_cidr
    id   = "local-vpc-${replace(var.vpc_cidr, "/", "-")}"
  }

  public_subnets = [
    for i, cidr in var.public_subnets :
    {
      id   = "pub-${i}-${cidr}"
      cidr = cidr
      az   = element(var.azs, i % length(var.azs))
    }
  ]

  private_subnets = [
    for i, cidr in var.private_subnets :
    {
      id   = "priv-${i}-${cidr}"
      cidr = cidr
      az   = element(var.azs, i % length(var.azs))
    }
  ]
}