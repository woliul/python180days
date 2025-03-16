# **Day 41: Continue Mini Project Development** 🏗️🚀

Today, we’ll **continue developing** your mini project, adding more **features, improvements, and refinements** based on the project you chose (either Bank Account Simulation or Student Management System).

---

## **1️⃣ Refining the Bank Account Simulation**

### **🔹 Feature 1: Adding Fees for Checking Accounts**
Let's add a **transaction fee** for the **CheckingAccount**. Every time someone withdraws from a Checking Account, they will incur a fee.

```python
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance, fee=2.00):
        super().__init__(account_holder, balance)
        self.fee = fee  # Transaction fee

    def withdraw(self, amount):
        if amount + self.fee <= self._balance:
            self._balance -= (amount + self.fee)
        else:
            print("Insufficient funds, including fee.")
    
    def account_type(self):
        return "Checking"

    def get_details(self):
        return super().get_details() + f", Fee: ${self.fee}"
```
- Now, **checking account** withdrawals include a fee, and the fee can be adjusted when creating the account.

---

### **🔹 Feature 2: Interest for Savings Accounts**
Let’s now add an **interest rate** for the **SavingsAccount** class. After every deposit, we can apply interest based on the balance.

```python
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate  # Apply interest to balance

    def account_type(self):
        return "Savings"

    def get_details(self):
        return super().get_details() + f", Interest Rate: {self.interest_rate*100}%"
```
- **Interest is applied** each time we call `apply_interest()`.

---

## **2️⃣ Refining the Student Management System**

### **🔹 Feature 1: Attendance Tracking**
Let’s add an **attendance tracker** to our `Student` class. This will be useful to track student presence in classes.

```python
class Student:
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id
        self._grades = []
        self._attendance = 0  # Track attendance

    def add_grade(self, grade):
        self._grades.append(grade)

    def add_attendance(self):
        self._attendance += 1  # Increment attendance

    def calculate_gpa(self):
        return sum(self._grades) / len(self._grades) if self._grades else 0

    def get_details(self):
        return f"Name: {self._name}, ID: {self._student_id}, GPA: {self.calculate_gpa():.2f}, Attendance: {self._attendance}"
```

- Now, you can **track the number of classes attended** by calling `add_attendance()`.

---

### **🔹 Feature 2: Display GPA Ranking**
We can display the students' GPAs in **descending order**, allowing us to see the best-performing students.

```python
class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        sorted_students = sorted(self.students, key=lambda stu: stu.calculate_gpa(), reverse=True)
        for stu in sorted_students:
            print(stu.get_details())
```
- Now, students will be displayed based on their GPA, with the **highest GPA** first.

---

## **3️⃣ Practice Tasks**
- **Bank Account**: Add a **method to transfer funds** between two accounts.
- **Student Management**: Allow a **Student** to **update their grade** and **recalculate GPA**.
- Implement **data persistence**: Store all account/student details in a file and read from it when the program starts (file I/O).

---

## **4️⃣ Reflection**
- How can the addition of **fees and interest** improve the **Bank Account** system’s realism?
- Why is **tracking attendance** helpful in the **Student Management System**?
- How does **sorting and ranking** students by GPA benefit the **School System**?

---

### **Tomorrow: Project Review and Optimization! 🔧**
We’ll **refactor and optimize** your code to ensure better performance and functionality.  
Let me know if you have any questions! 😊