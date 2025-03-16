# **Day 48: Intro to Web Basics: HTML/CSS & JavaScript Fundamentals (Extended Examples & Practice)**

In today's lesson, we’ll take a deeper dive into **HTML**, **CSS**, and **JavaScript** by providing extended examples and more hands-on practice.

---

## **What You’ll Learn:**
We’ll break down the main topics into three key areas:
1. **HTML Basics**  
2. **CSS Styling Techniques**  
3. **JavaScript Interactivity**

Each topic will include **three examples** and a **practice guide** to help reinforce your learning.

---

### **1. HTML Basics (Structure of Web Pages)**

#### **Example 1: Basic Page Structure**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Basic Web Page</title>
</head>
<body>
    <h1>My First Web Page</h1>
    <p>This is my very first web page created using HTML.</p>
</body>
</html>
```
- This is the most basic HTML structure.
- **`<!DOCTYPE html>`**: Tells the browser this is an HTML5 document.
- **`<head>`**: Contains meta information and the title.
- **`<body>`**: Contains the content visible on the page.

#### **Example 2: Adding Lists**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopping List</title>
</head>
<body>
    <h1>My Shopping List</h1>
    <ul>
        <li>Apples</li>
        <li>Bananas</li>
        <li>Carrots</li>
    </ul>
    <ol>
        <li>First task</li>
        <li>Second task</li>
    </ol>
</body>
</html>
```
- **`<ul>`**: Defines an unordered list (bullets).
- **`<ol>`**: Defines an ordered list (numbers).
- **`<li>`**: Represents each list item.

#### **Example 3: Adding Links and Images**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Web Page with Links</title>
</head>
<body>
    <h1>My Favorite Websites</h1>
    <p>Here are some of my favorite websites:</p>
    <ul>
        <li><a href="https://www.google.com" target="_blank">Google</a></li>
        <li><a href="https://www.wikipedia.org" target="_blank">Wikipedia</a></li>
    </ul>
    <img src="https://via.placeholder.com/150" alt="Placeholder Image">
</body>
</html>
```
- **`<a>`**: Defines a hyperlink. `href` specifies the link target.
- **`<img>`**: Displays an image. `src` specifies the image source URL.

---

### **HTML Practice Guide:**
1. **Create a personal webpage**: Add a heading, an introduction paragraph, and a list of your hobbies.
2. **Add an image**: Include an image of something that represents you (e.g., a favorite place or activity).
3. **Add links**: Add a few external links to your favorite websites or social media profiles.

---

### **2. CSS Styling Techniques (Designing Web Pages)**

#### **Example 1: Basic CSS Styling**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styled Page</title>
    <style>
        body {
            background-color: lightyellow;
            font-family: Arial, sans-serif;
        }
        h1 {
            color: darkblue;
            text-align: center;
        }
        p {
            font-size: 18px;
            color: darkgreen;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Styled Web Page</h1>
    <p>This webpage has some basic styling using CSS.</p>
</body>
</html>
```
- **`body`**: Sets the background color and font for the entire page.
- **`h1`**: Styles the heading, including color and text alignment.
- **`p`**: Styles the paragraph, setting the font size and color.

#### **Example 2: Using Classes and IDs for Targeted Styling**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class and ID Example</title>
    <style>
        .highlight {
            color: red;
            font-weight: bold;
        }
        #main-header {
            text-align: center;
            color: navy;
        }
    </style>
</head>
<body>
    <h1 id="main-header">Hello World</h1>
    <p class="highlight">This is some highlighted text.</p>
    <p>This text is not highlighted.</p>
</body>
</html>
```
- **`class`**: Used to apply the same style to multiple elements.
- **`id`**: Used to apply styles to a specific element.

#### **Example 3: CSS Flexbox Layout**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flexbox Layout</title>
    <style>
        .container {
            display: flex;
            justify-content: space-around;
            align-items: center;
            height: 100vh;
        }
        .box {
            width: 100px;
            height: 100px;
            background-color: lightblue;
            text-align: center;
            line-height: 100px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="box">Box 1</div>
        <div class="box">Box 2</div>
        <div class="box">Box 3</div>
    </div>
</body>
</html>
```
- **`display: flex;`**: Enables Flexbox layout.
- **`justify-content`**: Aligns the items horizontally.
- **`align-items`**: Aligns the items vertically.

---

### **CSS Practice Guide:**
1. **Change the background color** of your personal webpage using a different CSS color.
2. **Create a navigation bar** using an unordered list (`<ul>`) and style it with CSS.
3. **Create a flexbox layout** for multiple items (e.g., text boxes, images) and position them side by side.

---

### **3. JavaScript Interactivity (Adding Dynamic Content)**

#### **Example 1: Alert Message**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Alert</title>
</head>
<body>
    <h1>Click the Button to See a Message</h1>
    <button onclick="showAlert()">Click Me!</button>

    <script>
        function showAlert() {
            alert("Hello! This is a JavaScript alert.");
        }
    </script>
</body>
</html>
```
- **`onclick="showAlert()"`**: Triggers the `showAlert()` function when the button is clicked.
- **`alert()`**: Displays a popup message.

#### **Example 2: Changing Content Dynamically**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Content</title>
</head>
<body>
    <h1 id="headline">Hello, World!</h1>
    <button onclick="changeContent()">Change Heading</button>

    <script>
        function changeContent() {
            document.getElementById("headline").innerHTML = "Welcome to My Web Page!";
        }
    </script>
</body>
</html>
```
- **`document.getElementById("headline")`**: Selects the element with the id `headline`.
- **`innerHTML`**: Changes the content of the selected element.

#### **Example 3: Changing Background Color on Click**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Background Color</title>
</head>
<body>
    <h1>Click the Button to Change Background Color</h1>
    <button onclick="changeBackgroundColor()">Change Color</button>

    <script>
        function changeBackgroundColor() {
            document.body.style.backgroundColor = "lightblue";
        }
    </script>
</body>
</html>
```
- **`document.body.style.backgroundColor`**: Changes the background color of the entire page.

---

### **JavaScript Practice Guide:**
1. **Create a button** that, when clicked, changes the color of the page or an element.
2. **Use JavaScript to display the current date and time** when the user clicks a button.
3. **Write a small script** that asks the user for their name and then displays a greeting message on the page.

---



## **Review & Conclusion**
- **HTML** provides structure to a webpage using elements like headings, paragraphs, lists, and links.
- **CSS** controls the appearance of those elements, such as layout, colors, and fonts.
- **JavaScript** adds interactivity and dynamic features to the page, allowing users to interact with elements in real-time.

By now, you should feel more comfortable with these basic web technologies. The more you practice, the easier it will become to integrate these elements into your projects!

---

Feel free to try the examples and practices provided. Once you’ve completed them, let me know how it goes or if you need more help with anything. Happy coding! 😊