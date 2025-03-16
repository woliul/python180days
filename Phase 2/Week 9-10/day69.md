# **Day 69: Extra Exercises on APIs, Data Manipulation, & SQL**

Today, we’ll focus on extra exercises to reinforce everything you’ve learned so far. We’ll tackle:
- More advanced exercises with **APIs**.
- Performing **data manipulation** using **Python** and **SQL**.
- Solving challenging SQL queries.

This is your chance to consolidate your knowledge, test your skills, and challenge yourself with real-world tasks.

---

## **1️⃣ Working with APIs**

APIs (Application Programming Interfaces) allow different software systems to communicate with each other. Python makes it easy to interact with APIs using the **`requests`** library.

### **Exercise 1: Fetching Data from a Public API**

Let’s start by working with a **public API**. We will use the **OpenWeatherMap** API to fetch weather data for a given city.

### **Steps:**
1. **Get an API key** by signing up for a free account on [OpenWeatherMap](https://openweathermap.org/api).
2. **Install `requests`** if you haven't already:  
   ```bash
   pip install requests
   ```

3. **Fetch weather data:**

Here’s how you can use the `requests` library to get weather data for a city:

```python
import requests

# Replace 'your_api_key' with the actual API key you get from OpenWeatherMap
api_key = 'your_api_key'
city = 'London'

# Create the API URL
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Fetch the data
response = requests.get(url)
data = response.json()

# Extract weather information
temperature = data['main']['temp']
weather_description = data['weather'][0]['description']

print(f"Temperature: {temperature}K")
print(f"Weather: {weather_description}")
```

### **Task 1: Modify the Program**
- Modify the program to fetch the weather for multiple cities (e.g., New York, Paris, Tokyo).
- Print out the temperature in Celsius instead of Kelvin.
- Add error handling for situations where the API might not return data (e.g., invalid city name).

---

## **2️⃣ Advanced Data Manipulation in Python**

### **Exercise 2: Manipulating Data with Pandas**

Let’s continue working with **Pandas**, which is excellent for data manipulation and analysis.

Let’s say we have a CSV file `sales_data.csv` with sales information for a company. The columns are: `date`, `product`, `amount`, and `region`.

Example data:
```csv
date, product, amount, region
2025-03-01, Laptop, 1200, North
2025-03-01, Phone, 600, South
2025-03-02, Tablet, 800, East
2025-03-02, Laptop, 1300, North
```

### **Steps:**
1. **Load the Data into a DataFrame:**
   
```python
import pandas as pd

# Load CSV data into a Pandas DataFrame
df = pd.read_csv('sales_data.csv')

# Display the first few rows of the DataFrame
print(df.head())
```

2. **Data Manipulation:**
   - **Filter data by region:**
   ```python
   north_sales = df[df['region'] == 'North']
   print(north_sales)
   ```

   - **Calculate the total sales for each product:**
   ```python
   total_sales = df.groupby('product')['amount'].sum()
   print(total_sales)
   ```

   - **Sort the products by total sales in descending order:**
   ```python
   sorted_sales = total_sales.sort_values(ascending=False)
   print(sorted_sales)
   ```

   - **Convert `date` to a datetime object and filter sales by month:**
   ```python
   df['date'] = pd.to_datetime(df['date'])
   march_sales = df[df['date'].dt.month == 3]
   print(march_sales)
   ```

### **Task 2: Modify the Program**
- Add more products to the `sales_data.csv` file.
- Calculate the average sales amount per region.
- Write the manipulated data back to a new CSV file: `manipulated_sales_data.csv`.

---

## **3️⃣ Advanced SQL Queries**

Now that you’ve worked with databases and SQL, let’s tackle some advanced SQL queries to further hone your skills.

### **Exercise 3: Advanced SQL Queries**

Let’s assume you have a database with two tables: `orders` and `customers`.

**`orders` table:**
| order_id | customer_id | product_name | price | quantity | order_date |
|----------|-------------|--------------|-------|----------|------------|
| 1        | 1           | Laptop       | 1000  | 2        | 2025-03-01 |
| 2        | 2           | Phone        | 600   | 1        | 2025-03-02 |

**`customers` table:**
| customer_id | customer_name |
|-------------|---------------|
| 1           | Alice         |
| 2           | Bob           |

1. **Find the total sales (price * quantity) for each customer.**
   ```sql
   SELECT customers.customer_name, SUM(orders.price * orders.quantity) AS total_sales
   FROM orders
   JOIN customers ON orders.customer_id = customers.customer_id
   GROUP BY customers.customer_name;
   ```

2. **Find the customer who has spent the most.**
   ```sql
   SELECT customers.customer_name, SUM(orders.price * orders.quantity) AS total_spent
   FROM orders
   JOIN customers ON orders.customer_id = customers.customer_id
   GROUP BY customers.customer_name
   ORDER BY total_spent DESC
   LIMIT 1;
   ```

3. **Find all customers who have made orders in the last 30 days.**
   ```sql
   SELECT customers.customer_name
   FROM orders
   JOIN customers ON orders.customer_id = customers.customer_id
   WHERE orders.order_date >= DATE('now', '-30 days');
   ```

4. **Find the most popular product (based on the quantity sold).**
   ```sql
   SELECT product_name, SUM(quantity) AS total_quantity
   FROM orders
   GROUP BY product_name
   ORDER BY total_quantity DESC
   LIMIT 1;
   ```

### **Task 3: Modify the Queries**
- Modify the queries above to:
  - Calculate the **average** sales per customer.
  - Retrieve customers who have spent more than a certain amount (e.g., $1000).
  - Find the **least popular product** (based on quantity sold).

---

## **4️⃣ Combining SQL and Python for Data Analysis**

Now that you’ve worked on data analysis with both Pandas and SQL, try combining these tools. You can fetch data from a database, load it into a Pandas DataFrame, and perform further analysis using Python.

Here’s an example of how to fetch data from an SQLite database and analyze it with Pandas:

```python
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('store.db')

# Query the database
query = 'SELECT * FROM orders'
df = pd.read_sql(query, conn)

# Perform data analysis with Pandas
top_products = df.groupby('product_name')['quantity'].sum().sort_values(ascending=False)
print(top_products)

# Close the connection
conn.close()
```

---

## **🛠️ Practice Tasks**

### **Task 1: Work with APIs**
1. Write a program that fetches the current weather for your city using the OpenWeatherMap API and prints out the temperature in Celsius, the weather description, and the wind speed.
2. Modify the program to allow users to input any city and retrieve the weather information for that city.

### **Task 2: Data Manipulation with Pandas**
1. Add additional data to your `sales_data.csv` file (e.g., different regions, more products).
2. Calculate and print the **total sales per product** and **average sales per region** using Pandas.

### **Task 3: Advanced SQL Queries**
1. Work with a database (you can create your own `orders` and `customers` tables or use the provided examples).
2. Write and run SQL queries to find the **total sales per customer**, **the most popular product**, and **customers who spent the most**.

---

## **Tips for Success**
- APIs are powerful for retrieving live data and integrating external services into your projects.
- Pandas is a versatile library for performing data analysis and manipulation. Practice using its functions like `groupby()`, `sort_values()`, and `agg()` for more complex analyses.
- SQL is essential for data analysis, and understanding advanced queries like `JOIN`, `GROUP BY`, and `HAVING` will help you solve real-world problems efficiently.

---

### **Next Steps**
Tomorrow, we’ll focus on **reflecting** on all the work we’ve done this week and preparing for the next step in your Python learning journey.

Let me know if you need help with any of the exercises or have any questions! 😊