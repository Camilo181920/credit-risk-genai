from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = PROJECT_ROOT / "models"

MODEL_PATH = MODEL_DIR / "credit_model.joblib"
FEATURES_PATH = MODEL_DIR / "feature_names.joblib"
METADATA_PATH = MODEL_DIR / "metadata.json"

REPORTS_DIR = PROJECT_ROOT / "reports"

OPENAI_MODEL = "gpt-4.1-mini"
DEFAULT_THRESHOLD = 0.50