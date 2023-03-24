resource "google_cloudfunctions_function" "pubsub_function" {
    project = var.project_id
    name = var.pubsub_cloud_function_name
    runtime = var.function_config.runtime
    region = var.region

    description = "Deployment of cloud function for pubsub"
    
    available_memory_mb = var.function_config.memory_requirements
    source_archive_bucket = google_storage_bucket.function_code_bucket.name
    source_archive_object = google_storage_bucket_object.cloud_function_code.name
    service_account_email = var.pubsub_cloud_function_service_account

    event_trigger {
        event_type = "providers/cloud.pubsub/eventTypes/topic.publish"
        resource = var.function_config.topic_name
        failure_policy {
            retry = var.function_config.retry_bool
        }
    }

    entry_point = var.function_config.entry_point
    environment_variables = lookup(var.function_config, "environment_variables", {})
    vpc_connector = var.vpc_connector
    vpc_connector_egress_settings = var.vpc_connector_egress_settings
}


