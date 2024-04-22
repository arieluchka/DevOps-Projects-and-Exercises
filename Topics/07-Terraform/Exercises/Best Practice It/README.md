# Best Practice It

When writing code, it is important to keep it readable and user friendly, so other co-workers and colleagues will easly understand it's purpose, and for future you to easily remember your thought process.

In this Exercise, you will receive a `main.tf` file that deploys resources to the Azure cloud.

The file you will receive, wont follow best practices and will be written very poorly. Your task is to understand and modify the file to follow Terraform best practice and imporve the readability of the file.

Review the terraform deployment from the `/bad-practice` folder, and re-write it to the `/best-practice`, following the best practice guidelines.


## Some Best Practice Examples:
### Resource Referencing
When deploying resources that are dependend on other resource attributes, **It's better referencing the other resource**, than explicitly hard coding the attribute value.

This way, if an attribute will change (a resource name/location/id), other resources that depend on it won't have to be re-writen.

Example:

❌(in both resources, the rg name is hard coded)

`main.tf`

```
resource "azurerm_resource_group" "server_resource" {
  name     = "rg1-name"
  location = "eastus"
}

resource "azurerm_virtual_network" "server_vnet" {
  name                = "vnet1-name"
  address_space       = ["10.0.0.0/16"]
  location            = "eastus"
  resource_group_name = "rg1-name"
}
```

✔️(in the vnet resource, the rg name is referenced)

`main.tf`

```
resource "azurerm_resource_group" "server_resource" {
  name     = "rg1-name"
  location = "eastus"
}

resource "azurerm_virtual_network" "server_vnet" {
  name                = "vnet1-name"
  address_space       = ["10.0.0.0/16"]
  location            = "eastus"
  resource_group_name = azurerm_resource_group.server_resource.name
}
```

---

### variable usage 
Variables are a great way to improve the readability and reusability of your code.

Creating a `variables.tf` file, and defining some of the attributes there, will make it easier to reuse the code in the future or test a deployment with different parameters, without modifying the main file.

❌ (if we want to test a new location, we need to go to each resource and manually edit it)

`main.tf` 
```
resource "azurerm_resource_group" "server_resource" {
  name     = "rg1-name"
  location = "eastus"
}

resource "azurerm_virtual_network" "server_vnet" {
  name                = "vnet1-name"
  address_space       = ["10.0.0.0/16"]
  location            = "eastus"
  resource_group_name = azurerm_resource_group.server_resource.name
}
```

✔️ (if we want to test a new location, we can run terraform apply with a new location variable, without modifying the main file)

`variables.tf`
```
variable "location" {
  type = string
  default = "eastus"
}
```

`main.tf` 
```
resource "azurerm_resource_group" "server_resource" {
  name     = "rg1-name"
  location = var.location
}

resource "azurerm_virtual_network" "server_vnet" {
  name                = "vnet1-name"
  address_space       = ["10.0.0.0/16"]
  location            = var.location
  resource_group_name = azurerm_resource_group.server_resource.name
}
```

### More Best Practices
- [Naming conventions](https://www.terraform-best-practices.com/naming)
- [Code structure](https://www.terraform-best-practices.com/code-structure)

---

