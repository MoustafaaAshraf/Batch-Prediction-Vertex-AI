import os
from google.cloud import aiplatform

def run_pipeline():
    
    project_id = os.getenv('VERTEX_PROJECT_ID')
    location = os.getenv('VERTEX_LOCATION')
    pipeline_root = os.getenv('VERTEX_PIPELINE_ROOT')
    service_account = os.getenv('VERTEX_SA_EMAIL')
    
    aiplatform.init(project=project_id, location=location)
    
    pl = aiplatform.PipelineJob(
        display_name='batch-preds-pipeline',
        template_path='training.json',
        parameter_values={},
        pipeline_root=pipeline_root
    )
    
    pl.run(sync=True, service_account=service_account)
    
if __name__ == '__main__':
    run_pipeline()