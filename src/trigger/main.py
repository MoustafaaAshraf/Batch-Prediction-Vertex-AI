import argparse
import base64
import json
import os
import distutils.util
from typing import Optional, List

from loguru import logger
from google.cloud import aiplatform
from kfp.v2.google.client import AIPlatformClient

from src.trigger.utils import wait_pipeline_until_complete

def ps_handler(event, context) -> aiplatform.PipelineJob:
    
    event["data"] = base64.b64decode(event["data"]).decode("utf-8")
    event["data"] = json.loads(event["data"])
    
    return trigger_pipeline_from_payload(event)

def trigger_pipeline_from_payload(payload: dict, use_fallback: bool = True) -> aiplatform.PipelineJob:
    
    payload = convert_payload(payload)
    env = get_env()
    
    return trigger_pipeline(
        project_id=env['project_id'],
        location=env['location'],
        template_path=payload["attributes"]["template_path"],
        parameter_values=payload["data"],
        pipeline_root=env["pipeline_root"],
        service_account=env["service_account"],
        network=env["network"],
        enable_caching=payload["attributes"]["enable_caching"],
        mode=env["mode"],
        use_fallback=use_fallback
    )
    
def trigger_pipeline(
    project_id: str,
    location: str,
    template_path: str,
    parameter_values: dict,
    pipeline_root: str,
    service_account: str,
    network: str,
    enable_caching: bool,
    mode: str,
    use_fallback: bool = True
) -> aiplatform.PipelineJob:
    
    parameter_values.pop('project_id', None)
    parameter_values.pop('project_location', None)
    
    pipeline_job = aiplatform.PipelineJob(
        display_name=f"pipeline-job-{project_id}",
        template_path=template_path,
        pipeline_root=pipeline_root,
        parameter_values=parameter_values,
        enable_caching=False,
        project=project_id,
        # project_id='batch-preds',
        location=location,
        # service_account=service_account,
        # network=network,
    )
    
    pipeline_job.run(sync=True)
    
    job_id = pipeline_job.resource_name
    logger.info(f"Triggered pipeline with job_id: {job_id}")
    
    if mode == "run":
        wait_pipeline_until_complete(job_id)
        
    return None
    
def convert_payload(payload: dict) -> dict:
    """Converts the payload to the desired format
    
    Args:
        payload (dict): Payload from Pub/Sub message
    
    Returns:
        dict: Payload in desired format
    """
    # Make copy to not edit the original payload
    payload = payload.copy()
    
    # if missing, set to empty dict
    payload["data"] = payload.get("data", {})
    
    # if enable_caching is not None, convert to bool from str
    if ("enable_caching" in payload["attributes"] and payload["attributes"]["enable_caching"] is not None):
        payload["attributes"]["enable_caching"] = distutils.util.strtobool(payload["attributes"]["enable_caching"])
        
    else:
        payload["attributes"]["enable_caching"] = None
        
    # if PIPELINE_FILES_GCS_PATH is set, overwrite the one in payload
    env_value = os.environ.get("PIPELINE_FILES_GCS_PATH")
    if env_value is not None:
        payload["data"]["pipeline_files_gcs_path"] = env_value
        
    # if TEMPLATE_BASE_PATH is set, overwrite the one in payload
    env_value = os.environ.get("TEMPLATE_BASE_PATH")
    if env_value is not None:
        path = f"{env_value}/{payload['attributes']['template_path']}"
        payload["data"]["template_path"] = path
        
    # if MODEL_FILE_PATH is set, overwrite the one in payload
    env_value = os.environ.get("MODEL_FILE_PATH")
    if env_value and "model_file" in payload["data"]:
        payload["data"]["template_path"] = env_value
        
    return payload
    
def get_env() -> dict:
    """Returns the environment variables
    
    Returns:
        dict: Environment variables
    """
    project_id = os.environ.get("VERTEX_PROJECT_ID")
    location = os.environ.get("VERTEX_LOCATION")
    pipeline_root = os.environ.get("VERTEX_PIPELINE_ROOT")
    service_account = os.environ.get("VERTEX_SA_EMAIL")
    encryption_spec_key_name = os.environ.get("VERTEX_ENCRYPTION_SPEC_KEY_NAME") or None
    network = os.environ.get("VERTEX_NETWORK") or None
    mode = os.environ.get("VERTEX_TRIGGER_MODE") or None
    
    return {
        "project_id": project_id,
        "location": location,
        "pipeline_root": pipeline_root,
        "service_account": service_account,
        "encryption_spec_key_name": encryption_spec_key_name,
        "network": network,
        "mode": mode
    }
    
def get_args(args: List[str] = None) -> argparse.Namespace:
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload", type=str, help="Path to payload json file")
    return parser.parse_args(args)
    
def sandbox_run() -> aiplatform.PipelineJob:
    
    args = get_args()
    
    with open(args.payload, "r") as f:
        payload = json.load(f)
        
    return trigger_pipeline_from_payload(payload)

if __name__ == "__main__":
    sandbox_run()