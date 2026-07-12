from src.modeling.model_registry import load_pipeline

from src.modeling.inference import CreditInference

from src.explainability import ShapService

from src.services.customer_mapper import map_customer

class CreditService:
    """
    Servicio principal de evaluación crediticia.
    """


    def __init__(self):

        pipeline = load_pipeline()

        self.inference = CreditInference(
            pipeline
        )

        self.explainer = ShapService(
            pipeline
        )


    def evaluate(
        self,
        customer,
    ):
        """
        Evalúa un cliente y genera
        explicación del riesgo.
        """

        customer = map_customer(
            customer
        )


        explanation = (
            self.explainer
            .explain(customer)
        )


        top_features = list(
            dict.fromkeys(
                explanation["business_feature"]
                .tolist()
            )
        )

        shap_explanation = (
            explanation
            .to_dict(
                orient="records"
            )
        )

        assessment = (
            self.inference
            .predict(
                customer,
                top_features,
                shap_explanation,
            )
        )


        return assessment