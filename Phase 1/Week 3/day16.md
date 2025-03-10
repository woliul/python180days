# **Day 16: String Formatting (f-strings, `.format()`)**  

Today, you’ll learn how to **format strings** for clear and structured output. 🎯  

---

## **1️⃣ String Formatting Methods**  

### **1. f-strings (Python 3.6+) 🚀**  
✅ **Fast, easy, and readable!**  
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```
**Output:**  
```
My name is Alice and I am 25 years old.
```

**Formatting numbers with f-strings:**  
```python
price = 49.99
print(f"The price is ${price:.2f}")  # The price is $49.99
```

---

### **2. `.format()` Method (Older Alternative)**
```python
name = "Bob"
score = 95
print("Student: {} | Score: {}".format(name, score))
```
**Using Index Numbers:**  
```python
print("Student: {1} | Score: {0}".format(score, name))  # Change order
```

---

### **3. Using `%` Formatting (Older Style)**
```python
name = "Charlie"
height = 5.9
print("Name: %s, Height: %.1f" % (name, height))
```
✅ **This method is outdated**—use f-strings instead!

---

## **2️⃣ Practice Tasks**  

1️⃣ **Use f-strings** to display:  
   - Your name  
   - Your favorite number  
   - A formatted price (two decimal places)  

2️⃣ **Format a sentence using `.format()`** with at least **two placeholders**.  

3️⃣ **Align Text Output (Using f-strings)**  
```python
print(f"{'Item':<10}{'Price':>10}")
print(f"{'Apple':<10}{1.50:>10.2f}")
print(f"{'Banana':<10}{0.99:>10.2f}")
```
**Output:**
```
Item         Price
Apple        1.50
Banana       0.99
```

---

## **🔍 Reflection & Questions**  
- Which formatting method do you prefer? Why?  
- How does string formatting improve **code readability**?  
- What are **real-world uses** of formatted output?  

---

### **Tomorrow: Handling Errors with Try-Except 🚀**  
You’ll learn how to make your code more **robust and crash-proof!**  

Let me know if you have any questions! 😊