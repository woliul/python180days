# **Day 66: Mini Project: Data Analysis with File Data and SQL Integration**

Today, we'll combine everything we've learned so far and apply it in a mini project. We'll work with CSV/Excel data, integrate it with an SQLite database, and perform basic data analysis.

---

## **1️⃣ Project Overview**

We'll create a **mini-project** where we:
1. Read data from a CSV file.
2. Store the data in an SQLite database.
3. Perform some basic analysis using SQL queries.

Let’s say we have a CSV file containing information about a set of products in a store, including their `name`, `category`, `price`, and `quantity_in_stock`. Our goal is to:
- Import this data into a database.
- Perform analysis, such as filtering products by category or finding the total value of stock.

---

## **2️⃣ Project Steps**

### **Step 1: Prepare the CSV File**

Create a CSV file called `products.csv` with the following content:

```csv
name, category, price, quantity_in_stock
Laptop, Electronics, 999.99, 50
Phone, Electronics, 599.99, 200
Shirt, Clothing, 19.99, 150
Jeans, Clothing, 39.99, 100
Watch, Accessories, 89.99, 75
Sunglasses, Accessories, 29.99, 120
```

This CSV contains information about different products, their categories, prices, and quantities in stock.

---

### **Step 2: Create an SQLite Database and Table**

We’ll create a database called `store.db` and a table called `products` to store the data.

```python
import sqlite3
import csv

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Create a table for products
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    quantity_in_stock INTEGER
)
''')

conn.commit()
```

---

### **Step 3: Read the CSV File and Insert Data into the Database**

Next, we’ll read data from the `products.csv` file and insert it into the `products` table.

```python
# Open the CSV file
with open('products.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header
    next(csv_reader)
    
    # Insert data into the 'products' table
    for row in csv_reader:
        cursor.execute('''
        INSERT INTO products (name, category, price, quantity_in_stock)
        VALUES (?, ?, ?, ?)
        ''', (row[0], row[1], float(row[2]), int(row[3])))

# Commit the changes
conn.commit()
```

---

### **Step 4: Perform Some Data Analysis Using SQL Queries**

Now that we have the data in the database, let’s perform some basic analysis.

#### **Query 1: Retrieve all products in the "Electronics" category.**

```python
cursor.execute('''
SELECT * FROM products WHERE category = 'Electronics'
''')

electronics = cursor.fetchall()

for product in electronics:
    print(product)
```

#### **Query 2: Find the total value of stock for each product (price * quantity_in_stock).**

```python
cursor.execute('''
SELECT name, price, quantity_in_stock, (price * quantity_in_stock) AS stock_value
FROM products
''')

stock_values = cursor.fetchall()

for product in stock_values:
    print(product)
```

#### **Query 3: Find the average price of all products.**

```python
cursor.execute('''
SELECT AVG(price) FROM products
''')

average_price = cursor.fetchone()[0]
print(f"The average price of all products is ${average_price:.2f}")
```

#### **Query 4: Find the total number of products in each category.**

```python
cursor.execute('''
SELECT category, SUM(quantity_in_stock) FROM products GROUP BY category
''')

category_totals = cursor.fetchall()

for category in category_totals:
    print(f"{category[0]}: {category[1]} products")
```

---

### **Step 5: Conclusion & Reflection**

This mini-project helped you:
1. Read data from a CSV file.
2. Store it in an SQLite database.
3. Perform basic data analysis using SQL queries.

### **🛠️ Practice Tasks**

Now, it’s your turn to try it out with different data:

### **Task 1: Modify the Project**
1. Add a column for `supplier` in the `products` table.
2. Update the `products.csv` file to include a `supplier` column.
3. Re-import the CSV and add the new data to the database.

### **Task 2: Perform More Analysis**
1. Find the product with the highest price.
2. Calculate the total stock value of all products (sum of price * quantity_in_stock).
3. List all products with a quantity_in_stock greater than 100.

---

## **Tips for Success**
- Make sure you always use **parameterized queries** when inserting data to avoid SQL injection vulnerabilities.
- When working with large datasets, you may want to optimize queries by using indexing on frequently queried columns.

---

### **Next Steps**
Tomorrow, we’ll review some **advanced data handling techniques** to optimize the performance of your projects and explore error handling.

Let me know if you have any questions or need further assistance with the mini-project! 😊