# **Day 63: Mini Project: Build a Simple Web Scraper/API Consumer**

### **Learning:**

Today, we’re going to apply everything we’ve learned so far by building a **mini-project** that combines web scraping and consuming data from APIs.

This project will involve:
- Scraping data from a website (e.g., quotes or articles).
- Consuming an API to fetch and display data.
  
This mini-project will help you solidify your understanding of both web scraping and working with APIs.

---

### **Project Outline:**

We’re going to build an application that:
1. **Scrapes data** from a webpage (e.g., scraping quotes from `http://quotes.toscrape.com/`).
2. **Consumes an API** to fetch additional data (e.g., fetching weather information using an API).

By combining these techniques, you'll gain experience with both pulling static data from a website and dynamic data from an API.

---

### **Step 1: Web Scraping (Quotes)**

For this part, we’ll scrape a webpage for **quotes** using the `BeautifulSoup` library.

#### **Code to Scrape Quotes:**

```python
import requests
from bs4 import BeautifulSoup

# URL of the quotes page
url = "http://quotes.toscrape.com/"

# Send GET request
response = requests.get(url)

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all quotes on the page
quotes = soup.find_all('span', class_='text')

# Print all quotes
for quote in quotes:
    print(quote.text)
```

#### **Explanation:**
- **`requests.get(url)`**: Fetches the HTML content from the webpage.
- **`BeautifulSoup(response.text, 'html.parser')`**: Parses the HTML response.
- **`soup.find_all('span', class_='text')`**: Extracts all quotes by searching for the `span` tags with the class `text`.

---

### **Step 2: Consuming an API (Weather Data)**

Next, we’ll fetch data from an API. For example, we will use the **OpenWeatherMap API** to get current weather information for a city.

#### **How to Use OpenWeatherMap API:**
1. Sign up for a free API key on [OpenWeatherMap](https://openweathermap.org/api).
2. Once you have your API key, we can use it to request weather data.

#### **Example Code to Fetch Weather:**

```python
import requests

# Your OpenWeatherMap API key
api_key = 'your_api_key_here'

# City for which you want to fetch weather data
city = 'London'

# URL to make the GET request
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    main = data['main']
    weather = data['weather'][0]
    
    # Print the weather details
    print(f"City: {city}")
    print(f"Temperature: {main['temp']}°C")
    print(f"Weather: {weather['description']}")
else:
    print(f"Error fetching weather data: {response.status_code}")
```

#### **Explanation:**
- **API Key**: Use your unique key to authenticate the request.
- **Weather Data**: We’re pulling the **temperature** and **weather description** from the response.
- **Units**: The `units=metric` parameter returns the temperature in Celsius.

---

### **Step 3: Combine the Scraping and API Data**

Now that you can both scrape quotes and get weather information from an API, let’s combine both into one program. For example, we can display a random quote along with the current weather in a city.

#### **Full Code for Mini Project:**

```python
import requests
from bs4 import BeautifulSoup
import random

# URL of the quotes page
url = "http://quotes.toscrape.com/"

# Send GET request to scrape quotes
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('span', class_='text')

# Randomly select a quote
random_quote = random.choice(quotes).text

# API key for weather data
api_key = 'your_api_key_here'
city = 'London'

# Fetch weather data from OpenWeatherMap API
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
weather_response = requests.get(weather_url)

if weather_response.status_code == 200:
    weather_data = weather_response.json()
    main = weather_data['main']
    weather = weather_data['weather'][0]
    
    # Print quote and weather info
    print(f"Quote of the Day: {random_quote}")
    print(f"Weather in {city}: {main['temp']}°C, {weather['description']}")
else:
    print("Error fetching weather data.")
```

#### **Explanation:**
- **Scrape Random Quote**: We select a random quote from the scraped list using `random.choice()`.
- **Display Weather**: After fetching the weather data from the API, the program prints the temperature and weather description.
- **Combine Outputs**: Both the quote and the weather information are displayed together.

---

### **Practice and Customization:**

Now that you have the base for your mini-project, you can experiment and enhance it by adding more features:
1. **Error Handling**: Add more robust error handling to manage API failures, request errors, or empty quote pages.
2. **User Input**: Let the user input their preferred city for the weather report.
3. **Scrape Additional Data**: Scrape and display author names or tags along with the quotes.
4. **Save Data**: Store the scraped quotes and weather information in a text file or a database for later use.

---

### **Reflection:**

- How did you find combining web scraping with API consumption in this project? 
- Did you face any challenges while integrating the two technologies?
- What other features would you add to this project to enhance its functionality?

This mini-project brings together everything you've learned so far about web scraping and API consumption. Once you're comfortable with this, you can try creating your own larger projects! Let me know if you need any help with that!