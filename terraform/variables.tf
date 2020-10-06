variable client_id {}
variable client_secret {}


variable "resource_group" {
    default = "test-RG"
}

variable "location" {
    default = "eastus"
}

variable "net_interface" {
    default = "NIC1"
}

variable "vm_name" {
    default = "w01"
}

variable "pub_ip" {
    default = "myPublicIP"
}

variable  "vm_size" {
   default = "Standard_B1ms"
}

variable "os_disk_name" {
   default = "myosDisk"
}

variable "os_disk_type" {
    default = "Standard_LRS"

}


variable "image_publisher"{

    default = "Canonical"

}
variable "image_offer"{

    default = "UbuntuServer"
    
}
variable "image_sku"{

    default = "18.04-LTS"
    
}
variable "image_version"{
    default = "latest"
}