from src.data import load_data


def test_load_data():

    df = load_data("german_credit.csv")

    assert df.shape[0] > 0