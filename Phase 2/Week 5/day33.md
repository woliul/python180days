# **Day 33: Instance vs. Class Variables** 🆚  

Today, we’ll dive into **instance variables** and **class variables**, understanding how they behave differently and when to use each.  

---

## **1️⃣ What are Instance Variables?**
- Defined inside the **constructor (`__init__` method)** using `self`.
- Unique **to each instance** (object) of the class.
- Changing an instance variable **only affects that specific object**.

### **Example of Instance Variables**
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Unique to each dog
        self.breed = breed

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

print(dog1.name)  # Output: Buddy
print(dog2.name)  # Output: Max
```
Each dog has its own `name` and `breed`.

---

## **2️⃣ What are Class Variables?**
- Defined **outside** the constructor, at the class level.
- **Shared among all instances** of the class.
- Changing a class variable affects **all objects** unless overridden in an instance.

### **Example of Class Variables**
```python
class Dog:
    species = "Canine"  # Class variable (shared by all dogs)

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

print(dog1.species)  # Output: Canine
print(dog2.species)  # Output: Canine

# Changing the class variable for all instances
Dog.species = "Mammal"
print(dog1.species)  # Output: Mammal
print(dog2.species)  # Output: Mammal
```
Now, all dogs are labeled as `"Mammal"` because `species` is a **class variable**.

---

## **3️⃣ Instance vs. Class Variables in Action**
What happens if we **modify a class variable inside an instance**?

```python
class Dog:
    species = "Canine"  # Class variable

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

# Overriding the class variable for dog1 ONLY
dog1.species = "Wolf"

print(dog1.species)  # Output: Wolf (Changed only for this instance)
print(dog2.species)  # Output: Canine (Remains unchanged)
print(Dog.species)   # Output: Canine (Class-level remains unchanged)
```
Here, `dog1.species` creates a **new instance variable** that only affects `dog1`. The class variable `species` remains `"Canine"` for `dog2` and all other instances.

---

## **4️⃣ When to Use Which?**
| Feature          | Instance Variable (`self.attribute`) | Class Variable (`ClassName.attribute`) |
|-----------------|--------------------------------|--------------------------------|
| Defined in      | `__init__` (inside constructor) | At the class level (outside `__init__`) |
| Scope          | Unique to each object | Shared across all objects |
| Modification  | Affects only that specific object | Affects all instances unless overridden |

---

## **5️⃣ Practice Exercises**
Try implementing these concepts:

1️⃣ **Create a class `BankAccount`**  
- Add an **instance variable** `balance` (specific to each user).  
- Add a **class variable** `bank_name` (shared across all accounts).  
- Modify `bank_name` and observe how it affects all instances.  

2️⃣ **Modify an instance variable vs. a class variable**  
- Create multiple objects from a class and modify their attributes.  
- Observe how class variables affect all instances while instance variables remain unique.  

---

## **6️⃣ Reflection:**
- **How do class and instance variables impact memory usage and program behavior?**  
- **When would you use a class variable instead of an instance variable?**  
- **Can you think of a real-world example where class variables would be useful?**  

---

### **Tomorrow: Inheritance and Method Overriding**  
Next, we’ll explore **inheritance**—one of the most powerful features of OOP! 🚀  

Let me know if you have any questions! 😊