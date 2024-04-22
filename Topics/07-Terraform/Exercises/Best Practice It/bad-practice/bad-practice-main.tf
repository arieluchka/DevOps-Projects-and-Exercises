terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "=3.0.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# Virtual Machine
resource "azurerm_linux_virtual_machine" "example_vm" {
  name                = "MyVM"
  resource_group_name = "MyResourceGroup"
  location            = "eastus"
  size                = "Standard_DS1_v2"
  admin_username      = "adminuser"
  network_interface_ids = [
    azurerm_network_interface.example_nic.id,
  ]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "20.04-LTS"
    version   = "latest"
  }
}

# Subnet
resource "azurerm_subnet" "example_subnet" {
  name                 = "MySubnet"
  resource_group_name  = "MyResourceGroup"
  virtual_network_name = "MyVNet"
  address_prefixes     = ["10.0.1.0/24"]
}

# Virtual Network
resource "azurerm_virtual_network" "example_vnet" {
  name                = "MyVNet"
  address_space       = ["10.0.0.0/16"]
  location            = "eastus"
  resource_group_name = "MyResourceGroup"
}


# Public IP
resource "azurerm_public_ip" "example_ip" {
  name                = "MyPublicIP"
  location            = "eastus"
  resource_group_name = "MyResourceGroup"
  allocation_method   = "Dynamic"
}

# Network Security Group
resource "azurerm_network_security_group" "example_nsg" {
  name                = "MyNSG"
  location            = "eastus"
  resource_group_name = "MyResourceGroup"
}

# Network Interface
resource "azurerm_network_interface" "example_nic" {
  name                = "MyNIC"
  location            = "eastus"
  resource_group_name = "MyResourceGroup"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.example_subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.example_ip.id
  }
}

# Resource Group
resource "azurerm_resource_group" "example" {
  name     = "MyResourceGroup"
  location = "eastus"
}

