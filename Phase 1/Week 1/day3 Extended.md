### **Tuple vs List in Python**

#### **What is a List?**
A **list** is a collection of items that can be changed (mutable). You can add, remove, or modify elements in a list.

📌 **Example of a List**:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

🔹 **Key Features of Lists**:
- **Mutable** (can change elements)
- **Ordered** (keeps elements in the same order)
- **Can contain different data types** (e.g., numbers, strings, booleans)
- **Uses square brackets `[]`**

#### **What is a Tuple?**
A **tuple** is similar to a list, but it **cannot** be changed (immutable). Once created, you cannot add, remove, or modify elements.

📌 **Example of a Tuple**:
```python
fruits = ("apple", "banana", "cherry")
print(fruits)  # Output: ('apple', 'banana', 'cherry')
```

🔹 **Key Features of Tuples**:
- **Immutable** (cannot change elements)
- **Ordered** (keeps elements in the same order)
- **Can contain different data types**
- **Uses parentheses `()`**

---

### **When to Use a List vs. a Tuple?**
| Feature  | List  | Tuple  |
|----------|-------|--------|
| Can change? | ✅ Yes (Mutable) | ❌ No (Immutable) |
| Faster? | ❌ No (slower) | ✅ Yes (faster) |
| Uses more memory? | ✅ Yes | ❌ No |
| Used for? | Data that needs to change | Fixed data that should not change |

---

### **Tutorial: How to Use Lists and Tuples?**
#### **1️⃣ Creating a List**
```python
my_list = ["dog", "cat", "fish"]
print(my_list)
```
#### **2️⃣ Changing a List**
```python
my_list[1] = "rabbit"
print(my_list)  # Output: ['dog', 'rabbit', 'fish']
```
#### **3️⃣ Creating a Tuple**
```python
my_tuple = ("red", "blue", "green")
print(my_tuple)
```
#### **4️⃣ Trying to Change a Tuple (Will Give an Error)**
```python
my_tuple[1] = "yellow"  # ❌ ERROR: Tuples cannot be changed
```

---

### **Final Thoughts**
- Use **lists** when you need to modify data.
- Use **tuples** when you want data to remain constant for safety and speed.
