# **Day 18: File I/O Basics: Reading and Writing Files**  

Today, you’ll learn how to work with **files**—reading from them and writing to them. This is essential for storing and manipulating data in Python! 📂  

---

## **1️⃣ Opening a File**  
To work with a file, you first need to **open** it using the `open()` function:  
```python
file = open("example.txt", "r")  # Open for reading
```

### **File Modes:**
- `"r"` – **Read** (default). Opens the file for reading.
- `"w"` – **Write**. Creates a new file or overwrites an existing one.
- `"a"` – **Append**. Adds content to an existing file.
- `"b"` – **Binary**. For non-text files like images.

---

## **2️⃣ Reading from a File**  
There are a few ways to read from a file once it’s open:  

### **Read the entire content:**
```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

### **Read line by line:**
```python
file = open("example.txt", "r")
for line in file:
    print(line, end="")  # 'end=""' removes extra newlines
file.close()
```

### **Read a specific number of characters:**
```python
file = open("example.txt", "r")
content = file.read(5)  # Read the first 5 characters
print(content)
file.close()
```

---

## **3️⃣ Writing to a File**  
You can use the `write()` method to write text to a file. Be careful, because **writing to a file in "w" mode** will **overwrite** existing content!  

```python
file = open("example.txt", "w")  # Open for writing (overwrite)
file.write("Hello, world!")
file.close()
```

### **Appending to a file:**
```python
file = open("example.txt", "a")  # Open for appending
file.write("\nThis is a new line.")
file.close()
```

---

## **4️⃣ Closing the File**  
Once you’re done with a file, it’s important to **close** it using `file.close()` to free up resources.

Alternatively, you can use the `with` statement to **automatically close** the file after the block of code runs:
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```
✅ **`with` is preferred** because it guarantees that the file is properly closed.

---

## **🛠️ Practice Tasks**  
1️⃣ **Write a program that creates a file**, writes some text to it, and then reads it back.  
2️⃣ **Open an existing file** and print each line one by one.  
3️⃣ **Append new content** to a file without overwriting existing data.

---

## **🔍 Reflection & Questions**  
- Why is it important to **close** a file after using it?  
- How does using `with` make file handling safer and easier?  
- Can you think of a scenario where you'd use **appending to a file** instead of overwriting?  

---

### **Tomorrow: Combining Strings with File I/O (e.g., Logging Data) 📚**  
You'll learn how to **combine string manipulation** with **file I/O** for tasks like logging and data storage.  

Let me know if you have any questions! 😊