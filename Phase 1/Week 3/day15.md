# **Day 15: String Manipulation and Methods**  

Today, you’ll explore **string manipulation**—an essential skill for handling text in Python! 📝  

---

## **1️⃣ String Basics**  
A string is a sequence of characters enclosed in quotes:  
```python
text = "Hello, Python!"
```
✅ Strings can contain letters, numbers, and symbols.  

---

## **2️⃣ Common String Methods**  
Python provides many **built-in methods** to manipulate strings.  

### **Changing Case**
```python
s = "hello world"
print(s.upper())  # HELLO WORLD
print(s.lower())  # hello world
print(s.title())  # Hello World
```

### **Removing Whitespace**
```python
s = "   Python   "
print(s.strip())   # "Python" (removes spaces)
print(s.lstrip())  # "Python   "
print(s.rstrip())  # "   Python"
```

### **Finding and Replacing**
```python
s = "I love Python"
print(s.replace("Python", "coding"))  # "I love coding"
print(s.find("love"))  # 2 (index of "love")
print("Python" in s)  # True
```

### **Splitting and Joining**
```python
s = "apple,banana,orange"
words = s.split(",")  # ['apple', 'banana', 'orange']
print(words)

new_string = " - ".join(words)
print(new_string)  # "apple - banana - orange"
```

✅ **Use `split()` to break a string into a list and `join()` to merge a list into a string.**  

---

## **3️⃣ Reversing a String**
### **Using Slicing**
```python
s = "Python"
print(s[::-1])  # "nohtyP"
```

### **Using a Loop**
```python
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("Python"))  # "nohtyP"
```

---

## **🛠️ Practice Task**  
1. Write a program to **reverse a string** entered by the user.  
2. Take a sentence and **split it into words**, then **join it back with `-` as a separator**.  
3. Check if a word **exists** in a sentence using `.find()` or `in`.  

---

## **🔍 Reflection & Questions**  
- What **string method** did you find most useful?  
- How does **slicing** make string operations easier?  
- Can you think of real-world applications for string manipulation?  

---

### **Tomorrow: String Formatting Techniques! 🎯**  
You’ll learn how to create **clean and readable output** using **f-strings** and `.format()`.  

Let me know if you have any questions! 😊