# **Day 36: Practice – OOP Coding Exercises** 🚀🐍  

Today, we’ll put our **Object-Oriented Programming (OOP)** knowledge into practice with real-world coding exercises. These exercises will test your understanding of **classes, inheritance, polymorphism, encapsulation, and method overriding**.  

---

## **1️⃣ Challenge: Create a Library Management System** 📚  
**Task:**  
- Create a `Book` class with attributes: `title`, `author`, and `available` (default is `True`).  
- Implement methods to **borrow** and **return** a book.  
- Create a `Library` class that manages a collection of books.  

### **Expected Behavior:**
```python
book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("The Pragmatic Programmer", "Andy Hunt")

library = Library()
library.add_book(book1)
library.add_book(book2)

library.borrow_book("Python Crash Course")  # Marks as borrowed
library.return_book("Python Crash Course")  # Marks as available again
```

✅ Use **encapsulation** to prevent direct modification of `available`.  
✅ Use **polymorphism** if adding an `EBook` subclass.  

---

## **2️⃣ Challenge: Bank Account System** 🏦  
**Task:**  
- Create a `BankAccount` class with `owner`, `balance`, and methods for **deposit** and **withdraw**.  
- Create a `SavingsAccount` subclass that overrides `withdraw()` to ensure a **minimum balance** is maintained.  

### **Expected Behavior:**
```python
acc = SavingsAccount("Alice", 500)
acc.deposit(200)  # New balance: 700
acc.withdraw(100)  # Allowed
acc.withdraw(700)  # Should print "Insufficient funds"
```

✅ Use **inheritance** to extend `BankAccount`.  
✅ Use **method overriding** in `SavingsAccount`.  

---

## **3️⃣ Challenge: Shape Hierarchy & Polymorphism** 🔺🔵  
**Task:**  
- Create a `Shape` base class with a method `area()`.  
- Create `Rectangle` and `Circle` subclasses with **specific area calculations**.  
- Use **polymorphism** to process different shapes in a function.  

### **Expected Behavior:**
```python
shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    print(shape.area())  # Outputs area of each shape
```

✅ Demonstrate **polymorphism** by calling `area()` on different objects.  

---

## **4️⃣ Reflection:**
- **Which concepts were easiest/hardest to implement?**  
- **How does encapsulation prevent misuse of object attributes?**  
- **Why is method overriding useful in real-world applications?**  

---

### **Tomorrow: Reflection & OOP Review**  
We’ll summarize **key lessons** from the week and discuss **best practices** in OOP! 🚀  

Let me know if you have any questions! 😊