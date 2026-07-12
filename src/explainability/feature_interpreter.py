FEATURE_EXPLANATIONS = {

    "savings":
        "Nivel de ahorro del cliente",

    "credit_history":
        "Historial crediticio",

    "status":
        "Estado de cuenta corriente",

    "installment_rate":
        "Relación cuota / ingreso",

    "duration":
        "Duración del crédito",

    "amount":
        "Monto solicitado",

    "age":
        "Edad del cliente",

    "employment_duration":
        "Antigüedad laboral",

    "employment":
        "Antigüedad laboral",

    "housing":
        "Tipo de vivienda",

    "other_installment_plans":
        "Otros compromisos financieros",

    "number_credits":
        "Número de créditos activos",

    "property":
        "Nivel de patrimonio",

    "personal_status_sex":
        "Perfil personal del cliente",

    "other_debtors":
        "Existencia de otros deudores",

    "present_residence":
        "Tiempo de residencia",

    "job":
        "Tipo de ocupación",

    "people_liable":
        "Personas a cargo",

    "telephone":
        "Disponibilidad telefónica",

    "foreign_worker":
        "Condición laboral extranjera",

    "purpose":
        "Propósito del crédito",
}


def explain_feature(
    feature_name: str,
):

    clean_name = (
        feature_name
        .replace(
            "categorical__",
            ""
        )
        .replace(
            "numeric__",
            ""
        )
    )


    for key, explanation in FEATURE_EXPLANATIONS.items():

        if key in clean_name:

            return explanation


    return clean_name