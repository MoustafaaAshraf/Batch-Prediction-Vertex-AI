provider "google" {
    project     = "batch-preds"
    region      = "europe-west2"
    credentials = file("/Users/moustafa/Desktop/Repositories/GCP-keys/batch-pred/batch-preds-ea7c8c5b56c4.json")
}
