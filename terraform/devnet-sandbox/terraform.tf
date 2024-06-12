# initialize terraform using 'terraform init'
# plan out what will happen using 'terraform plan'
# apply this terraform file using 'terraform apply -auto-approve'
# remove this config using 'terraform destroy' & confirm removing the config using 'yes'

# This will create Loopback800 the DevNet Sandbox using the Cisco IOS XE provider and the CLI resource 
# Learn more here: https://registry.terraform.io/providers/CiscoDevNet/iosxe/latest/docs/resources/cli

terraform {
  required_providers {
    iosxe = {
      source = "CiscoDevNet/iosxe"
      version = "0.5.5"
    }
  }
}

provider "iosxe" {
  url = "https://devnetsandboxiosxe.cisco.com"
  insecure = true
  username = "admin"
  password = "C1sco12345"
}

resource "iosxe_cli" "example" {
  cli = <<-EOT
  interface Loopback880
  description configured-via-restconf-cli
  EOT
}