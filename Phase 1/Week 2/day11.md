# **Day 11: Nested Loops and List Comprehensions**  

Today, you'll learn how to **use loops inside loops (nested loops)** and make your code more efficient with **list comprehensions**.

---

## **1️⃣ Nested Loops**  
A **nested loop** is a loop inside another loop.  

### **Example: Nested `for` Loop (Multiplication Table)**
```python
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"{i} x {j} = {i * j}")
    print("------")
```
**Output:**  
```
1 x 1 = 1  
1 x 2 = 2  
1 x 3 = 3  
------  
2 x 1 = 2  
2 x 2 = 4  
2 x 3 = 6  
------  
3 x 1 = 3  
3 x 2 = 6  
3 x 3 = 9  
------  
```
✅ **Use nested loops when working with multi-dimensional data**, like tables or grids.

---

### **Example: Nested `while` Loop**
```python
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i}, {j})", end=" ")
        j += 1
    print()
    i += 1
```
**Output:**  
```
(1, 1) (1, 2) (1, 3)  
(2, 1) (2, 2) (2, 3)  
(3, 1) (3, 2) (3, 3)  
```
✅ Be careful with **while loops**, or you might create an **infinite loop**.

---

## **2️⃣ List Comprehensions**  
List comprehensions allow you to create **lists in a single line** of code.  

### **Basic List Comprehension**
```python
numbers = [x for x in range(5)]
print(numbers)
```
**Output:**  
```
[0, 1, 2, 3, 4]
```

✅ This is **shorter** than using a `for` loop.  

---

### **List Comprehension with Conditions**
```python
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
```
**Output:**  
```
[0, 2, 4, 6, 8]
```
✅ You can filter values inside list comprehensions!

---

### **Nested Loops in List Comprehensions**
```python
pairs = [(x, y) for x in range(2) for y in range(2)]
print(pairs)
```
**Output:**  
```
[(0, 0), (0, 1), (1, 0), (1, 1)]
```
✅ This is a compact way to generate **coordinate pairs or grids**.

---

## **🛠️ Practice Task**  
1. Write a **nested loop** to print a right-angle triangle pattern of `*`.  
2. Use **list comprehension** to create a list of **squares** of numbers from 1 to 10.  
3. Create a list of **even numbers** from 1 to 20 using **list comprehension**.  

---

## **🔍 Reflection & Questions**  
- When should you use **nested loops**?  
- How does **list comprehension** make code more readable?  
- Can you replace all `for` loops with **list comprehensions**?  

---

### **Tomorrow: Loop & Function Challenges 🚀**  
We'll combine loops and functions in **real-world coding exercises**.  

Let me know if you have any questions! 😊