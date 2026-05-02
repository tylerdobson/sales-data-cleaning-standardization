# Methodology

## Source

The source of truth is the UCI Online Retail II dataset, accessed through a CSV mirror so the build stays reproducible in this environment.

## Cleaning logic

The build uses row-level rules that match common retail cleanup work:

1. Normalize text fields by trimming whitespace and collapsing repeated spaces.
2. Parse invoice timestamps from UK-style `dd/mm/yyyy hh:mm` strings.
3. Reject invoices that start with `C`, which indicates a cancellation.
4. Reject rows with missing customer identifiers.
5. Reject rows with non-positive quantity or price.
6. Reject exact duplicate rows after canonicalization.
7. Calculate line revenue from quantity multiplied by price.

## Outputs

The processor writes:

- a cleaned CSV
- a rejected CSV with reasons
- a compact SQLite audit mart
- summary JSON for downstream docs
- proof images for portfolio review

## Notes on the SQLite output

The bundled SQLite file is a compact audit mart with summary and sample tables so it stays portable in GitHub. The full line-level outputs are still produced by the processor and can be regenerated locally on demand.

## Why this is credible

The numbers in the README and proof pack are generated from the actual dataset run, not hand-authored placeholders. That matters more than decoration: it makes the work reviewable, reproducible, and honest.
