from __future__ import annotations

import shap
import matplotlib.pyplot as plt


def create_explainer(model):
    """
    Crea el explicador SHAP para modelos basados en árboles.
    """

    # Extraemos el modelo del Pipeline de scikit-learn
    estimator = model.named_steps["model"]

    return shap.TreeExplainer(estimator)


def shap_values(model, transformed_data):
    """
    Calcula los valores SHAP.
    """

    explainer = create_explainer(model)

    values = explainer.shap_values(transformed_data)

    return explainer, values


def summary_plot(values, features):
    """
    Gráfico global de importancia.
    """

    shap.summary_plot(
        values,
        features,
        show=False
    )

    plt.tight_layout()
    plt.show()


def waterfall_plot(explainer, values, index=0):
    """
    Explicación individual.
    """

    shap.plots.waterfall(
        explainer(values[index]),
        show=False
    )

    plt.tight_layout()
    plt.show()