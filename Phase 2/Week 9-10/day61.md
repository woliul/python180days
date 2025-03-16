# **Day 61: Consuming APIs Using the `requests` Library**

### **Learning:**

Today, we’re going to focus on consuming APIs using the **`requests`** library in Python. We’ll build a simple **API consumer** application that makes GET, POST, PUT, and DELETE requests. By doing so, you’ll become comfortable with interacting with APIs in a practical way.

### **Key Concepts:**

1. **Understanding API Response:**
   - After sending an HTTP request (GET, POST, PUT, DELETE), the API will return a **response**. The response can contain the data you requested or a message indicating the status of the request.
   - **Status Code**: The response comes with a status code indicating whether the request was successful or not (e.g., **200 OK**, **404 Not Found**).
   - **Response Content**: The data returned by the API, often in **JSON format**.
   
2. **Using the `requests` Library:**
   The `requests` library allows you to send HTTP requests easily. We’ve already seen basic usage, but let’s explore more deeply.

#### **GET Request Example:**
A simple GET request fetches data from an API. Let's create a Python script to fetch **user data** from the `jsonplaceholder` API.

```python
import requests

# API endpoint for users
url = "https://jsonplaceholder.typicode.com/users"

# Send a GET request
response = requests.get(url)

# Check if the response was successful (status code 200)
if response.status_code == 200:
    users = response.json()  # Deserialize the JSON response
    for user in users:
        print(f"Name: {user['name']}, Email: {user['email']}")
else:
    print(f"Error: {response.status_code}")
```

- **response.json()**: Converts the JSON response into a Python dictionary or list.
- **response.status_code**: Check the HTTP status code to ensure the request was successful.

---

### **Post Request Example (Creating a New Resource):**

When interacting with APIs, you may need to send data to the server, for example, creating a new resource like a new user. This is where a **POST request** comes in.

Here’s how you would create a new user by sending a POST request with a JSON payload:

```python
import requests

# API endpoint for creating a user
url = "https://jsonplaceholder.typicode.com/users"

# New user data
new_user = {
    "name": "Alice Smith",
    "username": "alicesmith",
    "email": "alice.smith@example.com"
}

# Send a POST request to create a new user
response = requests.post(url, json=new_user)

# Check the response
if response.status_code == 201:
    print("New user created successfully!")
    print(response.json())  # Print the details of the created user
else:
    print(f"Failed to create user. Status code: {response.status_code}")
```

- **requests.post(url, json=data)**: Sends a POST request with the provided `data` in JSON format.
- **Status Code 201**: The server responds with 201 when the resource is created successfully.

---

### **PUT Request Example (Updating an Existing Resource):**

To **update** an existing resource, you’ll use the **PUT method**. This method allows you to send updated data to the API, replacing the existing resource.

Here’s an example where we update a user’s name:

```python
import requests

# API endpoint for updating a user (user with ID 1)
url = "https://jsonplaceholder.typicode.com/users/1"
updated_user = {
    "name": "John Doe Updated"
}

# Send a PUT request to update the user
response = requests.put(url, json=updated_user)

# Check the response
if response.status_code == 200:
    print("User updated successfully!")
    print(response.json())  # Print the updated user details
else:
    print(f"Failed to update user. Status code: {response.status_code}")
```

- **requests.put(url, json=data)**: Sends a PUT request to update the resource at the specified URL.
- **Status Code 200**: Indicates the resource was successfully updated.

---

### **DELETE Request Example (Removing a Resource):**

You may need to **delete** a resource using a **DELETE request**. In this example, we'll delete a user:

```python
import requests

# API endpoint for deleting a user (user with ID 1)
url = "https://jsonplaceholder.typicode.com/users/1"

# Send a DELETE request to remove the user
response = requests.delete(url)

# Check the response
if response.status_code == 200:
    print("User deleted successfully!")
else:
    print(f"Failed to delete user. Status code: {response.status_code}")
```

- **requests.delete(url)**: Sends a DELETE request to remove the resource at the specified URL.
- **Status Code 200**: Indicates the resource was successfully deleted.

---

### **Practice:**

1. **Create a New Post (POST Request):**
   - Use the **POST** method to create a new post (e.g., `"title": "My First Post"`, `"body": "This is my first post!"`).
   - Print the response to verify the post creation.

2. **Update an Existing Post (PUT Request):**
   - Use the **PUT** method to update the title of an existing post (e.g., Post with ID 1).
   - Check the updated post details.

3. **Delete a Post (DELETE Request):**
   - Use the **DELETE** method to delete a post (e.g., Post with ID 2).
   - Ensure the post is successfully deleted.

---

### **Reflection:**
- How confident do you feel about sending and handling GET, POST, PUT, and DELETE requests?
- Have you encountered any errors when interacting with APIs? If so, how did you resolve them?
- Do you have any further questions about handling HTTP requests and responses?

Once you feel comfortable with these operations, you’ll be able to interact with most APIs, create your own projects, and handle various tasks. Let me know if you need further assistance or if you’re ready to move on! 😊