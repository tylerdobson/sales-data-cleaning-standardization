# Data Dictionary

## fact_sales_clean
- `order_id`
- `order_date`
- `customer_name`
- `state`
- `product_category`
- `sales_amount`
- `quantity`
- `returned`
- `region`
- `source_file`

## fact_sales_rejected
Same columns as the clean table plus:
- `rejection_reason`

## audit_data_quality_summary
- `metric`
- `value`
