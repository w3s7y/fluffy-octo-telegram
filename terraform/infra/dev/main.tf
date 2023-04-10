terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.61.0"
    }
  }
}

provider "aws" {}

module "vpc" {
  source         = "../../modules/vpc"
  vpc_cidr_block = "172.0.0.0/8"
}

module "eks" {
  source = "../../modules/eks"
}

module "rds" {
  source = "../../modules/rds"
}
