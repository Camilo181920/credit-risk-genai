"""
Compatibilidad temporal.

La gestión oficial de modelos ahora se realiza en:

src.modeling.model_registry
"""

from src.modeling.model_registry import (
    save_pipeline,
    load_pipeline,
)


def save_model(
    model,
    filename=None,
):
    """
    Guarda un modelo usando el registro oficial.

    El argumento filename se conserva
    para no romper código antiguo.
    """

    return save_pipeline(
        model
    )


def load_model(
    filename=None,
):
    """
    Carga el modelo oficial.
    """

    return load_pipeline()