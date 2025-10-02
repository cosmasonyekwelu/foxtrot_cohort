**Foxtrot Cohort - Univelcity: Backend with Python Django**
**Week 1, Day 1: Introduction & Foundations**
**Learner: Cosmas Onyekwelu**

**1. Basic Programming Terms**

- **Program:** A set of instructions that tells a computer what to do.
- **Programming Language:** A formal language comprising a set of instructions used to produce various kinds of output (e.g., Python, JavaScript, Java). It's a bridge between human language and machine code (binary 1s and 0s).
- **Syntax:** The set of rules that defines the structure of a language. Just like grammar in English.
- **Variable:** A named container used to store data in memory. `name = "Univelcity"`
- **Data Types:** The classification of data items (e.g., `String` for text, `Integer` for whole numbers, `Boolean` for True/False).
- **Backend:** The "server-side" of a web application. It handles logic, database interactions, user authentication, and server configuration. The user doesn't see it directly.
- **Frontend:** The "client-side" of a web application. It's what users see and interact with in their browser (HTML, CSS, JavaScript).
- **Framework:** A collection of pre-written code that provides a structure to help developers build applications faster and more efficiently (e.g., Django for Python).

**2. Brief Introduction to Python and its Interpreter**

- **Python:** A high-level, general-purpose programming language known for its clear, readable syntax and its emphasis on code readability.
- **Python Interpreter:** A program that reads and executes Python code line-by-line. It translates human-readable Python code into machine-readable instructions on the fly. We use the CPython interpreter (the standard and most widely used one).

**3. Areas of Application of Python**

- **Web Development:** Building server-side logic for websites using frameworks like Django and Flask.
- **Data Science & Analytics:** Data manipulation (Pandas), visualization (Matplotlib, Seaborn), and machine learning (Scikit-learn, TensorFlow).
- **Artificial Intelligence & Machine Learning:** A leading language for AI research and building intelligent systems.
- **Automation & Scripting:** Automating repetitive tasks like file management, web scraping, and system administration.
- **Scientific & Numeric Computing:** Used in fields like biology, astronomy, and physics for complex calculations.

**4. Installation of Necessary Tools**

- **Python 3:** Installed the latest version of Python 3 from python.org. Verified installation using `python --version` in the command prompt.
- **Git:** Installed Git, a distributed version control system, to track changes in our code and collaborate with others.
- **Code Editor:** Set up a code editor (VS Code) for writing code efficiently.

**5. Introduction to Backend Programming**

- **Backend = server side** — deals with logic, database, APIs, authentication, validations, etc.
- Communicates with **front end** (web pages, apps) via **HTTP, JSON, REST**, etc.
- In Python, backend frameworks (e.g., **Django, Flask**) help build web applications, handle routing, models, views, templates, etc.
- The backend is the "engine" of a website. It processes requests from the frontend, works with the database, and sends back the appropriate response.

**6. Git, Command Line & Git Commands**

**6.1 Command Line / Terminal / Shell**

- Basic commands for navigating and managing files:
  - `pwd` (Print Working Directory): Shows the current folder
  - `ls` / `dir`: Lists files and folders in the current directory
  - `cd <directory_name>`: Changes directory
  - `cd ..`: Moves up to parent directory
  - `mkdir <folder_name>`: Creates a new folder
  - `echo <file_name>`: Creates a new file
  - `rm <file_name>`: Removes a file

**6.2 Git Basics**

- Git is a **version control system** — tracks changes in files, supports collaboration
- Common workflow: **clone → edit → commit → push → pull**

**6.3 Key Git Commands**

- `git init` — Initialize new Git repository
- `git clone <url>` — Clone remote repository to local machine
- `git status` — Show file status (modified, staged, untracked)
- `git add <file>` or `git add .` — Stage changes for commit
- `git commit -m "message"` — Commit staged changes with descriptive message
- `git push origin <branch>` — Push commits to remote repository
- `git pull` — Update local repository with remote changes
- `git branch` / `git checkout <branch>` / `git switch <branch>` — Branch management
- `git log` — Show commit history
- `git diff` — See changes between commits or working directory

**Project Setup:**

- Created a local folder named `foxtrot_cohort`
- Initialized a Git repository inside it using `git init`
- Created this `day_1.txt` file to document learnings
- Connected the local repo to a new remote repository on GitHub using `git remote add origin`
- Added, committed, and pushed the changes to GitHub using `git add`, `git commit`, and `git push`

---
