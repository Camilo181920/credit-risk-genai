from pathlib import Path

import joblib


MODEL_PATH = (
    Path(__file__)
    .resolve()
    .parents[2]
    / "models"
    / "credit_model.joblib"
)


def save_pipeline(
    pipeline,
):
    """
    Guarda un pipeline entrenado.
    """

    MODEL_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    joblib.dump(
        pipeline,
        MODEL_PATH,
    )


def load_pipeline():
    """
    Carga el pipeline entrenado.

    Returns
    -------
    Pipeline
        Modelo entrenado.

    Raises
    ------
    FileNotFoundError
        Si no existe el modelo.
    """

    if not MODEL_PATH.exists():

        raise FileNotFoundError(
            f"No existe el modelo entrenado: {MODEL_PATH}"
        )

    return joblib.load(
        MODEL_PATH
    )