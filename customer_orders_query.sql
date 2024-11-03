SELECT customers.customer_id, customers.first_name, customers.last_name, 
       products.product_name, order_items.order_id, orders.total_amount 
FROM orders
INNER JOIN order_items ON order_items.order_id = orders.order_id
INNER JOIN products ON order_items.product_id = products.product_id
INNER JOIN customers ON orders.customer_id = customers.customer_id
WHERE orders.order_date LIKE '2024-3%';

SELECT customers.customer_id, customers.first_name, customers.last_name, 
       products.product_name, order_items.order_id, orders.total_amount 
FROM orders
INNER JOIN order_items ON order_items.order_id = orders.order_id
INNER JOIN products ON order_items.product_id = products.product_id
INNER JOIN customers ON orders.customer_id = customers.customer_id
WHERE orders.order_date LIKE '2024-03%';
