from src.modeling.model_registry import load_pipeline


def load_model():
    """
    Compatibilidad con versiones anteriores.

    La lógica principal debe usar
    CreditService.
    """

    return load_pipeline()