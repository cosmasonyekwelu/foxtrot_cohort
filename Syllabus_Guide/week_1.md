# Introduction to Python - Comprehensive Guide

## Module 1: Basic Programming Terms

### Fundamental Programming Concepts

**Algorithm**: A step-by-step procedure or formula for solving a problem
```python
# Example: Algorithm to find the largest number in a list
def find_largest(numbers):
    # Step 1: Assume first number is largest
    largest = numbers[0]
    
    # Step 2: Compare with all other numbers
    for num in numbers:
        if num > largest:
            largest = num
    
    # Step 3: Return the largest number
    return largest

# Usage
numbers = [3, 7, 2, 9, 1]
print(f"Largest number: {find_largest(numbers)}")
```

**Variable**: A named storage location in memory that holds a value
```python
# Variables store data
student_name = "Alice"
student_age = 20
grade_average = 85.5
is_enrolled = True

print(f"Student: {student_name}")
print(f"Age: {student_age}")
print(f"Average: {grade_average}")
print(f"Enrolled: {is_enrolled}")
```

**Data Type**: Classification of data that tells the compiler/interpreter how to use the data
```python
# Different data types in Python
integer_number = 42           # int
floating_number = 3.14159     # float
text = "Hello, World!"        # str
is_valid = True               # bool
empty_value = None            # NoneType

print(f"Type of integer_number: {type(integer_number)}")
print(f"Type of floating_number: {type(floating_number)}")
print(f"Type of text: {type(text)}")
print(f"Type of is_valid: {type(is_valid)}")
print(f"Type of empty_value: {type(empty_value)}")
```

**Function**: A reusable block of code that performs a specific task
```python
# Function definition
def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    area = length * width
    return area

# Function calls
room_area = calculate_area(10, 5)
garden_area = calculate_area(15, 8)

print(f"Room area: {room_area} square units")
print(f"Garden area: {garden_area} square units")
```

**Conditional Statement**: Code that executes only if certain conditions are met
```python
# If-else statements
temperature = 25

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("The weather is pleasant.")
else:
    print("It's cold outside.")

# Multiple conditions
age = 18
has_license = True

if age >= 18 and has_license:
    print("You can drive a car.")
else:
    print("You cannot drive a car.")
```

**Loop**: Code that repeats until a certain condition is met
```python
# For loop - iterating a specific number of times
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

# While loop - repeats while condition is true
counter = 1
print("\nCounting with while loop:")
while counter <= 5:
    print(f"Counter: {counter}")
    counter += 1
```

**Syntax**: The set of rules that defines the structure of a programming language
```python
# Correct syntax
def greet(name):
    return f"Hello, {name}!"

# Incorrect syntax (would cause errors)
# def greet(name)
#     return "Hello, " + name
```

**Compiler vs Interpreter**
- **Compiler**: Translates entire program to machine code before execution
- **Interpreter**: Translates and executes code line by line

**Debugging**: The process of finding and fixing errors in code
```python
# Example of debugging by adding print statements
def calculate_average(numbers):
    print(f"Input numbers: {numbers}")  # Debug print
    total = sum(numbers)
    print(f"Total: {total}")  # Debug print
    average = total / len(numbers)
    print(f"Average: {average}")  # Debug print
    return average

scores = [85, 92, 78, 90]
result = calculate_average(scores)
print(f"Final result: {result}")
```

## Module 2: Brief Introduction of Python and Its Interpreter

### What is Python?
Python is a high-level, interpreted, general-purpose programming language known for its simplicity and readability.

### Key Features of Python
```python
# 1. Readable and Simple Syntax
# Compare Python with other languages:

# Python:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Much cleaner than equivalent in many other languages!

# 2. Interpreted Nature
x = 5
y = 10
result = x + y
print(result)  # The interpreter executes this line by line

# 3. Dynamic Typing
variable = 10        # Now it's an integer
print(type(variable))

variable = "hello"   # Now it's a string
print(type(variable))

variable = [1, 2, 3] # Now it's a list
print(type(variable))
```

### Python Interpreter
The Python interpreter is a program that reads and executes Python code.

```python
# How the interpreter works:
# 1. Reads the source code
# 2. Parses it into bytecode
# 3. Executes the bytecode

# You can see this in action:
import dis  # Disassembler for Python bytecode

def simple_function(x):
    return x * 2

# Show the bytecode
print("Bytecode for simple_function:")
dis.dis(simple_function)
```

### Python Implementation Types
```python
# CPython (Standard) - Written in C
# This is what most people use

# You can check your Python implementation
import platform
print(f"Python implementation: {platform.python_implementation()}")
print(f"Python version: {platform.python_version()}")
print(f"Compiler: {platform.python_compiler()}")

# Interactive Mode Example
# You can run Python in interactive mode by typing 'python' in terminal
# Then you can execute code line by line:

"""
$ python
Python 3.9.0 (default, Oct  6 2021, 00:00:00)
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 5
>>> y = 3
>>> x + y
8
>>> print("Hello, World!")
Hello, World!
>>> exit()
"""
```

### Python Execution Process
```python
# Demonstration of interpretation process
def demonstrate_interpretation():
    print("Step 1: This line is executed first")
    x = 10
    print(f"Step 2: x is assigned value {x}")
    y = x * 2
    print(f"Step 3: y is calculated as {y}")
    result = x + y
    print(f"Step 4: Final result is {result}")
    return result

# The interpreter executes this function line by line
final_result = demonstrate_interpretation()
print(f"Function returned: {final_result}")
```

## Module 3: Areas of Application of Python Programming Language

### Web Development
```python
# Flask web framework example (conceptual)
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/user/<name>')
def user_profile(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)
"""

print("Python is used in web frameworks like:")
print("- Django: High-level framework for rapid development")
print("- Flask: Microframework for lightweight applications")
print("- FastAPI: Modern framework for APIs")
```

### Data Science and Analytics
```python
# Data analysis example (conceptual)
import pandas as pd
import numpy as np

# Create sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 70000, 55000],
    'Department': ['IT', 'HR', 'IT', 'Finance']
}

# Create DataFrame
df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)
print("\nBasic Statistics:")
print(df.describe())

# Data visualization (conceptual)
"""
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['Salary'])
plt.title('Salaries by Employee')
plt.xlabel('Employee Name')
plt.ylabel('Salary')
plt.show()
"""
```

### Machine Learning and AI
```python
# Machine learning example (conceptual)
"""
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy:.2f}")
"""

print("Python ML Libraries:")
print("- scikit-learn: Traditional machine learning")
print("- TensorFlow: Deep learning framework")
print("- PyTorch: Research-focused deep learning")
print("- Keras: High-level neural networks API")
```

### Scientific Computing
```python
# Scientific computing example
import math
import statistics

# Mathematical operations
numbers = [2, 4, 6, 8, 10]

print("Scientific Computing Examples:")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Value of pi: {math.pi}")
print(f"Sine of 90 degrees: {math.sin(math.radians(90))}")
print(f"Mean of numbers: {statistics.mean(numbers)}")
print(f"Standard deviation: {statistics.stdev(numbers)}")

# Complex calculations
def calculate_compound_interest(principal, rate, time):
    """Calculate compound interest"""
    amount = principal * (1 + rate/100) ** time
    return amount

investment = 1000
interest_rate = 5
years = 10

final_amount = calculate_compound_interest(investment, interest_rate, years)
print(f"${investment} at {interest_rate}% for {years} years: ${final_amount:.2f}")
```

