from src.modeling.catalog import available_models
from src.modeling.trainer import ModelTrainer


def train_model(
    model,
    numeric_features,
    categorical_features,
    X_train,
    y_train,
):
    """
    Entrena un modelo usando el pipeline estándar.
    """

    trainer = ModelTrainer(
        model,
        numeric_features,
        categorical_features,
    )

    pipeline = trainer.fit(
        X_train,
        y_train,
    )

    return pipeline


__all__ = [
    "train_model",
    "available_models",
]