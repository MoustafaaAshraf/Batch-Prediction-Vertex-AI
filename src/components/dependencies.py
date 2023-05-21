import os

# Required images for components + Vertex training

PYTHON = "python:3.9"
PIPELINE_IMAGE_NAME = os.getenv("PIPELINE_IMAGE_NAME")

# Required packages and versions for components (ensure that these are in sync with pyproject.toml)

# Google SDK specific
GOOGLE_CLOUD_BIGQUERY = "google-cloud-bigquery==3.10.0"
GOOGLE_CLOUD_STORAGE = "google-cloud-storage==2.9.0"
GOOGLE_CLOUD_AIPLATFORM = "google-cloud-aiplatform==1.25.0"

# Miscellaneous
LOGURU = "loguru==0.6.0"

# Data science
PANDAS = "pandas==2.0.1"
SCIKIT_LEARN = "scikit-learn==1.2.2"
