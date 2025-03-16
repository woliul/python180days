# **Day 43: Extra Exercises on Advanced OOP Topics** 🧠💡

Today, we will focus on **additional exercises** to deepen your understanding of advanced **Object-Oriented Programming** (OOP) concepts and principles. These exercises will help reinforce key topics such as **encapsulation, abstraction, polymorphism**, and **design patterns**.

---

## **1️⃣ Exercise 1: Encapsulation and Data Hiding**

Encapsulation is about hiding the internal state of an object and providing controlled access to it. This ensures that the data is safe from unauthorized modification.

### **🔸 Task: Create an Account Class with Encapsulation**

Let’s create a class `Account` where we encapsulate the **balance** (making it a private attribute) and provide getter and setter methods for safe access.

```python
class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance  # Provide controlled access to balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount  # Set balance safely
        else:
            print("Error: Balance cannot be negative.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Error: Insufficient funds or invalid withdrawal amount.")
```

#### **What we did:**
- We **encapsulated the `__balance`** attribute by making it private (with two underscores).
- We provided **getter** and **setter** methods (`get_balance` and `set_balance`) to safely access and modify the balance.

---

## **2️⃣ Exercise 2: Abstraction with Abstract Base Classes**

Abstraction allows you to define abstract methods in a class, forcing derived classes to implement them. This is useful when you want to specify a common interface for multiple classes.

### **🔸 Task: Create an Abstract Class for Employees**

Let’s create an abstract class `Employee`, which will define an abstract method `calculate_salary()`. All employee types will need to implement this method.

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    @abstractmethod
    def calculate_salary(self):
        pass  # Must be implemented by subclasses

class FullTimeEmployee(Employee):
    def __init__(self, name, id_number, salary):
        super().__init__(name, id_number)
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, name, id_number, hourly_rate, hours_worked):
        super().__init__(name, id_number)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
```

#### **What we did:**
- We created an abstract class `Employee` with an abstract method `calculate_salary()`.
- `FullTimeEmployee` and `PartTimeEmployee` are subclasses that **implement** this method.

---

## **3️⃣ Exercise 3: Polymorphism**

Polymorphism allows objects of different classes to be treated as objects of a common superclass. The most common use of polymorphism is through method overriding.

### **🔸 Task: Demonstrate Polymorphism with Employee Types**

Let’s add polymorphism to the `Employee` example by showing how different employee types calculate their salaries.

```python
def print_salary(employee):
    print(f"{employee.name}'s Salary: {employee.calculate_salary()}")

# Create instances of different employee types
full_time_emp = FullTimeEmployee("Alice", 101, 50000)
part_time_emp = PartTimeEmployee("Bob", 102, 20, 120)

# Demonstrating polymorphism
print_salary(full_time_emp)
print_salary(part_time_emp)
```

#### **What we did:**
- We defined a function `print_salary()` that works for both `FullTimeEmployee` and `PartTimeEmployee` instances. This is **polymorphism** in action—different objects responding to the same method call, but with their own implementation of `calculate_salary()`.

---

## **4️⃣ Exercise 4: Design Patterns (Factory Pattern)**

A **Factory Pattern** is a creational design pattern that provides a way to create objects without specifying the exact class of object that will be created. It's useful when the creation process is complex.

### **🔸 Task: Implement a Factory Pattern for Account Types**

We’ll create a `BankAccountFactory` that produces different types of accounts based on the type of account requested (e.g., `CheckingAccount`, `SavingsAccount`).

```python
class BankAccountFactory:
    @staticmethod
    def create_account(account_type, account_holder, balance=0):
        if account_type == 'checking':
            return CheckingAccount(account_holder, balance)
        elif account_type == 'savings':
            return SavingsAccount(account_holder, balance)
        else:
            raise ValueError("Invalid account type.")

# Using the factory
factory = BankAccountFactory()
checking_account = factory.create_account('checking', 'Alice', 1000)
savings_account = factory.create_account('savings', 'Bob', 2000)

print(checking_account.get_details())
print(savings_account.get_details())
```

#### **What we did:**
- We created a **Factory** class (`BankAccountFactory`) that generates different types of accounts based on the requested type.
- The **factory pattern** simplifies the creation process, allowing for easy scalability if more account types are added in the future.

---

## **5️⃣ Practice Tasks:**
- **Design a `Vehicle` class** hierarchy using **polymorphism** (e.g., Car, Truck, Bike). Implement method overriding to calculate fuel efficiency.
- **Refactor the Bank Account system** to include **abstract base classes** for different account types (CheckingAccount, SavingsAccount, etc.).
- **Create a Factory Pattern** for different types of users in a social media application (Admin, User, Guest), with each type having different privileges and behavior.

---

## **6️⃣ Reflection**
- How does **abstraction** help in making code easier to maintain and extend?
- Why is **polymorphism** useful in scenarios with multiple subclasses that share a common interface?
- How can **encapsulation** improve security and data integrity in your application?
- What are the **advantages of using design patterns** like the Factory Pattern in large systems?

---

### **Next Steps: Week 6 Wrap-up and Final Review!** 🎉  
Tomorrow, we’ll focus on reflecting on your progress in **Week 6**, wrapping up everything you’ve learned, and preparing for the **final project review**.

Let me know if you have any questions or need further clarification on anything! 😊