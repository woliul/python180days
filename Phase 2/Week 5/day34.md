# **Day 34: Inheritance and Method Overriding** 🏗️🐍  

Today, we’ll explore **inheritance**, a key concept in **Object-Oriented Programming (OOP)** that allows us to create new classes based on existing ones. We’ll also learn about **method overriding**, which lets us change the behavior of inherited methods.  

---

## **1️⃣ What is Inheritance?**  
**Inheritance** allows a new class (**child class**) to **reuse** the properties and methods of an existing class (**parent class**).  

### **Key Benefits of Inheritance:**
✅ Avoids code duplication  
✅ Helps with better organization  
✅ Promotes reusability and scalability  

### **Syntax:**
```python
class ParentClass:
    # Parent class attributes and methods

class ChildClass(ParentClass):
    # Child class inherits everything from ParentClass
```

---

## **2️⃣ Example: Inheriting from a Parent Class**
Let's create a **`Vehicle`** class and a **`Car`** class that inherits from it.

```python
# Parent class
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def describe(self):
        return f"This is a {self.brand} with {self.wheels} wheels."

# Child class (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, wheels=4)  # Call the parent constructor
        self.model = model
        self.year = year

    def describe(self):  # Overriding the parent method
        return f"{self.year} {self.brand} {self.model} with {self.wheels} wheels."

# Creating an object of Car
car1 = Car("Toyota", "Corolla", 2022)

print(car1.describe())  # Output: 2022 Toyota Corolla with 4 wheels.
```

### **How it Works:**
- The `Car` class **inherits** from `Vehicle`.
- `super().__init__()` calls the parent constructor to initialize shared attributes.
- `describe()` is **overridden** in `Car` to provide a more specific message.

---

## **3️⃣ Method Overriding**
Sometimes, a child class needs to **modify** or **extend** a method from its parent class.  

This is done using **method overriding**, where the child class **redefines** a method with the same name.

### **Example of Method Overriding**
```python
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):  # Overriding the speak() method
        return "Woof!"

class Cat(Animal):
    def speak(self):  # Overriding the speak() method
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
```
Here, `Dog` and `Cat` **override** the `speak()` method from `Animal` to provide their own behavior.

---

## **4️⃣ Practice Exercises**
Try implementing the following:

1️⃣ **Create a `Person` class**  
   - Attributes: `name`, `age`  
   - Method: `introduce()` → prints `"Hi, my name is {name} and I am {age} years old."`  

2️⃣ **Create a `Student` class that inherits from `Person`**  
   - Add a new attribute: `grade`  
   - Override `introduce()` → `"Hi, I am {name}, {age} years old, and in grade {grade}."`  

3️⃣ **Experiment with `super()`**  
   - Ensure the `Student` class correctly calls the `Person` constructor using `super()`.

---

## **5️⃣ Reflection:**
- **Why is inheritance useful in programming?**  
- **How does method overriding allow us to customize behavior in child classes?**  
- **Can you think of a real-world example where inheritance would be beneficial?**  

---

### **Tomorrow: Polymorphism and Core OOP Principles**  
Next, we’ll explore **polymorphism**, which allows us to use a single interface for multiple types. 🚀  

Let me know if you have any questions! 😊