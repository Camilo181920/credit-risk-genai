from __future__ import annotations

import pandas as pd
from sklearn.metrics import confusion_matrix


def business_confusion_matrix(y_true, y_pred):
    """
    Devuelve la matriz de confusión como DataFrame.
    """
    cm = confusion_matrix(y_true, y_pred)

    return pd.DataFrame(
        cm,
        index=["Real Good", "Real Bad"],
        columns=["Pred Good", "Pred Bad"]
    )


def business_cost(
    y_true,
    y_pred,
    false_positive_cost: float = 1.0,
    false_negative_cost: float = 5.0,
):
    """
    Calcula un costo de negocio simple.
    """

    tn, fp, fn, tp = confusion_matrix(
        y_true,
        y_pred
    ).ravel()

    cost = (
        fp * false_positive_cost +
        fn * false_negative_cost
    )

    return {
        "False Positives": fp,
        "False Negatives": fn,
        "Business Cost": cost
    }