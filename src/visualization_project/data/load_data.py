from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CSV = ROOT / "data" / "raw" / "global_power_plant_database.csv"


def load_power_plants(path=DEFAULT_CSV):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            "Dataset missing. Put global_power_plant_database.csv at "
            f"{path} (download WRI Global Power Plant Database v1.3.0)."
        )
    return pd.read_csv(path)
