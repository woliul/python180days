# **Day 39: Practice – Build an OOP System** 🏗️🐍  

Today, you’ll apply **Object-Oriented Programming (OOP)** concepts to build a small **real-world application** using **multiple classes, encapsulation, inheritance, and abstraction**.

---

## **1️⃣ Project Idea: Employee Management System** 🏢  

### **🔹 Features**
- Add and remove employees  
- Store employee details (name, role, salary)  
- Calculate salary with bonuses (for managers)  
- Display employee details  

### **2️⃣ Step 1: Define the Base Class**
We'll start with an **abstract class** `Employee`, which enforces a `calculate_salary()` method for all employee types.

```python
from abc import ABC, abstractmethod

class Employee(ABC):  # Abstract base class
    def __init__(self, name, salary):
        self._name = name  # Encapsulation (protected)
        self._salary = salary

    @abstractmethod
    def calculate_salary(self):
        pass

    def get_details(self):
        return f"Name: {self._name}, Salary: ${self._salary}"
```
✅ **Encapsulation:** `_name` and `_salary` are **protected** attributes.  
✅ **Abstraction:** `calculate_salary()` **must be implemented** in subclasses.  

---

## **3️⃣ Step 2: Create Employee Types**
We’ll create two **subclasses**:  
1️⃣ `RegularEmployee`: Gets a **fixed salary**  
2️⃣ `Manager`: Gets **salary + bonus**  

```python
class RegularEmployee(Employee):
    def calculate_salary(self):
        return self._salary  # Fixed salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self._bonus = bonus

    def calculate_salary(self):
        return self._salary + self._bonus  # Salary + bonus
```
✅ **Inheritance** → `RegularEmployee` and `Manager` **inherit** from `Employee`.  
✅ **Polymorphism** → `calculate_salary()` works differently in both classes.  

---

## **4️⃣ Step 3: Create Employee Management System**
We’ll now create a `Company` class that **stores employees** and performs actions like **adding, removing, and displaying employees**.

```python
class Company:
    def __init__(self):
        self.employees = []  # List to store employees

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, name):
        self.employees = [e for e in self.employees if e._name != name]

    def display_employees(self):
        for emp in self.employees:
            print(emp.get_details() + f", Total Salary: ${emp.calculate_salary()}")

# Create a company
company = Company()

# Add employees
emp1 = RegularEmployee("Alice", 5000)
emp2 = Manager("Bob", 7000, 2000)

company.add_employee(emp1)
company.add_employee(emp2)

# Display all employees
company.display_employees()
```
✅ **Encapsulation** → `_name` and `_salary` are **protected** in `Employee`.  
✅ **Polymorphism** → `calculate_salary()` is **implemented differently** in subclasses.  
✅ **Composition** → `Company` **manages a list of Employee objects**.  

---

## **5️⃣ Practice Exercises**
🔹 **Extend the system**:
- Add an `Intern` class with a **stipend-based salary**.  
- Allow `Company` to **search for an employee by name**.  
- Implement a `Promote` method that **converts a `RegularEmployee` to a `Manager`**.  

---

## **6️⃣ Reflection**
- How does **inheritance** help reduce code duplication?  
- Why use **abstraction** for the base `Employee` class?  
- How does **encapsulation** protect our attributes from being modified directly?  

---

### **Tomorrow: Mini Project – Bank Account or Student Management System! 🚀**  
We’ll start building a **larger OOP-based project** with advanced features!  

Let me know if you have any questions! 😊