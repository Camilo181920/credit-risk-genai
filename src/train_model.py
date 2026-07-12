import json
from datetime import datetime

import joblib

from src.config.settings import MODEL_DIR

from src.data.loader import load_data

from src.modeling.data import (
    split_features_target,
    split_train_test,
    identify_columns,
)

from src.modeling.model_factory import (
    create_xgboost,
)

from src.modeling.trainer import (
    ModelTrainer,
)

from src.modeling.evaluation import (
    ModelEvaluator,
)

from src.modeling.model_registry import (
    save_pipeline,
)


TARGET = "credit_risk"


def train():

    print(
        "Loading dataset..."
    )

    df = load_data(
        "german_credit.csv"
    )

    X, y = split_features_target(
        df
    )

    numeric_features, categorical_features = (
        identify_columns(X)
    )

    X_train, X_test, y_train, y_test = (
        split_train_test(
            X,
            y,
        )
    )

    trainer = ModelTrainer(
        model=create_xgboost(),
        numeric_features=numeric_features,
        categorical_features=categorical_features,
    )

    print(
        "Training model..."
    )

    pipeline = trainer.fit(
        X_train,
        y_train,
    )

    print(
        "Evaluating..."
    )

    evaluator = ModelEvaluator()

    metrics = evaluator.evaluate(
        pipeline,
        X_test,
        y_test,
    )

    print(metrics)

    print(
        "Saving model..."
    )

    save_pipeline(
        pipeline
    )

    joblib.dump(
        X.columns.tolist(),
        MODEL_DIR / "feature_names.joblib",
    )

    metadata = {

        "project":
            "Credit Risk Analytics & GenAI Assistant",

        "algorithm":
            "XGBoost",

        "dataset":
            "German Credit Dataset",

        "target":
            TARGET,

        "version":
            "1.0.0",

        "trained_at":
            datetime.now().isoformat(),

        "roc_auc":
            float(
                metrics["roc_auc"]
            ),
    }

    with open(
        MODEL_DIR / "metadata.json",
        "w",
    ) as file:

        json.dump(
            metadata,
            file,
            indent=4,
        )

    print(
        "Training completed."
    )


if __name__ == "__main__":

    train()