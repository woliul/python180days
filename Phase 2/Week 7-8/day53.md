# **Day 53: Mini Project – Weather Data Fetcher Using APIs**

Today, we’re going to begin building your first mini project: a **Weather Data Fetcher** that uses an API to retrieve weather information for a specific city. We'll be using the **OpenWeather API** as an example to fetch live weather data.

---

## **1️⃣ Introduction to API Consumption**  
Now that we’ve planned the project, let’s start coding! We’ll use Python's `requests` module to send HTTP requests to an external API and fetch data.

---

### **1.1 Install the `requests` module**
If you haven't installed it yet, you'll need to install the `requests` module to make HTTP requests.

Open your terminal or command prompt and run:

```bash
pip install requests
```

---

## **2️⃣ How to Make an API Request**

### **2.1 Making a Simple GET Request**  
To interact with the OpenWeather API, you need to send a GET request to fetch weather data. Here’s a basic example:

```python
import requests

# Replace 'your_api_key' with your actual OpenWeather API key
api_key = 'your_api_key'
city = 'London'  # You can change this to any city

# Make the GET request to the OpenWeather API
response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')

# Parse the response JSON data
data = response.json()

# Check if the response is successful
if response.status_code == 200:
    # Extract data from the response
    temperature = data['main']['temp']
    weather_condition = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Display the weather information
    print(f"Weather in {city}: {weather_condition}, {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} km/h")
else:
    print("Error fetching data:", data.get('message', 'Unknown error'))
```

### **Explanation**:
- **API Endpoint**: The endpoint `http://api.openweathermap.org/data/2.5/weather` is used to fetch the weather data.
- **Query Parameters**: 
  - `q`: The city name you want to fetch data for.
  - `appid`: Your unique API key.
  - `units=metric`: Ensures temperature is returned in Celsius.
- **JSON Response**: The data is returned in JSON format, and we access specific fields like temperature, weather description, etc.

---

### **2.2 Replace with Your API Key**  
Before running the script, make sure you’ve signed up for an API key from [OpenWeather API](https://openweathermap.org/api). After you’ve got the API key, replace `'your_api_key'` in the code with your actual key.

---

## **3️⃣ Practice: Fetching Data from the Weather API**

### **3.1 Exercise**:  
Your task for today is to:
1. **Write a Python script** that fetches weather data for a city of your choice (other than London).
2. Print out the weather conditions, temperature, humidity, and wind speed.

### **Example** Output:
```text
Weather in New York: clear sky, 18°C, Humidity: 65%, Wind Speed: 5 km/h
```

---

## **4️⃣ Optional Extra Challenge: Handle Invalid City Names**

Sometimes users might input an invalid city name, or the API might not be able to find the city. It’s important to handle these errors gracefully.

### **4.1 Handling Invalid City Names**  
Modify your code to check if the city is valid. If not, show a user-friendly message like “City not found.”

```python
import requests

def get_weather(city):
    api_key = 'your_api_key'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_condition = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        print(f"Weather in {city}: {weather_condition}, {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} km/h")
    else:
        print("Error: City not found or unable to fetch data.")

# Ask the user for a city and fetch weather data
city = input("Enter city: ")
get_weather(city)
```

---

## **5️⃣ Reflection**

As you complete today’s practice:
- **What worked well** in your code?  
- **Were there any issues** or error messages that you had to troubleshoot?  
- **What changes** would you make to improve the app, such as adding additional features like displaying icons for weather conditions?

---

### **Next Steps for Day 54:**
Tomorrow, we’ll continue working on your project by adding **error handling** and enhancing the functionality of your weather app.

Let me know if you need help with any part of today’s task! 😊