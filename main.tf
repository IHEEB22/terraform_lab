
resource "kubernetes_service" "nginx_service" {
  metadata {
    name      = var.service_name
    namespace = var.namespace
  }

  spec {
    type = "NodePort"
    selector = {
      app = var.app_name
    }

    port {
      port        = 80
      target_port = 80
      node_port   = 30120
    }
  }
}


resource "kubernetes_deployment" "nginx_deployment" {
  metadata {
    name = var.deployment_name
  }
  spec {
    replicas = 2
    selector {
      match_labels = {
        app = var.app_name
      }
    }
    template {
      metadata {
        labels = {
          app = var.app_name
        }
      }
      spec {
        container {
          image = "nginx"
          name  = var.container_name
        }
      }
    }
  }
}