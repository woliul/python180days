### **Day 27: Mini Project: Shopping List Manager or Quiz App**

Today, you’ll start working on a **mini project** where you can choose between two options: **Shopping List Manager** or a **Quiz App**. This project will help you solidify the concepts you've learned so far, including working with data structures, functions, loops, and more.

---

## **1️⃣ Project 1: Shopping List Manager**

A **Shopping List Manager** helps users keep track of items they need to buy, modify quantities, or remove items from their shopping list.

### **Core Features:**
- Add an item to the list with its quantity.
- View the shopping list.
- Remove an item from the list.
- Update the quantity of an item.

### **Steps to Build:**
1. **Create a shopping list using a dictionary** with items as keys and quantities as values.
2. **Add items** using a function that prompts for an item name and quantity.
3. **View the shopping list** by looping through the dictionary and printing the items and quantities.
4. **Remove an item** by asking the user for the item name and removing it from the dictionary.
5. **Update an item's quantity** if it already exists in the dictionary.

#### Example Code Structure:
```python
# Define the shopping list as an empty dictionary
shopping_list = {}

# Function to add an item
def add_item(item, quantity):
    shopping_list[item] = quantity

# Function to view the shopping list
def view_list():
    print("Shopping List:")
    for item, quantity in shopping_list.items():
        print(f"{item}: {quantity}")

# Function to remove an item
def remove_item(item):
    if item in shopping_list:
        del shopping_list[item]
        print(f"{item} has been removed.")
    else:
        print(f"{item} not found.")

# Function to update an item's quantity
def update_quantity(item, quantity):
    if item in shopping_list:
        shopping_list[item] = quantity
        print(f"{item}'s quantity has been updated.")
    else:
        print(f"{item} not found.")

# Testing the functions
add_item("Milk", 2)
add_item("Eggs", 12)
view_list()
update_quantity("Milk", 3)
remove_item("Eggs")
view_list()
```

---

## **2️⃣ Project 2: Quiz App**

A **Quiz App** is a simple program that asks a user a series of questions and keeps track of the score.

### **Core Features:**
- Display multiple-choice questions to the user.
- Accept answers from the user.
- Track the score.
- Display the final score at the end.

### **Steps to Build:**
1. **Create a list of questions and answers** where each question has multiple choices and the correct answer.
2. **Use a loop** to ask each question and check if the user's answer is correct.
3. **Keep track of the score** by incrementing it each time the user answers correctly.
4. **Display the final score** after all the questions have been answered.

#### Example Code Structure:
```python
# List of questions and answers (question, list of options, correct answer)
quiz = [
    ("What is the capital of France?", ["Paris", "London", "Berlin"], "Paris"),
    ("What is 2 + 2?", ["3", "4", "5"], "4"),
    ("Which color is the sky?", ["Blue", "Green", "Red"], "Blue")
]

# Function to conduct the quiz
def take_quiz():
    score = 0
    for question, options, correct_answer in quiz:
        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        answer = input("Your answer: ")
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    
    print(f"\nYour final score is: {score}/{len(quiz)}")

# Start the quiz
take_quiz()
```

---

## **3️⃣ Additional Features (Optional)**

You can also add some extra features to either project, like:

- **For the Shopping List Manager:**
  - Save and load the shopping list from a file.
  - Sort the shopping list alphabetically by item name.
  
- **For the Quiz App:**
  - Randomize the order of questions.
  - Add a timer to answer each question.
  - Save the user’s scores in a file.

---

## **4️⃣ Practice and Challenges**

### **Task 1: Shopping List Manager**
1. Write a function that allows the user to view all items in the shopping list and their quantities.
2. Add error handling in case the user tries to remove or update an item that doesn’t exist in the list.

### **Task 2: Quiz App**
1. Modify the app to handle case-insensitive answers.
2. Add an option for the user to choose how many questions they want to answer.

---

### **Reflection & Questions:**
- **Which project did you choose to build? What challenges did you face while coding?**
- **How did you approach organizing the code for these projects?**
- **What additional features would you add to make these projects more interactive or useful?**

---

### **Tomorrow: Day 28 – Reflection on Data Structures and Mini Project Progress**

Tomorrow, you’ll take some time to reflect on the progress of your mini project and review the data structures you’ve learned so far. This is a great opportunity to review concepts, identify areas for improvement, and prepare for the next steps.

Let me know how your mini project is going or if you have any questions!