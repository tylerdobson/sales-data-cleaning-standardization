from __future__ import annotations

import pandas as pd


def split_duplicates(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    duplicate_mask = df.duplicated(
        subset=["order_id", "order_date", "customer_name", "sales_amount", "quantity"],
        keep="first",
    )
    rejected = df[duplicate_mask].copy()
    rejected["rejection_reason"] = "duplicate_order"
    cleaned = df[~duplicate_mask].copy()
    return cleaned, rejected
