// variable project_id
variable "project_id" {
    type        = string
    description = "The project ID to deploy to"
}

// variable region
variable "region" {
    type        = string
    description = "The region to deploy to"
}       

// variable pubsub_topic_name
variable "pubsub_topic_name" {
    type        = string
    description = "The name of the Pub/Sub topic"
}

// variable pubsub_subscr_ack_deadline
variable "pubsub_subscr_ack_deadline" {
    type        = number
    description = "The ack deadline of the Pub/Sub subscription"
}

// variable pubsub_service_account
variable "pubsub_service_account" {
    type        = string
    description = "The service account of the Pub/Sub subscription"
}

// variable cloud_run_name
variable "cloud_run_name" {
    type        = string
    description = "The name of the Cloud Run service"
}

// variable cloud_run_config
variable "cloud_run_config" {
    type = object({
        image = string
        service_account = string
        command = list(string)
        args = list(string)
        env_vars = map(string)
        container_port = string
        vpc_connector = string
    })
    description = "The configuration of the Cloud Run service"
}