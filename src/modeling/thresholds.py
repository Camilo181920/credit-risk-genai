import numpy as np

from sklearn.metrics import f1_score


def find_best_threshold(
    y_true,
    probabilities,
):

    thresholds = np.arange(
        0.10,
        0.95,
        0.05
    )

    best_threshold = 0.5
    best_score = 0

    for threshold in thresholds:

        predictions = (
            probabilities >= threshold
        ).astype(int)

        score = f1_score(
            y_true,
            predictions
        )

        if score > best_score:

            best_score = score

            best_threshold = threshold

    return best_threshold, best_score