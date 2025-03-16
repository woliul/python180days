# **Day 24: Working with Nested Data Structures**

Today, you'll explore **nested data structures**—which is when you have data structures like lists or dictionaries inside other lists or dictionaries. This is useful when you need to store more complex relationships or data hierarchies.

---

## **1️⃣ Nested Lists**

A **nested list** is simply a list that contains other lists as its elements.

### **Creating and Accessing Nested Lists:**

```python
# Example of a nested list
students = [
    ['Alice', 85, 'Math'],
    ['Bob', 90, 'Science'],
    ['Charlie', 75, 'History']
]

# Accessing elements in a nested list
print(students[0])  # ['Alice', 85, 'Math']
print(students[1][0])  # 'Bob' (Accessing Bob's name)
```

### **Modifying Nested Lists:**

You can modify the inner lists just like you would a normal list.

```python
# Changing Bob's score
students[1][1] = 95
print(students[1])  # ['Bob', 95, 'Science']
```

---

## **2️⃣ Nested Dictionaries**

A **nested dictionary** is a dictionary where the values are themselves dictionaries (or other data structures).

### **Creating and Accessing Nested Dictionaries:**

```python
# Example of a nested dictionary
grades = {
    'Alice': {'Math': 85, 'Science': 90},
    'Bob': {'Math': 88, 'History': 75},
    'Charlie': {'Science': 92, 'History': 78}
}

# Accessing nested dictionary values
print(grades['Alice'])  # {'Math': 85, 'Science': 90}
print(grades['Bob']['Math'])  # 88
```

### **Modifying Nested Dictionaries:**

You can add new key-value pairs or modify existing ones inside the nested dictionaries.

```python
# Adding a new subject for Alice
grades['Alice']['English'] = 88
print(grades['Alice'])  # {'Math': 85, 'Science': 90, 'English': 88}

# Modifying Charlie's Science score
grades['Charlie']['Science'] = 95
print(grades['Charlie']['Science'])  # 95
```

---

## **3️⃣ Practical Example: Managing a Class with Nested Data Structures**

### **Scenario:**
You want to store data about a class of students: their names, subjects, and scores. This could be done using a combination of **nested lists** and **nested dictionaries**.

```python
class_data = {
    'students': [
        {'name': 'Alice', 'scores': {'Math': 85, 'Science': 90}},
        {'name': 'Bob', 'scores': {'Math': 88, 'History': 75}},
        {'name': 'Charlie', 'scores': {'Science': 92, 'History': 78}}
    ]
}

# Accessing specific data
print(class_data['students'][0]['name'])  # 'Alice'
print(class_data['students'][1]['scores']['Math'])  # 88
```

---

## **4️⃣ Practice: Manipulating Nested Data Structures**

Now, it's time to practice!

### **Task 1: Work with Nested Lists**
1. Create a list of 5 students, each represented by a list containing their name and a list of their scores (for 3 subjects).
2. Write a program that calculates and prints the average score for each student.

### **Task 2: Work with Nested Dictionaries**
1. Create a dictionary to store 3 students' names as keys, with their scores in 3 subjects stored as nested dictionaries.
2. Write a program that prints the name of the student with the highest score in each subject.

---

### **Reflection & Questions:**
- **What challenges did you face when working with nested data structures?**
- **How do nested data structures make complex data easier to manage?**
- **Can you think of any real-world applications where you would use nested data structures (e.g., for representing organizations, multi-level categories, etc.)?**

---

## **Tomorrow: Day 25 – Advanced List Comprehensions and Lambda Functions**

Tomorrow, you’ll dive into **advanced list comprehensions** and **lambda functions**. You'll learn how to combine these tools to write more concise and powerful Python code!

Let me know if you have any questions or need more clarification on nested data structures!