from kfp.v2 import compiler, dsl
from src.components.model import save_txt

@dsl.pipeline(name='batch-preds-pipeline', description='Predictions Pipeline')
def prediction_pipeline():    
    
    # Component 2: Save dummy txt to GCS
    save_txt_op = save_txt()
    
def compile():
    compiler.Compiler().compile(
        pipeline_func=prediction_pipeline,
        package_path='prediction.json'
    )
    
if __name__ == '__main__':
    compile()