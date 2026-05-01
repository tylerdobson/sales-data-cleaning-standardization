from pathlib import Path
import pandas as pd

from src.standardize_values import standardize_values


def test_standardize_values():
    df = pd.DataFrame(
        {
            "order_id": ["X-1"],
            "order_date": ["01/05/2024"],
            "customer_name": ["  acme corp "],
            "state": ["ca"],
            "product_category": ["tech"],
            "sales_amount": ["$1,250.00"],
            "quantity": ["2"],
            "returned": ["n"],
            "region": ["west"],
            "source_file": ["sample.csv"],
        }
    )
    result = standardize_values(df, Path("data/reference"))
    assert result.loc[0, "customer_name"] == "Acme Corp"
    assert result.loc[0, "state"] == "California"
    assert result.loc[0, "product_category"] == "Technology"
    assert float(result.loc[0, "sales_amount"]) == 1250.00
    assert float(result.loc[0, "quantity"]) == 2.0
    assert result.loc[0, "returned"] == "No"
