# **Day 8: For and While Loops**  

Today, you’ll learn about **loops**, which allow your programs to repeat tasks efficiently instead of writing repetitive code manually.  

---

## **1️⃣ What is a Loop?**  
Loops let us **repeat a block of code multiple times** without writing it over and over.

### **Types of Loops in Python:**  
- **For loop** → Used when you know how many times you need to loop.  
- **While loop** → Used when you loop until a condition is met.  

---

## **2️⃣ For Loop**  
A **for loop** iterates over a sequence (like a list, range, or string).  

### **Example: Loop Through a List**
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```
**Output:**
```
apple
banana
cherry
```

✅ **Concepts Used:** Lists, Loops

---

### **Using `range()` in a For Loop**  
The `range()` function generates a sequence of numbers.  
```python
for i in range(5):
    print(i)
```
**Output:**  
```
0  
1  
2  
3  
4  
```
✅ `range(n)` generates numbers from `0` to `n-1`.  

---

## **3️⃣ While Loop**  
A **while loop** keeps running **until a condition becomes False**.  

### **Example: Counting from 1 to 5**
```python
count = 1

while count <= 5:
    print(count)
    count += 1
```
**Output:**  
```
1  
2  
3  
4  
5  
```
✅ **Make sure your condition eventually becomes False** or the loop will run forever!

---

### **4️⃣ Breaking Out of Loops**  
Use `break` to **exit a loop early**.  

```python
for num in range(10):
    if num == 5:
        break  # Stops the loop when num == 5
    print(num)
```
**Output:**  
```
0  
1  
2  
3  
4  
```

---

### **5️⃣ Skipping an Iteration with `continue`**  
Use `continue` to **skip the current iteration and move to the next one**.  

```python
for num in range(5):
    if num == 2:
        continue  # Skip number 2
    print(num)
```
**Output:**  
```
0  
1  
3  
4  
```

---

## **🛠️ Practice Task**  
1. Write a **for loop** that prints numbers from 10 to 1 in reverse.  
2. Use a **while loop** to keep asking the user for input until they type `"exit"`.  
3. Create a loop that **skips even numbers** and only prints odd numbers between 1-10.  

---

## **🔍 Reflection & Questions**  
- When should you use a **for loop** vs a **while loop**?  
- What happens if you forget to **increment** in a `while` loop?  
- How does `break` and `continue` change loop behavior?  

---

### **Tomorrow: Functions in Python! 🚀**  
You’ll learn how to **create and use functions** to make your code reusable.  

Let me know if you have any questions! 😊