-- Write your query below
SELECT c.customer_id, c.customer_name
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(DISTINCT CASE 
           WHEN o.product_name = 'A' THEN o.product_name 
       END) > 0
   AND COUNT(DISTINCT CASE 
           WHEN o.product_name = 'B' THEN o.product_name 
       END) > 0
   AND COUNT(DISTINCT CASE 
           WHEN o.product_name = 'C' THEN o.product_name 
       END) = 0
ORDER BY c.customer_name;