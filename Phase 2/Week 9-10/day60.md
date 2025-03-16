# **Day 60: Introduction to REST APIs and Their Usage**

### **Learning:**

Today, we’re going to dive into **REST APIs** and understand how to interact with them. **REST (Representational State Transfer)** is a popular architectural style for designing networked applications, especially for APIs. REST APIs are used to allow different systems to communicate over the web using standard HTTP methods.

---

### **Key Concepts:**

1. **What is a REST API?**
   - A **REST API** is an interface that allows different systems to communicate over the web using **HTTP** methods (GET, POST, PUT, DELETE, etc.). 
   - It's based on a set of principles or constraints, including statelessness, cacheability, and a client-server architecture.

2. **HTTP Methods:**
   REST APIs typically use the following HTTP methods to perform CRUD operations:
   - **GET**: Retrieve data from the server (e.g., get a list of users).
   - **POST**: Send data to the server to create a new resource (e.g., create a new user).
   - **PUT**: Update data on the server (e.g., update user details).
   - **DELETE**: Remove data from the server (e.g., delete a user).
   
   The requests typically include **headers** (for authentication, content type) and **body** (for sending data, especially with POST/PUT requests).

3. **API Endpoint:**
   - An **endpoint** is a URL used to access a specific resource or functionality from the API. For example:
     - `https://jsonplaceholder.typicode.com/users` (gets a list of users).
     - `https://jsonplaceholder.typicode.com/posts` (gets a list of posts).

4. **Status Codes:**
   - **200 OK**: The request was successful.
   - **201 Created**: A resource was successfully created.
   - **400 Bad Request**: The request was malformed or missing required parameters.
   - **404 Not Found**: The requested resource doesn’t exist.
   - **500 Internal Server Error**: The server encountered an error.

---

### **Using REST APIs with Python:**

To interact with REST APIs in Python, we typically use the `requests` library. This allows us to send HTTP requests and handle responses in a simple way.

#### **Basic Example with `requests` Library:**

Let’s start by making a **GET** request to an API and examining the response.

```python
import requests

# Example API endpoint
url = "https://jsonplaceholder.typicode.com/users"

# Make a GET request
response = requests.get(url)

# Check the response status code
if response.status_code == 200:
    users = response.json()  # Parse the JSON response
    for user in users:
        print(f"Name: {user['name']}, Email: {user['email']}")
else:
    print(f"Error: {response.status_code}")
```

#### **Explanation:**
- `requests.get(url)` makes a GET request to the provided URL.
- `response.json()` converts the JSON response into a Python dictionary or list.
- The `if` condition checks whether the response status code is 200 (indicating success).
- We then iterate over the users and print their names and emails.

---

### **Practice:**

#### 1. **GET Request:**
Make a GET request to the following API to fetch **posts** and print the title and body of each post.
- API URL: `https://jsonplaceholder.typicode.com/posts`

#### 2. **POST Request:**
You can create new resources (e.g., users or posts) using a **POST** request. For example, let’s create a new **user**.
```python
url = "https://jsonplaceholder.typicode.com/users"
new_user = {
    "name": "John Doe",
    "username": "johndoe",
    "email": "johndoe@example.com"
}

response = requests.post(url, json=new_user)

if response.status_code == 201:
    print("User created successfully!")
else:
    print(f"Failed to create user. Status code: {response.status_code}")
```
- `requests.post(url, json=data)` sends a POST request with JSON data to the API.
- The server should return the created resource, and the status code will typically be **201**.

#### 3. **Handling Errors:**
Handle different status codes and print appropriate messages based on whether the request was successful or not.
- For example, handle 404 errors if the requested resource does not exist.

---

### **Optional Practice:**

1. **PUT Request:**
   - Update an existing resource using a **PUT** request. For example, update the **name** of a user:
   ```python
   url = "https://jsonplaceholder.typicode.com/users/1"
   updated_user = {
       "name": "Jane Doe"
   }
   
   response = requests.put(url, json=updated_user)
   
   if response.status_code == 200:
       print("User updated successfully!")
   else:
       print(f"Failed to update user. Status code: {response.status_code}")
   ```

2. **DELETE Request:**
   - Delete a resource using the **DELETE** method. For example, delete the user you created earlier:
   ```python
   url = "https://jsonplaceholder.typicode.com/users/1"
   response = requests.delete(url)
   
   if response.status_code == 200:
       print("User deleted successfully!")
   else:
       print(f"Failed to delete user. Status code: {response.status_code}")
   ```

---

### **Reflection:**
- How comfortable are you with sending HTTP requests using `requests` and handling the responses?
- Did you encounter any issues with **status codes** or making requests?
- How well did you handle the **POST, PUT, and DELETE** requests?

Once you feel comfortable interacting with APIs using these HTTP methods, you'll be ready to take your skills to the next level and build more complex applications!

Let me know if you need any help or clarification on this!