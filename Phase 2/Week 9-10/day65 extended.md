Let's dive deeper into **SQL basics** and provide **extended examples**, **explanations**, and **practice tasks** for each of the concepts covered on Day 65.

---

## **1️⃣ SQL: Basic Queries and Operations**

### **1.1 SELECT: Retrieving Data**
The `SELECT` statement is used to query and retrieve data from one or more tables in a database. It allows you to specify which columns to retrieve, and optionally, which records to filter using the `WHERE` clause.

#### **Extended Example 1: Basic SELECT**
```sql
SELECT name, age FROM users;
```
This will return the **name** and **age** columns for all records in the **users** table. If there are 100 records in the table, this query will display all of them with only the **name** and **age**.

#### **Extended Example 2: Using SELECT with WHERE**
```sql
SELECT * FROM users WHERE age > 25;
```
This query retrieves all columns (`*`) from the **users** table, but only for users who are **older than 25**.

#### **Extended Example 3: SELECT with AND/OR Conditions**
```sql
SELECT name, city FROM users WHERE age > 20 AND city = 'New York';
```
This query will return the **name** and **city** of users who are older than 20 **and** live in **New York**.

---

### **1.2 WHERE: Filtering Data**
The `WHERE` clause is used to filter records based on specified conditions. You can use logical operators like `AND`, `OR`, and `NOT` for complex conditions.

#### **Extended Example 1: Filtering with WHERE**
```sql
SELECT * FROM users WHERE age < 30;
```
This query selects all records where the **age** is less than 30. It will return the full row data for all users under 30.

#### **Extended Example 2: Filtering with String Matching**
```sql
SELECT name, city FROM users WHERE city LIKE 'New%';
```
The **`LIKE`** keyword is used to search for a pattern. This query selects the **name** and **city** columns where the **city** starts with the string "New" (e.g., "New York", "New Jersey").

#### **Extended Example 3: Filtering with IN**
```sql
SELECT * FROM users WHERE city IN ('New York', 'Chicago');
```
The `IN` operator is useful when you want to match a column's value against a list of values. This query retrieves all users who live in either **New York** or **Chicago**.

---

### **1.3 INSERT INTO: Adding Data**
The `INSERT INTO` statement is used to add new records into a table. It can insert one or multiple rows at a time.

#### **Extended Example 1: Inserting a Single Record**
```sql
INSERT INTO users (name, age, city) VALUES ('Alice', 25, 'Los Angeles');
```
This query inserts a new row into the **users** table with the **name** "Alice", **age** 25, and **city** "Los Angeles".

#### **Extended Example 2: Inserting Multiple Records**
```sql
INSERT INTO users (name, age, city) VALUES 
('Bob', 30, 'Chicago'),
('Charlie', 22, 'San Francisco'),
('David', 35, 'New York');
```
This query inserts **three** new records into the **users** table at once.

#### **Extended Example 3: Inserting Data from Another Table**
```sql
INSERT INTO users (name, age, city)
SELECT name, age, city FROM temp_users WHERE age > 25;
```
Here, data is inserted from the `temp_users` table into the `users` table, but only for users who are older than 25.

---

### **1.4 UPDATE: Modifying Data**
The `UPDATE` statement is used to modify existing records in a table. It’s often combined with the `WHERE` clause to specify which records to update.

#### **Extended Example 1: Updating a Single Column**
```sql
UPDATE users SET age = 26 WHERE name = 'Alice';
```
This query updates the **age** of the user named **Alice** to **26**.

#### **Extended Example 2: Updating Multiple Columns**
```sql
UPDATE users SET age = 32, city = 'Boston' WHERE name = 'Bob';
```
This query updates both the **age** and **city** of the user named **Bob**.

#### **Extended Example 3: Conditional Update with JOIN**
```sql
UPDATE users SET age = 40
WHERE name IN (SELECT name FROM managers WHERE department = 'HR');
```
This query updates the **age** of all users who are also in the **HR** department (as per data in a **managers** table).

---

### **1.5 DELETE: Removing Data**
The `DELETE` statement is used to remove records from a table based on a condition.

#### **Extended Example 1: Deleting a Single Record**
```sql
DELETE FROM users WHERE name = 'Alice';
```
This query deletes the record for the user named **Alice**.

#### **Extended Example 2: Deleting Multiple Records**
```sql
DELETE FROM users WHERE age < 18;
```
This query deletes all users who are younger than **18** from the **users** table.

#### **Extended Example 3: Deleting All Records**
```sql
DELETE FROM users;
```
This query deletes **all** records from the **users** table. Be cautious with this one!

---

## **2️⃣ Practice Tasks**

### **Task 1: Create and Query a Database**

1. **Create a table `employees`** with the following columns:
   - `id` (integer, primary key)
   - `name` (text)
   - `age` (integer)
   - `department` (text)

2. **Insert 3 records** into the `employees` table:
   - `('John', 28, 'Sales')`
   - `('Jane', 34, 'Marketing')`
   - `('Jim', 22, 'Sales')`

3. **Query** all employees who are in the `Sales` department.

4. **Update** the `age` of `John` to `29`.

5. **Delete** the record of the employee in the `Marketing` department.

---

### **Task 2: Query Data with Conditions**

1. Create a table **`products`** with the following columns:
   - `product_id` (integer, primary key)
   - `name` (text)
   - `price` (decimal)
   - `category` (text)

2. **Insert 5 records** with product names, prices, and categories (e.g., 'Laptop', 'Shoes', 'TV', 'Phone', 'Headphones').

3. **Query** the names and prices of products where the price is greater than 100.

4. **Query** products in the `Electronics` category that cost less than 500.

---

### **Task 3: Modify Data**

1. Create a table **`students`** with columns:
   - `student_id` (integer, primary key)
   - `name` (text)
   - `grade` (text)
   - `age` (integer)

2. **Insert 4 student records** with `name`, `grade`, and `age`.

3. **Update** the grade of the student named `Alice` to `A+`.

4. **Delete** students who are older than 18.

---

## **3️⃣ Tips for Working with SQL**

- **Use `LIMIT`** when you only want to fetch a certain number of records. Example: `SELECT * FROM users LIMIT 5;`.
- **Back up your database** before running `DELETE` queries if you're working on production data.
- Always use **parameterized queries** (placeholders like `?`) when inserting data to prevent **SQL injection** vulnerabilities.

---

### **Next Steps**
Tomorrow, we will go deeper into handling databases, working with advanced data operations, and applying more complex SQL queries. Let me know if you need help with any of the tasks, and happy coding! 😊