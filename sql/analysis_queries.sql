-- Audit summary
SELECT metric, value
FROM audit_data_quality_summary
ORDER BY metric;

-- Monthly revenue trend
SELECT month, month_label, revenue
FROM monthly_revenue
ORDER BY month;

-- Revenue by country
SELECT country, revenue
FROM country_revenue
ORDER BY revenue DESC;

-- Revenue by product
SELECT stock_code, revenue
FROM product_revenue
ORDER BY revenue DESC;
