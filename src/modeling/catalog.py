from src.modeling.model_factory import (
    create_logistic_regression,
    create_random_forest,
    create_xgboost,
)


def available_models():
    """
    Catálogo de modelos disponibles.
    """

    return {
        "Logistic Regression": create_logistic_regression(),
        "Random Forest": create_random_forest(),
        "XGBoost": create_xgboost(),
    }