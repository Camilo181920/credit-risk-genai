from src.modeling.model_registry import load_pipeline
from src.modeling.inference import CreditInference


def test_prediction():

    model = load_pipeline()

    inference = CreditInference(model)

    customer = {

        "status": "A11",
        "loan_duration_months": 12,
        "credit_history_status": "A34",
        "purpose": "A43",
        "loan_amount": 2000,
        "savings": "A61",
        "employment_duration": "A73",
        "installment_ratio": 2,
        "personal_status_sex": "A93",
        "other_debtors": "A101",
        "present_residence": 2,
        "property": "A121",
        "customer_age": 35,
        "other_installment_plans": "A143",
        "housing": "A152",
        "number_credits": 1,
        "job": "A173",
        "people_liable": 1,
        "telephone": "A191",
        "foreign_worker": "A201"
    }

    result = inference.predict(customer)

    assert "prediction" in result

    assert "probability" in result