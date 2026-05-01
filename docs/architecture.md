# Architecture

## Summary

This project simulates a real business data-cleaning workflow for messy retail sales exports.

## Flow

1. Load multiple raw CSV files from `data/raw/`
2. Standardize inconsistent column names
3. Clean and standardize business values
4. Deduplicate repeated orders
5. Separate invalid records from valid records
6. Publish cleaned data to CSV and SQLite
7. Generate a markdown quality report

## Output Tables

- `fact_sales_clean`
- `fact_sales_rejected`
- `audit_data_quality_summary`
