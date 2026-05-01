from __future__ import annotations

import pandas as pd


def split_invalid_rows(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    cleaned = df.copy()
    invalid_frames: list[pd.DataFrame] = []

    rules = [
        (cleaned["order_date"].isna(), "missing_or_invalid_order_date"),
        (cleaned["sales_amount"].isna(), "invalid_sales_amount"),
        (cleaned["quantity"].isna(), "invalid_quantity"),
        (cleaned["quantity"] <= 0, "non_positive_quantity"),
        (cleaned["returned"] == "Unknown", "invalid_return_flag"),
    ]

    invalid_index = set()
    for mask, reason in rules:
        if mask.any():
            rejected = cleaned[mask].copy()
            rejected["rejection_reason"] = reason
            invalid_frames.append(rejected)
            invalid_index.update(rejected.index.tolist())

    rejected_all = pd.concat(invalid_frames, ignore_index=True) if invalid_frames else pd.DataFrame(columns=list(cleaned.columns) + ["rejection_reason"])
    valid = cleaned.drop(index=list(invalid_index)).copy()
    return valid.reset_index(drop=True), rejected_all.reset_index(drop=True)


def build_quality_summary(raw_df: pd.DataFrame, clean_df: pd.DataFrame, rejected_df: pd.DataFrame) -> pd.DataFrame:
    summary = [
        {"metric": "raw_rows", "value": int(len(raw_df))},
        {"metric": "clean_rows", "value": int(len(clean_df))},
        {"metric": "rejected_rows", "value": int(len(rejected_df))},
        {"metric": "distinct_orders_clean", "value": int(clean_df["order_id"].nunique())},
        {"metric": "distinct_customers_clean", "value": int(clean_df["customer_name"].nunique())},
    ]
    return pd.DataFrame(summary)
