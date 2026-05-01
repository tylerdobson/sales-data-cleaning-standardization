from __future__ import annotations

from pathlib import Path
import pandas as pd
from src.utils import normalize_column_name


def load_raw_files(raw_dir: Path) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for path in sorted(raw_dir.glob("*.csv")):
        df = pd.read_csv(path, dtype=str)
        df.columns = [normalize_column_name(col) for col in df.columns]
        df["source_file"] = path.name
        frames.append(df)
    if not frames:
        raise FileNotFoundError("No raw CSV files found.")
    return pd.concat(frames, ignore_index=True)
