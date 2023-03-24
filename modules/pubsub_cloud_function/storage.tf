locals {
  cf_code_path = "project_configurations/${var.project_id}/cloud_functions/${var.pubsub_cloud_function_name}"
}

resource "google_storage_bucket" "function_code_bucket" {
  project                     = var.project_id
  location                    = var.region
  name                        = "${var.project_id}-${var.pubsub_cloud_function_name}"
  uniform_bucket_level_access = true
  force_destroy               = true

  versioning {
    enabled = false
  }
}

data "archive_file" "cloud_function_zip" {
  type        = "zip"
  source_dir  = local.cf_code_path
  output_path = "project_configurations/${var.project_id}/cloud_functions/target/${var.project_id}-${var.pubsub_cloud_function_name}.zip"
}

resource "google_storage_bucket_object" "cloud_function_code" {
  name   = format("%s#%s.%s", "pipeline_pubsub_trigger", data.archive_file.cloud_function_zip.output_md5, "zip")
  bucket = google_storage_bucket.function_code_bucket.name
  source = data.archive_file.cloud_function_zip.output_path
}