# **Day 38: Advanced OOP – Encapsulation & Abstraction** 🛡️🔍  

Today, we take **OOP** to the next level by diving deeper into **encapsulation** and **abstraction**. These principles help us write **secure, modular, and maintainable** code.  

---

## **1️⃣ Encapsulation: Protecting Data** 🔒  
Encapsulation restricts **direct access** to attributes and methods, **protecting object integrity**.  

### **Access Modifiers in Python**
Python has **three types of access control**:  
| Modifier   | Syntax      | Accessibility |
|------------|------------|----------------------|
| **Public**   | `self.name`  | Accessible everywhere |
| **Protected** | `self._name` | Conventionally internal use only |
| **Private** | `self.__name` | Hidden from direct access |

### **Example: Encapsulation in Action**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Public
        self._bank_code = "XYZ123"  # Protected
        self.__balance = balance  # Private

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):  # Getter method to access private attribute
        return self.__balance

account = BankAccount("Alice", 500)
print(account.owner)  # ✅ Public: Accessible
print(account._bank_code)  # ⚠️ Protected: Accessible but discouraged
# print(account.__balance)  # ❌ Private: Throws an error
print(account.get_balance())  # ✅ Accessing private attribute via method
```
✅ **Encapsulation prevents unauthorized changes** to critical attributes.  
✅ **Getter methods** safely expose private data.  

---

## **2️⃣ Abstraction: Hiding Complexity** 🎭  
Abstraction lets you **hide complex details** and **expose only essential functionalities**.

### **Example: Abstract Base Class (ABC)**
```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class
    @abstractmethod
    def speak(self):
        pass  # Must be implemented by subclasses

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# animal = Animal()  # ❌ Cannot instantiate an abstract class
dog = Dog()
print(dog.speak())  # ✅ Woof!
```
✅ Abstract classes **define a blueprint** but **can’t be instantiated**.  
✅ **Child classes must implement** abstract methods.  

---

## **3️⃣ Practice Exercises**
1️⃣ **Modify a class using encapsulation**  
   - Create a `Person` class with **private attributes** for age and name.  
   - Use **getter & setter methods** to access/modify the attributes safely.  

2️⃣ **Implement abstraction**  
   - Create an `Employee` abstract class with an abstract method `calculate_salary()`.  
   - Subclasses `FullTimeEmployee` and `PartTimeEmployee` should implement this method differently.  

---

## **4️⃣ Reflection**
- How does **encapsulation improve data security**?  
- Why do we **use abstraction** instead of directly implementing all logic?  
- When should you **use abstract classes** in projects?  

---

### **Tomorrow: Building an OOP System** 🚀  
Next, we’ll **apply OOP principles** to build a **real-world system** (e.g., employee management).  

Let me know if you have any questions! 😊