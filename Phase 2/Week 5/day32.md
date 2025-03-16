# **Day 32: Methods and Constructors** 🚗💡  

Today, we’re diving deeper into **methods** and **constructors** in Python classes. These are fundamental for making your objects more useful and interactive.  

---

## **1️⃣ What are Methods?**
Methods are **functions defined inside a class** that operate on the objects created from that class.  

- **Instance Methods**: Work on individual objects (instances).  
- **Class Methods**: Work on the class itself.  
- **Static Methods**: Work independently of the instance and class.  

---

## **2️⃣ The Role of the Constructor (`__init__`)**  
The constructor is a **special method** in Python called `__init__()`. It is **automatically executed** when you create a new object. It **initializes attributes** for each object.

### **Example: Creating a Car Class with a Constructor**
```python
class Car:
    def __init__(self, make, model, year):
        """Constructor method to initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False  # Default attribute value

    def start_engine(self):
        """Instance method to start the car"""
        self.is_running = True
        return f"The {self.make} {self.model} is now running!"

    def stop_engine(self):
        """Instance method to stop the car"""
        self.is_running = False
        return f"The {self.make} {self.model} has been turned off."

# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2021)
car2 = Car("Ford", "Mustang", 2023)

# Calling methods
print(car1.start_engine())  # The Toyota Camry is now running!
print(car2.stop_engine())   # The Ford Mustang has been turned off.
```

---

## **3️⃣ Instance vs. Class Methods**  

By default, methods are **instance methods**, meaning they work with object-specific data. However, we can also define:  
- **Class Methods** (which use `@classmethod`) to work with class-level data.  
- **Static Methods** (which use `@staticmethod`) when a function does not need access to class attributes.

### **Example of Class and Static Methods**
```python
class Car:
    wheels = 4  # Class attribute (shared by all cars)

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @classmethod
    def change_wheel_count(cls, new_count):
        """Class method to change wheels for all Car instances"""
        cls.wheels = new_count

    @staticmethod
    def car_info():
        """Static method that doesn't access instance or class attributes"""
        return "Cars are a popular means of transportation."

# Using a class method
Car.change_wheel_count(6)  # Changes wheel count for all cars

# Using a static method
print(Car.car_info())  # Output: Cars are a popular means of transportation.
```

---

## **4️⃣ Practice Exercises**
Try these coding tasks to reinforce today’s learning:

1️⃣ **Create a class `Person`** with attributes `name` and `age`. Add an instance method `greet()` that prints `"Hello, my name is {name} and I am {age} years old."`  

2️⃣ **Modify the `Car` class**:
   - Add a method `drive()` that prints `"The {make} {model} is driving!"`
   - Add a `@classmethod` to change a class attribute.
   - Add a `@staticmethod` that prints general car facts.

3️⃣ **Experiment with multiple objects** of your class and test their attributes/methods.

---

## **5️⃣ Reflection:**
- **What is the role of a constructor in Python classes?**  
- **How do instance methods interact with object attributes?**  
- **When would you use a class method vs. a static method?**  

---

### **Tomorrow: Instance vs. Class Variables**
Next, we’ll explore **instance variables vs. class variables** and how they affect your objects. 🚀  

Let me know if you have any questions! 😊