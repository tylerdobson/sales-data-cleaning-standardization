from __future__ import annotations

from pathlib import Path
import sqlite3
import pandas as pd


def write_outputs(clean_df: pd.DataFrame, rejected_df: pd.DataFrame, summary_df: pd.DataFrame, cleaned_dir: Path, sqlite_dir: Path, reports_dir: Path) -> None:
    cleaned_dir.mkdir(parents=True, exist_ok=True)
    sqlite_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    clean_csv = cleaned_dir / "sales_cleaned.csv"
    rejected_csv = cleaned_dir / "sales_rejected.csv"
    summary_csv = cleaned_dir / "data_quality_summary.csv"

    clean_df.to_csv(clean_csv, index=False)
    rejected_df.to_csv(rejected_csv, index=False)
    summary_df.to_csv(summary_csv, index=False)

    db_path = sqlite_dir / "sales_cleaning.db"
    with sqlite3.connect(db_path) as conn:
        clean_df.to_sql("fact_sales_clean", conn, if_exists="replace", index=False)
        rejected_df.to_sql("fact_sales_rejected", conn, if_exists="replace", index=False)
        summary_df.to_sql("audit_data_quality_summary", conn, if_exists="replace", index=False)

    report_path = reports_dir / "cleaning_report.md"
    report_lines = [
        "# Sales Data Cleaning Report",
        "",
        f"- Raw rows: **{len(summary_df[summary_df['metric']=='raw_rows']) and int(summary_df.loc[summary_df['metric']=='raw_rows','value'].iloc[0])}**",
        f"- Clean rows: **{len(summary_df[summary_df['metric']=='clean_rows']) and int(summary_df.loc[summary_df['metric']=='clean_rows','value'].iloc[0])}**",
        f"- Rejected rows: **{len(summary_df[summary_df['metric']=='rejected_rows']) and int(summary_df.loc[summary_df['metric']=='rejected_rows','value'].iloc[0])}**",
        "",
        "## Rejection reasons",
        "",
    ]
    if rejected_df.empty:
        report_lines.append("- No rejected rows.")
    else:
        counts = rejected_df["rejection_reason"].value_counts().sort_index()
        for reason, count in counts.items():
            report_lines.append(f"- **{reason}**: {count}")
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