### Automation and Scripting
```python
# File system automation
import os
import shutil

def organize_files(directory):
    """Organize files by extension"""
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # Get file extension
            _, extension = os.path.splitext(filename)
            extension = extension.lower()
            
            # Create folder for extension if it doesn't exist
            ext_folder = os.path.join(directory, extension[1:] + "_files")
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
            
            # Move file
            source = os.path.join(directory, filename)
            destination = os.path.join(ext_folder, filename)
            shutil.move(source, destination)
            print(f"Moved {filename} to {ext_folder}")

print("Python is excellent for:")
print("- File management and organization")
print- Web scraping and data extraction")
print("- System administration tasks")
print("- Automated testing")
```

### Game Development
```python
# Simple text-based game
import random
import time

def number_guessing_game():
    """Simple number guessing game"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return
        
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"Game over! The number was {secret_number}.")

# Uncomment to play the game
# number_guessing_game()

print("\nPython in Game Development:")
print("- PyGame: Library for game development")
print("- Arcade: Modern game development library")
print("- Panda3D: 3D game engine")
```

## Module 4: Installation of Necessary Tools

### Installing Python

#### Windows Installation
```python
# Steps for Windows:
"""
1. Visit python.org/downloads
2. Download Python 3.x.x installer
3. Run installer
4. CHECK "Add Python to PATH" option
5. Choose "Install Now" or "Customize installation"
6. Verify installation by opening Command Prompt and typing: python --version
"""

# Verification script for Windows
import sys
import platform

print("Python Installation Details:")
print(f"Version: {sys.version}")
print(f"Platform: {platform.system()} {platform.release()}")
print(f"Architecture: {platform.architecture()[0]}")
print(f"Python Executable: {sys.executable}")
```

#### macOS Installation
```python
# Steps for macOS:
"""
Method 1: Official Installer
1. Visit python.org/downloads
2. Download macOS installer
3. Open .pkg file and follow instructions
4. Verify with: python3 --version

Method 2: Homebrew
1. Install Homebrew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. Install Python: brew install python
3. Verify: python3 --version
"""

print("macOS Specific Checks:")
print(f"System: {platform.system()} {platform.mac_ver()[0]}")
print(f"Python Path: {sys.prefix}")
```

#### Linux Installation
```python
# Steps for Linux:
"""
Ubuntu/Debian:
sudo apt update
sudo apt install python3 python3-pip

CentOS/RHEL:
sudo yum install python3 python3-pip

Fedora:
sudo dnf install python3 python3-pip

Verify: python3 --version
"""

print("Linux Environment Check:")
print(f"Platform: {platform.platform()}")
print(f"Python Prefix: {sys.prefix}")
```

### Installing Code Editor/IDE

#### VS Code Installation and Setup
```python
# VS Code Python Setup:
"""
1. Download VS Code from code.visualstudio.com
2. Install Python extension from Microsoft
3. Create a new file with .py extension
4. Start coding with IntelliSense support
"""

# Demonstration of IDE features
def demonstrate_ide_features():
    """
    This function demonstrates features you get with a proper IDE:
    - Syntax highlighting
    - Code completion
    - Error detection
    - Debugging support
    - Git integration
    """
    numbers = [1, 2, 3, 4, 5]
    
    # IDE will show suggestions for list methods
    squared = [x**2 for x in numbers]
    
    return squared

result = demonstrate_ide_features()
print(f"IDE features demonstration result: {result}")
```

#### Jupyter Notebook Installation
```python
# Jupyter Notebook for Data Science:
"""
Installation:
pip install jupyterlab

Usage:
jupyter lab

Benefits:
- Interactive coding
- Immediate feedback
- Great for data analysis and visualization
- Combine code, text, and visualizations
"""

print("Jupyter Notebook Advantages:")
advantages = [
    "Interactive execution of code cells",
    "Inline visualization of plots and charts",
    "Mix code, text, and equations",
    "Perfect for data exploration",
    "Easy sharing of results"
]

for i, advantage in enumerate(advantages, 1):
    print(f"{i}. {advantage}")
```

### Package Management with pip
```python
# Using pip to manage Python packages
"""
Common pip commands:
- Install package: pip install package_name
- Install specific version: pip install package_name==1.0.0
- Upgrade package: pip install --upgrade package_name
- Uninstall package: pip uninstall package_name
- List installed packages: pip list
- Save requirements: pip freeze > requirements.txt
- Install from requirements: pip install -r requirements.txt
"""

# Demonstration of package installation benefits
def demonstrate_packages():
    """
    After installing packages like:
    - pip install requests
    - pip install pandas
    - pip install matplotlib
    """
    
    # Example of what you can do with installed packages
    print("Popular Python Packages:")
    packages = {
        "requests": "HTTP library for making API calls",
        "pandas": "Data manipulation and analysis",
        "numpy": "Numerical computing",
        "matplotlib": "Plotting and visualization",
        "scikit-learn": "Machine learning",
        "django": "Web framework",
        "flask": "Micro web framework"
    }
    
    for package, description in packages.items():
        print(f"  {package}: {description}")

demonstrate_packages()
```

### Virtual Environments
```python
# Creating and using virtual environments
"""
Why use virtual environments?
- Isolate project dependencies
- Avoid version conflicts
- Reproducible environments

Creating a virtual environment:

Windows:
python -m venv myenv
myenv\Scripts\activate

macOS/Linux:
python3 -m venv myenv
source myenv/bin/activate

Deactivate with: deactivate
"""

import venv
import subprocess
import sys

def demonstrate_venv_importance():
    print("Virtual Environment Benefits:")
    benefits = [
        "Project-specific dependencies",
        "No conflicts between project requirements",
        "Easy to share and reproduce environments",
        "Clean system Python installation"
    ]
    
    for benefit in benefits:
        print(f"  ✓ {benefit}")

demonstrate_venv_importance()
```

## Module 5: First Python Code

### Your First Python Program
```python
# The traditional first program
print("Hello, World!")

# Let's break it down:
# - 'print' is a built-in function
# - Parentheses () contain the arguments
# - "Hello, World!" is a string (text)
# - The entire line is a statement
```

### Understanding Basic Program Structure
```python
# A complete simple Python program
def main():
    """Main function that coordinates the program"""
    # Get user input
    name = input("Please enter your name: ")
    
    # Process the input
    greeting = create_greeting(name)
    
    # Output the result
    print(greeting)
    
    # Demonstrate some calculations
    demonstrate_calculations()

def create_greeting(name):
    """Create a personalized greeting"""
    return f"Hello, {name}! Welcome to Python programming."

def demonstrate_calculations():
    """Show basic arithmetic operations"""
    print("\nLet's do some calculations:")
    
    # Basic arithmetic
    a = 15
    b = 4
    
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} // {b} = {a // b}")  # Integer division
    print(f"{a} % {b} = {a % b}")   # Modulus (remainder)

# This ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
```

### Interactive Python Session
```python
# Example of an interactive Python session
"""
Open terminal/command prompt and type 'python' or 'python3'

You'll see something like:
Python 3.9.0 (default, Oct  6 2021, 00:00:00)
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>

Now you can type commands directly:
>>> 2 + 2
4
>>> name = "Alice"
>>> print(f"Hello, {name}")
Hello, Alice
>>> numbers = [1, 2, 3, 4, 5]
>>> sum(numbers)
15
>>> exit()
"""

# Let's simulate an interactive session in a script
def simulate_interactive_session():
    print("Simulating Interactive Python Session:")
    print(">>> x = 10")
    x = 10
    print(">>> y = 20")
    y = 20
    print(">>> x + y")
    print(x + y)
    print(">>> message = 'Python is fun!'")
    message = 'Python is fun!'
    print(">>> print(message)")
    print(message)
    print(">>> len(message)")
    print(len(message))

simulate_interactive_session()
```

