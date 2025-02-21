# **Day 5: Conditionals & Comparison Operators**  

Today, you’ll learn how to make decisions in your Python programs using **if-else statements** and **comparison operators**.  

---

## **1️⃣ What Are Conditionals?**  
Conditionals allow your program to make **decisions** based on certain conditions.  

### **Example: Checking if Someone is Old Enough to Vote**  
```python
age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```
✅ If the condition (`age >= 18`) is **True**, the first block runs. Otherwise, the `else` block runs.  

---

## **2️⃣ Comparison Operators**  
These operators **compare values** and return `True` or `False`.  

| **Operator** | **Description**           | **Example**        | **Result** |
|-------------|---------------------------|--------------------|------------|
| `==`        | Equal to                   | `5 == 5`          | `True`     |
| `!=`        | Not equal to               | `5 != 3`          | `True`     |
| `>`         | Greater than               | `10 > 5`          | `True`     |
| `<`         | Less than                  | `3 < 7`           | `True`     |
| `>=`        | Greater than or equal to   | `5 >= 5`          | `True`     |
| `<=`        | Less than or equal to      | `4 <= 6`          | `True`     |

---

## **3️⃣ If-Elif-Else: Multiple Conditions**  
Use `elif` (else-if) when checking multiple conditions.  

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

✅ Python **checks conditions in order**. If one condition is `True`, the rest are skipped.  

---

## **4️⃣ Logical Operators (AND, OR, NOT)**  
Logical operators help combine multiple conditions.  

| **Operator** | **Description**        | **Example**                     | **Result** |
|-------------|------------------------|--------------------------------|------------|
| `and`       | Both conditions must be `True` | `x > 5 and x < 10`   | `True` if `x` is 6-9 |
| `or`        | At least one condition is `True` | `x == 5 or x == 10` | `True` if `x` is 5 or 10 |
| `not`       | Reverses `True` to `False` | `not(x > 5)`         | `True` if `x <= 5` |

### **Example: Checking Login Credentials**
```python
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Access granted!")
else:
    print("Access denied.")
```

✅ **Both conditions must be True** for access to be granted.

---

## **5️⃣ Nested If Statements**  
You can have `if` statements inside other `if` statements.  

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can enter.")
    else:
        print("You need an ID.")
else:
    print("You are too young.")
```

---

## **🛠️ Practice Task**
1. **Write a program** that asks the user for a number and prints whether it is **positive, negative, or zero**.  
2. **Create a grading system** that takes input from the user and prints `"A"`, `"B"`, `"C"`, or `"Fail"`.  
3. **Check if a number is even or odd** using `if-else`.  

---

## **🔍 Reflection & Questions**
- What happens if you forget to use `elif` and only use `if`?  
- When should you use `and` vs `or`?  
- Try experimenting with different values—how does your program behave?  

---

### **Next: Combining Variables & Data Structures**  
Get ready for a mix of everything you’ve learned so far! 🚀  

Let me know if you have any questions. 😊