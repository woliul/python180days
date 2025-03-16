# **Day 55: Extra Exercises on Modules and Package Integration**

Today we’ll focus on **modules** and **packages** in Python, which are essential for organizing and structuring your code. We will also do some extra exercises to solidify your understanding and improve your ability to integrate external libraries into your projects.

---

## **1️⃣ What Are Modules and Packages?**

### **1.1 Modules**  
In Python, a **module** is simply a file containing Python definitions and statements. A module can contain functions, classes, variables, and runnable code. You can import and use a module in other Python programs, making it easier to organize your code.

**Example**:  
If you have a file called `math_operations.py` with the following content:

```python
# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

You can use this module in another Python file like so:

```python
import math_operations

result = math_operations.add(3, 5)
print(result)  # Output: 8
```

### **1.2 Packages**  
A **package** is a collection of modules in directories that contain an `__init__.py` file. It helps organize related modules together, especially when the project grows larger.

For example, you can have a package called `math_operations` that contains multiple modules, like:

```
math_operations/
    __init__.py
    addition.py
    subtraction.py
    multiplication.py
```

To use the package, you’d import the modules like this:

```python
from math_operations import addition, subtraction

result = addition.add(2, 3)
print(result)  # Output: 5
```

---

## **2️⃣ Creating a Simple Module**

### **2.1 Writing Your First Module**  
Let’s start by writing a simple module. Create a file named `greetings.py`:

```python
# greetings.py
def greet(name):
    return f"Hello, {name}!"
```

Now, in another file, you can use this module:

```python
import greetings

print(greetings.greet("Alice"))
```

---

### **2.2 Organizing Code into Packages**  
Let’s organize your previous weather app into a package structure. Create a package folder called `weather_app` and move the weather-related code into different modules.

Directory structure:

```
weather_app/
    __init__.py
    fetch_weather.py
    error_handling.py
    display.py
```

In `fetch_weather.py`, you can keep the code that fetches data from the API, in `error_handling.py` you can manage errors, and in `display.py`, you can format and show the output.

#### Example:

- **fetch_weather.py**:

```python
import requests

def get_weather_data(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()
```

- **error_handling.py**:

```python
def handle_error(response):
    if response.get("cod") != 200:
        return f"Error: {response.get('message')}"
    return None
```

- **display.py**:

```python
def display_weather(city, data):
    temperature = data['main']['temp']
    weather_condition = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    
    print(f"Weather in {city}: {weather_condition}, {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} km/h")
```

Finally, in your main app file, you can import and use these modules:

```python
from weather_app import fetch_weather, error_handling, display

city = input("Enter city: ")
api_key = 'your_api_key'
data = fetch_weather.get_weather_data(city, api_key)

error = error_handling.handle_error(data)
if error:
    print(error)
else:
    display.display_weather(city, data)
```

---

## **3️⃣ Practice: Exercises on Modules and Packages**

### **Exercise 1: Split Your Weather App into Modules**
- Split the weather app you built earlier into different modules:
  - One module for fetching data (`fetch_weather.py`).
  - One for handling errors (`error_handling.py`).
  - One for displaying the output (`display.py`).
- Make sure each module has a clear, single responsibility.

### **Exercise 2: Use Python Standard Library Modules**
Try using some **Python standard library modules** in your weather app:
- **`time`**: Print the current time when displaying the weather.
- **`os`**: Use the `os` module to create a folder to store logs of user input.
- **`json`**: If you’re handling data, use the `json` module to save the weather data to a JSON file.

Example with `time` module:

```python
import time

def display_weather(city, data):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    temperature = data['main']['temp']
    weather_condition = data['weather'][0]['description']
    
    print(f"Weather in {city} at {current_time}: {weather_condition}, {temperature}°C")
```

---

## **4️⃣ Review and Reflection**

As you work through the exercises:
- **How well did the modularization** of your code work? Was it easier to organize and manage?
- **What improvements** could you make to your app by splitting the code into modules?
- **Were there any challenges** you encountered while using or creating packages and modules?

---

## **Next Steps for Day 56: Reflection on Week 8**
In the next session, we’ll reflect on everything you’ve learned this week, review key concepts, and prepare for the next steps in your learning journey.

Let me know if you have any questions today! 😊