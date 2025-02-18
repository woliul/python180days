Great to hear you're ready for Day 3! Let's dive into it.

---

### **Day 3: Lists and Tuples**  

**Learning (9:00 - 10:00 PM)**  
Today we’ll cover:  
1. **Lists:** Creating and manipulating lists.  
2. **Tuples:** How they differ from lists and how to use them.  

---

### **1. What is a List?**  
A **list** is a collection of ordered items. The items can be of any data type (strings, integers, floats, etc.) and can even include other lists.  
- Lists are **mutable**, which means you can change their contents (add, remove, or modify items).

**Creating a list:**  
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

**Accessing items in a list:**  
```python
first_fruit = fruits[0]  # Indexing starts from 0
print(first_fruit)  # Output: apple
```

**Modifying lists:**  
```python
fruits[1] = "orange"  # Changes 'banana' to 'orange'
print(fruits)  # Output: ['apple', 'orange', 'cherry']
```

**List methods:**  
- `.append()`: Adds an item to the end of the list.  
- `.remove()`: Removes the first occurrence of a specified item.  
- `.pop()`: Removes the item at the specified index (or last item by default).  
- `.sort()`: Sorts the list in ascending order.  

```python
fruits.append("grape")  # Adds 'grape' to the end
fruits.remove("orange")  # Removes 'orange'
fruits.sort()  # Sorts the list alphabetically
print(fruits)
```

---

### **2. What is a Tuple?**  
A **tuple** is similar to a list, but it is **immutable**, meaning that once a tuple is created, you cannot modify it (no adding, removing, or changing items).

**Creating a tuple:**  
```python
coordinates = (10, 20, 30)
print(coordinates)
```

**Accessing items in a tuple:**  
```python
x = coordinates[0]  # Accessing the first item
print(x)  # Output: 10
```

**Key differences between lists and tuples:**  
- Lists are mutable (changeable), tuples are immutable (unchangeable).  
- Lists use square brackets (`[]`), tuples use parentheses (`()`).

---

### **Practice Exercises (10:00 - 11:30 PM)**  

1. **Exercise 1:**  
   - Create a list of your favorite foods and print it.  
   - Change one item in the list and print it again.  
   - Add a new item to the list and print it.

2. **Exercise 2:**  
   - Create a tuple containing three numbers and print it.  
   - Try to change an item in the tuple (you will get an error) to understand that tuples are immutable.

3. **Exercise 3:**  
   - Create a list of numbers. Sort the list, remove an item, and then print the updated list.
   Example:  
   ```python
   numbers = [3, 1, 4, 5, 2]
   numbers.sort()  # Sorts the numbers
   numbers.remove(4)  # Removes the number 4
   print(numbers)
   ```

4. **Exercise 4 (Challenge):**  
   - Create a list with mixed data types (e.g., string, integer, float). Print the list and access each item.
   Example:  
   ```python
   mixed_list = ["John", 25, 5.8]
   print(mixed_list)
   print(mixed_list[0])  # Access the name
   print(mixed_list[1])  # Access the age
   ```

---

Once you’ve completed these exercises or if you have any questions, just let me know! I'm here to help. 😊