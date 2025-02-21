# **Day 4: Dictionaries & Sets**  

Today, you’ll learn about **dictionaries** (key-value pairs) and **sets** (unordered unique items). These are useful for organizing and managing data efficiently.

---

## **1️⃣ What is a Dictionary?**  
A **dictionary** is a collection of **key-value pairs**, where each key is unique, and it allows fast lookups.  

### **Example of a Dictionary**  
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```
Here,  
- `"name"`, `"age"`, and `"city"` are **keys**  
- `"Alice"`, `25`, and `"New York"` are **values**  

✅ **Dictionaries use curly braces `{}` and key-value pairs separated by `:`.**

---

## **2️⃣ Accessing Dictionary Values**  
You can access values using keys:
```python
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 25
```

### **Using `.get()` to Avoid Errors**
```python
print(person.get("city"))   # Output: New York
print(person.get("height"))  # Output: None (instead of an error)
```

---

## **3️⃣ Modifying Dictionaries**
### **Adding and Updating Values**
```python
person["job"] = "Developer"  # Add new key-value pair
person["age"] = 26  # Update value
print(person)
```

### **Removing Items**
```python
person.pop("city")  # Removes 'city' key
del person["age"]   # Removes 'age' key
person.clear()      # Removes all key-value pairs
```

✅ **Dictionaries are mutable**, so you can modify them anytime.

---

## **4️⃣ Looping Through a Dictionary**
### **Loop through keys**
```python
for key in person:
    print(key)  
# Output: name, job
```

### **Loop through values**
```python
for value in person.values():
    print(value)  
# Output: Alice, Developer
```

### **Loop through keys & values**
```python
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# job: Developer
```

---

## **5️⃣ What is a Set?**
A **set** is an unordered collection of unique elements.

### **Example of a Set**
```python
numbers = {1, 2, 3, 4, 5, 5, 3}
print(numbers)  # Output: {1, 2, 3, 4, 5} (removes duplicates)
```

✅ **Sets do not allow duplicate values**.  

---

## **6️⃣ Common Set Operations**
### **Adding and Removing Items**
```python
fruits = {"apple", "banana", "cherry"}
fruits.add("mango")  # Adds an item
fruits.remove("banana")  # Removes an item
```

### **Set Operations (Union, Intersection, Difference)**
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # Union: {1, 2, 3, 4, 5, 6}
print(a & b)  # Intersection: {3, 4}
print(a - b)  # Difference: {1, 2}
```

✅ **Sets are useful when you need to store unique values and perform fast operations.**

---

## **🛠️ Practice Task**
1. **Create a dictionary for a student** with keys `"name"`, `"age"`, `"grade"`, and `"subject"`. Print one value.  
2. **Modify the dictionary** by adding a new key `"hobby"`.  
3. **Create two sets** of favorite sports and find the common sports (intersection).  

---

## **🔍 Reflection & Questions**
- When would you use a dictionary instead of a list?  
- What happens if you try to access a key that doesn’t exist?  
- Why are sets useful for removing duplicates?  

---

### **Next: Conditionals & Comparison Operators**  
You’ll learn how to use `if-else` statements to make decisions in Python! 🚀  

Let me know if you have any questions. 😊
