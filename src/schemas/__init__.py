from dataclasses import dataclass, field


@dataclass
class CreditAssessment:
    """
    Resultado de evaluación crediticia.

    Representa la salida del modelo
    y la información utilizada por
    el asistente GenAI.
    """

    probability: float

    risk_level: str

    prediction: int

    top_features: list[str] = field(
        default_factory=list
    )