### Writing and Running Python Files
```python
# Steps to create and run a Python file:
"""
1. Create a new file with .py extension (e.g., my_program.py)
2. Write your Python code in the file
3. Save the file
4. Run it from terminal: python my_program.py
"""

# Example of a well-structured Python file
"""
# my_program.py

\"\"\"
This is a sample Python program that demonstrates
basic programming concepts and good structure.
\"\"\"

# Import statements at the top
import math
import datetime

# Constants (usually in ALL_CAPS)
PI = math.pi
COMPANY_NAME = "Awesome Corp"

# Function definitions
def calculate_circle_area(radius):
    \"\"\"Calculate the area of a circle\"\"\"
    return PI * (radius ** 2)

def get_current_greeting():
    \"\"\"Return appropriate greeting based on time of day\"\"\"
    current_hour = datetime.datetime.now().hour
    
    if current_hour < 12:
        return "Good morning!"
    elif current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Main program logic
def main():
    \"\"\"Main function that runs the program\"\"\"
    print(f"{get_current_greeting()} Welcome to {COMPANY_NAME}!")
    
    # Get user input
    try:
        radius = float(input("Enter the radius of a circle: "))
        
        # Calculate and display result
        area = calculate_circle_area(radius)
        print(f"The area of a circle with radius {radius} is {area:.2f}")
        
    except ValueError:
        print("Please enter a valid number!")

# Standard boilerplate to call main()
if __name__ == "__main__":
    main()
"""
```

### Common Beginner Mistakes and Solutions
```python
# Example of common errors and how to fix them

def demonstrate_common_errors():
    print("Common Beginner Errors and Solutions:")
    
    # 1. Syntax Error - missing colon
    print("\n1. Syntax Error - missing colon:")
    print("Incorrect: if x == 5")
    print("Correct: if x == 5:")
    
    # 2. Name Error - using undefined variable
    print("\n2. Name Error - undefined variable:")
    print("Incorrect: print(undefined_variable)")
    print("Correct: my_variable = 5; print(my_variable)")
    
    # 3. Type Error - wrong data type
    print("\n3. Type Error - wrong data type:")
    print("Incorrect: '5' + 3")
    print("Correct: int('5') + 3 or '5' + str(3)")
    
    # 4. Indentation Error - inconsistent spacing
    print("\n4. Indentation Error:")
    print("Incorrect:")
    print("def my_function():")
    print("print('Hello')  # Missing indentation")
    print("Correct:")
    print("def my_function():")
    print("    print('Hello')  # Proper indentation")
    
    # 5. Value Error - invalid conversion
    print("\n5. Value Error:")
    print("Incorrect: int('hello')")
    print("Correct: Use try-except or validate input")

demonstrate_common_errors()

# Proper error handling example
def safe_division():
    """Demonstrate proper error handling"""
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))
        
        result = numerator / denominator
        print(f"Result: {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Uncomment to test error handling
# safe_division()
```

## Module 6: Python Syntax

### Basic Syntax Rules
```python
# 1. Statements and Lines
# Each line is typically one statement
x = 5
y = 10
result = x + y

# Multiple statements on one line (not recommended for readability)
x = 5; y = 10; result = x + y

# Line continuation with backslash or parentheses
long_string = "This is a very long string that " \
              "spans multiple lines for better " \
              "readability in the code."

long_calculation = (1 + 2 + 3 + 4 + 5 +
                   6 + 7 + 8 + 9 + 10)

print(long_string)
print(f"Long calculation result: {long_calculation}")
```

### Indentation and Code Blocks
```python
# Python uses indentation to define code blocks
# Standard is 4 spaces (not tabs)

def demonstrate_indentation():
    # This is the function block
    print("This is inside the function")
    
    if True:
        # This is inside the if block
        print("This is inside the if statement")
        
        for i in range(3):
            # This is inside the for loop
            print(f"Loop iteration: {i}")
    
    # Back to function block
    print("Back in function block")

demonstrate_indentation()

# Incorrect indentation examples
def bad_indentation_example():
    # This would cause IndentationError
    # print("No indentation")  # WRONG!
    print("Proper indentation")  # CORRECT

bad_indentation_example()
```

### Comments and Documentation
```python
# Single-line comments start with #

"""
Multi-line comments can use triple quotes
This is often used for docstrings and block comments
"""

def calculate_volume(length, width, height):
    """
    Calculate the volume of a rectangular prism.
    
    Parameters:
    length (float): The length of the prism
    width (float): The width of the prism
    height (float): The height of the prism
    
    Returns:
    float: The volume calculated as length * width * height
    """
    volume = length * width * height  # Calculate volume
    return volume

# Inline comments should be used sparingly and meaningfully
result = calculate_volume(5, 3, 2)  # Volume of 5x3x2 box

print(f"Volume: {result}")

# Accessing docstrings
print("\nFunction documentation:")
print(calculate_volume.__doc__)
```

### Naming Conventions
```python
# Python naming conventions (PEP 8)

# Variables and functions: snake_case
student_name = "Alice"
average_grade = 85.5
def calculate_final_score():
    pass

# Constants: UPPER_CASE
MAX_STUDENTS = 100
DEFAULT_TIMEOUT = 30

# Classes: PascalCase
class StudentRecord:
    pass

class CourseManagementSystem:
    pass

# Private variables/methods: _single_leading_underscore
_internal_variable = "internal use"

def _private_method():
    pass

# Strongly private: __double_leading_underscore
__very_private_variable = "really private"

def demonstrate_naming():
    """Show examples of proper naming"""
    # Good variable names
    user_age = 25
    item_price = 19.99
    is_logged_in = True
    
    # Bad variable names (avoid these)
    # a = 25  # Too vague
    # temp = 19.99  # Not descriptive
    # flag = True  # Unclear what it represents
    
    print(f"User age: {user_age}")
    print(f"Item price: ${item_price}")
    print(f"Logged in: {is_logged_in}")

demonstrate_naming()
```

### Import Statements
```python
# Different ways to import modules

# 1. Import entire module
import math
import datetime

# 2. Import specific functions/classes
from random import randint, choice
from statistics import mean, median

# 3. Import with alias
import numpy as np
import pandas as pd

# 4. Import all (generally not recommended)
# from math import *

def demonstrate_imports():
    """Show how to use imported modules"""
    
    # Using math module
    radius = 5
    circle_area = math.pi * (radius ** 2)
    print(f"Area of circle with radius {radius}: {circle_area:.2f}")
    
    # Using random module
    random_number = randint(1, 100)
    fruits = ["apple", "banana", "cherry"]
    random_fruit = choice(fruits)
    
    print(f"Random number: {random_number}")
    print(f"Random fruit: {random_fruit}")
    
    # Using statistics
    test_scores = [85, 92, 78, 96, 88]
    average_score = mean(test_scores)
    median_score = median(test_scores)
    
    print(f"Test scores: {test_scores}")
    print(f"Average: {average_score:.1f}")
    print(f"Median: {median_score}")

demonstrate_imports()
```

