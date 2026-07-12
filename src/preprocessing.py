from __future__ import annotations

import pandas as pd

from sklearn.model_selection import train_test_split

TARGET = "credit_risk"


def split_features_target(
    df: pd.DataFrame,
):
    """
    Separa variables predictoras y objetivo.
    """

    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    return X, y


def split_train_test(
    X,
    y,
    test_size: float = 0.20,
    random_state: int = 42,
):

    return train_test_split(
        X,
        y,
        stratify=y,
        test_size=test_size,
        random_state=random_state,
    )