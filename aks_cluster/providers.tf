terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.40"
    }
    tls = {
      source  = "hashicorp/tls"
      version = ">=3.1"
    }
  }
  required_version = ">= 1.2.0"
}

provider "azurerm" {
  features {}
}