# **Day 3: Lists, Tuples & Basic List Operations**  

Today, you’ll learn about **lists and tuples**, how to store multiple values, and perform operations like adding, removing, and accessing elements.  

---

## **1️⃣ What is a List?**  
A **list** is an ordered, changeable collection of items. It allows duplicates and can store **different data types**.  

### **Example of a List:**  
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 3.14, True, 42]
```

---

## **2️⃣ Accessing List Elements**
You can access elements using **indexing** (starting from `0`):
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
```

You can also use **negative indexing**:
```python
print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana
```

---

## **3️⃣ Slicing Lists**  
You can extract portions of a list using slicing (`start:stop:step`):
```python
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])   # Output: [20, 30, 40] (index 1 to 3)
print(numbers[:3])    # Output: [10, 20, 30] (first 3 elements)
print(numbers[2:])    # Output: [30, 40, 50, 60] (from index 2 to end)
print(numbers[::2])   # Output: [10, 30, 50] (every 2nd element)
```

---

## **4️⃣ Modifying Lists**
Lists are **mutable**, meaning you can change them.  

### **Adding Elements**
```python
fruits = ["apple", "banana"]
fruits.append("cherry")  # Adds at the end
print(fruits)  # Output: ['apple', 'banana', 'cherry']

fruits.insert(1, "mango")  # Insert at a specific index
print(fruits)  # Output: ['apple', 'mango', 'banana', 'cherry']
```

### **Removing Elements**
```python
fruits.pop()   # Removes last element
fruits.remove("banana")  # Removes specific item
del fruits[0]  # Removes item at index 0
fruits.clear()  # Removes all elements
```

---

## **5️⃣ What is a Tuple?**
A **tuple** is like a list but **immutable** (cannot be changed after creation).  

### **Example of a Tuple:**  
```python
colors = ("red", "green", "blue")
print(colors[0])  # Output: red
```
✅ **Tuples use parentheses `()` instead of square brackets `[]`**.  

### **Trying to Modify a Tuple (Error!)**
```python
colors[0] = "yellow"  # ❌ This will cause an error
```

If you need to modify it, **convert it to a list**:
```python
colors_list = list(colors)
colors_list.append("yellow")
colors = tuple(colors_list)
print(colors)  # Output: ('red', 'green', 'blue', 'yellow')
```

---

## **6️⃣ Checking if an Item Exists**
```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
print("grape" in fruits)   # Output: False
```

---

## **🛠️ Practice Task**
1. **Create a list of your favorite movies** and print the first and last movie.  
2. **Take user input to create a list** of their three favorite foods.  
3. **Convert a list to a tuple** and try modifying it (observe the error).  

---

## **🔍 Reflection & Questions**
- What is the difference between a list and a tuple?  
- When should you use a tuple instead of a list?  
- What happens if you try to access an index that does not exist?  

---

### **In day 4: We will learn about Dictionaries & Sets**  
You’ll learn how to store and manage key-value pairs! 🚀  

Let me know if you have any questions. 😊
