SELECT customer_id, MIN(order_date) FROM orders
GROUP BY customers
ORDER BY customer_id;

SELECT customer_id, AVG(freight) AS avg_freight FROM orders
GROUP BY customer_id
ORDER BY avg_freight;

SELECT o.order_id, NUM(DISTINCT product_id) AS product_count 
FROM order_details o
GROUP BY order_id HAVING(count(*)) >= 5
ORDER BY product_count DESC;