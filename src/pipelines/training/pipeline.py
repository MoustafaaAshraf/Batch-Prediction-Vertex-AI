from kfp.v2 import compiler, dsl
from src.pipelines import generate_query
import pathlib
from google_cloud_pipeline_components.v1.bigquery import BigqueryQueryJobOp
from google_cloud_pipeline_components.experimental.custom_job.utils import create_custom_training_job_op_from_component
from src.components.model.train import train_model

@dsl.pipeline(name='batch-preds-pipeline', description='training Pipeline')
def training_pipeline():
    
    # queries_folder = pathlib.Path(__file__).parent / "queries"
    
    # ingest_query = generate_query(
    #     queries_folder / "training_query.sql",
    # )
    
    # query_op = BigqueryQueryJobOp(
    #     project='batch-preds-387415',
    #     location='us-central1',
    #     # query=ingest_query
    #     query='SELECT 1+2 AS Result'
    # )
    
    train_model()
    
    
    
def compile():
    compiler.Compiler().compile(
        pipeline_func=training_pipeline,
        package_path='training.json'
    )
    
if __name__ == '__main__':
    compile()