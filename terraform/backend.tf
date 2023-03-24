terraform {
  backend "gcs" {
    bucket = "terraform_backend_tefa"
    prefix = "terraform/state"
  }
}
