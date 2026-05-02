# Sales Cleaning Standardization

A real-data cleaning project built on the UCI Online Retail II dataset.

## What this proves

This project takes messy retail line items and turns them into a clean, documented, analysis-ready dataset with repeatable rules and audit evidence.

Real audit results from the build:

- Input rows: `525,461`
- Clean rows: `400,916`
- Rejected rows: `124,545`
- Net revenue after cleaning: `$8,798,233.74`
- Gross line revenue scanned: `$9,539,484.63`
- Cancelled line revenue excluded: `$629,855.37`

## Cleaning rules

The pipeline standardizes and validates each row using practical retail rules:

- trim text fields and normalize country names
- parse UK-style invoice timestamps
- reject cancelled invoices
- reject missing customer IDs
- reject non-positive quantities
- reject non-positive prices
- reject duplicate rows after normalization
- write a clean CSV, a rejected CSV, a compact SQLite audit mart, and proof images

## Proof pack

The repo includes generated evidence under `out/proof/`:

- [audit-summary.png](./out/proof/audit-summary.png)
- [market-structure.png](./out/proof/market-structure.png)
- [sample-rows.png](./out/proof/sample-rows.png)

## Reproducible build

1. Run `node src/process-online-retail-ii.mjs`
2. Run `powershell -NoProfile -ExecutionPolicy Bypass -File src/render-proof.ps1`

The processor uses the real Online Retail II CSV mirror and writes the cleaned dataset, rejected rows, SQLite audit mart, summary JSON, and markdown report.

## Repository layout

- `src/process-online-retail-ii.mjs` regenerates the dataset and audit artifacts
- `src/render-proof.ps1` renders the proof images
- `out/` contains the generated audit evidence
- `docs/` contains the supporting case-study writeup
- `sql/analysis_queries.sql` contains SQL used for review
- `tests/cleaning_rules.test.mjs` checks the core cleaning rules

## Source

UCI Online Retail II mirror:

https://raw.githubusercontent.com/PacktWorkshops/The-Data-Analysis-Workshop/master/Chapter08/Datasets/online_retail_II.csv

## Interview summary

This project shows that I can take a real retail feed, enforce business-quality rules, preserve rejected records for auditability, and ship a compact proof pack with actual numbers rather than toy examples.
