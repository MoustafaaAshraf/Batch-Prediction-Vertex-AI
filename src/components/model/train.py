from pathlib import Path

from kfp.v2.dsl import Dataset, Input, Model, Output, component

from src.components.dependencies import JOBLIB, LOGURU, PANDAS, PYTHON, SCIKIT_LEARN


@component(
    base_image=PYTHON,
    packages_to_install=[LOGURU, SCIKIT_LEARN, PANDAS, JOBLIB],
    output_component_file=str(Path(__file__).with_suffix(".yaml")),
)
def train_model(
    training_data: Input[Dataset],
    target_column: str,
    model_params: dict,
    model: Output[Model],
) -> None:
    """_summary_

    Args:
        training_data (Input[Dataset]): _description_
        target_column (str): _description_
        model_params (dict): _description_
        model (Output[Model]): _description_
    """
    import joblib
    import pandas as pd
    from sklearn.tree import DecisionTreeClassifier

    df_train = pd.read_csv(training_data.path)
    y = df_train.pop(target_column)

    dtc = DecisionTreeClassifier(**model_params)
    dtc.fit(X=df_train, y=y)

    model_path = model.uri + "/model.joblib"
    joblib.dump(dtc, model_path)
