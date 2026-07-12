from pathlib import Path
import json
from datetime import datetime

import joblib

from sklearn.model_selection import train_test_split

from src.data.loader import load_data

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

from src.config.settings import (
    MODEL_DIR,
)


TARGET = "credit_risk"


def prepare_data(df):

    X = df.drop(
        columns=[TARGET]
    )

    y = df[TARGET]

    return X, y



def identify_columns(X):

    numeric_features = (
        X.select_dtypes(
            include=[
                "int64",
                "float64",
            ]
        )
        .columns
        .tolist()
    )

    categorical_features = (
        X.select_dtypes(
            include=[
                "object",
            ]
        )
        .columns
        .tolist()
    )

    return (
        numeric_features,
        categorical_features,
    )



def train():

    print(
        "Loading dataset..."
    )

    df = load_data(
        "german_credit.csv"
    )


    X, y = prepare_data(
        df
    )


    numeric_features, categorical_features = (
        identify_columns(X)
    )


    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y,
        )
    )


    model = create_xgboost()


    trainer = ModelTrainer(
        model,
        numeric_features,
        categorical_features,
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