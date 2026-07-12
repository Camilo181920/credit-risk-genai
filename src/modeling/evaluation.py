import pandas as pd

from src.modeling.metrics import (
    classification_metrics,
)


class ModelEvaluator:
    """
    Evalúa un modelo entrenado.
    """

    def evaluate(
        self,
        model,
        X_test,
        y_test,
    ):

        predictions = model.predict(
            X_test
        )

        probabilities = (
            model.predict_proba(
                X_test
            )[:, 1]
        )

        metrics = classification_metrics(
            y_test,
            predictions,
            probabilities,
        )

        return pd.Series(metrics)