# **Day 17: Error Handling with Try-Except**  

Today, you'll learn how to **handle errors** in Python using `try-except` blocks. This prevents your program from crashing when something unexpected happens! 🚀  

---

## **1️⃣ Why Use Error Handling?**  
Without error handling, a simple mistake (like dividing by zero or entering a wrong input) can **crash** the program.  

Example **without** error handling:  
```python
num = int(input("Enter a number: "))  # If user enters a letter, this crashes!
print(10 / num)  # If num = 0, this crashes!
```
💥 **Crashes if:**  
- The user enters **non-numeric input**  
- The user enters **zero** (division error)  

---

## **2️⃣ Using Try-Except to Handle Errors**  
```python
try:
    num = int(input("Enter a number: "))  
    print(10 / num)  
except ValueError:
    print("Invalid input! Please enter a number.")  
except ZeroDivisionError:
    print("Cannot divide by zero!")
```
✅ **Now the program doesn't crash!**  

---

## **3️⃣ Using `finally` (Runs No Matter What)**
```python
try:
    file = open("data.txt", "r")  # Attempt to open a file
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing the file.")
```
✅ **`finally` always runs**, whether there's an error or not.  

---

## **4️⃣ Raising Custom Errors**  
You can force an error using `raise`:  
```python
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative!")
```
🚨 **Stops execution if the condition is met.**  

---

## **🛠️ Practice Tasks**  
1️⃣ **Write a program that asks for a number and handles these errors:**  
   - Invalid input (non-numeric)  
   - Division by zero  

2️⃣ **Modify a file-reading program** to handle a missing file error.  

3️⃣ **Create a function that raises an error** if the user enters a negative number for age.  

---

## **🔍 Reflection & Questions**  
- How does `try-except` improve **user experience**?  
- When should you use **finally**?  
- Why might **raising an error** be useful?  

---

### **Tomorrow: Reading & Writing Files (File I/O) 📂**  
You'll learn how to **read and write** files in Python!  

Let me know if you have any questions! 😊