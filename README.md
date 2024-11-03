# SQL_demonstration
In this project I created a relational database, populated it with fake data, and performed a sample query using joins to get a specific view.

## Setting up the database 
ecommerce.db was created using sqlite3 and the Command Line Interface (CL) of the Linux Ubuntu distribution using the command 'sqlite3 ecommerce.db'

Next I wrote an SQL query to create the tables I wanted:
- customers is the list of customers, with customer-specific data
- products is a list of 20 products
- orders is the list of order information, who made the order, when, and how much
- order_items breaks down how much product is ordered

Reference the [Table Configuration.md](<Table Configuration.md>) for the specifics of how that was set up. 

##Creating the test data
Using 3 python files [order_items_sampleData](<order_items_sampleData.py>), [order_sampleData](<order_sampleData.py>), [customer_sampleData](<order_sampleData.py>) and an SQL script [product_sampleData_script](<customer_sampleData_script.sql>)

### Custom View
