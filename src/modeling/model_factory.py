from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier


def create_logistic_regression():
    """
    Crea una Regresión Logística.
    """

    return LogisticRegression(
        max_iter=1000,
        random_state=42,
    )


def create_random_forest():
    """
    Crea un Random Forest.
    """

    return RandomForestClassifier(
        n_estimators=300,
        random_state=42,
    )


def create_xgboost():
    """
    Crea un modelo XGBoost.
    """

    return XGBClassifier(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=5,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        eval_metric="logloss",
    )