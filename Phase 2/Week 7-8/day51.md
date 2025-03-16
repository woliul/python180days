# **Day 51: Mini Project - Package Management and Reusable Components**

Today, we’ll apply everything you've learned so far by working on a **mini-project**. This project will help you practice **package management** and creating **reusable components**. By the end of the day, you’ll have a small project with clean, modular design, and you’ll see how package management can improve your workflow.

---

## **Mini Project Overview:**
### **Goal:**
Create a small Python project that fetches data from an API and processes it. The project will use external packages and will be structured using modules to keep your code organized and reusable.

### **Steps:**
1. **Create a Python project structure.**
2. **Install necessary external packages.**
3. **Build the main logic of the project.**
4. **Make the project modular by organizing code into reusable functions and modules.**
5. **Manage dependencies using a `requirements.txt` file.**

---

## **1. Create the Project Structure**

First, let’s create the basic folder structure for the project. This is what it might look like:

```plaintext
my_project/
│
├── venv/                 # Virtual environment directory
│
├── app/                  # Main code for your project
│   ├── __init__.py       # Marks the folder as a package
│   ├── fetcher.py        # Contains code for fetching API data
│   └── processor.py      # Contains code for processing data
│
├── requirements.txt      # List of project dependencies
│
└── README.md             # Project description
```

- **`fetcher.py`**: Will contain the logic to fetch data from a public API.
- **`processor.py`**: Will handle the data processing logic (e.g., filtering or organizing data).
- **`requirements.txt`**: This file will store all the external dependencies.

---

## **2. Install Necessary External Packages**

We will need **requests** to fetch data from an API and maybe **pandas** for processing and organizing the data.

- Activate your virtual environment:
  ```bash
  source venv/bin/activate  # On macOS/Linux
  .\venv\Scripts\activate   # On Windows
  ```

- Install **requests** and **pandas**:
  ```bash
  pip install requests pandas
  ```

- Generate the `requirements.txt` file to store these dependencies:
  ```bash
  pip freeze > requirements.txt
  ```

Your `requirements.txt` will look like this:
```plaintext
requests==2.28.1
pandas==1.5.3
```

---

## **3. Build the Main Logic**

### **Fetching Data (Fetcher Module)**
In the `fetcher.py` file, we will write a function to fetch data from an API. Let’s use the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/), which is a free fake online REST API for testing and prototyping.

```python
# app/fetcher.py
import requests

def fetch_data(url):
    """
    Fetch data from the given URL.
    :param url: The API URL to fetch data from
    :return: JSON response if successful, None if failed
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch data (Status code: {response.status_code})")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
```

- **`fetch_data`** function:
  - It takes a URL as input and attempts to retrieve data.
  - If successful, it returns the data in JSON format. If there’s an issue, it prints an error message and returns `None`.

### **Processing the Data (Processor Module)**
In the `processor.py` file, we will process the data we fetch. Here, let's assume we want to process a list of posts and extract only the titles.

```python
# app/processor.py
import pandas as pd

def process_data(data):
    """
    Process the fetched data and extract the titles of posts.
    :param data: List of data fetched from the API
    :return: Pandas DataFrame containing the post titles
    """
    if not data:
        return None
    
    titles = [item['title'] for item in data]  # Extract titles
    df = pd.DataFrame(titles, columns=['Title'])  # Create a DataFrame
    return df
```

- **`process_data`** function:
  - Takes the list of posts (or any data) as input.
  - Extracts the titles from the list of posts.
  - Creates a Pandas DataFrame and returns it.

---

## **4. Bringing Everything Together in `main.py`**

Now, let’s create the main script to bring everything together. The `main.py` file will call the functions from both `fetcher.py` and `processor.py`, fetch the data, process it, and display the results.

```python
# app/main.py
from app.fetcher import fetch_data
from app.processor import process_data

def main():
    url = 'https://jsonplaceholder.typicode.com/posts'
    
    # Fetch data from API
    print("Fetching data...")
    data = fetch_data(url)
    
    if data:
        # Process the fetched data
        print("Processing data...")
        df = process_data(data)
        
        if df is not None:
            # Display the first 5 rows of the data
            print("\nFirst 5 Titles:\n")
            print(df.head())

if __name__ == "__main__":
    main()
```

- **`main.py`**:
  - Fetches data using the `fetch_data` function.
  - Processes the data using the `process_data` function.
  - Displays the first 5 titles from the API data using Pandas' `.head()`.

---

## **5. Running the Project**

1. **Activate the virtual environment** (if not already activated):
   ```bash
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate   # On Windows
   ```

2. **Run the `main.py` script**:
   ```bash
   python app/main.py
   ```

You should see output like this:

```
Fetching data...
Processing data...

First 5 Titles:

                                               Title
0  sunt aut facere repellat provident occaecati ...
1                     qui est esse
2            ea molestias quasi exercitationem repellat qui
3                      eum et est occaecati
4                    nihil nihil consequatur
```

---

## **6. Review and Next Steps**

- You successfully created a **modular Python project** that uses **external packages** to fetch and process data.
- The project was organized into separate files for each component (`fetcher.py` for fetching data, `processor.py` for data processing).
- You used **`requirements.txt`** to manage dependencies and create a reproducible environment.
- The project structure ensures that your code is clean, organized, and easy to maintain.

---

## **Practice:**
- Extend the project by adding more functionality, such as:
  - Save the processed data into a CSV file using `df.to_csv()`.
  - Add error handling for cases where the API might be down.
  - Explore more about using **Pandas** to manipulate and analyze the data.
  
---

### **What’s Next?**
Tomorrow, we’ll reflect on all that we’ve learned so far and look forward to the next phase of your Python journey. Feel free to ask if you need help or have any questions!