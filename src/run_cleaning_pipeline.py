from __future__ import annotations

from pathlib import Path

from src.load_data import load_raw_files
from src.clean_columns import standardize_columns
from src.standardize_values import standardize_values
from src.deduplicate import split_duplicates
from src.validate_data import split_invalid_rows, build_quality_summary
from src.build_outputs import write_outputs


def run() -> None:
    project_root = Path(".")
    raw_dir = project_root / "data" / "raw"
    reference_dir = project_root / "data" / "reference"
    cleaned_dir = project_root / "data" / "cleaned"
    sqlite_dir = project_root / "outputs" / "sqlite"
    reports_dir = project_root / "outputs" / "reports"

    raw_df = load_raw_files(raw_dir)
    structured_df = standardize_columns(raw_df)
    standardized_df = standardize_values(structured_df, reference_dir)
    deduped_df, duplicate_rejected = split_duplicates(standardized_df)
    clean_df, invalid_rejected = split_invalid_rows(deduped_df)
    rejected_df = duplicate_rejected.copy()
    if not invalid_rejected.empty:
        rejected_df = rejected_df._append(invalid_rejected, ignore_index=True)

    clean_df = clean_df.sort_values(by=["order_date", "order_id"]).reset_index(drop=True)
    summary_df = build_quality_summary(raw_df, clean_df, rejected_df)

    write_outputs(clean_df, rejected_df, summary_df, cleaned_dir, sqlite_dir, reports_dir)

    print("Cleaning pipeline complete.")
    print(f"Raw rows: {len(raw_df)}")
    print(f"Clean rows: {len(clean_df)}")
    print(f"Rejected rows: {len(rejected_df)}")


if __name__ == "__main__":
    run()
