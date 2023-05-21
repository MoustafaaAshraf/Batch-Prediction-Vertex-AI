from kfp.v2 import compiler, dsl
from src.pipelines import generate_query
# from src.components.model import save_txt
from src.components.bigquery import bq_query_to_table
import pathlib

@dsl.pipeline(name='batch-preds-pipeline', description='training Pipeline')
def training_pipeline():
    
    queries_folder = pathlib.Path(__file__).parent / "queries"
    
    ingest_query = generate_query(
        queries_folder / "training_query.sql",
    )
    
    # Component 1: Save dummy txt to GCS
    first_op = bq_query_to_table(
        query=ingest_query,
        bq_client_project_id='batch_pred',
        destination_project_id='batch_pred'
    )
    
    
    
def compile():
    compiler.Compiler().compile(
        pipeline_func=training_pipeline,
        package_path='training.json'
    )
    
if __name__ == '__main__':
    compile()