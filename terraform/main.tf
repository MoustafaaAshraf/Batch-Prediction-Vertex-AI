module "pubsub_trigger" {
    source = "./modules/pubsub_trigger"
    project_id = var.project_id
    region = var.region
    pubsub_topic_name = "${var.pubsub_topic_name}-${var.name_suffix}"
    cloud_run_name = "${var.cloud_run_name}-${var.name_suffix}"
    pubsub_service_account = var.pubsub_service_account
    pubsub_subscr_ack_deadline = var.pubsub_subscr_ack_deadline
    cloud_run_config = var.cloud_run_config
}

module "pubsub_scheduler" {
    for_each = var.cloud_schedulers_config
    source = "./modules/pubsub_scheduler"
    project_id = var.project_id
    region = var.region
    scheduler_name = "${each.value.name}-${var.name_suffix}"
    description = lookup(each.value, "description", null)
    schedule = each.value.schedule
    time_zone = lookup(each.value, "time_zone", "UTC")
    topic_id = module.pubsub_trigger.pubsub_id
    attributes = jsondecode(file(each.value.payload_file)).attributes
    data = base64encode(jsonencode(jsondecode(file(each.value.payload_file)).data))
    depends_on = [
        module.pubsub_trigger
    ]
}

resource "google_monitoring_notification_channel" "email" {
    for_each = toset(var.notification_emails)
    project = var.project_id
    display_name = "Email channel for ${each.value}"
    type = "email"
    labels = {
        email_address = each.key
    }
}

resource "google_monitoring_alert_policy" "fail_alert_policy" {
    display_name = "${var.alert_prefix}-fail-alert-policy-${var.name_suffix}"
    combiner = "OR"
    project = var.project_id

    conditions {
        display_name = "Alert Failure (${var.alert_prefix}-fail-alert-policy)"
        condition_threshold {
            filter = "resource.type = \"aiplatform.googleapis.com/PipelineJob\""
            duration = "0s"
            comparison = "COMPARISON_GT"
            threshold_value = 0.5
        }
    }

    notification_channels = concat(
        [for email in google_monitoring_notification_channel.email : email.name]
    )
}