### Basic Syntax Examples
```python
# Comprehensive syntax demonstration

def syntax_demonstration():
    """Demonstrate various Python syntax elements"""
    
    # Variable assignment
    counter = 0
    message = "Hello, Python!"
    pi_value = 3.14159
    
    # Basic operations
    a = 10
    b = 3
    
    arithmetic_results = {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b,
        "floor_division": a // b,
        "modulus": a % b,
        "exponent": a ** b
    }
    
    print("Arithmetic Operations:")
    for operation, result in arithmetic_results.items():
        print(f"  {operation}: {result}")
    
    # String operations
    greeting = "Hello"
    name = "Alice"
    
    full_greeting = greeting + " " + name  # Concatenation
    repeated_greeting = greeting * 3       # Repetition
    
    print(f"\nString Operations:")
    print(f"  Concatenation: {full_greeting}")
    print(f"  Repetition: {repeated_greeting}")
    print(f"  Upper case: {greeting.upper()}")
    print(f"  String length: {len(greeting)}")
    
    # List operations
    numbers = [1, 2, 3, 4, 5]
    numbers.append(6)           # Add to end
    numbers.insert(0, 0)        # Insert at beginning
    numbers.remove(3)           # Remove value
    
    print(f"\nList Operations:")
    print(f"  Numbers: {numbers}")
    print(f"  First element: {numbers[0]}")
    print(f"  Last element: {numbers[-1]}")
    print(f"  Slice [1:4]: {numbers[1:4]}")
    
    # Conditional statements
    temperature = 22
    
    if temperature > 30:
        weather = "Hot"
    elif temperature > 20:
        weather = "Warm"
    elif temperature > 10:
        weather = "Cool"
    else:
        weather = "Cold"
    
    print(f"\nConditional Logic:")
    print(f"  Temperature: {temperature}°C - {weather}")
    
    # Loops
    print(f"\nLoop Examples:")
    
    print("  Counting 1-5:")
    for i in range(1, 6):
        print(f"    {i}", end=" ")
    print()
    
    print("  While loop:")
    count = 5
    while count > 0:
        print(f"    {count}", end=" ")
        count -= 1
    print()

syntax_demonstration()
```

## Module 7: Variable Assignment

### Basic Variable Assignment
```python
# Simple variable assignment
name = "Alice"
age = 25
height = 5.6
is_student = True

print("Basic Variable Assignment:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# Multiple assignment in one line
x, y, z = 1, 2, 3
print(f"\nMultiple Assignment: x={x}, y={y}, z={z}")

# Assigning same value to multiple variables
a = b = c = 10
print(f"Same Value: a={a}, b={b}, c={c}")
```

### Variable Naming Rules and Best Practices
```python
def demonstrate_naming_rules():
    """Show proper variable naming conventions"""
    
    # Valid variable names
    student_name = "Bob"           # Letters, numbers, underscore
    _private_data = "secret"       # Can start with underscore
    counter2 = 5                   # Can contain numbers
    MAX_SIZE = 100                 # Constants in uppercase
    
    # Invalid variable names (would cause SyntaxError)
    # 2nd_value = 10              # Cannot start with number
    # student-name = "Alice"      # Cannot use hyphen
    # class = "Math"              # Cannot use keywords
    
    print("Valid Variable Names:")
    print(f"  student_name: {student_name}")
    print(f"  _private_data: {_private_data}")
    print(f"  counter2: {counter2}")
    print(f"  MAX_SIZE: {MAX_SIZE}")
    
    # Descriptive vs non-descriptive names
    print("\nDescriptive vs Non-descriptive Names:")
    
    # Good - descriptive
    hourly_wage = 15.50
    hours_worked = 40
    weekly_pay = hourly_wage * hours_worked
    
    # Bad - non-descriptive
    # h = 15.50
    # w = 40
    # p = h * w
    
    print(f"  Descriptive: hourly_wage=${hourly_wage}, hours_worked={hours_worked}")
    print(f"  Weekly pay: ${weekly_pay}")

demonstrate_naming_rules()
```

### Dynamic Typing in Python
```python
# Python is dynamically typed - variables can change type
def demonstrate_dynamic_typing():
    variable = 10
    print(f"Initial type: {type(variable)}, value: {variable}")
    
    variable = "Now I'm a string"
    print(f"Changed type: {type(variable)}, value: {variable}")
    
    variable = [1, 2, 3]
    print(f"Changed type: {type(variable)}, value: {variable}")
    
    variable = 3.14
    print(f"Changed type: {type(variable)}, value: {variable}")

demonstrate_dynamic_typing()

# Type checking and conversion
def demonstrate_type_operations():
    # Type checking
    values = [42, "hello", 3.14, True, [1, 2, 3]]
    
    print("\nType Checking:")
    for value in values:
        print(f"  Value: {value}, Type: {type(value)}")
    
    # Type conversion
    print("\nType Conversion:")
    
    number_str = "123"
    number_int = int(number_str)
    number_float = float(number_str)
    
    print(f"  Original string: '{number_str}'")
    print(f"  Converted to int: {number_int}")
    print(f"  Converted to float: {number_float}")
    
    # Back to string
    back_to_str = str(number_int)
    print(f"  Back to string: '{back_to_str}'")

demonstrate_type_operations()
```

### Variable Scope
```python
# Understanding variable scope
global_variable = "I'm global"

def demonstrate_scope():
    """Demonstrate local and global scope"""
    
    local_variable = "I'm local"
    global_variable = "I'm local too (shadows global)"  # This creates a new local variable
    
    print("Inside function:")
    print(f"  Local variable: {local_variable}")
    print(f"  Global variable (shadowed): {global_variable}")
    
    # To modify global variable
    global truly_global_variable
    truly_global_variable = "I can be accessed anywhere"

def modify_global():
    """Demonstrate modifying global variables"""
    global global_variable
    global_variable = "I modified the global variable"

print("Before function calls:")
print(f"Global variable: {global_variable}")

demonstrate_scope()
print(f"After demonstrate_scope(): {global_variable}")

modify_global()
print(f"After modify_global(): {global_variable}")

# Nested scope example
def outer_function():
    outer_var = "I'm in outer function"
    
    def inner_function():
        inner_var = "I'm in inner function"
        print(f"  Inner can access: {outer_var}")  # Can access outer scope
        return inner_var
    
    result = inner_function()
    # print(inner_var)  # This would cause error - inner_var not accessible here
    return result

print(f"\nNested scope result: {outer_function()}")
```

### Advanced Assignment Techniques
```python
# Advanced assignment patterns
def advanced_assignment_techniques():
    """Demonstrate advanced variable assignment patterns"""
    
    # Swapping variables (Pythonic way)
    a, b = 5, 10
    print(f"Before swap: a={a}, b={b}")
    a, b = b, a  # Elegant swap
    print(f"After swap: a={a}, b={b}")
    
    # Extended unpacking (Python 3+)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first, *middle, last = numbers
    print(f"First: {first}, Middle: {middle}, Last: {last}")
    
    # Unpacking in loops
    coordinates = [(1, 2), (3, 4), (5, 6)]
    print("Coordinate unpacking:")
    for x, y in coordinates:
        print(f"  x={x}, y={y}")
    
    # Dictionary unpacking
    student_info = {'name': 'Alice', 'age': 20, 'major': 'CS'}
    name, age, major = student_info.values()
    print(f"Student: {name}, Age: {age}, Major: {major}")
    
    # Walrus operator (Python 3.8+) - assignment expressions
    data = "Python Programming"
    if (n := len(data)) > 10:
        print(f"String '{data}' has {n} characters (more than 10)")
    
    # Multiple return values unpacking
    def get_student_info():
        return "Bob", 22, "Mathematics"
    
    student_name, student_age, student_major = get_student_info()
    print(f"Unpacked: {student_name}, {student_age}, {student_major}")

advanced_assignment_techniques()
```

