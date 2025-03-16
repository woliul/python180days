# **Day 65: Intro to SQL: Basic SQL Queries & Database Concepts**

Today, we’ll introduce you to **SQL (Structured Query Language)**, the language used to interact with databases. You’ll learn how to perform basic database operations using SQL, and we’ll work with SQLite, which is a simple, lightweight database engine that comes built-in with Python.

---

## **1️⃣ What is SQL?**

**SQL** is a standard language for managing and manipulating relational databases. It allows you to perform operations like:
- Retrieving data
- Inserting new data
- Updating existing data
- Deleting data

Relational databases store data in tables (think of spreadsheets), where each table contains rows and columns. Each row represents a record, and each column represents an attribute of the record.

---

## **2️⃣ Basic SQL Queries**

### **2.1 SELECT: Retrieve Data**
The **SELECT** statement is used to query data from a table.

```sql
SELECT column1, column2 FROM table_name;
```

**Example:**
```sql
SELECT name, age FROM users;
```
This query retrieves the `name` and `age` columns from the `users` table.

If you want to retrieve all columns, use `*`:
```sql
SELECT * FROM users;
```

### **2.2 WHERE: Filter Data**
The **WHERE** clause filters records based on a condition.

```sql
SELECT * FROM users WHERE age > 25;
```
This query retrieves all columns from the `users` table where the age is greater than 25.

### **2.3 INSERT INTO: Add Data**
The **INSERT INTO** statement is used to add new records into a table.

```sql
INSERT INTO table_name (column1, column2, column3) VALUES (value1, value2, value3);
```

**Example:**
```sql
INSERT INTO users (name, age, city) VALUES ('Alice', 30, 'New York');
```

This adds a new record into the `users` table with the values `'Alice'`, `30`, and `'New York'`.

### **2.4 UPDATE: Modify Data**
The **UPDATE** statement modifies existing records in a table.

```sql
UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
```

**Example:**
```sql
UPDATE users SET age = 31 WHERE name = 'Alice';
```

This updates the `age` of the user named `'Alice'` to `31`.

### **2.5 DELETE: Remove Data**
The **DELETE** statement removes records from a table.

```sql
DELETE FROM table_name WHERE condition;
```

**Example:**
```sql
DELETE FROM users WHERE age < 18;
```

This deletes records from the `users` table where the `age` is less than 18.

---

## **3️⃣ Using SQLite in Python**

**SQLite** is a simple, file-based database engine. It’s perfect for small projects and is built into Python via the `sqlite3` module.

### **3.1 Create a Database and Table**

First, let’s create a database and a table:

```python
import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table called 'users'
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
```

### **3.2 Inserting Data into SQLite**

To insert data into the `users` table:

```python
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Insert a record
cursor.execute('''
INSERT INTO users (name, age, city)
VALUES ('Alice', 30, 'New York')
''')

# Commit and close
conn.commit()
conn.close()
```

### **3.3 Querying Data from SQLite**

Now, let’s query the data from the `users` table:

```python
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Select all records from 'users'
cursor.execute('SELECT * FROM users')

# Fetch all results
results = cursor.fetchall()

# Print each result
for row in results:
    print(row)

conn.close()
```

This will print all records from the `users` table.

---

## **🛠️ Practice Tasks**

### **Task 1: Create a Database**
1. Create a new SQLite database called `school.db` and create a table called `students` with the columns: `id`, `name`, `age`, and `grade`.

### **Task 2: Insert Data**
1. Insert at least three student records into the `students` table. Include values for `name`, `age`, and `grade`.

### **Task 3: Query Data**
1. Write an SQL query to select all students whose `age` is greater than 20.
2. Write an SQL query to select all students with a `grade` of `'A'`.

### **Task 4: Update Data**
1. Write an SQL query to update the `age` of a student with `id = 2` to `22`.

### **Task 5: Delete Data**
1. Write an SQL query to delete a student with `id = 3` from the `students` table.

---

## **Tips for Success**
- When running SQL queries, make sure to **commit** changes using `conn.commit()` so that your changes are saved to the database.
- Use **parameterized queries** (using placeholders like `?`) to avoid SQL injection vulnerabilities in real-world applications.

---

### **Next Steps**
Tomorrow, we'll dive deeper into combining SQL with file data for data analysis and handling more advanced data operations.

Let me know if you have any questions or need further assistance! 😊