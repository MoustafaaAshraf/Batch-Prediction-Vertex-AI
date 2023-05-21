variable "project_id" {
    type = string
    description = "The project ID to deploy to"
}

variable "region" {
    type = string
    description = "The region to deploy to"
}       

variable "name_suffix" {
    type = string
    description = "The suffix to append to the names of the resources"
}

variable "prediction_pipeline_name" {
    type = string
    description = "The name of the prediction pipeline"
}

variable "metric_prefix" {
    type = string
    description = "The prefix to use for the metrics"
}

variable "alert_prefix" {
    type = string
    description = "The prefix to use for the alerts"
}

variable "notification_emails" {
    type = list(string)
    description = "The emails to send alerts to"
    default = [ ]
}

variable "notification_email" {
    type = list(string)
    description = "The emails to send alerts to"
    default = [ ]
}

variable "pubsub_topic_name" {
    type = string
    description = "The name of the Pub/Sub topic"
}

variable "pubsub_service_account" {
    type = string
    description = "The service account to use for the Pub/Sub topic"
}

variable "pubsub_subscr_ack_deadline" {
    type = number
    description = "The acknowledgement deadline for the Pub/Sub subscription"
}

variable "cloud_run_name" {
    type = string
    description = "The name of the Cloud Run service"
}

variable "cloud_run_config" {
    description = "The configuration for the Cloud Run service"
    type = object({
        image = string
        service_account = string
        command = list(string)
        args = list(string)
        env_vars = map(string)
        container_port = string
        vpc_connector = string
    })
    default = {
        args = [ "src.trigger.app:app", "--config=./src/trigger/config.py" ]
        command = [ "gunicorn" ]
        container_port = "8080"
        env_vars = {}
        image = "europe-west2-docker.pkg.dev/batch-preds/docker-repo/batch-prediction"
        service_account = "terraform@batch-preds.iam.gserviceaccount.com"
        vpc_connector = "cloud-functions-connector"
    }
}

variable "cloud_schedulers_config" {
    description = "The configuration for the Cloud Scheduler jobs"
    type = map(object({
        name = string
        description = string
        schedule = string
        time_zone = string
        payload_file = string
    }))
    default = {}
}