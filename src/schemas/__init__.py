from dataclasses import dataclass, field


@dataclass
class CreditAssessment:
    """
    Resultado de evaluación crediticia.

    Contiene la predicción del modelo,
    los factores principales de riesgo
    y la explicación SHAP.
    """

    probability: float

    risk_level: str

    prediction: int

    top_features: list[str] = field(
        default_factory=list
    )

    explanation: list[dict] = field(
        default_factory=list
    )