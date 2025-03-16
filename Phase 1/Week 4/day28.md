# **Day 28: Reflection – Review Data Structures & Mini Project Progress**

Today is all about reflecting on what you’ve learned so far. You’ll review the **data structures** you’ve studied, reflect on your **mini project progress**, and identify areas where you need improvement.

---

## **1️⃣ Review: Advanced Data Structures**

Over the last few days, you’ve learned some advanced data structures, such as **nested lists**, **nested dictionaries**, and **comprehensions**. Let’s do a quick review of these key concepts:

### **Nested Lists**
- A **nested list** is a list that contains other lists. It’s useful when dealing with multi-dimensional data.
  
  Example:
  ```python
  students = [
      ['Alice', 85, 'Math'],
      ['Bob', 90, 'Science'],
      ['Charlie', 75, 'History']
  ]
  ```

### **Nested Dictionaries**
- A **nested dictionary** is a dictionary where the values are other dictionaries or data structures.
  
  Example:
  ```python
  grades = {
      'Alice': {'Math': 85, 'Science': 90},
      'Bob': {'Math': 88, 'History': 75},
      'Charlie': {'Science': 92, 'History': 78}
  }
  ```

### **List Comprehensions**
- **List comprehensions** allow you to create new lists by applying an expression to an existing list or iterable.
  
  Example:
  ```python
  even_numbers = [x for x in range(10) if x % 2 == 0]
  ```

### **Lambda Functions**
- A **lambda function** is a small, anonymous function that is used to write simple expressions.
  
  Example:
  ```python
  square = lambda x: x ** 2
  ```

---

## **2️⃣ Review: Mini Project Progress**

### **Shopping List Manager / Quiz App**

Take a moment to review your mini project:

- **What functionality did you implement?**
- **What features were easy to build, and which ones did you find more challenging?**
- **Did you encounter any bugs or issues while building your project?**

---

## **3️⃣ Areas to Reflect On and Improve**

Here are some things to think about and improve:

### **1. Data Structures:**
- **Nested Data Structures:** Review how you handled nested lists and dictionaries. Could your shopping list or quiz app benefit from using nested data structures? For example:
  - In the **Shopping List Manager**, you might want to store items with additional details (e.g., price or category). Consider using **nested dictionaries** for each item.
  - In the **Quiz App**, consider using a **nested dictionary** to store questions with possible answers and the correct one.

### **2. Functions & Error Handling:**
- **Functions:** Did you create well-defined functions to handle specific tasks? Try breaking down your code into smaller, reusable functions.
- **Error Handling:** Did you use `try-except` blocks to prevent errors like user input mistakes or missing data?

### **3. Extra Features to Add:**
- **Shopping List Manager:**
  - Add the ability to **save** and **load** your shopping list from a file, so the list persists even after closing the program.
  - Allow users to sort items by name or quantity.
  
- **Quiz App:**
  - Consider adding **randomization** of questions and answers.
  - Add a **timer** for each question, so users have a limited time to answer.
  - Track the **user's previous scores** and compare them with the current score.

---

## **4️⃣ Reflect on Challenges and Successes**

- **Challenges:**
  - What parts of the project were difficult for you? (e.g., understanding nested structures, handling user input)
  - How did you overcome those challenges? (e.g., debugging, researching Python documentation)

- **Successes:**
  - Which part of the project went well? Was there a moment when you were particularly proud of solving a problem or implementing a feature?
  - Did you learn any new Python techniques or libraries while building your project?

---

## **5️⃣ Tomorrow: Day 29 – Git Basics & Extra Practice**

Tomorrow, you’ll learn **Git Basics**, which is essential for version control. You’ll also have the opportunity to practice anything that’s still unclear or challenging from this week.

Take some time today to wrap up your mini project, make any improvements, and get ready to dive into version control!

---

### **Reflection Questions:**
- What have you learned about **working with complex data structures** so far? Are there any areas you'd like to revisit?
- Which feature of your mini project are you most proud of? Why?
- What would you like to focus on next in your Python journey?

Feel free to share your thoughts or ask questions, and I’ll be happy to help you move forward!