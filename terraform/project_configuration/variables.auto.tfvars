project_id = "batch-preds"
region = "europe-west2"

pubsub_topic_name = "batch-preds_topic"
pubsub_subscr_ack_deadline = 600
pubsub_service_account = "terraform@batch_preds.iam.gserviceaccount.com"
cloud_run_name = "batch-preds-trigger"
name_suffix = "batch-preds"

prediction_pipeline_name = "batch-preds-pipeline"
metric_prefix = "batch-preds-metric"
alert_prefix = "batch-preds-alert"
notification_email = [
    "mosafehashf@gmail.com"
]

cloud_schedulers_config = {
    prediction = {
        name = "batch-preds-prediction-scheduler"
        description = "Scheduler for batch-preds prediction pipeline"
        schedule = "* * * * *"
        time_zone = "UTC"
        payload_file = "../src/pipelines/predictions/payloads/prediction.json"
    }
}


