from sklearn.pipeline import Pipeline

from src.modeling.preprocessing import (
    build_preprocessor,
)


def build_pipeline(
    model,
    numeric_features,
    categorical_features,
):
    """
    Construye el pipeline completo.
    """

    preprocessor = build_preprocessor(
        numeric_features,
        categorical_features,
    )

    return Pipeline(
        steps=[
            (
                "preprocessing",
                preprocessor,
            ),
            (
                "model",
                model,
            ),
        ]
    )