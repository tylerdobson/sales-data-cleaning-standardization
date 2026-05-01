# Sales Data Cleaning and Standardization

## Overview

I built this project to show that I can take messy business sales data and turn it into something clean, validated, and analysis-ready. The project simulates a real-world scenario where monthly sales exports arrive in inconsistent formats and need to be standardized before they can be used for reporting.

I used Python to load multiple messy CSV files, standardize columns and values, separate bad records from valid ones, publish clean outputs to CSV and SQLite, and generate a short data-quality report.

---

## Why I Built This Project

I wanted a portfolio project that showed practical data-cleaning skills, not just analysis after the data was already perfect. In real work, raw files usually have inconsistent column names, mixed date formats, duplicate records, invalid values, and messy business labels. This project shows how I would handle that process.

---

## Tools Used

- Python
- Pandas
- CSV
- SQLite
- Markdown

---

## Repository Structure

```text
sales-data-cleaning-standardization/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── reference/
├── outputs/
│   ├── reports/
│   └── sqlite/
├── src/
│   ├── run_cleaning_pipeline.py
│   ├── load_data.py
│   ├── clean_columns.py
│   ├── standardize_values.py
│   ├── validate_data.py
│   ├── deduplicate.py
│   ├── build_outputs.py
│   └── utils.py
├── sql/
│   └── analysis_queries.sql
├── docs/
│   ├── architecture.md
│   ├── data_dictionary.md
│   ├── github_setup.md
│   └── resume_bullets.md
└── tests/
    └── test_cleaning_rules.py
```

---

## Business Scenario

This project assumes I receive messy sales exports from different reporting periods. Each file has different formatting and quality problems. My job is to preserve the raw files, apply consistent cleaning rules, reject invalid records, and create a final dataset that could be used for downstream reporting.

---

## Cleaning Rules

The pipeline:
- standardizes column names across files
- trims whitespace
- standardizes customer names
- maps inconsistent state values to one standard form
- maps category variations to one standard form
- parses dates into a consistent format
- converts sales amounts to numeric values
- converts quantity to numeric values
- standardizes return flags
- separates duplicate rows
- rejects invalid business records

---

## How to Run

```bash
python -m src.run_cleaning_pipeline
```

After the run, review:
- `data/cleaned/sales_cleaned.csv`
- `data/cleaned/sales_rejected.csv`
- `data/cleaned/data_quality_summary.csv`
- `outputs/sqlite/sales_cleaning.db`
- `outputs/reports/cleaning_report.md`

---

## Main Outputs

### Clean dataset
- `data/cleaned/sales_cleaned.csv`

### Rejected records
- `data/cleaned/sales_rejected.csv`

### Data quality summary
- `data/cleaned/data_quality_summary.csv`

### SQLite output
- `outputs/sqlite/sales_cleaning.db`

### Quality report
- `outputs/reports/cleaning_report.md`

---

## SQLite Tables

- `fact_sales_clean`
- `fact_sales_rejected`
- `audit_data_quality_summary`

---

## What This Project Demonstrates

This project demonstrates:
- practical data cleaning
- repeatable transformation logic
- data validation
- deduplication
- rejected-row handling
- CSV publishing
- SQLite loading
- project documentation

---

## How I Would Explain This In an Interview

I would describe this as a practical data-cleaning and standardization project. I built a Python pipeline that takes messy monthly sales exports, applies consistent cleaning rules, separates invalid records, and publishes both clean and rejected outputs. I also wrote the cleaned data to SQLite so it can be reviewed with SQL after the transformation process is complete.
