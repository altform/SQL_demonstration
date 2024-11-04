# Table Configuration

This section outlines the setup and configuration of the relational tables used in this project. All data implemented is fictional and auto-generated, serving solely to showcase SQL capabilities in a controlled environment.

## Table Structure

Four tables were created for this fictional e-commerce database.

### 1. Customers Table
- **Customer ID** (Primary Key): An auto-incremented identifier for each unique customer.
- **First Name**: Customer's first name.
- **Last Name**: Customer's last name.
- **Email**: Customer's email address.
- **Phone Number**: Customer's contact phone number.

### 2. Products Table
- **Product ID** (Primary Key): A unique, auto-incremented identifier for each product.
- **Product Name**: The name of the product.
- **Category**: The category to which the product belongs.
- **Price**: The price per unit of the product.
- **Stock**: The available quantity of each product in stock.

### 3. Orders Table
- **Order ID** (Primary Key): A unique, auto-incremented identifier for each order.
- **Customer ID**: Links the order to a customer by a randomly assigned ID between 1 and 550.
- **Order Date**: A randomly generated date representing when the order was placed.
- **Total Amount**: The total monetary value of the order.

### 4. Order Items Table
- **Order Item ID** (Primary Key): A unique, auto-incremented identifier for each item within an order.
- **Order ID**: References the associated order from the Orders table.
- **Product ID**: References the associated product from the Products table.
- **Quantity**: The number of units of the product in the specific order item.
- **Price**: The per-unit price of the product in each order item.


    
