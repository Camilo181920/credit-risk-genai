SELECT
    customer_segment,
    COUNT(*) AS total_customers,
    AVG(income) AS average_income
FROM customers
GROUP BY customer_segment;