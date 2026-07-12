from src.modeling.model_registry import (
    load_metadata
)


def test_metadata():

    metadata = load_metadata()

    assert metadata["project"] == "Credit Risk Analytics & GenAI Assistant"