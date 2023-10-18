-- Displays the average tempreture (Farenheit) by city ordered by tempreture (descending)
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
