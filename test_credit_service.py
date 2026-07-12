from src.services.credit_service import CreditService


customer = {

    "status": "A11",

    "loan_duration_months": 24,

    "credit_history_status": "A32",

    "purpose": "A43",

    "loan_amount": 5000,

    "savings": "A61",

    "employment_duration": "A73",

    "installment_ratio": 2,

    "personal_status_sex": "A93",

    "other_debtors": "A101",

    "present_residence": 4,

    "property": "A121",

    "customer_age": 35,

    "other_installment_plans": "A143",

    "housing": "A152",

    "number_credits": 1,

    "job": "A173",

    "people_liable": 1,

    "telephone": "A192",

    "foreign_worker": "A201",

}


service = CreditService()


result = service.evaluate(
    customer
)


print(result)

print()

print(
    "Risk:",
    result.risk_level
)

print(
    "Probability:",
    result.probability
)

print(
    "Features:",
    result.top_features
)