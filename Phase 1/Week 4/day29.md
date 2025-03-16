# **Day 29: Git Basics & Extra Practice**

Today, you'll get introduced to **Git**, a version control system that is essential for tracking and managing changes to your code over time. Additionally, you'll have some **extra practice** time to revisit challenging topics or refine your mini project.

---

## **1️⃣ Introduction to Git: What is Version Control?**

### **Version Control:**
Version control allows you to keep track of changes in your codebase, collaborate with others, and revert back to previous versions if necessary.

**Git** is one of the most widely used version control systems. It helps you manage changes and store code in repositories, making it easier to keep track of your progress and share your code with others.

### **Key Concepts in Git:**
- **Repository (Repo):** A repository is a place where your project files are stored, along with their version history.
- **Commit:** A commit is a snapshot of your project at a particular point in time. Each commit has a unique ID.
- **Branch:** A branch allows you to work on different features or fixes separately, without affecting the main codebase.
- **Merge:** When you’re ready, you can merge your changes from one branch back into the main branch (typically called `main` or `master`).
- **Push:** Pushing sends your local changes to a remote repository (e.g., GitHub).
- **Pull:** Pulling retrieves changes from a remote repository.

---

## **2️⃣ Getting Started with Git: Initial Setup**

### **Step 1: Install Git**
If you haven’t already, download and install Git:
- [Git Download](https://git-scm.com/downloads)

After installation, you can verify it by running the following command in your terminal:
```bash
git --version
```

### **Step 2: Configure Git**
Set up your username and email in Git (Git uses this information for commits):
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### **Step 3: Initialize a Git Repository**
To start using Git in a project, navigate to the project directory and run:
```bash
git init
```
This initializes a Git repository in the folder, allowing you to track changes.

### **Step 4: Check Status**
Check the status of your files in the repository:
```bash
git status
```
It shows which files have been changed and are ready to be committed.

---

## **3️⃣ Basic Git Commands**

### **1. Adding Files to the Repository**
Before committing, you need to add files to the staging area. Use:
```bash
git add <filename>  # Add a specific file
git add .           # Add all files
```

### **2. Committing Changes**
After adding files to the staging area, commit them to the repository:
```bash
git commit -m "Your commit message"
```
The commit message should describe the changes you made, like “Initial commit” or “Fixed bug in shopping list app.”

### **3. Pushing to Remote Repository (GitHub)**

If you want to push your changes to a remote repository (e.g., GitHub), you first need to create a repository on GitHub and link it with your local repo.

- Create a repository on GitHub and get the repository URL.
- Link your local Git repository to GitHub:
  ```bash
  git remote add origin <GitHub repository URL>
  ```

- Push your changes to GitHub:
  ```bash
  git push -u origin main
  ```

---

## **4️⃣ Extra Practice: Revisit Challenging Topics**

### **Task 1: Review Key Topics from the Last Few Days**
Take some time to revisit topics you may have found challenging or areas where you need more practice, such as:

- **Lambda functions and list comprehensions**
- **Nested data structures (lists and dictionaries)**
- **Mini project improvements or additional features**

### **Task 2: Practice Using Git Locally**
- **Initialize a Git repository** in a test folder and practice adding, committing, and pushing changes.
- **Experiment with branches:** Create a new branch, make some changes, then merge the branch back into `main`.

### **Task 3: GitHub Practice**
- Create a repository on **GitHub**.
- Commit your mini project code and **push it to GitHub** so you can track your progress over time.

---

## **5️⃣ Reflection & Questions:**
- **How did using Git help you organize your mini project or other code?**
- **Did you encounter any challenges while setting up or using Git?**
- **Which of the topics this week (Git, extra practice) did you find most useful, and why?**

---

## **6️⃣ Tomorrow: Day 30 – Final Reflection for Phase 1 & Git Best Practices**

Tomorrow, we’ll wrap up Phase 1 of your learning journey! You’ll summarize everything you’ve learned and reflect on your progress, making sure you're ready to move on to the next phase of your Python learning.

Let me know if you need help with any of the Git commands or have questions about anything from today’s lesson!