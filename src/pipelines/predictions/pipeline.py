from kfp.v2 import compiler, dsl
from src.components.model import save_txt
from src.components.bigquery import query_to_table

@dsl.pipeline(name='batch-preds-pipeline', description='Predictions Pipeline')
def prediction_pipeline():    
    
    # Component 1: Save dummy txt to GCS
    save_txt_op = query_to_table(
        query='',
        bq_client_project_id='',
        destination_project_id=''
    )
    
def compile():
    compiler.Compiler().compile(
        pipeline_func=prediction_pipeline,
        package_path='prediction.json'
    )
    
if __name__ == '__main__':
    compile()