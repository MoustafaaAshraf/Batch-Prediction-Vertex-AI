variable "source_code_bucket" {
  type = string
  description = "(Required) Name for the Google Cloud Storage bucket where the source code will be stored"
  default = null
}

variable "output_path" {
  type = string
  description = "(Required) Output location of the cloud function"
  default = null
}

variable "source_dir" { 
  type = string
  description = "(Required) Directory containing main.py and requirements.txt"
  default = null
}

variable "pipeline_root" {
  type = string
  description = "(Required) Pipeline root"
  default = null
}

variable "environment_service_account" {
  type = string
  description = "(Optional) Environment service account"
  default = null
}

variable "vpc_connector" {
  type = string
  description = "(Required) VPC connector"
  default = null
}

variable "vpc_connector_egress_settings" {
  type = string
  description = "(Required) VPC connector egress settings"
  default = "ALL_TRAFFIC"
}

variable "region" {
  type = string
  default = "europe-west2"
  description = "(Optional) The region in which to create the Google Cloud Storage bucket"
}

variable "project_id" {
  type = string
  default = "batch-preds"
  description = "(Optional) The ID of the Google Cloud project"
}

variable "pubsub_cloud_function_name" {
  type = string
  description = "(Optional) Name of the cloud function"
}

variable "function_config" {
    type = object({
        runtime = string
        memory_requirements = number
        entry_point = string
        topic_name = string
        retry_bool = bool
        environment_variables = map(string)
    })
    description = "(Required) Cloud function configuration"
}

variable "pubsub_cloud_function_service_account" {
    type = string
    description = "(Required) Service account configuration"
}
