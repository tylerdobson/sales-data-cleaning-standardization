from __future__ import annotations

import pandas as pd


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    expected = [
        "order_id",
        "order_date",
        "customer_name",
        "state",
        "product_category",
        "sales_amount",
        "quantity",
        "returned",
        "region",
        "source_file",
    ]
    missing = [col for col in expected if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return df[expected].copy()
