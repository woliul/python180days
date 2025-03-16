# **Day 68: Review and Debugging Session for Data Projects**

Today is a **review and debugging day**, where we’ll focus on refining your data projects, solving common issues, and reviewing techniques to troubleshoot and optimize your code.

---

## **1️⃣ Reviewing Data Projects**

Let's take a step back and review the data-related projects you've worked on so far. Here are some points to consider as you review your work:

### **1.1 Project Structure**
- **Database Design:** Is your database normalized? Are the tables logically structured?
  - Make sure you separate data into multiple tables where necessary, using foreign keys to establish relationships.
  - Avoid storing repetitive data in one table. For example, instead of storing the same product details in every order, store the product details in a separate `products` table and reference it in the `orders` table using a product ID.

### **1.2 Data Integrity**
- **Consistency:** Have you ensured the consistency of your data? Are there any rows with null or invalid values?
  - Consider using **constraints** such as `NOT NULL`, `UNIQUE`, and `CHECK` when creating tables to enforce data integrity.

  Example of creating a table with constraints:
  ```sql
  CREATE TABLE products (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      price REAL CHECK (price > 0),
      quantity_in_stock INTEGER CHECK (quantity_in_stock >= 0)
  );
  ```

### **1.3 Code Quality**
- **Clarity:** Is your code clean and easy to understand? Are you using meaningful variable names, and are your functions and methods well-organized?
- **Reusability:** Is your code reusable? Can you extract portions of it into functions or modules that can be reused in other projects?

---

## **2️⃣ Common Debugging Techniques**

In any project, you’ll run into bugs and issues. Here are some common debugging techniques to help you identify and fix problems.

### **2.1 Use of Print Statements**
One of the simplest ways to debug code is by using **print statements**. If your code isn't behaving as expected, insert print statements to check the flow of execution and the values of variables at different points.

Example:
```python
print(f"Product Name: {product_name}, Price: {product_price}")
```

This will give you insights into where the issue might be happening.

### **2.2 Using a Debugger**
Python comes with a built-in debugger called **`pdb`** (Python Debugger), which allows you to set breakpoints and step through your code line by line.

Here’s how you can use it:

1. Import `pdb` at the top of your script:
   ```python
   import pdb
   ```

2. Add `pdb.set_trace()` where you want to start debugging:
   ```python
   pdb.set_trace()
   ```

When the code execution reaches this point, the program will pause, and you'll enter an interactive debugger session. You can inspect variables, run commands, and step through the code.

### **2.3 Use of Exception Handling**
As discussed before, using **`try-except`** blocks can help identify errors and prevent crashes. To get more detailed information about the error, print the error message:

```python
try:
    # Your code
except Exception as e:
    print(f"Error: {e}")
```

This will give you the exact error message, which can be incredibly helpful in identifying what went wrong.

### **2.4 Logging**
Sometimes, you may want to log messages for later inspection, especially in larger projects. The **`logging`** module allows you to log messages at different severity levels (INFO, WARNING, ERROR, etc.).

Example:
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
```

You can review logs to track down where things are going wrong, especially in larger applications.

---

## **3️⃣ Common Issues and Solutions**

Here are some common problems you may encounter and how to fix them:

### **3.1 SQL Syntax Errors**
- **Issue:** Incorrect SQL syntax.
  - **Solution:** Double-check your SQL queries for typos or missing keywords. Remember, SQL keywords like `SELECT`, `FROM`, and `WHERE` should always be in uppercase.

### **3.2 Missing or Invalid Data**
- **Issue:** The program is inserting invalid or missing data into the database.
  - **Solution:** Add validation before inserting data into the database. Ensure that no `NULL` values are inserted into columns that require data. Use `CHECK` constraints to enforce valid values.

### **3.3 Slow Query Performance**
- **Issue:** Queries are taking too long to execute.
  - **Solution:** Optimize your SQL queries by:
    - Adding **indexes** on frequently queried columns.
    - Using **LIMIT** and **OFFSET** to paginate large results.
    - Avoiding **SELECT *;** and instead selecting only the columns you need.
    - Breaking large queries into smaller ones if needed.

---

## **4️⃣ Best Practices for Debugging and Review**

Here are some best practices for debugging and reviewing your code and projects:

### **4.1 Keep Track of Changes**
When working on a project, especially as it grows in complexity, it’s important to **keep track of your changes**. Use a **version control system** like **Git** to keep track of your code changes. This allows you to revert to a previous version if something goes wrong.

### **4.2 Write Unit Tests**
Testing is an essential part of any development process. Writing **unit tests** ensures that your code works as expected and helps catch bugs early on.

For example, if you have a function that calculates the total stock value (price * quantity_in_stock), you can write a test to check if the function works correctly:

```python
import unittest

class TestStockValueCalculation(unittest.TestCase):
    def test_stock_value(self):
        self.assertEqual(calculate_stock_value(10, 20), 200)
        
if __name__ == '__main__':
    unittest.main()
```

### **4.3 Review and Refactor**
Always **review** your code after completing a task or a project. Refactor it to improve readability and performance. Look for areas where you can:
- Optimize loops
- Simplify functions
- Improve variable names

---

## **🛠️ Practice Tasks**

### **Task 1: Debug Your Project**
1. Review your previous projects and check for any areas where the code could be improved or optimized.
2. Add error handling (e.g., try-except blocks) to ensure your program runs smoothly even when things go wrong.
3. Use **print statements** or a **debugger** to find and fix any bugs.

### **Task 2: Refactor Code**
1. Refactor your code for better readability and efficiency. Try using smaller, reusable functions and simplifying complex code.

### **Task 3: Write Unit Tests**
1. Write unit tests for some of your functions to ensure they work correctly.

---

## **Tips for Success**
- Debugging can be a challenging process, but with patience and the right tools, you can solve any issue.
- Keep your code organized and easy to understand by following best practices and refactoring regularly.
- Unit tests and version control can save you time and effort in the long run.

---

### **Next Steps**
Tomorrow, we’ll dive into more advanced data manipulation techniques, focusing on handling more complex data structures and performing more sophisticated analysis.

Let me know if you need help with anything or have any questions! 😊