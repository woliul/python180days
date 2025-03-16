# **Day 54: Continue API Project Development – Enhancing the Weather App**

Today, we’ll be enhancing your weather app by adding **error handling** and improving the user experience. By the end of today’s session, your app will be more robust and handle common issues such as invalid user input and network errors.

---

## **1️⃣ Enhancing Your Weather App with Error Handling**

When building real-world applications, it’s important to handle potential errors gracefully. Let's add some error handling to make sure your app responds correctly if something goes wrong.

### **1.1 Common Errors to Handle**
- **Invalid City Name**: If the user enters a city that doesn’t exist, the API will return an error.
- **Network Issues**: If there’s a problem with the internet connection or the API server, the app should handle that.
- **Incorrect API Key**: If your API key is incorrect or expired, the API will return an error.

---

### **1.2 Implementing Error Handling**
We’ll modify the code to:
- Handle invalid city names.
- Catch network issues (like when the user is offline).
- Display a user-friendly message for any other errors.

### **1.3 Code Example with Error Handling**

Here’s how you can modify your weather app to handle common errors:

```python
import requests

def get_weather(city):
    api_key = 'your_api_key'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        # Attempt to make the request to the API
        response = requests.get(url)
        
        # Raise an exception if the status code is not 200 (OK)
        response.raise_for_status()
        
        # Parse the JSON data from the response
        data = response.json()
        
        # Check if the city exists in the response
        if data.get("cod") != 200:
            print(f"Error: {data.get('message')}")
        else:
            # Extract weather details
            temperature = data['main']['temp']
            weather_condition = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            # Print the weather details
            print(f"Weather in {city}: {weather_condition}, {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} km/h")
    
    except requests.exceptions.RequestException as e:
        # Handle any issues with the request
        print(f"Error fetching data: {e}")
    
    except ValueError:
        # Handle any issues with parsing the JSON
        print("Error: Unable to parse the weather data.")
    
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected error: {e}")

# Ask the user for a city and fetch weather data
city = input("Enter city: ")
get_weather(city)
```

### **Explanation**:
- **`response.raise_for_status()`**: This raises an error if the HTTP request didn’t return a successful status code (e.g., 404 or 500).
- **`requests.exceptions.RequestException`**: Catches network-related issues (e.g., no internet connection).
- **Check for `cod != 200`**: The API returns a `cod` (code) value, and a non-200 value means the request wasn’t successful (e.g., city not found).
- **General Exception Handling**: If something unexpected happens, it’s caught by the final `except` block.

---

## **2️⃣ Optional Challenge: Displaying Weather Icons**
One cool feature you can add is displaying weather icons based on the weather condition (e.g., sunny, rainy, cloudy). OpenWeather provides icons for different weather conditions.

### **2.1 How to Use Weather Icons**  
The OpenWeather API returns the icon code for weather conditions. You can use this to display the icon next to the weather details.

- Each weather condition comes with an icon code like `"01d"` for clear skies, `"02d"` for a few clouds, etc.
- You can construct the URL for the icon image by appending the icon code to the base URL:
  ```python
  icon_code = data['weather'][0]['icon']
  icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
  print(f"Icon URL: {icon_url}")
  ```

This will provide the URL to the icon that you can display in your app’s output.

---

## **3️⃣ Practice: Enhancing Your App**
### **Exercise**:  
1. Add **error handling** to your existing weather app to handle network errors and invalid city names.
2. **Test your app** with:
   - A valid city name.
   - An invalid city name (e.g., "InvalidCity123").
   - Simulate network issues (you can disconnect from the internet temporarily).
   
3. **Optional**: Implement the display of weather icons by using the icon code from the API response.

---

## **4️⃣ Reflection**

As you work through the error handling and enhancements:
- **Did the error handling work as expected?** Did you catch any unexpected errors during testing?
- **How did the app behave when you tested invalid cities or network issues?** Did it give clear and helpful messages to the user?
- **How can you improve the user experience** (e.g., by adding a better UI, such as a graphical interface)?

---

## **Next Steps for Day 55**:
Tomorrow, we’ll continue with additional exercises related to Python **modules** and **packages**, which will help you organize your code even better. You’ll also work on some challenges to further deepen your understanding.

Let me know if you run into any issues today! 😊