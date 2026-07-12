COLUMN_MAPPING = {

    "loan_duration_months":
        "duration",

    "credit_history_status":
        "credit_history",

    "loan_amount":
        "amount",

    "installment_ratio":
        "installment_rate",

    "customer_age":
        "age",

}


def map_customer(customer: dict):

    mapped = {}

    for key, value in customer.items():

        model_key = COLUMN_MAPPING.get(
            key,
            key
        )

        mapped[model_key] = value


    return mapped