# **Day 25: Advanced List Comprehensions and Lambda Functions**

Today, you’ll learn how to **supercharge** your Python skills by combining **advanced list comprehensions** with **lambda functions**. This will allow you to write concise, efficient, and powerful code.

---

## **1️⃣ Advanced List Comprehensions**

### **Recap: Basic List Comprehension**
A list comprehension provides a concise way to create lists in Python. Here's the basic syntax:

```python
# Basic syntax
new_list = [expression for item in iterable]
```

Example:
```python
squares = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

### **Advanced List Comprehensions with Conditionals**

You can add conditions to list comprehensions. These conditionals allow you to filter out unwanted values or only include specific ones.

- **With `if` Condition:**

```python
# Example: Get even squares
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

- **With `if` and `else` Condition:**

You can also use `if-else` in a list comprehension to apply different expressions based on the condition.

```python
# Example: If even, square it; if odd, cube it
numbers = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(5)]
print(numbers)  # [0, 1, 4, 27, 16]
```

---

## **2️⃣ Lambda Functions**

### **What is a Lambda Function?**
A **lambda function** is a small anonymous function that can have any number of arguments but only one expression. It’s like a shorthand for defining simple functions.

### **Basic Syntax:**
```python
lambda arguments: expression
```

### **Example of a Lambda Function:**

```python
# Regular function
def add(x, y):
    return x + y

# Equivalent lambda function
add_lambda = lambda x, y: x + y
print(add_lambda(3, 5))  # 8
```

### **Using Lambda with List Comprehensions:**

Lambda functions are often used with functions like `map()`, `filter()`, and `sorted()`. You can also use them directly in list comprehensions to create more complex expressions.

```python
# Example: Use lambda to create a list of doubled values
numbers = [1, 2, 3, 4, 5]
doubled = [lambda x: x * 2 for x in numbers]
print([f(1) for f in doubled])  # [2, 4, 6, 8, 10]
```

---

## **3️⃣ Combining List Comprehensions and Lambda Functions**

You can now combine the power of list comprehensions with lambda functions to write even more efficient code.

### **Example: Sorting with Lambda in List Comprehension**

```python
# Sorting a list of tuples by the second element
pairs = [(1, 2), (3, 4), (5, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(5, 1), (1, 2), (3, 4)]
```

---

## **4️⃣ Practice: Use Advanced List Comprehensions and Lambda Functions**

### **Task 1: Advanced List Comprehensions**
1. Create a list of numbers from 1 to 20 and generate a new list containing the squares of only the even numbers.
2. Modify the previous list comprehension to return `-1` for odd numbers and square for even numbers.

### **Task 2: Lambda Functions**
1. Create a lambda function to calculate the area of a rectangle given the length and width.
2. Use a lambda function inside `sorted()` to sort a list of strings by their lengths.

---

### **Reflection & Questions:**
- **How do list comprehensions improve the readability of your code compared to traditional loops?**
- **What are the advantages of using lambda functions instead of regular functions?**
- **How do you think these techniques can make your Python code more concise and efficient?**

---

## **Tomorrow: Day 26 – Sorting Techniques Using Key Functions**

Tomorrow, you’ll learn how to **sort** complex data structures using **key functions**. Sorting is a fundamental operation, and mastering it will help you handle data efficiently.

Let me know if you need any clarifications on list comprehensions or lambda functions!