# **Day 35: Polymorphism and Core OOP Principles** 🎭🐍  

Today, we’ll dive into **polymorphism**, one of the key principles of **Object-Oriented Programming (OOP)**. We'll also revisit the **four core OOP principles** to strengthen our understanding.  

---

## **1️⃣ What is Polymorphism?**  
Polymorphism allows objects of **different classes** to be **treated as objects of a common superclass**. It enables **a single interface** to represent different types of objects.  

### **Why is Polymorphism Important?**
✅ Allows for **flexible and reusable** code  
✅ Enables **method overriding** for customization  
✅ Supports **code generalization**, making maintenance easier  

---

## **2️⃣ Example of Polymorphism: Overriding Methods**
Polymorphism lets different child classes define their own **versions** of a method while keeping the same method name.

```python
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Using polymorphism
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.speak())  
```
### **Output:**
```
Woof!
Meow!
Some generic sound
```
Even though we are calling the same method (`speak()`), **each object behaves differently** based on its class.

---

## **3️⃣ Polymorphism in Action: The `len()` Function**
Python's built-in `len()` function is an example of **polymorphism** because it works on **different data types**.

```python
print(len("Python"))  # Works on a string → Output: 6
print(len([1, 2, 3, 4]))  # Works on a list → Output: 4
print(len({"name": "Alice", "age": 25}))  # Works on a dictionary → Output: 2
```
Even though `len()` is a single function, it behaves **differently** depending on the object it is called on.

---

## **4️⃣ Operator Overloading**
Polymorphism in Python also allows us to **override operators** using **magic methods** (dunder methods like `__add__`, `__sub__`).

### **Example: Overloading `+` Operator**
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages  # Adding pages of two books

book1 = Book("Python Basics", 200)
book2 = Book("OOP Concepts", 300)

print(book1 + book2)  # Output: 500 (Sum of pages)
```
Here, we **redefine** the `+` operator to add pages instead of numbers.

---

## **5️⃣ The Four Core OOP Principles**
OOP is built on **four fundamental concepts**:

| Principle      | Description |
|---------------|------------|
| **Encapsulation** | Restricting direct access to object data; using **getter/setter** methods. |
| **Abstraction** | Hiding implementation details, exposing only the essentials. |
| **Inheritance** | Allowing child classes to reuse and extend parent class functionality. |
| **Polymorphism** | Using a single interface for multiple object types. |

---

## **6️⃣ Practice Exercises**
1️⃣ **Create a `Shape` class** with a method `area()`.  
   - Create `Rectangle` and `Circle` subclasses.  
   - Override `area()` in each subclass to calculate the correct area.  

2️⃣ **Demonstrate polymorphism**  
   - Write a function that takes a list of `Shape` objects and prints their areas.  

3️⃣ **Overload an operator (`+`, `*`)** in a class of your choice.  

---

## **7️⃣ Reflection:**
- **How does polymorphism make code more flexible?**  
- **Why is method overriding useful in OOP?**  
- **Can you think of real-world scenarios where polymorphism is applied?**  

---

### **Tomorrow: OOP Practice & Challenges**  
Next, we’ll solve **real-world coding exercises** to strengthen our OOP skills. 🚀  

Let me know if you have any questions! 😊