### Constants and Immutability
```python
# Constants (convention - not enforced)
def demonstrate_constants():
    """Show how to use constants in Python"""
    
    # Convention: UPPER_CASE for constants
    PI = 3.14159
    MAX_CONNECTIONS = 100
    DEFAULT_TIMEOUT = 30
    COMPANY_NAME = "AwesomeTech Inc."
    
    print("Constants (by convention):")
    print(f"  PI: {PI}")
    print(f"  MAX_CONNECTIONS: {MAX_CONNECTIONS}")
    print(f"  DEFAULT_TIMEOUT: {DEFAULT_TIMEOUT}")
    print(f"  COMPANY_NAME: {COMPANY_NAME}")
    
    # Note: These can still be changed (Python doesn't enforce constants)
    # PI = 3.0  # This would work but is against convention
    
    # Using constants in calculations
    radius = 5
    circle_area = PI * (radius ** 2)
    circumference = 2 * PI * radius
    
    print(f"\nCircle with radius {radius}:")
    print(f"  Area: {circle_area:.2f}")
    print(f"  Circumference: {circumference:.2f}")

demonstrate_constants()

# Immutable vs Mutable types
def demonstrate_mutability():
    """Show difference between mutable and immutable types"""
    
    # Immutable types (cannot be changed in-place)
    immutable_string = "hello"
    immutable_tuple = (1, 2, 3)
    immutable_int = 42
    
    print("\nImmutable Types:")
    print(f"  Original string: {immutable_string}")
    # immutable_string[0] = 'H'  # This would cause TypeError
    
    new_string = immutable_string.upper()  # Returns new string
    print(f"  New string: {new_string}")
    print(f"  Original unchanged: {immutable_string}")
    
    # Mutable types (can be changed in-place)
    mutable_list = [1, 2, 3]
    mutable_dict = {'a': 1, 'b': 2}
    
    print("\nMutable Types:")
    print(f"  Original list: {mutable_list}")
    mutable_list.append(4)  # Modifies original list
    print(f"  Modified list: {mutable_list}")
    
    mutable_dict['c'] = 3  # Modifies original dictionary
    print(f"  Modified dict: {mutable_dict}")

demonstrate_mutability()
```

## Module 8: Simple Operations

### Arithmetic Operations
```python
def demonstrate_arithmetic_operations():
    """Show all basic arithmetic operations in Python"""
    
    a = 15
    b = 4
    
    print("Basic Arithmetic Operations:")
    print(f"a = {a}, b = {b}")
    print(f"Addition (a + b): {a + b}")
    print(f"Subtraction (a - b): {a - b}")
    print(f"Multiplication (a * b): {a * b}")
    print(f"Division (a / b): {a / b}")
    print(f"Floor Division (a // b): {a // b}")
    print(f"Modulus/Remainder (a % b): {a % b}")
    print(f"Exponentiation (a ** b): {a ** b}")
    
    # Order of operations (PEMDAS)
    result = 10 + 5 * 2 ** 3 / 4 - 1
    print(f"\nOrder of Operations: 10 + 5 * 2 ** 3 / 4 - 1 = {result}")
    
    # Using parentheses to control order
    result_with_parentheses = (10 + 5) * (2 ** 3) / (4 - 1)
    print(f"With Parentheses: (10 + 5) * (2 ** 3) / (4 - 1) = {result_with_parentheses:.2f}")

demonstrate_arithmetic_operations()
```

### Comparison Operations
```python
def demonstrate_comparison_operations():
    """Show comparison operations that return True or False"""
    
    x = 10
    y = 5
    z = 10
    
    print("Comparison Operations:")
    print(f"x = {x}, y = {y}, z = {z}")
    print(f"Equal (x == z): {x == z}")
    print(f"Not Equal (x != y): {x != y}")
    print(f"Greater Than (x > y): {x > y}")
    print(f"Less Than (x < y): {x < y}")
    print(f"Greater Than or Equal (x >= z): {x >= z}")
    print(f"Less Than or Equal (y <= x): {y <= x}")
    
    # String comparisons
    name1 = "Alice"
    name2 = "Bob"
    name3 = "Alice"
    
    print(f"\nString Comparisons:")
    print(f"name1 = '{name1}', name2 = '{name2}', name3 = '{name3}'")
    print(f"name1 == name3: {name1 == name3}")
    print(f"name1 != name2: {name1 != name2}")
    print(f"name1 < name2 (alphabetical): {name1 < name2}")  # 'A' comes before 'B'
    
    # Multiple comparisons
    age = 25
    print(f"\nMultiple Comparisons (age = {age}):")
    print(f"18 <= age <= 30: {18 <= age <= 30}")
    print(f"age < 18 or age > 65: {age < 18 or age > 65}")

demonstrate_comparison_operations()
```

### Logical Operations
```python
def demonstrate_logical_operations():
    """Show logical operations with boolean values"""
    
    # Basic logical operations
    true_value = True
    false_value = False
    
    print("Logical Operations:")
    print(f"True and True: {True and True}")
    print(f"True and False: {True and False}")
    print(f"False and True: {False and True}")
    print(f"False and False: {False and False}")
    
    print(f"\nTrue or True: {True or True}")
    print(f"True or False: {True or False}")
    print(f"False or True: {False or True}")
    print(f"False or False: {False or False}")
    
    print(f"\nNot True: {not True}")
    print(f"Not False: {not False}")
    
    # Practical examples
    age = 25
    has_license = True
    has_car = False
    
    print(f"\nPractical Examples (age={age}, has_license={has_license}, has_car={has_car}):")
    print(f"Can drive: {age >= 18 and has_license}")
    print(f"Can rent car: {age >= 21 and has_license and has_car}")
    print(f"Needs public transport: {not has_car or not has_license}")
    
    # Short-circuit evaluation
    def expensive_operation():
        print("  This expensive operation was executed!")
        return True
    
    print(f"\nShort-circuit Evaluation:")
    print("False and expensive_operation():")
    result1 = False and expensive_operation()  # expensive_operation not called
    
    print("True or expensive_operation():")
    result2 = True or expensive_operation()    # expensive_operation not called
    
    print("True and expensive_operation():")
    result3 = True and expensive_operation()   # expensive_operation is called

demonstrate_logical_operations()
```

### Assignment Operations
```python
def demonstrate_assignment_operations():
    """Show various assignment operations"""
    
    # Basic assignment
    x = 10
    print(f"Basic assignment: x = {x}")
    
    # Augmented assignment operators
    x += 5  # Equivalent to x = x + 5
    print(f"After x += 5: x = {x}")
    
    x -= 3  # Equivalent to x = x - 3
    print(f"After x -= 3: x = {x}")
    
    x *= 2  # Equivalent to x = x * 2
    print(f"After x *= 2: x = {x}")
    
    x /= 4  # Equivalent to x = x / 4
    print(f"After x /= 4: x = {x}")
    
    x //= 2  # Equivalent to x = x // 2
    print(f"After x //= 2: x = {x}")
    
    x **= 3  # Equivalent to x = x ** 3
    print(f"After x **= 3: x = {x}")
    
    # String augmented assignment
    text = "Hello"
    text += " World"  # String concatenation
    print(f"String assignment: text = '{text}'")
    
    # List augmented assignment
    numbers = [1, 2, 3]
    numbers += [4, 5]  # List extension
    print(f"List assignment: numbers = {numbers}")

demonstrate_assignment_operations()
```

