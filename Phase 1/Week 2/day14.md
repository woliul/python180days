# **Day 14: Reflection & Improving Your Mini Project**  

Today is all about **reviewing, testing, and improving** your mini project! 🎯  

---

## **1️⃣ Review Your Code**  
Ask yourself these questions:  
✅ Does my code **work correctly** for all cases?  
✅ Did I **handle errors** (e.g., invalid input, division by zero)?  
✅ Can I **make my code cleaner** using functions and loops?  

### **Example: Improving Code Structure**
Instead of:  
```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print(num1 / num2)
```
Use **functions** to simplify:  
```python
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return "Cannot divide by zero!" if num2 == 0 else num1 / num2
    else:
        return "Invalid operation!"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
print(calculate(num1, num2, operation))
```
✅ **Functions** make your code **more readable and reusable**.  

---

## **2️⃣ Debugging & Testing**  
Run your program and test:  
- **Edge cases** (e.g., negative numbers, zero, invalid inputs).  
- **User experience** (Is it clear? Easy to use?).  
- **Unexpected inputs** (What happens if the user types letters instead of numbers?).  

### **Example: Handling Input Errors**
```python
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a number.")
```
✅ **Using `try-except` prevents crashes** and improves the user experience.

---

## **3️⃣ Bonus: Add More Features 🚀**  
If you’re done, try adding **new features**:  

### **For Calculator:**  
🔹 Allow multiple calculations before exiting.  
🔹 Add an **exponentiation (`**`) and modulo (`%`)** operation.  
🔹 Format output to **2 decimal places** (`round(result, 2)`).  

### **For Number Guessing Game:**  
🔹 Add a **difficulty level** (easy, medium, hard).  
🔹 Limit the **number of guesses** (e.g., 10 attempts).  
🔹 Give **hints** (e.g., "You're getting closer!").  

---

## **4️⃣ Final Reflection & Takeaways**  
- What was **easy** and what was **challenging** in this project?  
- What **bugs** did you fix, and how?  
- How could you **improve the user experience**?  

---

### **Next Week: Strings, Error Handling & File I/O) 📂**  
You’ll learn how to **read, write, and manage files** in Python.  

Let me know if you have any questions! 😊