# **Day 45: Python Modules and Standard Libraries**

Today, we’ll dive into **Python modules** and explore some **standard libraries** that can make your coding life easier. Modules are essentially pre-written Python code that you can import into your program to help you perform various tasks. You’ll also get familiar with a few built-in libraries like `math`, `datetime`, `os`, and others!

---

## **What You’ll Learn:**

### **1. What is a Module?**
A module is a file containing Python code, and it can define functions, variables, and classes. You can import and use the code inside any Python program. 

You can use built-in modules (which are already included in Python) or create your own custom modules.

#### **How to Import a Module:**
```python
import math
```
After importing, you can use functions or constants from the module, such as:
```python
result = math.sqrt(25)
print(result)  # Output: 5.0
```

### **2. Common Standard Libraries**
Python comes with a set of **standard libraries** that allow you to perform various tasks like handling dates, performing mathematical operations, and working with files. Some important standard libraries are:

- **`math`**: For mathematical operations.
- **`datetime`**: For working with dates and times.
- **`os`**: For interacting with the operating system (e.g., file manipulation).
- **`random`**: For generating random numbers.
- **`sys`**: For accessing system-specific parameters and functions.

---

## **Practice:**

### **1. Experiment with the `math` module:**
The `math` module has useful mathematical functions, constants, and operations. Here are a few examples:

#### **Example**:
```python
import math

# Square root
print(math.sqrt(16))  # Output: 4.0

# Pi constant
print(math.pi)  # Output: 3.141592653589793

# Factorial
print(math.factorial(5))  # Output: 120
```

### **2. Experiment with the `datetime` module:**
The `datetime` module allows you to work with dates and times. You can get the current date, time, or perform date arithmetic.

#### **Example**:
```python
import datetime

# Get today's date
today = datetime.date.today()
print("Today's date:", today)  # Output: e.g., 2025-03-16

# Get the current time
now = datetime.datetime.now()
print("Current time:", now.strftime("%H:%M:%S"))  # Output: current time in HH:MM:SS format
```

### **3. Experiment with the `random` module:**
The `random` module generates random numbers, which can be useful for various tasks like games or simulations.

#### **Example**:
```python
import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print(random_number)  # Output: a random number between 1 and 10
```

### **4. Experiment with the `os` module:**
The `os` module provides functions to interact with the operating system, such as getting the current working directory or listing files in a directory.

#### **Example**:
```python
import os

# Get the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

# List files in the current directory
files = os.listdir()
print("Files in the current directory:", files)
```

---

## **Review:**
- Modules allow you to reuse code and perform tasks without reinventing the wheel.
- The `math`, `datetime`, `random`, and `os` modules are great for various tasks.
- Practice by experimenting with these modules to familiarize yourself with their functions.

---

### **What’s Next?**
Tomorrow, you’ll learn how to **create your own custom modules** and keep your code well-organized. You’ll start writing your own reusable code that you can import into different projects!

Let me know if you have any questions! 😊