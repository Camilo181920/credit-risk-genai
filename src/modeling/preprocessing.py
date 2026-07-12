from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler


def build_preprocessor(
    numeric_features,
    categorical_features,
):
    """
    Construye el preprocesador del pipeline.
    """

    numeric_pipeline = Pipeline(
        steps=[
            (
                "scaler",
                StandardScaler(),
            )
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            (
                "encoder",
                OneHotEncoder(
                    handle_unknown="ignore"
                ),
            )
        ]
    )

    return ColumnTransformer(
        transformers=[
            (
                "numeric",
                numeric_pipeline,
                numeric_features,
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_features,
            ),
        ]
    )