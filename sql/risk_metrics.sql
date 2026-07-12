SELECT
    risk_level,
    COUNT(*) AS total_clients,
    AVG(default_probability) AS avg_probability
FROM customer_predictions
GROUP BY risk_level;