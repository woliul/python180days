Let’s go over each technique in detail with **extended examples**, each including at least three variations for better understanding. 

---

### **1️⃣ Data Handling Optimization Techniques**

---

#### **1.1 Use of Indexes**

An **index** is used to speed up query performance. It helps the database find the rows that match a condition more quickly. Below are three examples using indexes in different scenarios.

**Example 1: Index on a single column**
- Indexing a column that is frequently used in **WHERE** clauses to speed up searches.

```sql
CREATE INDEX idx_users_name ON users (name);
```
This index speeds up queries like:
```sql
SELECT * FROM users WHERE name = 'Alice';
```

**Example 2: Index on multiple columns**
- Composite indexes are created on multiple columns when queries filter by multiple columns simultaneously.

```sql
CREATE INDEX idx_orders_user_id_price ON orders (user_id, price);
```
This index speeds up queries like:
```sql
SELECT * FROM orders WHERE user_id = 3 AND price > 100;
```

**Example 3: Index on a column with sorting**
- Creating an index on a column that is used in **ORDER BY** to improve sorting speed.

```sql
CREATE INDEX idx_products_price ON products (price);
```
This index optimizes queries like:
```sql
SELECT * FROM products ORDER BY price DESC;
```

---

#### **1.2 Batch Inserts**

Batch inserts help improve performance when inserting large volumes of data into a table.

**Example 1: Using `executemany()` for batch inserts**
- Instead of inserting one row at a time, use `executemany()` to insert multiple rows in one go.

```python
# Batch insert data using executemany
data = [('Alice', 30, 'New York'), ('Bob', 25, 'Los Angeles'), ('Charlie', 35, 'Chicago')]
cursor.executemany('''
INSERT INTO users (name, age, city) VALUES (?, ?, ?)
''', data)
conn.commit()
```

**Example 2: Insert data from a CSV file in batches**
- Reading from a CSV and inserting data in batches can improve efficiency when dealing with large datasets.

```python
import csv

# Batch insert from CSV
with open('large_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    data = [(row[0], int(row[1]), row[2]) for row in csv_reader]
    cursor.executemany('''
    INSERT INTO users (name, age, city) VALUES (?, ?, ?)
    ''', data)
    conn.commit()
```

**Example 3: Insert large amounts of data using a generator**
- Use a generator function to insert data in chunks, which is memory efficient for very large datasets.

```python
def batch_insert_data(batch_size=1000):
    with open('large_data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        batch = []
        for row in csv_reader:
            batch.append((row[0], int(row[1]), row[2]))
            if len(batch) >= batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

# Insert data in batches of 1000 rows
for batch in batch_insert_data(1000):
    cursor.executemany('''
    INSERT INTO users (name, age, city) VALUES (?, ?, ?)
    ''', batch)
    conn.commit()
```

---

#### **1.3 Use of Pandas for Handling Large Datasets**

Pandas is excellent for handling and processing large datasets before inserting them into the database.

**Example 1: Read and insert large CSV file using pandas**
- Read the entire CSV file into a pandas DataFrame, process the data, and then insert it into the database.

```python
import pandas as pd

df = pd.read_csv('large_dataset.csv')

# Data Transformation: Add a new column with modified values
df['new_column'] = df['existing_column'] * 2

# Insert data into the database
for row in df.itertuples():
    cursor.execute('''
    INSERT INTO table_name (column1, column2) VALUES (?, ?)
    ''', (row.column1, row.column2))
conn.commit()
```

**Example 2: Filtering and Processing Data**
- Use pandas to filter rows and process the data before inserting into the database.

```python
df = pd.read_csv('sales_data.csv')

# Filter data for rows where sales > 1000
df_filtered = df[df['sales'] > 1000]

# Insert the filtered data into the database
for row in df_filtered.itertuples():
    cursor.execute('''
    INSERT INTO sales (product, sales, date) VALUES (?, ?, ?)
    ''', (row.product, row.sales, row.date))
conn.commit()
```

**Example 3: Handling missing data**
- Use pandas to fill or drop missing values in a DataFrame before inserting into the database.

```python
df = pd.read_csv('customer_data.csv')

# Fill missing age values with the mean age
df['age'].fillna(df['age'].mean(), inplace=True)

# Insert cleaned data into the database
for row in df.itertuples():
    cursor.execute('''
    INSERT INTO customers (name, age, city) VALUES (?, ?, ?)
    ''', (row.name, row.age, row.city))
conn.commit()
```

