# **Day 9: Functions – Definition, Calling, and Return Statements**  

Today, you’ll learn about **functions**, which allow you to write reusable blocks of code, making your programs more **efficient** and **organized**.  

---

## **1️⃣ What is a Function?**  
A **function** is a reusable block of code that performs a specific task. Instead of repeating the same code multiple times, you can **define a function once** and **call it whenever needed**.  

---

## **2️⃣ Defining and Calling a Function**  
### **Syntax:**
```python
def function_name():
    # Code inside the function
```
You **call** a function by writing its name followed by parentheses `()`.  

### **Example: Defining and Calling a Function**  
```python
def greet():
    print("Hello, welcome to Python!")

# Calling the function
greet()
```
**Output:**  
```
Hello, welcome to Python!
```
✅ Functions help you **avoid repetition** and **organize** your code.

---

## **3️⃣ Function with Parameters**  
Functions can take **parameters** (inputs) to make them more flexible.

### **Example: Function with One Parameter**  
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
```
**Output:**  
```
Hello, Alice!  
Hello, Bob!  
```
✅ Parameters allow functions to **handle different values** dynamically.

---

## **4️⃣ Return Statement**  
The `return` keyword **sends back a result** from the function.  

### **Example: Function That Returns a Value**
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```
**Output:**  
```
8
```
✅ **Without `return`**, the function performs a task but does not give back a value.

---

## **5️⃣ Default Parameter Values**  
You can provide **default values** for function parameters.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()        # Uses default value
greet("Sam")   # Uses given argument
```
**Output:**  
```
Hello, Guest!  
Hello, Sam!  
```
✅ Default parameters **make functions more flexible**.

---

## **🛠️ Practice Task**  
1. Write a function that **takes two numbers** as input and returns their product.  
2. Create a function that **returns the square** of a given number.  
3. Write a function that greets a user with a **default name if no name is provided**.  

---

## **🔍 Reflection & Questions**  
- What happens if you call a function **without parentheses**?  
- How is `return` different from `print()` in a function?  
- Why are functions useful in programming?  

---

### **Tomorrow: Function Parameters & Arguments 🚀**  
We’ll dive deeper into function arguments, including **default values, keyword arguments, and multiple parameters**.  

Let me know if you have any questions! 😊