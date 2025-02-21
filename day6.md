# **Day 6: Review – Combining Variables & Data Structures**  

Today, you’ll apply everything you’ve learned so far by combining **variables, lists, dictionaries, conditionals, and user input** to solve real-world problems.  

---

## **1️⃣ Recap: What Have You Learned?**  

| **Concept**      | **Example**                                      |
|-----------------|--------------------------------------------------|
| **Variables**   | `name = "Alice"`                                  |
| **Data Types**  | `age = 25`, `height = 5.7`, `is_student = True`   |
| **Lists**       | `fruits = ["apple", "banana", "cherry"]`          |
| **Tuples**      | `colors = ("red", "green", "blue")`               |
| **Dictionaries**| `person = {"name": "Bob", "age": 30}`             |
| **Sets**        | `unique_numbers = {1, 2, 3, 3, 4}`                |
| **Conditionals**| `if age >= 18: print("Adult")`                    |

---

## **2️⃣ Combining Variables & Data Structures**
Now, let’s **combine lists, dictionaries, and conditionals**.

### **Example 1: Store & Retrieve Student Information**
```python
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"},
    "Charlie": {"age": 19, "grade": "C"}
}

name = input("Enter student name: ")

if name in students:
    print(f"{name} is {students[name]['age']} years old and has a grade of {students[name]['grade']}.")
else:
    print("Student not found.")
```

✅ **Concepts Used:** Dictionary, User Input, Conditionals

---

### **Example 2: Shopping List Program**
```python
shopping_list = ["milk", "eggs", "bread"]

item = input("Enter an item to add: ")
if item not in shopping_list:
    shopping_list.append(item)
    print(f"{item} added to your list.")
else:
    print(f"{item} is already in your list.")

print("Updated shopping list:", shopping_list)
```

✅ **Concepts Used:** Lists, Conditionals, User Input

---

### **Example 3: Even/Odd Checker with Sets**
```python
numbers = {1, 2, 3, 4, 5, 6}

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
```

✅ **Concepts Used:** Loops, Sets, Conditionals

---

## **🛠️ Practice Tasks**
1. **Create a dictionary** storing 3 friends’ names as keys and their favorite foods as values. Allow the user to enter a name and print their favorite food.  
2. **Modify a list**: Take user input for a new task, add it to a `to_do` list, and print the updated list.  
3. **Write a program** that checks if a user-entered number is in a predefined set of lucky numbers.  

---

## **🔍 Reflection & Questions**
- How do lists and dictionaries work together?  
- Why is it useful to check if an item exists before adding it?  
- What happens if you try to modify a tuple?  

---

### **Tomorrow: Reflection & Improvements**  
Tomorrow, you’ll review what you’ve learned and reflect on challenges. 🚀  

Let me know if you have any questions! 😊