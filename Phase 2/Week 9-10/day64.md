# **Day 64: Handling CSV/Excel Files: Reading & Writing Data**  

In today’s lesson, you’ll learn how to handle CSV and Excel files, which are common formats for data storage and manipulation. This is a very useful skill when working with real-world datasets.

---

## **1️⃣ Handling CSV Files**

### **What is a CSV file?**
A **CSV (Comma Separated Values)** file is a text file where each line represents a record, and each field (or column) in that record is separated by a comma. It’s a simple format used to store tabular data.

### **1.1 Reading CSV Files**

To read CSV files in Python, we will use the **`csv`** module. Here’s how you can do it:

```python
import csv

# Open the CSV file in read mode
with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Loop through the rows and print each one
    for row in csv_reader:
        print(row)
```

In the example above, each **`row`** is a list of values corresponding to the fields in the CSV file. This will print each row of the CSV file as a list.

---

### **1.2 Writing to CSV Files**

You can write data to CSV files using the `csv.writer()` method. Here’s an example:

```python
import csv

# Data to write
data = [["name", "age", "city"], ["Alice", 25, "New York"], ["Bob", 30, "Chicago"]]

# Open a new CSV file to write
with open('output.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Write the data to the file
    csv_writer.writerows(data)
```

In this example, we are writing a list of lists (`data`) to a new file `output.csv`. The `writerows()` method writes multiple rows at once.

---

## **2️⃣ Handling Excel Files**

### **What is an Excel File?**
An **Excel** file is typically used for more complex data with multiple sheets. In Python, we often use the `pandas` library to read/write Excel files.

### **2.1 Reading Excel Files**

First, install the `pandas` and `openpyxl` libraries if you don’t have them:

```bash
pip install pandas openpyxl
```

To read an Excel file with `pandas`:

```python
import pandas as pd

# Read the Excel file
df = pd.read_excel('data.xlsx')

# Print the first few rows of the file
print(df.head())
```

The `df.head()` function shows the first 5 rows of the data in the Excel sheet.

---

### **2.2 Writing to Excel Files**

You can also write data to Excel files using `pandas`:

```python
import pandas as pd

# Sample DataFrame to write to Excel
data = {'name': ['Alice', 'Bob'], 'age': [25, 30], 'city': ['New York', 'Chicago']}
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
```

The `index=False` argument ensures that the row index is not included in the output Excel file.

---

## **🛠️ Practice Tasks**

Now that you’ve learned how to handle CSV and Excel files, let’s put your skills to the test!

### **Task 1: Read a CSV File**
1. Create a CSV file with the following data:
   ```
   name, age, city
   Alice, 25, New York
   Bob, 30, Chicago
   Charlie, 28, San Francisco
   ```
2. Write a Python program to read the file and print each row.

### **Task 2: Write to a CSV File**
1. Write a Python program that creates a CSV file containing the names of your favorite movies and their release years.
2. Example data to write:
   ```
   title, year
   The Matrix, 1999
   Inception, 2010
   The Dark Knight, 2008
   ```

### **Task 3: Read an Excel File**
1. Download any simple Excel file (e.g., a sheet containing product data).
2. Write a Python program to read the file using `pandas` and display the first 5 rows.

### **Task 4: Write to an Excel File**
1. Create a DataFrame with product names and their prices.
2. Write the DataFrame to an Excel file using `pandas`.

---

## **Tips for Success**
- Always ensure the file paths are correct when opening files.
- If the data in your file is too large to fit into memory, you can read it in **chunks** using `pandas.read_csv()` with the `chunksize` parameter.

---

### **Next Steps**  
Tomorrow, we’ll dive into **SQL** and **database queries**, which will help you build a more powerful backend for your projects. But for now, focus on practicing these file-handling skills.

Let me know if you run into any issues or need further clarification! 😊