### Bitwise Operations
```python
def demonstrate_bitwise_operations():
    """Show bit-level operations (advanced but useful)"""
    
    a = 10  # Binary: 1010
    b = 4   # Binary: 0100
    
    print("Bitwise Operations:")
    print(f"a = {a} (binary: {bin(a)}), b = {b} (binary: {bin(b)})")
    print(f"AND (a & b): {a & b} (binary: {bin(a & b)})")
    print(f"OR (a | b): {a | b} (binary: {bin(a | b)})")
    print(f"XOR (a ^ b): {a ^ b} (binary: {bin(a ^ b)})")
    print(f"NOT (~a): {~a} (binary: {bin(~a)})")
    print(f"Left Shift (a << 1): {a << 1} (binary: {bin(a << 1)})")
    print(f"Right Shift (a >> 1): {a >> 1} (binary: {bin(a >> 1)})")
    
    # Practical bitwise examples
    print(f"\nPractical Bitwise Examples:")
    
    # Check if number is even or odd
    number = 7
    is_even = (number & 1) == 0
    print(f"{number} is even: {is_even}")
    
    # Multiply/divide by powers of 2
    value = 5
    doubled = value << 1  # Multiply by 2
    halved = value >> 1   # Divide by 2 (integer division)
    print(f"{value} * 2 = {doubled}, {value} // 2 = {halved}")

demonstrate_bitwise_operations()
```

### Membership and Identity Operations
```python
def demonstrate_membership_identity():
    """Show 'in' and 'is' operations"""
    
    # Membership operations (in, not in)
    fruits = ["apple", "banana", "cherry"]
    sentence = "The quick brown fox jumps over the lazy dog"
    
    print("Membership Operations:")
    print(f"Fruits list: {fruits}")
    print(f"'banana' in fruits: {'banana' in fruits}")
    print(f"'orange' in fruits: {'orange' in fruits}")
    print(f"'apple' not in fruits: {'apple' not in fruits}")
    
    print(f"\nSentence: '{sentence}'")
    print(f"'fox' in sentence: {'fox' in sentence}")
    print(f"'cat' in sentence: {'cat' in sentence}")
    
    # Identity operations (is, is not)
    print(f"\nIdentity Operations:")
    
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a  # c references the same object as a
    
    print(f"a = {a}, b = {b}, c = a")
    print(f"a == b (value equality): {a == b}")
    print(f"a is b (identity equality): {a is b}")
    print(f"a is c (identity equality): {a is c}")
    print(f"a is not b: {a is not b}")
    
    # None checking (always use 'is' for None)
    value = None
    print(f"\nvalue is None: {value is None}")
    print(f"value is not None: {value is not None}")

demonstrate_membership_identity()
```

### Operator Precedence
```python
def demonstrate_operator_precedence():
    """Show operator precedence rules"""
    
    # Operator precedence from highest to lowest:
    # 1. Parentheses ()
    # 2. Exponentiation **
    # 3. Multiplication *, Division /, Floor Division //, Modulus %
    # 4. Addition +, Subtraction -
    # 5. Comparison ==, !=, >, >=, <, <=
    # 6. Logical not
    # 7. Logical and
    # 8. Logical or
    
    print("Operator Precedence Examples:")
    
    # Without parentheses
    result1 = 2 + 3 * 4 ** 2
    print(f"2 + 3 * 4 ** 2 = {result1}")
    
    # With parentheses to change order
    result2 = (2 + 3) * (4 ** 2)
    print(f"(2 + 3) * (4 ** 2) = {result2}")
    
    result3 = 2 + (3 * 4) ** 2
    print(f"2 + (3 * 4) ** 2 = {result3}")
    
    # Complex logical expression
    a, b, c = 5, 10, 15
    logical_result = a < b and b < c or a > c
    print(f"\na={a}, b={b}, c={c}")
    print(f"a < b and b < c or a > c = {logical_result}")
    
    # With parentheses for clarity
    logical_result_clear = (a < b and b < c) or a > c
    print(f"(a < b and b < c) or a > c = {logical_result_clear}")

demonstrate_operator_precedence()
```

## Module 9: Data Types and Type Conversion

### Fundamental Data Types
```python
def demonstrate_basic_data_types():
    """Show all basic data types in Python"""
    
    print("Basic Data Types in Python:")
    
    # Integer (int)
    age = 25
    print(f"Integer: age = {age}, type = {type(age)}")
    
    # Float (floating point)
    price = 19.99
    temperature = -5.5
    print(f"Float: price = {price}, type = {type(price)}")
    print(f"Float: temperature = {temperature}, type = {type(temperature)}")
    
    # String (str)
    name = "Alice"
    message = 'Hello, World!'
    multiline = """This is a
    multi-line
    string"""
    print(f"String: name = '{name}', type = {type(name)}")
    print(f"Multi-line string: {multiline}")
    
    # Boolean (bool)
    is_student = True
    has_graduated = False
    print(f"Boolean: is_student = {is_student}, type = {type(is_student)}")
    print(f"Boolean: has_graduated = {has_graduated}, type = {type(has_graduated)}")
    
    # NoneType
    empty_value = None
    print(f"NoneType: empty_value = {empty_value}, type = {type(empty_value)}")

demonstrate_basic_data_types()
```

### Collection Data Types
```python
def demonstrate_collection_types():
    """Show collection data types"""
    
    print("Collection Data Types:")
    
    # List (ordered, mutable)
    fruits = ["apple", "banana", "cherry"]
    numbers = [1, 2, 3, 4, 5]
    mixed_list = [1, "hello", 3.14, True]
    
    print(f"List: fruits = {fruits}, type = {type(fruits)}")
    print(f"List: numbers = {numbers}, type = {type(numbers)}")
    print(f"Mixed List: {mixed_list}")
    
    # Tuple (ordered, immutable)
    coordinates = (10, 20)
    colors = ("red", "green", "blue")
    single_tuple = (5,)  # Note the comma for single-element tuple
    
    print(f"Tuple: coordinates = {coordinates}, type = {type(coordinates)}")
    print(f"Tuple: colors = {colors}, type = {type(colors)}")
    print(f"Single-element tuple: {single_tuple}, type = {type(single_tuple)}")
    
    # Dictionary (key-value pairs)
    student = {"name": "Alice", "age": 20, "major": "CS"}
    grades = {"math": 85, "science": 92, "history": 78}
    
    print(f"Dictionary: student = {student}, type = {type(student)}")
    print(f"Dictionary: grades = {grades}, type = {type(grades)}")
    
    # Set (unordered, unique elements)
    unique_numbers = {1, 2, 3, 2, 1}  # Duplicates removed
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    print(f"Set: unique_numbers = {unique_numbers}, type = {type(unique_numbers)}")
    print(f"Set: vowels = {vowels}, type = {type(vowels)}")

demonstrate_collection_types()
```

### Type Conversion (Casting)
```python
def demonstrate_type_conversion():
    """Show how to convert between different data types"""
    
    print("Type Conversion (Casting):")
    
    # String to numeric types
    number_str = "123"
    price_str = "45.67"
    
    str_to_int = int(number_str)
    str_to_float = float(price_str)
    
    print(f"String '{number_str}' to int: {str_to_int}, type: {type(str_to_int)}")
    print(f"String '{price_str}' to float: {str_to_float}, type: {type(str_to_float)}")
    
    # Numeric to string
    int_to_str = str(42)
    float_to_str = str(3.14159)
    
    print(f"Int 42 to string: '{int_to_str}', type: {type(int_to_str)}")
    print(f"Float 3.14159 to string: '{float_to_str}', type: {type(float_to_str)}")
    
    # Float to int (truncates decimal part)
    float_num = 9.99
    float_to_int = int(float_num)
    print(f"Float {float_num} to int: {float_to_int}")
    
    # Boolean conversions
    print(f"\nBoolean Conversions:")
    print(f"int(True) = {int(True)}")
    print(f"int(False) = {int(False)}")
    print(f"bool(1) = {bool(1)}")
    print(f"bool(0) = {bool(0)}")
    print(f"bool('Hello') = {bool('Hello')}")
    print(f"bool('') = {bool('')}")
    
    # List, tuple, set conversions
    print(f"\nCollection Conversions:")
    numbers_list = [1, 2, 3, 2, 1]
    numbers_tuple = tuple(numbers_list)
    numbers_set = set(numbers_list)
    
    print(f"Original list: {numbers_list}")
    print(f"To tuple: {numbers_tuple}, type: {type(numbers_tuple)}")
    print(f"To set (duplicates removed): {numbers_set}, type: {type(numbers_set)}")

demonstrate_type_conversion()
```

