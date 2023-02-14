
variable "aks_location" {
}
variable "aks_resource_group_name" {
}
variable "aks_prefix" {
}

variable "aks_agents_size" {
}
variable "aks_agents_pool_name" {
}

variable "rbac_aad" {
  type    = bool
  default = false
}
variable "role_based_access_control_enabled" {
  type    = bool
  default = true
}