import pandas as pd


def prepare_power_plants(data: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with basic numeric conversion; raw data remains unchanged."""
    result = data.copy()
    for column in ("latitude", "longitude", "capacity_mw", "commissioning_year"):
        if column in result:
            result[column] = pd.to_numeric(result[column], errors="coerce")
    return result