### Type Checking and Validation
```python
def demonstrate_type_checking():
    """Show how to check and validate data types"""
    
    print("Type Checking and Validation:")
    
    # Using type() function
    values = [42, "hello", 3.14, True, [1, 2, 3], None]
    
    print("Checking types with type():")
    for value in values:
        print(f"  Value: {value:>10} -> Type: {type(value).__name__}")
    
    # Using isinstance() for type checking
    print(f"\nUsing isinstance():")
    test_value = 3.14
    
    checks = [
        isinstance(test_value, int),
        isinstance(test_value, float),
        isinstance(test_value, str),
        isinstance(test_value, (int, float))  # Check multiple types
    ]
    
    print(f"Value: {test_value}")
    print(f"  is int? {checks[0]}")
    print(f"  is float? {checks[1]}")
    print(f"  is str? {checks[2]}")
    print(f"  is int or float? {checks[3]}")
    
    # Practical type validation function
    def validate_input(value, expected_type):
        """Validate that input is of expected type"""
        if not isinstance(value, expected_type):
            raise TypeError(f"Expected {expected_type.__name__}, got {type(value).__name__}")
        return value
    
    print(f"\nInput Validation:")
    try:
        valid_number = validate_input(42, int)
        print(f"Valid input: {valid_number}")
        
        # This will raise TypeError
        invalid_input = validate_input("not a number", int)
    except TypeError as e:
        print(f"Validation error: {e}")

demonstrate_type_checking()
```

### Advanced Type Operations
```python
def demonstrate_advanced_type_operations():
    """Show advanced operations with data types"""
    
    print("Advanced Type Operations:")
    
    # String operations
    text = "Python Programming"
    print(f"Original string: '{text}'")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    print(f"Title case: {text.title()}")
    print(f"Length: {len(text)}")
    print(f"Contains 'Python': {'Python' in text}")
    print(f"Split into words: {text.split()}")
    
    # List operations
    numbers = [1, 2, 3, 4, 5]
    print(f"\nOriginal list: {numbers}")
    print(f"Length: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
    print(f"Sliced [1:4]: {numbers[1:4]}")
    print(f"Reversed: {numbers[::-1]}")
    
    # Dictionary operations
    student = {"name": "Alice", "age": 20, "major": "Computer Science"}
    print(f"\nDictionary: {student}")
    print(f"Keys: {list(student.keys())}")
    print(f"Values: {list(student.values())}")
    print(f"Items: {list(student.items())}")
    print(f"Get 'name': {student.get('name')}")
    print(f"Get 'grade' with default: {student.get('grade', 'Not available')}")
    
    # Set operations
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    print(f"\nSet A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Union: {set_a | set_b}")
    print(f"Intersection: {set_a & set_b}")
    print(f"Difference (A - B): {set_a - set_b}")
    print(f"Symmetric Difference: {set_a ^ set_b}")

demonstrate_advanced_type_operations()
```

## Module 10: Introduction and Usage of Popular Python Functions

### Built-in Functions
```python
def demonstrate_builtin_functions():
    """Show commonly used built-in functions"""
    
    print("Essential Built-in Functions:")
    
    # print() - Output function
    print("Hello, World!")
    name = "Alice"
    age = 25
    print(f"My name is {name} and I'm {age} years old.")
    
    # len() - Get length of sequences
    items = [1, 2, 3, 4, 5]
    text = "Python"
    print(f"\nLength of list {items}: {len(items)}")
    print(f"Length of string '{text}': {len(text)}")
    
    # type() - Get object type
    values = [42, 3.14, "hello", True, [1, 2, 3]]
    print(f"\nType checking:")
    for value in values:
        print(f"  {value} -> {type(value).__name__}")
    
    # input() - Get user input
    # user_name = input("Enter your name: ")
    # print(f"Hello, {user_name}!")
    
    # int(), float(), str(), bool() - Type conversion
    print(f"\nType conversion:")
    print(f"int('123') = {int('123')}")
    print(f"float('3.14') = {float('3.14')}")
    print(f"str(42) = '{str(42)}'")
    print(f"bool('hello') = {bool('hello')}")
    print(f"bool('') = {bool('')}")
    
    # range() - Generate number sequences
    print(f"\nRange examples:")
    print(f"range(5): {list(range(5))}")
    print(f"range(1, 6): {list(range(1, 6))}")
    print(f"range(0, 10, 2): {list(range(0, 10, 2))}")
    
    # sum(), min(), max() - Mathematical operations
    numbers = [10, 5, 8, 3, 15]
    print(f"\nMath operations on {numbers}:")
    print(f"sum: {sum(numbers)}")
    print(f"min: {min(numbers)}")
    print(f"max: {max(numbers)}")

demonstrate_builtin_functions()
```

### String Functions
```python
def demonstrate_string_functions():
    """Show commonly used string methods"""
    
    text = "  Python Programming is Fun!  "
    sentence = "the quick brown fox jumps over the lazy dog"
    
    print("String Methods:")
    print(f"Original text: '{text}'")
    
    # Case conversion
    print(f"\nCase Conversion:")
    print(f"upper(): '{text.upper()}'")
    print(f"lower(): '{text.lower()}'")
    print(f"title(): '{text.title()}'")
    print(f"capitalize(): '{text.capitalize()}'")
    print(f"swapcase(): '{text.swapcase()}'")
    
    # Searching and checking
    print(f"\nSearching and Checking:")
    print(f"startswith('Python'): {text.startswith('Python')}")
    print(f"endswith('Fun!'): {text.endswith('Fun!')}")
    print(f"find('Programming'): {text.find('Programming')}")
    print(f"count('m'): {text.count('m')}")
    print(f"isalpha(): {text.strip().isalpha()}")  # False due to spaces and !
    print(f"isdigit(): {'123'.isdigit()}")
    
    # Modification
    print(f"\nModification:")
    print(f"strip(): '{text.strip()}'")
    print(f"replace('Python', 'Java'): '{text.replace('Python', 'Java')}'")
    print(f"split(): {text.strip().split()}")
    print(f"join(): {'-'.join(['a', 'b', 'c'])}")
    
    # Formatting
    print(f"\nFormatting:")
    name = "Alice"
    age = 25
    print(f"f-string: My name is {name} and I'm {age} years old")
    print("format(): My name is {} and I'm {} years old".format(name, age))

demonstrate_string_functions()
```

### List Functions
```python
def demonstrate_list_functions():
    """Show commonly used list methods"""
    
    numbers = [1, 2, 3, 4, 5]
    fruits = ["apple", "banana", "cherry"]
    
    print("List Methods:")
    print(f"Original numbers: {numbers}")
    print(f"Original fruits: {fruits}")
    
    # Adding elements
    print(f"\nAdding Elements:")
    numbers.append(6)
    print(f"append(6): {numbers}")
    
    numbers.insert(2, 99)
    print(f"insert(2, 99): {numbers}")
    
    numbers.extend([7, 8, 9])
    print(f"extend([7,8,9]): {numbers}")
    
    # Removing elements
    print(f"\nRemoving Elements:")
    removed = numbers.pop()
    print(f"pop(): removed {removed}, list: {numbers}")
    
    removed = numbers.pop(2)
    print(f"pop(2): removed {removed}, list: {numbers}")
    
    numbers.remove(4)
    print(f"remove(4): {numbers}")
    
    # Searching and information
    print(f"\nSearching and Information:")
    print(f"index(3): {numbers.index(3)}")
    print(f"count(2): {numbers.count(2)}")
    print(f"len(numbers): {len(numbers)}")
    
    # Sorting and reversing
    print(f"\nSorting and Reversing:")
    numbers.sort()
    print(f"sort(): {numbers}")
    
    numbers.reverse()
    print(f"reverse(): {numbers}")
    
    # List comprehensions (advanced but very useful)
    print(f"\nList Comprehensions:")
    squares = [x**2 for x in range(1, 6)]
    even_numbers = [x for x in range(10) if x % 2 == 0]
    
    print(f"Squares: {squares}")
    print(f"Even numbers: {even_numbers}")

demonstrate_list_functions()
```

