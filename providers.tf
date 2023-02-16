terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.11.0"
    }
  }
}

provider "kubernetes" {
  config_path    = var.config_file_path
  config_context = "minikube"
}
resource "kubernetes_namespace" "namespace" {
  metadata {
    name = "nginx-app"
  }
}
