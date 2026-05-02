# Data Dictionary

## Clean output fields

- `invoice`: retail invoice number
- `stock_code`: product or service code
- `description`: normalized item description
- `quantity`: positive integer quantity
- `invoice_date`: ISO 8601 timestamp derived from the source file
- `invoice_month`: `YYYY-MM` bucket used for trend analysis
- `unit_price`: positive unit price in source currency
- `customer_id`: customer identifier
- `country`: normalized country label
- `line_revenue`: `quantity * unit_price`

## Rejected output fields

- `invoice`: source invoice number
- `stock_code`: source stock code
- `description`: normalized item description
- `quantity`: original parsed quantity when available
- `invoice_date`: original or parsed timestamp value
- `unit_price`: original parsed unit price
- `customer_id`: source customer identifier
- `country`: normalized country label
- `line_revenue`: calculated revenue when it can be trusted
- `rejection_reason`: primary reason the row was excluded

## Audit summary fields

- `input_rows`: raw rows processed
- `clean_rows`: rows kept for analysis
- `rejected_rows`: rows excluded by the quality rules
- `gross_line_revenue`: revenue scanned before exclusions
- `net_line_revenue`: revenue kept after exclusions
- `cancelled_line_revenue`: revenue removed from cancelled invoices
- `rejection_breakdown`: primary reason counts
- `top_countries`: revenue by country
- `top_products`: revenue by stock code
- `monthly_trend`: monthly revenue trend
