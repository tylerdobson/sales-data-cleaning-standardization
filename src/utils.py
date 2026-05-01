from __future__ import annotations

from pathlib import Path
import re
import pandas as pd


COLUMN_ALIASES = {
    "order id": "order_id",
    "order_id": "order_id",
    "orderdate": "order_date",
    "order date": "order_date",
    "customer name": "customer_name",
    "customer": "customer_name",
    "state": "state",
    "state_name": "state",
    "product category": "product_category",
    "category": "product_category",
    "sales amount": "sales_amount",
    "amount": "sales_amount",
    "quantity": "quantity",
    "qty": "quantity",
    "returned": "returned",
    "return_flag": "returned",
    "region": "region",
    "region_name": "region",
}


def normalize_column_name(name: str) -> str:
    cleaned = name.strip().lower().replace("_", " ")
    cleaned = re.sub(r"\s+", " ", cleaned)
    return COLUMN_ALIASES.get(cleaned, cleaned.replace(" ", "_"))


def load_mapping_csv(path: Path) -> dict[str, str]:
    df = pd.read_csv(path)
    return {
        str(row["raw_value"]).strip().lower(): str(row["standard_value"]).strip()
        for _, row in df.iterrows()
    }
