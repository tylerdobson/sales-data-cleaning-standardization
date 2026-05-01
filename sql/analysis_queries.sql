-- Clean table row count
SELECT COUNT(*) AS clean_row_count
FROM fact_sales_clean;

-- Rejected row count by reason
SELECT
    rejection_reason,
    COUNT(*) AS rejected_count
FROM fact_sales_rejected
GROUP BY rejection_reason
ORDER BY rejected_count DESC, rejection_reason;

-- Total sales by state
SELECT
    state,
    ROUND(SUM(sales_amount), 2) AS total_sales
FROM fact_sales_clean
GROUP BY state
ORDER BY total_sales DESC;

-- Total sales by product category
SELECT
    product_category,
    ROUND(SUM(sales_amount), 2) AS total_sales
FROM fact_sales_clean
GROUP BY product_category
ORDER BY total_sales DESC;

-- Returned order rate
SELECT
    ROUND(
        SUM(CASE WHEN returned = 'Yes' THEN 1 ELSE 0 END) * 1.0 / COUNT(*),
        4
    ) AS returned_order_rate
FROM fact_sales_clean;

-- Monthly sales trend
SELECT
    substr(order_date, 1, 7) AS sales_month,
    ROUND(SUM(sales_amount), 2) AS total_sales
FROM fact_sales_clean
GROUP BY substr(order_date, 1, 7)
ORDER BY sales_month;

-- Top customers by sales
SELECT
    customer_name,
    ROUND(SUM(sales_amount), 2) AS total_sales
FROM fact_sales_clean
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 10;
