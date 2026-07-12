from __future__ import annotations

import pandas as pd


def create_age_group(
    df: pd.DataFrame,
):
    """
    Crea grupos de edad del cliente.
    """

    df = df.copy()

    df["age_group"] = pd.cut(
        df["customer_age"],
        bins=[
            18,
            30,
            45,
            60,
            100,
        ],
        labels=[
            "Young",
            "Adult",
            "Middle Age",
            "Senior",
        ],
    )

    return df


def create_loan_category(
    df: pd.DataFrame,
):
    """
    Categoriza clientes según monto del préstamo.
    """

    df = df.copy()

    df["loan_category"] = pd.qcut(
        df["loan_amount"],
        q=4,
        labels=[
            "Low",
            "Medium",
            "High",
            "Very High",
        ],
    )

    return df


def create_customer_profile(
    df: pd.DataFrame,
):
    """
    Pipeline de creación de variables de cliente.
    """

    df = create_age_group(df)

    df = create_loan_category(df)

    return df