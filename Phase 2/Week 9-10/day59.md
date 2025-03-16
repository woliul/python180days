# **Day 59: JSON and Data Serialization Basics**

### **Learning:**

Today, we’re going to dive into **JSON (JavaScript Object Notation)**, a lightweight data-interchange format that's commonly used when working with **APIs** and **web scraping**. Understanding how to **serialize** and **deserialize** JSON will be an essential skill as you continue to work with APIs and data.

---

### **Key Concepts:**

1. **What is JSON?**
   - **JSON** is a text format that’s easy for humans to read and write and easy for machines to parse and generate. It is primarily used for storing and exchanging data between a server and a web application or between different systems.
   - JSON data is often used in API responses.

2. **JSON Structure:**
   - JSON is a **key-value** pair structure. It looks like a dictionary or an object in Python.
     Example JSON:
     ```json
     {
       "name": "Alice",
       "age": 30,
       "city": "New York"
     }
     ```

3. **Serialization**:
   - Serialization is the process of converting a Python object (like a dictionary) into a JSON string that can be sent over a network or saved to a file.
   
4. **Deserialization**:
   - Deserialization is the reverse process: converting a JSON string back into a Python object (like a dictionary or list).

---

### **Python’s `json` Module**:
Python provides a built-in **`json`** module to work with JSON data. It has two key functions that we will focus on:

- **`json.dumps()`**: Serializes a Python object to a JSON string.
- **`json.loads()`**: Deserializes a JSON string to a Python object.

---

### **Examples:**

#### 1. **Serialization:**
Let's say you have a dictionary in Python and want to convert it to a JSON string.

```python
import json

# Python dictionary
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Convert Python dictionary to JSON string
json_string = json.dumps(data)

print(json_string)  # Output: '{"name": "Alice", "age": 30, "city": "New York"}'
```

#### 2. **Deserialization:**
Now, let’s take a JSON string and convert it back to a Python dictionary.

```python
# JSON string
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

# Convert JSON string to Python dictionary
data = json.loads(json_string)

print(data)
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

#### 3. **Handling Complex Data:**
You can also work with more complex data, like nested lists or dictionaries.

```python
import json

# Complex data (nested)
data = {
    "name": "Alice",
    "address": {
        "street": "123 Main St",
        "city": "New York"
    },
    "hobbies": ["Reading", "Hiking"]
}

# Serialize to JSON
json_string = json.dumps(data, indent=4)  # Using indent for pretty-printing
print(json_string)
```
Output:
```json
{
    "name": "Alice",
    "address": {
        "street": "123 Main St",
        "city": "New York"
    },
    "hobbies": [
        "Reading",
        "Hiking"
    ]
}
```

---

### **Practice:**

#### 1. **Serialization Exercise:**
Write a Python program that converts the following Python dictionary into a JSON string:
```python
person_info = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "skills": ["Python", "JavaScript", "SQL"]
}
```
Then, print the resulting JSON string.

#### 2. **Deserialization Exercise:**
Given the following JSON string, convert it back into a Python object and print it:
```json
{
  "product": "Laptop",
  "price": 899.99,
  "in_stock": true
}
```
You should convert it into a Python dictionary and print the individual elements like `product`, `price`, and `in_stock`.

#### 3. **Nested Data:**
Create a JSON string that represents a list of three products, where each product has:
- `name`
- `price`
- `rating`
Use this list and deserialize it back into a Python object. Print each product's details.

---

### **Optional Practice:**

1. **Save and Load JSON Data:**
   - Serialize the data into a JSON file instead of just a string.
   - Deserialize the data from a file back into a Python object.
   ```python
   # Writing JSON data to a file
   with open("data.json", "w") as f:
       json.dump(data, f, indent=4)
   
   # Reading JSON data from a file
   with open("data.json", "r") as f:
       data = json.load(f)
       print(data)
   ```

---

### **Reflection:**

- How comfortable are you working with **JSON** now?
- Do you feel ready to handle more complex API responses, such as pagination or error messages in JSON format?
- Have you practiced saving and reading JSON files yet? If not, try it today to reinforce your skills.

Let me know if you need clarification on any of these topics! Once you're done with these exercises, you'll be better equipped to handle APIs and their JSON responses. Happy coding! 😊