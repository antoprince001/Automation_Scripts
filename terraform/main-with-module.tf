terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.43.0"
    }
  }
}

provider "azurerm" {
    features {}
    skip_provider_registration = true
}

resource "azurerm_resource_group" "rg" {
    name = "812-3caf6473-create-a-private-module-registry-in-t" 
    location = "West US"
}

module "securestorage" {
  source  = "app.terraform.io/aztflearner/securestorage/azurerm"
  version = "1.0.0"
  resource_group_name = azurerm_resource_group.rg.name
  location = azurerm_resource_group.rg.location
  environment = "Production"
  storage_account_name = "tfsaprd871"
  
}
