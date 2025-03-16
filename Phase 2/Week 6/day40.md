# **Day 40: Mini Project – Bank Account or Student Management System** 🏦🎓  

Today, you’ll **start coding** a mini-project using **OOP concepts** like **encapsulation, inheritance, abstraction, and polymorphism**.  

---

## **1️⃣ Choose Your Mini Project**
You can pick **one** of these two projects:  

### **🔹 Option 1: Bank Account Simulation** 🏦  
**Features:**  
✅ Create **savings** and **checking** accounts  
✅ Deposit and withdraw money  
✅ Display account details  

OR  

### **🔹 Option 2: Student Management System** 🎓  
**Features:**  
✅ Add students with **name, ID, and grades**  
✅ Calculate **GPA**  
✅ Display student details  

---

## **2️⃣ Step 1: Define the Base Class**
We'll create an **abstract base class** for both projects.  

### **Bank Account Base Class**
```python
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder  # Encapsulation
        self._balance = balance

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_details(self):
        return f"Account Holder: {self._account_holder}, Balance: ${self._balance}"
```

---

### **Student Base Class**
```python
class Student:
    def __init__(self, name, student_id):
        self._name = name  # Encapsulation
        self._student_id = student_id
        self._grades = []

    def add_grade(self, grade):
        self._grades.append(grade)

    def calculate_gpa(self):
        return sum(self._grades) / len(self._grades) if self._grades else 0

    def get_details(self):
        return f"Name: {self._name}, ID: {self._student_id}, GPA: {self.calculate_gpa():.2f}"
```

---

## **3️⃣ Step 2: Create Subclasses**
For **BankAccount**, we’ll create **CheckingAccount** and **SavingsAccount**:  
```python
class CheckingAccount(BankAccount):
    def account_type(self):
        return "Checking"

class SavingsAccount(BankAccount):
    def account_type(self):
        return "Savings"
```

For **Student Management**, we can extend the `Student` class for **Undergraduate** and **Graduate** students:  
```python
class UndergraduateStudent(Student):
    def student_level(self):
        return "Undergraduate"

class GraduateStudent(Student):
    def student_level(self):
        return "Graduate"
```

---

## **4️⃣ Step 3: Create a Management System**
For **Bank Management**:
```python
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def display_accounts(self):
        for acc in self.accounts:
            print(acc.get_details() + f", Type: {acc.account_type()}")

# Create Bank and Accounts
bank = Bank()
acc1 = CheckingAccount("Alice", 1000)
acc2 = SavingsAccount("Bob", 5000)

bank.add_account(acc1)
bank.add_account(acc2)
bank.display_accounts()
```

For **Student Management**:
```python
class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for stu in self.students:
            print(stu.get_details())

# Create Students
school = School()
stu1 = UndergraduateStudent("John", 101)
stu1.add_grade(90)
stu1.add_grade(85)

stu2 = GraduateStudent("Emma", 201)
stu2.add_grade(95)
stu2.add_grade(88)

school.add_student(stu1)
school.add_student(stu2)
school.display_students()
```

---

## **5️⃣ Practice Tasks**
- Add a **withdrawal limit** for **SavingsAccount**  
- Allow **Student** to **add multiple grades** and **display best grade**  
- Implement a **search function** to find students/accounts by name  

---

## **6️⃣ Reflection**
- How does **inheritance** help avoid rewriting similar code?  
- Why is **encapsulation** used to restrict access to sensitive data?  
- How would you **expand** this project further?  

---

### **Tomorrow: Continue Mini Project Development! 🚀**  
Let me know if you have any questions! 😊