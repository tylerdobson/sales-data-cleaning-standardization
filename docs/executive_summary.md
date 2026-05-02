# Executive Summary

This project rebuilds a sales-cleaning portfolio piece around a real retail dataset instead of toy exports. The UCI Online Retail II source provided enough scale and messiness to demonstrate the work a production analyst would actually do: clean timestamps, remove cancellations, handle missing customer IDs, reject invalid line items, deduplicate rows, and preserve a traceable audit trail.

## Key outcomes

- `525,461` source rows processed
- `400,916` rows kept for analysis
- `124,545` rows rejected with reasons
- `$8.80M` net revenue retained after cleaning
- `$629.9K` of cancelled line revenue removed from the analysis set

## Why it is stronger than the old version

- The source data is real.
- The rules are business-shaped, not synthetic.
- The proof images are generated from the audited outputs.
- The SQLite file is compact and reviewable.
- The project can be rerun from the script without manual cleanup.
