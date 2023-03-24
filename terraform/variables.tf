variable "project_id" {
    description = "The ID of the Google Cloud project"
    default     = "batch-preds"
}

variable "region" {
    description = "The region in which to create the Google Cloud Storage bucket"
    default     = "europe-west2"
}

variable "pubsub_cloud_function_config" {
    description = "values for the cloud function"
}
