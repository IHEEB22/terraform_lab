output "deployment_name" {
  value = kubernetes_deployment.nginx_deployment.metadata[0].name
}
output "service_name" {
  value     = "hello"
  sensitive = true
}