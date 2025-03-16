# **Day 48: Intro to Web Basics: HTML/CSS & JavaScript Fundamentals (Overview)**

Today, we are stepping into the world of **web development**! This may seem like a big leap from Python, but trust me, it’s all connected. While Python is a powerful backend language, **HTML**, **CSS**, and **JavaScript** are the core technologies used for creating and styling web pages.

We’ll start with the **basics** and introduce you to HTML (structure), CSS (styling), and JavaScript (interaction). You'll also learn how to build a **static webpage**. The goal is to understand how Python fits into the broader context of web development.

---

## **What You’ll Learn:**

### **1. What is HTML?**
HTML (Hypertext Markup Language) is the **standard language** used to create and design the structure of web pages. Think of it as the **skeleton** of a webpage. It tells the browser what content to display and how it’s structured.

- HTML consists of **elements** which are enclosed in tags like `<html>`, `<body>`, `<h1>`, `<p>`, etc.
- Tags are typically written as `<tagname>content</tagname>`.

#### **HTML Structure Example:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Web Page</title>
</head>
<body>
    <h1>Welcome to My Web Page</h1>
    <p>This is a paragraph of text on my website.</p>
</body>
</html>
```

- **`<html>`**: Represents the entire webpage.
- **`<head>`**: Contains metadata (like the title, character encoding).
- **`<body>`**: Contains the visible content of the page (headings, paragraphs, images, etc.).

### **2. What is CSS?**
CSS (Cascading Style Sheets) is used for styling the HTML elements on the webpage. It controls the **layout, colors, fonts**, and positioning of the content.

You can either:
1. Use **inline styles** within an HTML element.
2. Use **internal styles** within a `<style>` block in the `<head>` section.
3. Use **external stylesheets** by linking a separate `.css` file.

#### **CSS Example (inline style):**
```html
<h1 style="color: blue;">Welcome to My Web Page</h1>
```

#### **CSS Example (internal style):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Styled Web Page</title>
    <style>
        body {
            background-color: lightgray;
            font-family: Arial, sans-serif;
        }
        h1 {
            color: darkblue;
        }
        p {
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Styled Web Page</h1>
    <p>This page has some basic styling using CSS!</p>
</body>
</html>
```

- **`body {}`**: Styles the body of the page.
- **`h1 {}`**: Styles the heading `<h1>`.
- **`p {}`**: Styles the paragraph `<p>`.

### **3. What is JavaScript?**
JavaScript is a **scripting language** that adds **interactivity** to web pages. It is used to create dynamic content such as interactive forms, buttons, and animations.

#### **JavaScript Example (alert):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Interactive Page</title>
</head>
<body>
    <button onclick="alert('Hello, World!')">Click Me!</button>
</body>
</html>
```

- **`<button onclick="alert('Hello, World!')">Click Me!</button>`**: When clicked, the button will display an alert box with the message "Hello, World!".

### **4. Putting It All Together**
Let’s now create a basic webpage using **HTML**, **CSS**, and **JavaScript**. The webpage will display a greeting, and the button will change the background color when clicked.

#### **Complete Example:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Web Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: darkblue;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: lightblue;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: lightcoral;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Interactive Web Page!</h1>
    <p>Click the button below to change the background color.</p>
    <button onclick="changeBackgroundColor()">Click Me!</button>

    <script>
        function changeBackgroundColor() {
            document.body.style.backgroundColor = "lightgreen";
        }
    </script>
</body>
</html>
```

- **HTML**: Provides the structure of the page (heading, paragraph, button).
- **CSS**: Styles the body, heading, and button.
- **JavaScript**: Adds functionality to the button so that it changes the background color when clicked.

---

## **Practice:**

### **1. Create Your Own Web Page**
Try building your own basic webpage with HTML, CSS, and JavaScript. It can be a personal webpage, a small portfolio, or a fun project!

Here’s an idea:
- **A simple webpage with your name and a button** that changes the color of the page when clicked.

**HTML Structure**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Web Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            text-align: center;
        }
        h1 {
            color: #333;
        }
        button {
            padding: 15px 30px;
            font-size: 18px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Web Page</h1>
    <button onclick="changeColor()">Change Background Color</button>

    <script>
        function changeColor() {
            let colors = ["lightblue", "lightgreen", "lightyellow", "lightpink"];
            let randomColor = colors[Math.floor(Math.random() * colors.length)];
            document.body.style.backgroundColor = randomColor;
        }
    </script>
</body>
</html>
```

### **2. Experiment with More JavaScript Interactivity:**
- Add a **form** with an input field and a button. When the user submits the form, display the input value in an alert box using JavaScript.

---

## **Review:**
- **HTML** is the structure of a webpage (content).
- **CSS** styles the webpage (layout, colors, fonts).
- **JavaScript** adds interactivity (buttons, alerts, dynamic content).

---

### **What’s Next?**
In the next few days, we’ll explore **Python packages** and **pip** for managing packages, and we’ll also dive into using **virtual environments**. You’ll also get a chance to start building more complex Python projects!

Let me know if you need any further explanations or have questions! Happy coding! 😊