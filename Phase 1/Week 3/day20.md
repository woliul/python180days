# **Day 20: Mini Project – Text File Analysis**  

Today, you're going to combine all your knowledge about **strings**, **file I/O**, and **error handling** into a mini project: **Text File Analysis**! 📊📝

In this project, we’ll read a text file, process its content, and extract useful information.

---

## **1️⃣ Mini Project: Text File Analysis**

### **Objective:**
We'll create a program that performs the following tasks:
- Read a text file containing a sample of text data.
- Count the total number of words.
- Count the number of unique words.
- Find the most common word in the text.
- Log the analysis results to a new file.

---

## **2️⃣ Plan for the Project:**

### **Step 1: Read the File**  
We start by reading the contents of a text file. We’ll assume you have a text file named `sample.txt`.

```python
def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()
```

### **Step 2: Count Total Number of Words**  
We split the file content into words using the `split()` method. Then, count how many words there are.

```python
def count_words(text):
    words = text.split()
    return len(words)
```

### **Step 3: Count Unique Words**  
Convert the list of words to a set to remove duplicates, then count the unique words.

```python
def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)
```

### **Step 4: Find the Most Common Word**  
We can use Python's `collections.Counter` to easily count word frequency and find the most common one.

```python
from collections import Counter

def most_common_word(text):
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(1)  # Returns a list of the most common word with its count
```

### **Step 5: Log Results to a New File**  
Finally, we write the results to a new file for analysis or future reference.

```python
def log_results(file_name, total_words, unique_words, common_word):
    with open(file_name, "w") as file:
        file.write(f"Total words: {total_words}\n")
        file.write(f"Unique words: {unique_words}\n")
        file.write(f"Most common word: {common_word[0][0]} (appears {common_word[0][1]} times)\n")
```

---

## **3️⃣ Full Code Example**

Here’s how the complete program looks:

```python
from collections import Counter

def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

def most_common_word(text):
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(1)

def log_results(file_name, total_words, unique_words, common_word):
    with open(file_name, "w") as file:
        file.write(f"Total words: {total_words}\n")
        file.write(f"Unique words: {unique_words}\n")
        file.write(f"Most common word: {common_word[0][0]} (appears {common_word[0][1]} times)\n")

# Main function
def analyze_text_file(input_file, output_file):
    text = read_file(input_file)
    total_words = count_words(text)
    unique_words = count_unique_words(text)
    common_word = most_common_word(text)
    log_results(output_file, total_words, unique_words, common_word)

# Running the analysis
input_file = "sample.txt"  # Text file to be analyzed
output_file = "analysis_results.txt"  # File to log the results
analyze_text_file(input_file, output_file)
```

---

## **4️⃣ Practice Tasks:**

1️⃣ **Create your own text file** (`sample.txt`) and use the program to analyze it. Make sure it contains enough content for word analysis.

2️⃣ **Modify the code to include additional analyses**, such as:
   - Count how many times a specific word appears.
   - Find the shortest and longest words in the text.

3️⃣ **Log additional information** like the total number of lines in the text file or the average length of words.

---

## **🔍 Reflection & Questions:**

- How did you **combine everything** you've learned about strings, files, and loops in this project?  
- What new challenges did you face while analyzing the file?  
- How can this type of analysis be useful in **real-world applications**, such as processing user input or analyzing logs?  

---

### **Tomorrow: Reflection on Week 3 – Strings, Error Handling & File I/O**

Tomorrow, we’ll reflect on everything you’ve learned this week. You can document your progress and clarify any doubts. 😊

Let me know if you have any questions about this project!