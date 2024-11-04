import sqlite3
from faker import Faker

# Initialize Faker and create a connection to SQLite database
fake = Faker()
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Create the customers table (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone_num TEXT
    );
''')

# Function to insert sample data
def insert_sample_data(n):
    for _ in range(n):
        first_name = fake.first_name()  # Generate a random first name (TEXT)
        last_name = fake.last_name()    # Generate a random last name (TEXT)
        email = fake.unique.email()     # Generate a unique email address (TEXT)
        phone_num = fake.phone_number() # Generate a random phone number (TEXT)

        # Insert the generated data into the customers table
        try:
            cursor.execute('''
                INSERT INTO customers (first_name, last_name, email, phone_num)
                VALUES (?, ?, ?, ?)
            ''', (first_name, last_name, email, phone_num))
        except sqlite3.IntegrityError:
            # If there's a conflict with the UNIQUE email constraint, skip that row
            print(f"Duplicate email found: {email}, skipping insertion.")

# Generate 50 sample rows of data
insert_sample_data(50)

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("Sample data inserted successfully.")