---

### **2️⃣ Error Handling in Python**

---

#### **2.1 Try-Except Blocks**

Using **`try-except`** blocks can prevent your program from crashing and allow you to handle errors gracefully.

**Example 1: Handling database errors**
- Catching errors related to database connection and query execution.

```python
try:
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM non_existent_table')
except sqlite3.Error as e:
    print(f"Database error occurred: {e}")
finally:
    conn.close()
```

**Example 2: Handling file errors**
- Handle situations where the file may not exist or cannot be read.

```python
try:
    with open('non_existent_file.csv', 'r') as file:
        # Processing the file
        pass
except FileNotFoundError:
    print("The specified file was not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

**Example 3: Handling data integrity errors**
- Using error handling when inserting data to ensure the data is valid (e.g., avoiding duplicates or incorrect data types).

```python
try:
    cursor.execute('''
    INSERT INTO users (name, age, city) VALUES (?, ?, ?)
    ''', ('Alice', 'invalid_age', 'New York'))
    conn.commit()
except sqlite3.IntegrityError as e:
    print(f"Data Integrity error: {e}")
except Exception as e:
    print(f"Error: {e}")
```

---

#### **2.2 Handling File Errors**

**Example 1: Checking file existence**
- Ensure that the file exists before trying to read it.

```python
import os

file_path = 'data.csv'
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        # Process the file
        pass
else:
    print(f"File {file_path} does not exist!")
```

**Example 2: Using try-except to handle file read errors**
- Handle errors when reading a file.

```python
try:
    with open('data.csv', 'r') as file:
        # Read and process the file
        pass
except IOError:
    print("File could not be opened!")
except Exception as e:
    print(f"Unexpected error occurred: {e}")
```

**Example 3: Handling permission errors**
- Catch permission-related errors when trying to write to a file.

```python
try:
    with open('restricted_file.csv', 'w') as file:
        file.write("data")
except PermissionError:
    print("You don't have permission to write to this file!")
```

---

### **3️⃣ Optimizing SQL Queries**

---

#### **3.1 Use of Joins**

**Example 1: Basic `JOIN`**
- Combining data from two tables using an `INNER JOIN` to retrieve information from both.

```sql
SELECT users.name, orders.product_name, orders.quantity
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

**Example 2: Left Join**
- Using `LEFT JOIN` to include all rows from the `users` table, even if no matching rows exist in the `orders` table.

```sql
SELECT users.name, orders.product_name, orders.quantity
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

**Example 3: Multiple Joins**
- Joining more than two tables together.

```sql
SELECT users.name, orders.product_name, categories.category_name
FROM users
JOIN orders ON users.id = orders.user_id
JOIN categories ON orders.category_id = categories.id;
```

---

#### **3.2 Limit and Offset for Pagination**

**Example 1: Simple Pagination**
- Using `LIMIT` and `OFFSET` to fetch data in smaller chunks.

```sql
SELECT * FROM users LIMIT 10 OFFSET 20;
```

This query fetches the 21st to 30th rows from the `users` table.

**Example 2: Pagination with sorting**
- Combining `LIMIT`, `OFFSET`, and `ORDER BY` to paginate results with sorting.

```sql
SELECT * FROM products ORDER BY price DESC LIMIT 10 OFFSET 10;
```

This fetches the next 10 products ordered by price in descending order.

**Example 3: Dynamic Pagination**
- Using `LIMIT` and `OFFSET` for dynamic pagination in an application.

```python
page = 2
page_size = 10
offset = (page - 1) * page_size

cursor.execute(f'SELECT * FROM users LIMIT {page_size} OFFSET {offset}')
```

---

#### **3.3 Avoiding SELECT *** 

**Example 1: Specifying Columns**
- Instead of selecting all columns, specify only the columns you need.

```sql
SELECT name, age FROM users;
```

**Example 2: Avoiding large data fetch**
- Avoid fetching large amounts of unnecessary data (e.g., selecting all rows from a huge table).

```sql
SELECT name, email FROM users WHERE active = 1;
```

**Example 3: Select with aggregation**
- Only select aggregated data if you need a summary.

```sql
SELECT category, COUNT(*) FROM products GROUP BY category;
```

---

This comprehensive guide with extended examples should give you a solid understanding of each technique and its real-world application. Let me know if you have any further questions!