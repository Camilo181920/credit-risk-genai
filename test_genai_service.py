from src.services import GenAIService
from src.schemas import CreditAssessment


assessment = CreditAssessment(

    probability=0.7082,

    risk_level="HIGH",

    prediction=1,

    top_features=[

        "Nivel de ahorro del cliente",

        "Otros compromisos financieros",

        "Estado de cuenta corriente",

        "Relación cuota / ingreso",

    ]

)


service = GenAIService()


report = service.generate_credit_report(
    assessment
)


print(report)