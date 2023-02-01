terraform {
  required_providers {
    kubernetes = {
      source = "hashicorp/kubernetes"
      version = "2.11.0"
    }
  }
}

provider "kubernetes" {
  config_path    = "/home/iheb/.kube/config"
  config_context = "minikube"
}
resource "kubernetes_namespace" "namespace" {
  metadata {
    name = "nginx-app"
  }
}

resource "kubernetes_service" "nginx" {
  metadata {
    name = "nginx-service"
    namespace = "default"
  }

  spec {
    type = "NodePort"
    selector = {
      app = "nginx"
    }

    port {
      port = 80
      target_port = 80
      node_port = 30120
    }
  }
}


resource "kubernetes_deployment" "nginx_deployment" {
  metadata {
    name = "nginx-deployment"
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "nginx"
      }
    }
    template {
      metadata {
        labels = {
          app = "nginx"
        }
      }
      spec {
        container {
          image = "nginx"
          name  = "nginx"
        }
      }
    }
  }
}