from src.data import load_data

from src.business_metrics import business_summary


def test_business_metrics():

    df = load_data("german_credit.csv")

    summary = business_summary(df)

    assert len(summary) == 4