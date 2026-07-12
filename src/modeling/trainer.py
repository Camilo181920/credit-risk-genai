from src.modeling.pipeline_builder import build_pipeline


class ModelTrainer:

    def __init__(
        self,
        model,
        numeric_features,
        categorical_features,
    ):

        self.pipeline = build_pipeline(
            model,
            numeric_features,
            categorical_features,
        )

    def fit(
        self,
        X_train,
        y_train,
    ):

        self.pipeline.fit(
            X_train,
            y_train,
        )

        return self.pipeline

    def predict(
        self,
        X,
    ):

        return self.pipeline.predict(X)

    def predict_proba(
        self,
        X,
    ):

        return self.pipeline.predict_proba(X)