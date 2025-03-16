# **Day 67: Advanced Data Handling Techniques**

In today's lesson, we will dive into more **advanced data handling techniques** that can help you work efficiently with larger datasets, handle errors, and optimize your code for better performance.

---

## **1️⃣ Data Handling Optimization Techniques**

As you start working with larger datasets, it becomes crucial to handle them efficiently. Here are some strategies you can use:

### **1.1 Use of Indexes**

In SQL databases, **indexes** are used to speed up the retrieval of data. Without indexes, the database has to scan the entire table to retrieve data, which can be slow for large tables.

For example, if you're querying a `users` table frequently based on the `name` column, you should create an index on that column:

```sql
CREATE INDEX idx_users_name ON users (name);
```

### **1.2 Batch Inserts**

Inserting large amounts of data into a database one row at a time can be slow. You can speed up the process by **batch inserting** multiple rows at once:

```python
# Batch insert data
data = [('Alice', 30, 'New York'), ('Bob', 25, 'Los Angeles'), ('Charlie', 35, 'Chicago')]

cursor.executemany('''
INSERT INTO users (name, age, city) VALUES (?, ?, ?)
''', data)

conn.commit()
```

This approach is much faster than inserting one row at a time.

### **1.3 Use of Pandas for Handling Large Datasets**

When dealing with large datasets in Python, **`pandas`** is a powerful tool that can help you handle and process the data more efficiently.

You can use `pandas` to read large CSV files, perform data transformations, and then insert the data into your database:

```python
import pandas as pd

# Read large CSV file using pandas
df = pd.read_csv('large_dataset.csv')

# Do some data transformations
df['new_column'] = df['existing_column'] * 2

# Insert data into the database
for row in df.itertuples():
    cursor.execute('''
    INSERT INTO table_name (column1, column2) VALUES (?, ?)
    ''', (row.column1, row.column2))

conn.commit()
```

### **1.4 Avoiding Redundant Data**

To avoid redundancy and unnecessary storage, make sure you normalize your database. This means breaking data into smaller tables and linking them through relationships (foreign keys), rather than repeating data in one large table.

For example, instead of storing the full address for each order, you could store the address in a separate `addresses` table and link it to the `orders` table via a foreign key.

---

## **2️⃣ Error Handling in Python**

### **2.1 Try-Except Blocks**

Python’s **`try-except`** block is used to handle exceptions (errors) that may occur during execution. This is particularly useful when dealing with file I/O, database connections, and other operations that might fail.

Here’s how you can use it to handle database errors:

```python
try:
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    
    # Sample query that may fail
    cursor.execute('SELECT * FROM non_existent_table')
    conn.commit()

except sqlite3.Error as e:
    print(f"Error occurred: {e}")
    
finally:
    conn.close()
```

The `finally` block ensures that the database connection is closed, even if an error occurs.

### **2.2 Handling File Errors**

When working with files (like CSV or Excel), it’s important to handle cases where the file might not exist or be readable:

```python
try:
    with open('data.csv', 'r') as file:
        # Process the file
        pass
except FileNotFoundError:
    print("The file does not exist!")
except Exception as e:
    print(f"An error occurred: {e}")
```

This way, you prevent your program from crashing when a file is missing or corrupted.

---

## **3️⃣ Optimizing SQL Queries**

### **3.1 Use of Joins**

When you need to query multiple tables at once, you can use **joins**. Joins allow you to combine rows from two or more tables based on a related column.

For example, if you have a `users` table and an `orders` table, you can join them on the `user_id` column:

```sql
SELECT users.name, orders.product_name, orders.quantity
FROM users
JOIN orders ON users.id = orders.user_id;
```

This query will return the names of users and the products they ordered.

### **3.2 LIMIT and OFFSET for Pagination**

When dealing with large datasets, it’s a good idea to paginate the results instead of loading everything at once. You can use the `LIMIT` and `OFFSET` clauses in SQL for this:

```sql
SELECT * FROM users LIMIT 10 OFFSET 20;
```

This query will return the 21st to the 30th rows from the `users` table.

### **3.3 Avoiding SELECT ***

Instead of selecting all columns (`SELECT *`), specify the columns you need to avoid loading unnecessary data:

```sql
SELECT name, age FROM users;
```

This can significantly speed up queries, especially when working with large tables.

---

## **🛠️ Practice Tasks**

### **Task 1: Indexing**
1. Create an index on the `price` column in the `products` table and test the query performance by selecting products with prices greater than a certain value.

### **Task 2: Batch Insert**
1. Modify the code you used for inserting product data and try using `executemany()` for batch insertion. Compare the performance with inserting one row at a time.

### **Task 3: Error Handling**
1. Write a program that connects to a database and reads data from a table, using `try-except` blocks to handle any errors (e.g., incorrect table name).

### **Task 4: Optimizing Queries**
1. Modify a previous query to use `JOIN` to combine data from two related tables (e.g., `users` and `orders`).
2. Use `LIMIT` and `OFFSET` to fetch data in chunks from a large table.

---

## **Tips for Success**
- Always optimize your database queries for better performance, especially when working with large datasets.
- Use error handling to ensure your program runs smoothly even when things go wrong.

---

### **Next Steps**
Tomorrow, we’ll focus on reviewing your projects, debugging techniques, and refining your data handling skills.

Let me know if you have any questions or need further clarification on any topic! 😊