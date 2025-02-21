# **Day 2: Variables and Data Types**  

## **1️⃣ What Are Variables?**  
A **variable** is like a labeled box that stores data. It allows you to store and reuse values in your program.  

### **Example:**  
```python
name = "Alice"
age = 25
height = 5.6
```
Here:  
- `name` stores a **string** (`"Alice"`)  
- `age` stores an **integer** (`25`)  
- `height` stores a **float** (`5.6`)  

---

## **2️⃣ Data Types in Python**  

| **Type**     | **Example**            | **Description**                          |
|-------------|------------------------|------------------------------------------|
| **String**  | `"Hello"`               | Text, always inside quotes (`""` or `''`) |
| **Integer** | `10`, `-5`, `1000`      | Whole numbers                           |
| **Float**   | `3.14`, `-0.5`, `2.0`   | Numbers with decimal points             |
| **Boolean** | `True`, `False`         | Represents `True` or `False` values     |

---

## **3️⃣ Assigning Variables**
You can assign values to variables using `=`:
```python
city = "New York"
score = 99
pi = 3.1415
is_raining = False
```

✅ Python is **dynamically typed**, so you don’t need to specify the type. The interpreter figures it out.

---

## **4️⃣ Printing Variables**  
Use `print()` to display variable values:  
```python
name = "Bob"
age = 30
print(name)
print(age)
```
**Output:**  
```
Bob
30
```

You can combine strings using **f-strings**:  
```python
print(f"My name is {name} and I am {age} years old.")
```
**Output:**  
```
My name is Bob and I am 30 years old.
```

---

## **5️⃣ Changing Variable Values**
Variables can be updated:
```python
x = 10
print(x)  # Output: 10

x = 20
print(x)  # Output: 20
```

---

## **6️⃣ Taking User Input**
Use `input()` to get data from the user:
```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

All `input()` values are strings. Convert them when needed:
```python
age = int(input("Enter your age: "))  # Converts input to an integer
print(f"Next year, you’ll be {age + 1} years old!")
```

---

## **🛠️ Practice Task**
1. **Create variables** for your name, age, and favorite color. Print them.
2. Ask the user for their **favorite number**, double it, and print the result.
3. Write a program that **asks for the user’s birth year** and calculates their current age.

---

## **🔍 Reflection & Questions**
- What’s the difference between `int`, `float`, and `string`?  
- What happens if you try to add a number and a string? (`"5" + 5`)  
- Try assigning different values to the same variable. What happens?  

---

### **In day 3: we will work on Lists, Tuples & Basic List Operations**  
Get ready to work with collections of data! 🚀  

Let me know if you have any questions. 😊
