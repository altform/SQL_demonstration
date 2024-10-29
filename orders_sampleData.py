import sqlite3
from faker import Faker
import random

# Set up Faker and database connection
fake = Faker()
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Number of records to generate
num_orders = 1000  # Adjust the number of orders as needed

# Generate and insert fake data for orders
orders_data = []
for _ in range(num_orders):
    customer_id = random.randint(1, 550)                     # Random customer_id between 1 and 550
    order_date = fake.date_between(start_date="-2y", end_date="today")  # Random date within the last 2 years
    total_amount = round(random.uniform(20.0, 500.0), 2)     # Random total amount between $20 and $500

    # Append generated data to orders_data list
    orders_data.append((customer_id, order_date, total_amount))

# Insert data into orders table
cursor.executemany('''
    INSERT INTO orders (customer_id, order_date, total_amount)
    VALUES (?, ?, ?)
''', orders_data)

# Commit changes and close the connection
conn.commit()
conn.close()

print(f"Inserted {num_orders} fake order records successfully.")

