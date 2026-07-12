from pathlib import Path

import pandas as pd

from src.config.settings import RAW_DATA_DIR


def load_data(
    filename: str,
) -> pd.DataFrame:
    """
    Carga un dataset CSV ubicado en data/raw/.

    Parameters
    ----------
    filename:
        Nombre del archivo CSV.

    Returns
    -------
    pandas.DataFrame
    """

    filepath: Path = RAW_DATA_DIR / filename

    if not filepath.exists():
        raise FileNotFoundError(
            f"No existe el archivo: {filepath}"
        )

    return pd.read_csv(filepath)