from __future__ import annotations

import pandas as pd
import shap

from src.explainability.feature_interpreter import (
    explain_feature,
)

class ShapService:
    """
    Servicio de explicabilidad usando SHAP.
    """


    def __init__(
        self,
        pipeline,
    ):

        self.pipeline = pipeline

        self.preprocessor = (
            pipeline.named_steps[
                "preprocessing"
            ]
        )

        self.model = (
            pipeline.named_steps[
                "model"
            ]
        )

        self.explainer = shap.TreeExplainer(
            self.model
        )


    def explain(
        self,
        customer,
        top_n: int = 5,
    ):
        """
        Obtiene variables más influyentes
        en la predicción.
        """

        customer_df = pd.DataFrame(
            [customer]
        )


        transformed = (
            self.preprocessor
            .transform(customer_df)
        )


        shap_values = (
            self.explainer
            .shap_values(
                transformed
            )
        )


        values = shap_values[0]


        feature_names = (
            self.preprocessor
            .get_feature_names_out()
        )


        explanation = pd.DataFrame(
            {
                "feature": feature_names,
                "business_feature": [
                    explain_feature(
                        feature
                    )
                    for feature in feature_names
                ],
                "impact": values,
            }
        )


        explanation["importance"] = (
            explanation["impact"]
            .abs()
        )


        return (
            explanation
            .sort_values(
                "importance",
                ascending=False,
            )
            .head(top_n)
            [
                [
                    "business_feature",
                    "impact",
                    "importance",
                ]
            ]
        )