terraform {
  required_providers {
    vault = {
      source = "hashicorp/vault"
      version = "3.15.0"
    }
  }
}

provider "vault" {
  auth_login {
    path = "auth/kubernetes/cluster-services-role"
  }
}
