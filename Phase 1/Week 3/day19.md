# **Day 19: Combining Strings with File I/O (e.g., Logging Data)**

Today, you’ll learn how to combine **string manipulation** and **file I/O** to handle tasks like **logging data** or **processing file content**. This is a great skill for storing and analyzing data. 📚💻

---

## **1️⃣ Logging Data to a File**

### **What is logging?**
Logging allows you to **track events** or errors in your program by saving them to a file, which can be useful for debugging or keeping records.

### **Example: Logging Events to a File**

Let’s create a program that logs user actions (like logging in):
```python
def log_action(action):
    with open("log.txt", "a") as file:
        file.write(f"{action}\n")

log_action("User logged in.")
log_action("User clicked a button.")
```
Here, every time we call `log_action()`, the action is **appended** to the `log.txt` file. The newline `\n` ensures each action is on a separate line.

---

## **2️⃣ Reading and Processing File Content**

You can read file content and manipulate the data. Let’s **count how many times a word** appears in a file:
```python
def count_word_occurrences(filename, word):
    with open(filename, "r") as file:
        content = file.read()
    word_count = content.lower().count(word.lower())  # Case-insensitive count
    return word_count

# Example usage
word_count = count_word_occurrences("log.txt", "user")
print(f"The word 'user' appears {word_count} times.")
```
Here, we:
- Open the file and read its content.
- Use the `count()` method to count occurrences of the word.

---

## **3️⃣ Combining Strings and File I/O for Dynamic Logging**

You can also use string formatting to **include more dynamic data** in your logs (e.g., date, username, etc.):
```python
import datetime

def log_action(action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as file:
        file.write(f"{timestamp} - {action}\n")

log_action("User logged in.")
log_action("User logged out.")
```
In this example, we added a timestamp to each log entry.

---

## **4️⃣ Writing to a File with Multiple Data Types**

Sometimes you need to log not just strings, but also numbers, or even lists:
```python
data = [1, 2, 3, 4, 5]
with open("data_log.txt", "a") as file:
    file.write(f"Data: {data}\n")  # This will log the list as a string
```
If you want to format this more neatly (e.g., saving numbers one by one):
```python
with open("data_log.txt", "a") as file:
    for item in data:
        file.write(f"{item}\n")
```

---

## **🛠️ Practice Tasks**

1️⃣ **Create a program that logs events** (e.g., user actions or application status updates) with a timestamp.

2️⃣ **Write a program to read a file and count the number of lines** in the file.

3️⃣ **Process a file's content** and search for a specific keyword (e.g., a username or an error message), then print how many times it appears.

---

## **🔍 Reflection & Questions**

- What are the **advantages** of using logging in a program?  
- How does **formatting strings** with dynamic data improve file I/O tasks?  
- Can you think of **other scenarios** where you might log data?  

---

### **Tomorrow: Mini Project – Text File Analysis 📊**

Tomorrow, you’ll apply everything you’ve learned so far to **analyze text file data** in a mini project!  

Let me know if you have any questions! 😊