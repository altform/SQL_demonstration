#Table Configuration
This section will document how the relational table was set up and configured.

##Table initiation

4 tables were created for my fictional database setup
**1. Customer Table**
    - Customer ID (primary key) - auto-incremented number identifying each unique customer
    - First Name - customers first name
    - Last Name - customers last name
    - Email - customers email
    - Phone number - customers phone number
**2. Product Talbe**
    - Product ID (primary key) - unique auto incremented id for each product
    - Product Name - name of the product
    - Category - the category the product is related to
    - Price - the price per product
    - Stock - the number of each product is available
**3. Orders Table**
    - Order ID (primary key) - unique auto-incremented id for each order
    - Customer ID - auto generate number from 1- 500 to tie a random customer to an order
    - Order Date -  A random date generated to represent the date of the order
    - Total Amount - The total amount of the order

