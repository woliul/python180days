# **Day 23: Sets and Dictionary Comprehensions**

Today, we’re going to dive into **sets** and **dictionary comprehensions**, both of which are powerful tools for managing data in Python.

---

## **1️⃣ Sets in Python**

### **What is a Set?**
- A set is an **unordered** collection of **unique** items.
- Sets automatically remove duplicates, which makes them useful when you need to track unique items.
- Unlike lists, sets **do not maintain order**.

### **Creating a Set:**
You can create a set by using curly braces `{}` or the `set()` function.

```python
# Using curly braces
fruits = {'apple', 'banana', 'cherry'}
print(fruits)  # {'banana', 'apple', 'cherry'}

# Using set() function (converts a list to a set)
numbers = set([1, 2, 3, 4, 4])
print(numbers)  # {1, 2, 3, 4} (duplicate 4 is removed)
```

### **Set Operations:**
- **Adding items:** `add()`
- **Removing items:** `remove()` or `discard()` (no error if item doesn't exist with `discard`)
- **Set Union:** `|` or `.union()`
- **Set Intersection:** `&` or `.intersection()`
- **Set Difference:** `-` or `.difference()`

```python
# Example of set operations
fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')  # Adds 'orange' to the set
fruits.remove('banana')  # Removes 'banana' from the set
print(fruits)  # {'apple', 'cherry', 'orange'}

# Set union, intersection, and difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
print(set1 & set2)  # Intersection: {3}
print(set1 - set2)  # Difference: {1, 2}
```

---

## **2️⃣ Dictionary Comprehensions**

A **dictionary comprehension** allows you to create or modify dictionaries in a compact, readable way. It’s similar to list comprehensions, but for key-value pairs.

### **Basic Syntax:**

```python
{key: value for key, value in iterable}
```

- **Example 1:** Create a dictionary with numbers as keys and their squares as values.
```python
squares = {x: x ** 2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

- **Example 2:** Convert a list of tuples to a dictionary.
```python
pairs = [('apple', 1), ('banana', 2), ('cherry', 3)]
fruit_dict = {key: value for key, value in pairs}
print(fruit_dict)  # {'apple': 1, 'banana': 2, 'cherry': 3}
```

- **Example 3:** Apply conditions in the comprehension.
```python
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

---

## **3️⃣ Practice: Build Comprehensions for Sets and Dictionaries**

Now it’s time to practice using **sets** and **dictionary comprehensions**.

### **Task 1: Work with Sets**
1. Create a set of 5 unique numbers.
2. Add a number to the set and remove an existing number.
3. Perform a set union, intersection, and difference with another set.

### **Task 2: Use Dictionary Comprehensions**
1. Create a dictionary using a comprehension that maps numbers from 1 to 5 to their cubes.
2. Modify the comprehension to only include numbers whose cubes are even.
3. Create a dictionary from a list of student names and their scores, then filter out students who scored below 50.

---

## **Reflection & Questions:**
- **Which set operation did you find most useful in your code?**
- **How does dictionary comprehension improve the readability of your code compared to a traditional loop?**
- **Can you think of real-world applications where sets and dictionary comprehensions would be helpful?**

---

## **Tomorrow: Day 24 – Working with Nested Data Structures**

Tomorrow, you’ll explore **nested data structures** (e.g., dictionaries with lists inside). This is important for working with more complex data and managing data relationships.

Feel free to ask if you have any questions about sets or dictionary comprehensions!