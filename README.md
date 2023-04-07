# GCP Batch Prediction Infrastructure with Terraform, Vertex AI, Artifact Registry, Kubeflow, and PubSub

This repository contains the code to set up a batch prediction infrastructure on Google Cloud Platform (GCP) using Terraform. The infrastructure includes Cloud Scheduler, Vertex AI, Artifact Registry, Kubeflow, and PubSub. The project leverages GCP Artifact Registry to run Kubeflow pipeline components on custom images built locally and uses Poetry for package management.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set up GCP and Service Account](#2-set-up-gcp-and-service-account)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Build and Push Custom Images](#4-build-and-push-custom-images)
  - [5. Initialize Terraform and Deploy Infrastructure](#5-initialize-terraform-and-deploy-infrastructure)
  - [6. Deploy the Kubeflow Pipeline](#6-deploy-the-kubeflow-pipeline)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automates the creation of GCP resources for batch prediction using Terraform
- Sets up a Vertex AI pipeline that processes sample data upon PubSub trigger
- Utilizes GCP Artifact Registry for running Kubeflow pipeline components on custom images
- Employs Poetry for package management

## Requirements

- GCP Account with Billing enabled
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed and configured
- [Terraform](https://www.terraform.io/downloads.html) v0.13 or higher
- [Docker](https://docs.docker.com/get-docker/) installed
- [Poetry](https://python-poetry.org/docs/#installation) installed
- [Kubeflow Pipelines SDK](https://www.kubeflow.org/docs/components/pipelines/sdk/install-sdk/) v1.8.0 or higher

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine.

```sh
git clone https://github.com/yourusername/gcp-batch-prediction-infrastructure.git
cd gcp-batch-prediction-infrastructure

### 2. Set up GCP and Service Account

Ensure you have a GCP account with billing enabled. Create a new GCP project or select an existing one.

```sh
gcloud projects create PROJECT_ID
gcloud config set project PROJECT_ID

Create a service account with the necessary roles and download the JSON key:

```sh
gcloud iam service-accounts create terraform --display-name "Terraform Service Account"
gcloud projects add-iam-policy-binding PROJECT_ID --member "serviceAccount:terraform@PROJECT_ID.iam.gserviceaccount.com" --role "roles/owner"
gcloud iam service-accounts keys create terraform-key.json --iam-account terraform@PROJECT_ID.iam.gserviceaccount.com


### 3. Install Dependencies

Install the Python dependencies using Poetry:

```sh
poetry install

### 4. Build and Push Custom Images

Log in to Google Container Registry:

```sh
gcloud auth configure-docker

Build and push custom images to GCP Artifact Registry:

docker build -t eu.gcr.io/PROJECT_ID/YOUR_IMAGE_NAME:YOUR_TAG -f Dockerfile .
docker push eu.gcr.io/PROJECT_ID/YOUR_IMAGE_NAME:YOUR_TAG
