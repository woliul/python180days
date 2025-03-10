# **Day 10: Function Parameters, Arguments, and Default Values**  

Today, you'll **enhance your functions** by learning different ways to pass data using parameters and arguments.  

---

## **1️⃣ Function Parameters vs. Arguments**  
- **Parameters** → Variables inside the function definition (`def add(a, b)`).  
- **Arguments** → Actual values passed when calling the function (`add(3, 5)`).  

### **Example: Function with Multiple Parameters**  
```python
def add(a, b):
    return a + b

result = add(3, 5)  # 3 and 5 are arguments
print(result)
```
**Output:**  
```
8
```
✅ You can pass **any data type** as arguments (numbers, strings, lists, etc.).

---

## **2️⃣ Default Parameter Values**  
You can **set default values** for parameters to make them optional.  

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()        # Uses default value
greet("Alice") # Uses given argument
```
**Output:**  
```
Hello, Guest!  
Hello, Alice!  
```
✅ Default values **prevent errors** if an argument is missing.

---

## **3️⃣ Positional vs. Keyword Arguments**  
### **Positional Arguments (Order Matters)**
```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet("dog", "Buddy")  # Correct order
```
**Output:**  
```
I have a dog named Buddy.
```

### **Keyword Arguments (Order Doesn't Matter)**
```python
describe_pet(name="Buddy", animal="dog")  # Named arguments
```
✅ Keyword arguments make code **clearer** and **less error-prone**.

---

## **4️⃣ Handling Multiple Arguments (`*args`)**  
If you **don’t know** how many arguments a function will take, use `*args`.  

```python
def sum_numbers(*numbers):
    return sum(numbers)

print(sum_numbers(1, 2, 3, 4, 5))  # Pass multiple values
```
**Output:**  
```
15
```
✅ `*args` lets you pass **any number of positional arguments**.

---

## **5️⃣ Handling Multiple Keyword Arguments (`**kwargs`)**  
Use `**kwargs` for **multiple named arguments**.  

```python
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="New York")
```
**Output:**  
```
name: Alice  
age: 25  
city: New York  
```
✅ `**kwargs` is useful for **dynamic** key-value pairs.

---

## **🛠️ Practice Task**  
1. Create a function `calculate_total(price, tax=0.1)` that returns the total with tax.  
2. Write a function that accepts any number of arguments and returns their **average**.  
3. Build a function `user_profile(**info)` that takes any number of **named details** and prints them.  

---

## **🔍 Reflection & Questions**  
- What happens if you **don't provide an argument** for a required parameter?  
- How does `*args` differ from a normal parameter?  
- When should you use keyword arguments (`**kwargs`) instead of positional ones?  

---

### **Tomorrow: Nested Loops & List Comprehensions 🚀**  
You'll learn how to **optimize loops** and work with **compact list operations**.  

Let me know if you have any questions! 😊