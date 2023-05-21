from kfp.v2.dsl import component
from src.components.dependencies import GOOGLE_CLOUD_STORAGE

@component(base_image='python:3.8', packages_to_install=["google-cloud-storage"])
def save_txt():
    
    from google.cloud import storage
    from datetime import datetime

    