from src.modeling.evaluation import ModelEvaluator


def evaluate_model(
    model,
    X_test,
    y_test,
):
    """
    Compatibilidad con código antiguo.
    """

    evaluator = ModelEvaluator()

    return evaluator.evaluate(
        model,
        X_test,
        y_test,
    )