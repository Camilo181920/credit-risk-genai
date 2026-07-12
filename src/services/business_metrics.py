import pandas as pd


def default_rate(
    df: pd.DataFrame,
) -> float:
    """
    Calcula la tasa de clientes con default.
    """

    return df["credit_risk"].mean()


def average_loan(
    df: pd.DataFrame,
) -> float:
    """
    Calcula el monto promedio de crédito.
    """

    return df["loan_amount"].mean()


def average_age(
    df: pd.DataFrame,
) -> float:
    """
    Calcula la edad promedio del cliente.
    """

    return df["customer_age"].mean()


def business_summary(
    df: pd.DataFrame,
) -> pd.Series:
    """
    Genera indicadores principales del negocio.
    """

    summary = {

        "Clientes": len(df),

        "Monto Promedio": average_loan(df),

        "Edad Promedio": average_age(df),

        "Tasa Default": default_rate(df),

    }

    return pd.Series(summary)