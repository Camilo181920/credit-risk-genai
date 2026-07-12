import pandas as pd


def identify_columns(df):

    numerical = df.select_dtypes(
        include=["int64","float64"]
    ).columns.tolist()

    categorical = df.select_dtypes(
        include="object"
    ).columns.tolist()

    return numerical, categorical