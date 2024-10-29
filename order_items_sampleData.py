import sqlite3
import random
from faker import Faker

# Initialize Faker and connect to the database
fake = Faker()
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Retrieve existing order_ids and product_ids
cursor.execute("SELECT order_id FROM orders")
order_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT product_id, price FROM products")
products = cursor.fetchall()  # List of (product_id, price) tuples

# Number of order items to generate
num_order_items = 1000  # Adjust as needed

# Generate fake data for order_items
order_items_data = []
for _ in range(num_order_items):
    order_id = random.choice(order_ids)                 # Randomly select an existing order_id
    product_id, base_price = random.choice(products)    # Randomly select an existing product and its price
    quantity = random.randint(1, 5)                     # Random quantity between 1 and 5
    price = round(base_price * quantity, 2)             # Calculate total price based on quantity

    order_items_data.append((order_id, product_id, quantity, price))

# Insert generated data into the order_items table
cursor.executemany('''
    INSERT INTO order_items (order_id, product_id, quantity, price)
    VALUES (?, ?, ?, ?)
''', order_items_data)

# Commit and close the connection
conn.commit()
conn.close()

print(f"Inserted {num_order_items} fake order items successfully.")
