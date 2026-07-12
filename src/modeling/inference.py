from __future__ import annotations

import pandas as pd

from src.schemas import CreditAssessment


class CreditInference:
    """
    Servicio de inferencia del modelo crediticio.
    """

    def __init__(
        self,
        pipeline,
        threshold: float = 0.50,
    ):

        self.pipeline = pipeline
        self.threshold = threshold


    def predict(
        self,
        customer,
        top_features=None,
    ) -> CreditAssessment:
        """
        Predicción individual.
        """

        customer_df = pd.DataFrame(
            [customer]
        )


        probability = float(
            self.pipeline
            .predict_proba(
                customer_df
            )[0][1]
        )


        prediction = int(
            probability >= self.threshold
        )


        return CreditAssessment(

            probability=probability,

            risk_level=self._risk_level(
                probability
            ),

            prediction=prediction,

            top_features=(
                top_features
                if top_features
                else []
            ),
        )


    def _risk_level(
        self,
        probability,
    ):

        if probability >= 0.70:
            return "HIGH"

        if probability >= 0.40:
            return "MEDIUM"

        return "LOW"