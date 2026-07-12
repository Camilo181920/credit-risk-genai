from src.genai import generate_report


class GenAIService:
    """
    Servicio para generar reportes
    crediticios usando IA Generativa.
    """


    def generate_credit_report(
        self,
        assessment,
    ):

        return generate_report(
            assessment
        )