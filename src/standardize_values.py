from __future__ import annotations

from pathlib import Path
import pandas as pd

from src.utils import load_mapping_csv


def standardize_values(df: pd.DataFrame, reference_dir: Path) -> pd.DataFrame:
    state_map = load_mapping_csv(reference_dir / "state_mapping.csv")
    category_map = load_mapping_csv(reference_dir / "category_mapping.csv")

    cleaned = df.copy()

    for col in ["order_id", "customer_name", "state", "product_category", "returned", "region"]:
        cleaned[col] = cleaned[col].fillna("").astype(str).str.strip()

    cleaned["customer_name"] = cleaned["customer_name"].str.replace(r"\s+", " ", regex=True).str.title()
    cleaned["region"] = cleaned["region"].str.title()

    cleaned["state"] = cleaned["state"].str.lower().map(state_map).fillna(cleaned["state"].str.title())
    cleaned["product_category"] = (
        cleaned["product_category"].str.lower().map(category_map).fillna(cleaned["product_category"].str.title())
    )

    cleaned["returned"] = cleaned["returned"].str.lower().map(
        {
            "y": "Yes",
            "yes": "Yes",
            "true": "Yes",
            "n": "No",
            "no": "No",
            "false": "No",
        }
    ).fillna("Unknown")

    cleaned["order_date"] = pd.to_datetime(cleaned["order_date"], errors="coerce").dt.date.astype("string")

    money = (
        cleaned["sales_amount"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    cleaned["sales_amount"] = pd.to_numeric(money, errors="coerce")

    cleaned["quantity"] = pd.to_numeric(cleaned["quantity"], errors="coerce")

    return cleaned
