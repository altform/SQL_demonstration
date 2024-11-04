# SQL Demonstration Project

This project demonstrates the creation and manipulation of a relational database using SQLite3. I created a sample e-commerce database, populated it with mock data, and performed a query using joins to generate a meaningful dataset view.

## Database Setup

The database, `ecommerce.db`, was created using SQLite3 on the Linux Ubuntu command line with the command:

```bash
sqlite3 ecommerce.db
```
An SQL script was written to define the following tables:

- **customers:** Contains customer-specific data.
- **products:** Stores information for 20 products.
- **orders:** Includes order details such as the customer who placed the order, the date, and the total amount.
- **order_items:** Breaks down each order by product, specifying the quantity ordered per item.
  
For detailed table configurations, please see [Table Configuration Doc](<Table_configuration.md>)

## Generating Test Data
To populate the database with sample data, I used both Python scripts and SQL:

**Python Scripts**
  - [order_items_sampleData](<order_items_sampleData.py>)
  - [order_sampleData](<orders_sampleData.py>)
  - [customer_sampleData](<customers_sampleData_script.py>)

**SQL Script**
  - [product_sampleData_script](<product_sampleData_script.sql>)
    
## Custom Data View
To demonstrate SQL querying capabilities, I created a custom view that retrieves a comprehensive dataset, including customer details (ID, first name, and last name), products ordered, order ID, and order totals. This view leverages inner joins across the relevant tables to consolidate the data into a single, cohesive output.