### Dictionary Functions
```python
def demonstrate_dictionary_functions():
    """Show commonly used dictionary methods"""
    
    student = {
        "name": "Alice",
        "age": 20,
        "major": "Computer Science",
        "grades": [85, 92, 78]
    }
    
    print("Dictionary Methods:")
    print(f"Original dictionary: {student}")
    
    # Accessing elements
    print(f"\nAccessing Elements:")
    print(f"student['name']: {student['name']}")
    print(f"student.get('age'): {student.get('age')}")
    print(f"student.get('phone', 'Not available'): {student.get('phone', 'Not available')}")
    
    # Adding and modifying
    print(f"\nAdding and Modifying:")
    student["email"] = "alice@university.edu"
    print(f"Added email: {student}")
    
    student["age"] = 21
    print(f"Updated age: {student}")
    
    # Keys, values, and items
    print(f"\nKeys, Values, and Items:")
    print(f"keys(): {list(student.keys())}")
    print(f"values(): {list(student.values())}")
    print(f"items(): {list(student.items())}")
    
    # Removing elements
    print(f"\nRemoving Elements:")
    removed_grade = student.pop("grades")
    print(f"pop('grades'): removed {removed_grade}, dict: {student}")
    
    removed_item = student.popitem()
    print(f"popitem(): removed {removed_item}, dict: {student}")
    
    # Dictionary comprehensions
    print(f"\nDictionary Comprehensions:")
    squares = {x: x**2 for x in range(1, 6)}
    word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
    
    print(f"Number squares: {squares}")
    print(f"Word lengths: {word_lengths}")

demonstrate_dictionary_functions()
```

### Mathematical Functions
```python
import math
import random

def demonstrate_math_functions():
    """Show mathematical functions from math and random modules"""
    
    print("Mathematical Functions:")
    
    # Basic math functions
    print("Math Module Functions:")
    print(f"math.sqrt(16) = {math.sqrt(16)}")
    print(f"math.pow(2, 3) = {math.pow(2, 3)}")
    print(f"math.fabs(-5.5) = {math.fabs(-5.5)}")
    print(f"math.floor(3.7) = {math.floor(3.7)}")
    print(f"math.ceil(3.2) = {math.ceil(3.2)}")
    print(f"math.pi = {math.pi}")
    print(f"math.e = {math.e}")
    
    # Trigonometric functions
    print(f"\nTrigonometric Functions:")
    angle_degrees = 45
    angle_radians = math.radians(angle_degrees)
    print(f"sin({angle_degrees}°) = {math.sin(angle_radians):.3f}")
    print(f"cos({angle_degrees}°) = {math.cos(angle_radians):.3f}")
    print(f"tan({angle_degrees}°) = {math.tan(angle_radians):.3f}")
    
    # Random functions
    print(f"\nRandom Module Functions:")
    print(f"random.random() = {random.random()}")  # Float between 0 and 1
    print(f"random.randint(1, 10) = {random.randint(1, 10)}")  # Integer in range
    print(f"random.uniform(1.5, 5.5) = {random.uniform(1.5, 5.5):.2f}")  # Float in range
    
    # Random choices
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print(f"random.choice(fruits) = {random.choice(fruits)}")
    print(f"random.sample(fruits, 3) = {random.sample(fruits, 3)}")
    
    # Shuffling
    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    print(f"Shuffled numbers: {numbers}")

demonstrate_math_functions()
```

### File Handling Functions
```python
import os

def demonstrate_file_functions():
    """Show file and directory operations"""
    
    print("File and Directory Functions:")
    
    # File operations
    print("File Operations:")
    
    # Writing to a file
    with open("example.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")
        file.write("Python file handling is easy!\n")
    
    print("Created 'example.txt' with some content")
    
    # Reading from a file
    with open("example.txt", "r") as file:
        content = file.read()
        print(f"File content:\n{content}")
    
    # Reading line by line
    print("Reading line by line:")
    with open("example.txt", "r") as file:
        for i, line in enumerate(file, 1):
            print(f"Line {i}: {line.strip()}")
    
    # Directory operations
    print(f"\nDirectory Operations:")
    print(f"Current directory: {os.getcwd()}")
    print(f"Files in current directory: {os.listdir('.')}")
    
    # File information
    if os.path.exists("example.txt"):
        file_stats = os.stat("example.txt")
        print(f"File size: {file_stats.st_size} bytes")
        print(f"Last modified: {file_stats.st_mtime}")
    
    # Clean up
    os.remove("example.txt")
    print("Cleaned up: removed 'example.txt'")

demonstrate_file_functions()
```

### Practical Function Examples
```python
def demonstrate_practical_functions():
    """Show practical examples combining multiple functions"""
    
    print("Practical Function Examples:")
    
    # Data processing pipeline
    def process_student_data(students):
        """Process student data and generate report"""
        
        # Calculate averages
        averages = {}
        for name, grades in students.items():
            averages[name] = sum(grades) / len(grades)
        
        # Find top student
        top_student = max(averages, key=averages.get)
        top_score = averages[top_student]
        
        # Generate report
        report = []
        report.append("STUDENT GRADE REPORT")
        report.append("=" * 50)
        
        for name, avg in sorted(averages.items()):
            status = "EXCELLENT" if avg >= 90 else "GOOD" if avg >= 80 else "NEEDS IMPROVEMENT"
            report.append(f"{name:15} {avg:6.2f} {status}")
        
        report.append("-" * 50)
        report.append(f"Top Student: {top_student} ({top_score:.2f})")
        
        return "\n".join(report)
    
    # Sample data
    student_grades = {
        "Alice": [85, 92, 78, 96],
        "Bob": [67, 74, 80, 72],
        "Charlie": [95, 88, 92, 98],
        "Diana": [82, 79, 85, 88]
    }
    
    # Generate and print report
    report = process_student_data(student_grades)
    print(report)
    
    # String processing example
    def analyze_text(text):
        """Analyze text and return statistics"""
        words = text.split()
        characters = len(text)
        word_count = len(words)
        unique_words = len(set(words))
        avg_word_length = sum(len(word) for word in words) / word_count
        
        return {
            "characters": characters,
            "words": word_count,
            "unique_words": unique_words,
            "average_word_length": avg_word_length,
            "most_common_words": sorted(set(words), key=words.count, reverse=True)[:3]
        }
    
    sample_text = "Python is a powerful programming language. Python is easy to learn and Python is fun to use."
    analysis = analyze_text(sample_text)
    
    print(f"\nText Analysis:")
    for key, value in analysis.items():
        print(f"  {key}: {value}")

demonstrate_practical_functions()
```

This comprehensive introduction to Python covers all fundamental concepts from basic programming terms to practical function usage. Each module builds upon the previous one, providing a solid foundation for Python programming with detailed explanations and practical code examples.