# Python Data Structures & Looping Constructs - Comprehensive Guide

## Module 1: Use of IF/ELSE/ELIF Statements

### Understanding Conditional Statements

Conditional statements allow your program to make decisions and execute different code blocks based on conditions.

### Basic IF Statement

```python
# Simple if statement
age = 18
if age >= 18:
    print("You are eligible to vote.")
    print("Please register to vote.")

# If with multiple conditions
temperature = 25
if temperature > 30:
    print("It's hot outside.")
if temperature < 10:
    print("It's cold outside.")
if 10 <= temperature <= 30:
    print("The weather is pleasant.")

# Using comparison operators
x = 10
y = 5

if x > y:
    print("x is greater than y")
if x < y:
    print("x is less than y")
if x == y:
    print("x is equal to y")
if x != y:
    print("x is not equal to y")
```

### IF-ELSE Statements

```python
# Basic if-else
age = 16
if age >= 18:
    print("You can watch the movie.")
else:
    print("You are too young for this movie.")

# Multiple conditions with elif
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Nested if-else statements
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive a car.")
    else:
        print("You are old enough but need a license.")
else:
    print("You are too young to drive.")
```

### Advanced Conditional Examples

```python
# Multiple conditions with logical operators
age = 25
income = 50000
credit_score = 700

# Using and, or, not
if age >= 18 and income >= 30000 and credit_score >= 650:
    print("Loan approved!")
else:
    print("Loan denied.")

# Complex conditions
temperature = 28
is_weekend = True
has_umbrella = False

if (temperature > 25 and is_weekend) or (temperature > 30):
    if has_umbrella:
        print("Perfect day for the beach with umbrella!")
    else:
        print("Great beach day, but bring sunscreen!")
elif temperature < 10:
    print("Stay indoors, it's cold!")
else:
    print("Regular day activities.")

# Conditional expressions (ternary operator)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Multiple ternary operations
score = 75
result = "Excellent" if score >= 90 else "Good" if score >= 70 else "Needs Improvement"
print(f"Score {score}: {result}")

# Using 'in' with conditions
fruits = ['apple', 'banana', 'orange']
user_fruit = 'banana'

if user_fruit in fruits:
    print(f"{user_fruit} is available!")
else:
    print(f"Sorry, {user_fruit} is not available.")

# Checking multiple values
day = "Monday"
if day in ["Saturday", "Sunday"]:
    print("It's the weekend!")
else:
    print("It's a weekday.")
```

### Practical Application Examples

```python
# User authentication system
def authenticate_user(username, password, user_database):
    """Authenticate user with username and password"""
    if username in user_database:
        if user_database[username] == password:
            return "Login successful!"
        else:
            return "Invalid password!"
    else:
        return "Username not found!"

# Test authentication
users = {
    "alice": "password123",
    "bob": "secret456",
    "charlie": "mypass789"
}

print(authenticate_user("alice", "password123", users))
print(authenticate_user("alice", "wrongpass", users))
print(authenticate_user("eve", "password123", users))

# Grade calculator with multiple criteria
def calculate_grade(score, attendance, participation):
    """Calculate final grade based on multiple factors"""
    if score >= 90 and attendance >= 90 and participation >= 80:
        return "A - Excellent!"
    elif score >= 80 and attendance >= 80:
        return "B - Good job!"
    elif score >= 70 and attendance >= 70:
        return "C - Satisfactory"
    elif score >= 60:
        return "D - Needs improvement"
    else:
        return "F - Failed"

# Test grade calculation
student1 = calculate_grade(85, 95, 90)
student2 = calculate_grade(92, 75, 85)  # Lower attendance affects grade
student3 = calculate_grade(45, 90, 95)  # Low score fails

print(f"Student 1: {student1}")
print(f"Student 2: {student2}")
print(f"Student 3: {student3}")
```

## Module 2: For/While Loop Statements

### FOR Loops

```python
# Basic for loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

# Looping through a list
fruits = ["apple", "banana", "cherry", "date"]
print("\nFruits in the basket:")
for fruit in fruits:
    print(f"- {fruit}")

# Looping with index using enumerate
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Looping through strings
message = "Python"
print("\nCharacters in 'Python':")
for char in message:
    print(char)

# Nested for loops
print("\nMultiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Empty line between tables
```

### WHILE Loops

```python
# Basic while loop
counter = 1
print("Counting with while loop:")
while counter <= 5:
    print(f"Counter: {counter}")
    counter += 1

# While loop with user input
print("\nNumber guessing game:")
import random
secret_number = random.randint(1, 10)
guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")

# While loop with break
print("\nCounting with break:")
number = 1
while True:
    print(number)
    number += 1
    if number > 5:
        break

# While loop with continue
print("\nOdd numbers with continue:")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
```

### Advanced Loop Examples

```python
# Loop control with else
print("Searching for a number:")
for i in range(1, 6):
    if i == 3:
        print("Found the number 3!")
        break
else:
    print("Number 3 not found in range.")

# This will execute the else block
for i in range(1, 3):
    if i == 5:
        print("Found 5!")
        break
else:
    print("Number 5 not found in range.")

# Practical example: Password validation
def validate_password(password):
    """Validate password strength"""
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if len(password) >= 8 and has_upper and has_lower and has_digit:
        return "Strong password!"
    else:
        return "Weak password. Must be 8+ chars with upper, lower, and digit."

print(validate_password("Weak"))
print(validate_password("StrongPass123"))

# Menu system with while loop
def calculator_menu():
    """Simple calculator with menu"""
    while True:
        print("\n=== Calculator Menu ===")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = num1 + num2
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = num1 - num2
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = num1 * num2
                    print(f"Result: {num1} × {num2} = {result}")
                elif choice == '4':
                    if num2 != 0:
                        result = num1 / num2
                        print(f"Result: {num1} ÷ {num2} = {result}")
                    else:
                        print("Error: Cannot divide by zero!")
            except ValueError:
                print("Error: Please enter valid numbers!")
        else:
            print("Invalid choice! Please enter 1-5.")

# Uncomment to run the calculator
# calculator_menu()
```

## Module 3: Iterators, Iterables & Generators

### Understanding Iterables and Iterators

```python
# What are iterables?
# An iterable is any object capable of returning its members one at a time
# Examples: lists, strings, dictionaries, tuples, sets

# Basic iterable examples
my_list = [1, 2, 3, 4, 5]
my_string = "Hello"
my_dict = {'a': 1, 'b': 2, 'c': 3}

print("List iteration:")
for item in my_list:
    print(item)

print("\nString iteration:")
for char in my_string:
    print(char)

print("\nDictionary iteration:")
for key in my_dict:
    print(f"{key}: {my_dict[key]}")

# Manual iteration using iter() and next()
print("\nManual iteration:")
numbers = [10, 20, 30, 40]
iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
print(next(iterator))  # 40
# print(next(iterator))  # This would raise StopIteration

# Creating a custom iterator
class CountDown:
    """Custom iterator that counts down from a given number"""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1

print("\nCustom countdown iterator:")
countdown = CountDown(5)
for number in countdown:
    print(number)
```

### Generators

```python
# Generator functions use yield instead of return
def simple_generator():
    """A simple generator function"""
    print("Start")
    yield 1
    print("After first yield")
    yield 2
    print("After second yield")
    yield 3
    print("End")

# Using the generator
gen = simple_generator()
print("First next():", next(gen))
print("Second next():", next(gen))
print("Third next():", next(gen))
# print("Fourth next():", next(gen))  # Would raise StopIteration

# Practical generator: Fibonacci sequence
def fibonacci_generator(limit):
    """Generate Fibonacci numbers up to limit"""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

print("\nFibonacci numbers up to 50:")
for num in fibonacci_generator(50):
    print(num, end=" ")

# Generator expression (similar to list comprehension but lazy)
numbers = [1, 2, 3, 4, 5]
squares_gen = (x**2 for x in numbers)  # Generator expression
squares_list = [x**2 for x in numbers]  # List comprehension

print(f"\nGenerator: {squares_gen}")  # Generator object
print(f"List: {squares_list}")       # Actual list

# Using the generator
print("Squares from generator:")
for square in squares_gen:
    print(square)
```

### Advanced Generator Examples

```python
# Infinite sequence generator
def infinite_counter():
    """Generate an infinite sequence of numbers"""
    num = 0
    while True:
        yield num
        num += 1

# Use with caution - infinite loop!
# for i in infinite_counter():
#     print(i)
#     if i > 10:  # Add break condition
#         break

# File reading generator
def read_large_file(filename):
    """Generator to read large files line by line"""
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")

# Simulate file reading
lines = ["Line 1", "Line 2", "Line 3", "Line 4"]
for line in read_large_file("dummy.txt"):
    print(line)  # This won't execute due to file not found

# Batch processing generator
def batch_processor(data, batch_size):
    """Process data in batches"""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

data = list(range(1, 21))  # [1, 2, 3, ..., 20]
print("Batch processing:")
for batch in batch_processor(data, 5):
    print(f"Processing batch: {batch}")

# Generator with state
def stateful_generator():
    """Generator that maintains state between calls"""
    total = 0
    count = 0

    while True:
        value = yield
        if value is None:
            break
        total += value
        count += 1
        yield total / count  # Return average

# Using stateful generator
gen = stateful_generator()
next(gen)  # Start the generator

gen.send(10)  # Send 10 and get average
print(f"Average after 10: {next(gen)}")

gen.send(20)  # Send 20 and get average
print(f"Average after 20: {next(gen)}")

gen.send(30)  # Send 30 and get average
print(f"Average after 30: {next(gen)}")
```

## Module 4: Map, Filter & Reduce

### Map Function

```python
# map(function, iterable) applies function to each item

# Basic map examples
numbers = [1, 2, 3, 4, 5]

# Using lambda with map
squared = list(map(lambda x: x ** 2, numbers))
print(f"Numbers: {numbers}")
print(f"Squared: {squared}")

# Using regular function with map
def to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

fahrenheit_temps = [32, 68, 86, 104, 212]
celsius_temps = list(map(to_celsius, fahrenheit_temps))

print(f"Fahrenheit: {fahrenheit_temps}")
print(f"Celsius: {[round(temp, 1) for temp in celsius_temps]}")

# Map with multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]

sums = list(map(lambda x, y, z: x + y + z, numbers1, numbers2, numbers3))
print(f"Numbers 1: {numbers1}")
print(f"Numbers 2: {numbers2}")
print(f"Numbers 3: {numbers3}")
print(f"Sums: {sums}")

# Practical example: Processing user data
def format_user(user_data):
    """Format user data for display"""
    name, age, city = user_data
    return f"{name.title()} ({age}) from {city.title()}"

users = [
    ("alice", 25, "new york"),
    ("bob", 30, "los angeles"),
    ("charlie", 22, "chicago")
]

formatted_users = list(map(format_user, users))
for user in formatted_users:
    print(user)
```

### Filter Function

```python
# filter(function, iterable) keeps items where function returns True

# Basic filter examples
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"All numbers: {numbers}")
print(f"Even numbers: {evens}")

# Filter numbers greater than 5
large_numbers = list(filter(lambda x: x > 5, numbers))
print(f"Numbers > 5: {large_numbers}")

# Using regular function with filter
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = list(filter(is_prime, range(1, 20)))
print(f"Prime numbers 1-20: {primes}")

# Practical example: Data validation
def is_valid_email(email):
    """Check if email has valid format"""
    return '@' in email and '.' in email and len(email) > 5

emails = [
    "user@example.com",
    "invalid-email",
    "test@domain.org",
    "short",
    "another@company.com"
]

valid_emails = list(filter(is_valid_email, emails))
print(f"All emails: {emails}")
print(f"Valid emails: {valid_emails}")

# Filter with None (removes falsy values)
mixed_data = [0, 1, "hello", "", None, 42, False, "world", True]
truthy_values = list(filter(None, mixed_data))
print(f"Mixed data: {mixed_data}")
print(f"Truthy values: {truthy_values}")
```

### Reduce Function

```python
from functools import reduce

# reduce(function, iterable) applies function cumulatively

# Basic reduce examples
numbers = [1, 2, 3, 4, 5]

# Sum of numbers
total = reduce(lambda x, y: x + y, numbers)
print(f"Numbers: {numbers}")
print(f"Sum: {total}")

# Product of numbers
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")

# Maximum number
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum: {maximum}")

# Practical reduce examples
# Flatten nested lists
nested_lists = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda x, y: x + y, nested_lists)
print(f"Nested lists: {nested_lists}")
print(f"Flattened: {flattened}")

# String concatenation
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda x, y: x + y, words)
print(f"Words: {words}")
print(f"Sentence: {sentence}")

# Complex example: Word frequency counter
def word_frequency(text):
    """Count word frequency using reduce"""
    words = text.lower().split()

    def update_freq(freq_dict, word):
        freq_dict[word] = freq_dict.get(word, 0) + 1
        return freq_dict

    return reduce(update_freq, words, {})

text = "hello world hello python world python python"
freq = word_frequency(text)
print(f"Text: {text}")
print(f"Word frequency: {freq}")

# Reduce with initial value
numbers = [1, 2, 3, 4]
# Without initial value
sum1 = reduce(lambda x, y: x + y, numbers)
# With initial value
sum2 = reduce(lambda x, y: x + y, numbers, 10)

print(f"Numbers: {numbers}")
print(f"Sum without initial: {sum1}")
print(f"Sum with initial 10: {sum2}")
```

### Combined Usage

```python
# Using map, filter, and reduce together
numbers = list(range(1, 11))

# Process: filter even numbers -> square them -> sum them
result = reduce(
    lambda x, y: x + y,
    map(
        lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)

print(f"Numbers 1-10: {numbers}")
print(f"Sum of squares of even numbers: {result}")

# Step by step explanation:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

squared_evens = list(map(lambda x: x ** 2, even_numbers))
print(f"Squared even numbers: {squared_evens}")

total_sum = reduce(lambda x, y: x + y, squared_evens)
print(f"Total sum: {total_sum}")

# Practical example: Data processing pipeline
def process_student_grades(students):
    """Process student grades: filter passing, adjust scores, calculate average"""

    # Filter students with passing grades (>= 60)
    passing_students = filter(lambda s: s['grade'] >= 60, students)

    # Adjust grades (add 5 bonus points, max 100)
    adjusted_grades = map(lambda s: {**s, 'grade': min(s['grade'] + 5, 100)}, passing_students)

    # Calculate average of adjusted grades
    grades_list = list(adjusted_grades)
    if grades_list:
        total = reduce(lambda acc, s: acc + s['grade'], grades_list, 0)
        average = total / len(grades_list)
        return average, grades_list
    else:
        return 0, []

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 45},
    {'name': 'Charlie', 'grade': 92},
    {'name': 'Diana', 'grade': 58},
    {'name': 'Eve', 'grade': 78}
]

avg_grade, processed_students = process_student_grades(students)
print(f"Original students: {students}")
print(f"Processed students (passing with bonus): {processed_students}")
print(f"Average adjusted grade: {avg_grade:.2f}")
```

## Module 5: List Comprehension

### Basic List Comprehension

```python
# Basic syntax: [expression for item in iterable]

# Traditional approach
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)

# List comprehension approach
squares_comp = [num ** 2 for num in numbers]

print(f"Numbers: {numbers}")
print(f"Squares (traditional): {squares}")
print(f"Squares (comprehension): {squares_comp}")

# More examples
# Create list of even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers 1-10: {evens}")

# Convert strings to uppercase
fruits = ["apple", "banana", "cherry"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(f"Fruits: {fruits}")
print(f"Uppercase fruits: {uppercase_fruits}")

# Extract first characters
words = ["hello", "world", "python"]
first_chars = [word[0] for word in words]
print(f"Words: {words}")
print(f"First characters: {first_chars}")
```

### List Comprehension with Conditions

```python
# Conditional list comprehension
numbers = list(range(1, 11))

# Only even numbers
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Numbers greater than 5
large_numbers = [x for x in numbers if x > 5]
print(f"Numbers > 5: {large_numbers}")

# Even numbers squared, odd numbers as is
processed = [x**2 if x % 2 == 0 else x for x in numbers]
print(f"Processed numbers: {processed}")

# Multiple conditions
special_numbers = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print(f"Numbers divisible by 2 and 3: {special_numbers}")

# Practical example: Data filtering
students = [
    {"name": "Alice", "grade": 85, "attendance": 90},
    {"name": "Bob", "grade": 45, "attendance": 70},
    {"name": "Charlie", "grade": 92, "attendance": 95},
    {"name": "Diana", "grade": 78, "attendance": 85}
]

# Students with grade >= 70 and attendance >= 80
good_students = [student for student in students
                if student["grade"] >= 70 and student["attendance"] >= 80]
print("Good students:")
for student in good_students:
    print(f"  {student['name']}: Grade {student['grade']}, Attendance {student['attendance']}%")
```

### Nested List Comprehension

```python
# Basic nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten the matrix
flattened = [num for row in matrix for num in row]
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")

# Create multiplication table
multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("Multiplication table 1-5:")
for row in multiplication_table:
    print(row)

# Transpose a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"Original matrix: {matrix}")
print(f"Transposed matrix: {transposed}")

# Practical example: Cartesian product
colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]

# Create all combinations of colors and sizes
products = [(color, size) for color in colors for size in sizes]
print("Color-Size combinations:")
for product in products:
    print(f"  {product[0]} {product[1]}")
```

### Advanced List Comprehension

```python
# Using functions in comprehensions
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate prime numbers
primes = [x for x in range(2, 50) if is_prime(x)]
print(f"Prime numbers under 50: {primes}")

# Nested data processing
data = [
    {"name": "Alice", "scores": [85, 92, 78]},
    {"name": "Bob", "scores": [65, 70, 80]},
    {"name": "Charlie", "scores": [95, 88, 92]}
]

# Get all scores above 80
high_scores = [score for student in data for score in student["scores"] if score > 80]
print(f"All scores above 80: {high_scores}")

# Get students with any score above 90
top_students = [student["name"] for student in data if any(score > 90 for score in student["scores"])]
print(f"Students with scores above 90: {top_students}")

# Dictionary-like operations with list comprehension
text = "hello world this is a test hello world"
words = text.split()

# Word frequency using list comprehension and count
unique_words = list(set(words))
word_freq = [(word, words.count(word)) for word in unique_words]
print(f"Word frequency: {word_freq}")

# Conditional value transformation
numbers = [10, -5, 20, -8, 30, -12]
processed = [x if x > 0 else 0 for x in numbers]
print(f"Original: {numbers}")
print(f"Processed (negative -> 0): {processed}")
```

## Module 6: A Brief Introduction to Data Structures

### What are Data Structures?

Data structures are ways of organizing and storing data so that they can be accessed and modified efficiently.

### Common Python Data Structures

```python
# 1. Lists - Ordered, mutable collections
fruits_list = ["apple", "banana", "cherry"]
print(f"List: {fruits_list}")

# 2. Tuples - Ordered, immutable collections
colors_tuple = ("red", "green", "blue")
print(f"Tuple: {colors_tuple}")

# 3. Sets - Unordered collections of unique elements
unique_numbers = {1, 2, 3, 2, 1}  # Duplicates removed
print(f"Set: {unique_numbers}")

# 4. Dictionaries - Key-value pairs
person_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(f"Dictionary: {person_dict}")

# 5. Strings - Immutable sequences of characters
message = "Hello, Python!"
print(f"String: {message}")
```

### Choosing the Right Data Structure

```python
# When to use each data structure:

# List: When you need an ordered collection that can change
shopping_list = ["milk", "eggs", "bread"]
shopping_list.append("butter")  # Easy to modify

# Tuple: When you need an ordered collection that shouldn't change
coordinates = (40.7128, -74.0060)  # Latitude, longitude - fixed values

# Set: When you need to ensure uniqueness or perform set operations
unique_visitors = {"user1", "user2", "user1"}  # Only stores unique users

# Dictionary: When you need to store key-value pairs for fast lookups
user_profile = {
    "username": "alice123",
    "email": "alice@example.com",
    "age": 25
}

# Practical example: Different structures for different purposes
class StudentManagement:
    def __init__(self):
        # List for ordered collection of students
        self.students_list = ["Alice", "Bob", "Charlie"]

        # Tuple for fixed course information
        self.course_info = ("Python 101", "Dr. Smith", 3)

        # Set for unique student IDs
        self.student_ids = {1001, 1002, 1003, 1001}  # 1001 appears only once

        # Dictionary for student details
        self.student_details = {
            1001: {"name": "Alice", "grade": "A"},
            1002: {"name": "Bob", "grade": "B"},
            1003: {"name": "Charlie", "grade": "A-"}
        }

    def display_info(self):
        print(f"Students (list): {self.students_list}")
        print(f"Course info (tuple): {self.course_info}")
        print(f"Student IDs (set): {self.student_ids}")
        print(f"Student details (dict): {self.student_details}")

# Usage
manager = StudentManagement()
manager.display_info()
```

## Module 7: List and List Operations

### Creating Lists

```python
# Different ways to create lists
empty_list = []
print(f"Empty list: {empty_list}")

# List with elements
fruits = ["apple", "banana", "cherry"]
print(f"Fruits list: {fruits}")

# Using list constructor
numbers = list(range(1, 6))
print(f"Numbers from range: {numbers}")

# From string
chars = list("hello")
print(f"Characters from string: {chars}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Mixed data types
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
print(f"Mixed list: {mixed_list}")
```

### List Operations - Access and Modification

```python
# Accessing elements
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(f"First fruit: {fruits[0]}")        # apple
print(f"Last fruit: {fruits[-1]}")        # elderberry
print(f"Second fruit: {fruits[1]}")       # banana
print(f"Slice 1-3: {fruits[1:4]}")       # ['banana', 'cherry', 'date']

# Modifying elements
fruits[1] = "blueberry"
print(f"After modification: {fruits}")

# Adding elements
fruits.append("fig")                      # Add to end
print(f"After append: {fruits}")

fruits.insert(2, "cantaloupe")            # Insert at specific position
print(f"After insert: {fruits}")

fruits.extend(["grape", "honeydew"])      # Add multiple elements
print(f"After extend: {fruits}")

# Removing elements
removed = fruits.pop()                    # Remove and return last element
print(f"Removed: {removed}, List: {fruits}")

removed = fruits.pop(2)                   # Remove at specific index
print(f"Removed index 2: {removed}, List: {fruits}")

fruits.remove("date")                     # Remove first occurrence of value
print(f"After remove 'date': {fruits}")

del fruits[0]                            # Delete by index
print(f"After del fruits[0]: {fruits}")

# Clear list
fruits.clear()
print(f"After clear: {fruits}")
```

### List Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
print(f"Original: {numbers}")
print(f"numbers[2:6]: {numbers[2:6]}")      # [2, 3, 4, 5]
print(f"numbers[:4]: {numbers[:4]}")        # [0, 1, 2, 3]
print(f"numbers[5:]: {numbers[5:]}")        # [5, 6, 7, 8, 9]
print(f"numbers[-3:]: {numbers[-3:]}")      # [7, 8, 9]

# Step slicing
print(f"numbers[::2]: {numbers[::2]}")      # [0, 2, 4, 6, 8] - every 2nd
print(f"numbers[1::2]: {numbers[1::2]}")    # [1, 3, 5, 7, 9] - every 2nd from index 1
print(f"numbers[::-1]: {numbers[::-1]}")    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - reverse

# Modifying with slices
numbers[2:5] = [20, 30, 40]                # Replace slice
print(f"After slice replacement: {numbers}")

numbers[1:1] = [15, 25]                    # Insert without replacing
print(f"After slice insertion: {numbers}")

del numbers[3:6]                           # Delete slice
print(f"After slice deletion: {numbers}")
```

### List of Lists (2D Lists)

```python
# Creating 2D lists (matrices)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("2D List (Matrix):")
for row in matrix:
    print(row)

# Accessing elements
print(f"Element at [1][2]: {matrix[1][2]}")  # 6
print(f"First row: {matrix[0]}")             # [1, 2, 3]
print(f"Second column: {[row[1] for row in matrix]}")  # [2, 5, 8]

# Modifying 2D lists
matrix[0][0] = 10
matrix[1].append(7)  # Add to second row
print("\nModified Matrix:")
for row in matrix:
    print(row)

# Creating a 2D list with list comprehension
rows, cols = 3, 4
matrix_comp = [[i * j for j in range(cols)] for i in range(rows)]
print("\nMatrix from comprehension:")
for row in matrix_comp:
    print(row)

# Practical example: Tic-Tac-Toe board
def create_tic_tac_toe():
    """Create and display a tic-tac-toe board"""
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # Make some moves
    board[0][0] = 'X'
    board[1][1] = 'O'
    board[2][2] = 'X'

    print("\nTic-Tac-Toe Board:")
    for i, row in enumerate(board):
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("-----------")

create_tic_tac_toe()
```

### List Methods and Operations

```python
fruits = ["apple", "banana", "cherry", "apple", "date"]

# Common list methods
print(f"Original list: {fruits}")

# Count occurrences
apple_count = fruits.count("apple")
print(f"Count of 'apple': {apple_count}")

# Find index
banana_index = fruits.index("banana")
print(f"Index of 'banana': {banana_index}")

# Copy list
fruits_copy = fruits.copy()
print(f"Copy: {fruits_copy}")

# Reverse list
fruits.reverse()
print(f"Reversed: {fruits}")

# Sort list
fruits.sort()
print(f"Sorted: {fruits}")

fruits.sort(reverse=True)
print(f"Sorted descending: {fruits}")

# Custom sort
words = ["apple", "Banana", "cherry", "Date"]
words.sort()  # Case-sensitive sort
print(f"Case-sensitive sort: {words}")

words.sort(key=str.lower)  # Case-insensitive sort
print(f"Case-insensitive sort: {words}")

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"Concatenated: {combined}")

# Repetition
repeated = list1 * 3
print(f"Repeated: {repeated}")

# Membership testing
print(f"2 in list1: {2 in list1}")        # True
print(f"7 in list1: {7 in list1}")        # False

# Length
print(f"Length of list1: {len(list1)}")   # 3
```

## Module 8: Dictionary and Common Dictionary Operations

### Creating Dictionaries

```python
# Different ways to create dictionaries
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Dictionary with key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"Person dictionary: {person}")

# Using dict constructor
person2 = dict(name="Bob", age=30, city="Boston")
print(f"Person2 dictionary: {person2}")

# From list of tuples
pairs = [("name", "Charlie"), ("age", 35), ("city", "Chicago")]
person3 = dict(pairs)
print(f"Person3 dictionary: {person3}")

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares}")

# Mixed key types (though usually keys are strings or numbers)
mixed_keys = {
    "string_key": "value1",
    123: "value2",
    (1, 2): "value3"  # Tuple as key (must be immutable)
}
print(f"Mixed keys dictionary: {mixed_keys}")
```

### Dictionary Operations - Access and Modification

```python
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "grades": [85, 92, 78]
}

# Accessing values
print(f"Student name: {student['name']}")
print(f"Student age: {student['age']}")

# Using get() method (safer - returns None if key doesn't exist)
print(f"Student GPA: {student.get('gpa')}")  # None
print(f"Student GPA with default: {student.get('gpa', 'Not available')}")

# Adding/Modifying elements
student["gpa"] = 3.8  # Add new key
student["age"] = 21   # Modify existing key
print(f"After modifications: {student}")

# Update multiple values
student.update({"age": 22, "year": "Junior"})
print(f"After update: {student}")

# Removing elements
removed_grade = student.pop("grades")  # Remove and return value
print(f"Removed grades: {removed_grade}")
print(f"After pop: {student}")

removed_item = student.popitem()  # Remove and return last inserted item
print(f"Removed item: {removed_item}")
print(f"After popitem: {student}")

del student["major"]  # Delete specific key
print(f"After del: {student}")

# student.clear()  # Clear all elements
```

### Dictionary Methods

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "occupation": "Engineer"
}

# Getting keys, values, and items
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Iterating through dictionary
print("\nIterating through dictionary:")
for key in person:
    print(f"  {key}: {person[key]}")

print("\nIterating through items:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Checking for keys
print(f"'name' in person: {'name' in person}")      # True
print(f"'salary' in person: {'salary' in person}")  # False

# Copying dictionaries
person_copy = person.copy()
print(f"Original: {person}")
print(f"Copy: {person_copy}")

# Setdefault - get value or set default if key doesn't exist
age = person.setdefault("age", 30)      # Key exists, returns current value
salary = person.setdefault("salary", 50000)  # Key doesn't exist, sets default
print(f"Age: {age}, Salary: {salary}")
print(f"After setdefault: {person}")
```

### Advanced Dictionary Operations

```python
# Dictionary comprehension with conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}  # Note: 'b' appears in both

# Method 1: update() - modifies dict1
dict1.update(dict2)
print(f"After update: {dict1}")

# Method 2: unpacking (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}  # Later values overwrite earlier ones
print(f"Merged: {merged}")

# Method 3: collections.ChainMap
from collections import ChainMap
chain = ChainMap(dict1, dict2)
print(f"ChainMap: {dict(chain)}")

# Nested dictionaries
company = {
    "employee1": {
        "name": "Alice",
        "position": "Developer",
        "skills": ["Python", "JavaScript", "SQL"]
    },
    "employee2": {
        "name": "Bob",
        "position": "Designer",
        "skills": ["Photoshop", "Illustrator", "Figma"]
    }
}

print("\nCompany employees:")
for emp_id, emp_info in company.items():
    print(f"  {emp_id}:")
    print(f"    Name: {emp_info['name']}")
    print(f"    Position: {emp_info['position']}")
    print(f"    Skills: {', '.join(emp_info['skills'])}")

# Accessing nested values
print(f"Employee1 skills: {company['employee1']['skills']}")
print(f"First skill of employee1: {company['employee1']['skills'][0]}")
```

### Practical Dictionary Examples

```python
# Word frequency counter
def word_frequency(text):
    """Count frequency of each word in text"""
    words = text.lower().split()
    frequency = {}

    for word in words:
        # Remove punctuation
        word = word.strip('.,!?;:"')
        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency

text = "Hello world hello Python world Python programming"
freq = word_frequency(text)
print("Word frequency:")
for word, count in freq.items():
    print(f"  {word}: {count}")

# Student grade management system
class GradeBook:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        self.students[name] = []

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].append(grade)
        else:
            print(f"Student {name} not found!")

    def get_average(self, name):
        if name in self.students and self.students[name]:
            return sum(self.students[name]) / len(self.students[name])
        return 0

    def display_grades(self):
        print("\nGrade Book:")
        for name, grades in self.students.items():
            avg = self.get_average(name)
            print(f"  {name}: Grades {grades}, Average: {avg:.2f}")

# Usage
grade_book = GradeBook()
grade_book.add_student("Alice")
grade_book.add_student("Bob")

grade_book.add_grade("Alice", 85)
grade_book.add_grade("Alice", 92)
grade_book.add_grade("Alice", 78)
grade_book.add_grade("Bob", 88)
grade_book.add_grade("Bob", 91)

grade_book.display_grades()
```

## Module 9: Tuples and Sets

### Tuples - Immutable Sequences

```python
# Creating tuples
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Single element tuple (note the comma)
single_tuple = (1,)
print(f"Single element tuple: {single_tuple}")

# Multiple elements
colors = ("red", "green", "blue")
print(f"Colors tuple: {colors}")

# Without parentheses (tuple packing)
numbers = 1, 2, 3, 4, 5
print(f"Numbers tuple: {numbers}")

# Using tuple constructor
tuple_from_list = tuple([1, 2, 3])
print(f"Tuple from list: {tuple_from_list}")

# Tuple unpacking
a, b, c = colors
print(f"Unpacked: a={a}, b={b}, c={c}")

# Extended unpacking (Python 3+)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")
```

### Tuple Operations and Methods

```python
# Basic tuple operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"Combined: {combined}")

# Repetition
repeated = tuple1 * 3
print(f"Repeated: {repeated}")

# Membership
print(f"2 in tuple1: {2 in tuple1}")      # True
print(f"7 in tuple1: {7 in tuple1}")      # False

# Indexing and slicing
print(f"First element: {tuple1[0]}")      # 1
print(f"Last element: {tuple1[-1]}")      # 3
print(f"Slice: {tuple1[1:3]}")           # (2, 3)

# Tuple methods
fruits = ("apple", "banana", "cherry", "apple")

# Count occurrences
apple_count = fruits.count("apple")
print(f"Count of 'apple': {apple_count}")

# Find index
banana_index = fruits.index("banana")
print(f"Index of 'banana': {banana_index}")

# Length
print(f"Length: {len(fruits)}")           # 4

# Why use tuples?
# 1. Immutable - data integrity
coordinates = (40.7128, -74.0060)  # Latitude, longitude shouldn't change

# 2. Faster than lists
import time

list_test = [1, 2, 3, 4, 5]
tuple_test = (1, 2, 3, 4, 5)

# 3. Can be used as dictionary keys (because they're immutable)
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}
print(f"Location at NY coordinates: {locations[(40.7128, -74.0060)]}")
```

### Sets - Unordered Unique Collections

```python
# Creating sets
empty_set = set()
print(f"Empty set: {empty_set}")

# Set with elements
fruits = {"apple", "banana", "cherry"}
print(f"Fruits set: {fruits}")

# From list (removes duplicates)
numbers = set([1, 2, 2, 3, 3, 3, 4, 5])
print(f"Numbers set (duplicates removed): {numbers}")

# Set comprehension
squares = {x**2 for x in range(1, 6)}
print(f"Squares set: {squares}")

# Mixed data types
mixed_set = {1, "hello", 3.14, (1, 2)}  # Can contain immutable types
print(f"Mixed set: {mixed_set}")

# Note: Sets cannot contain mutable types like lists
# invalid_set = {1, [2, 3]}  # This would raise TypeError
```

### Set Operations and Methods

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set1: {set1}")
print(f"Set2: {set2}")

# Basic set operations
print(f"Union: {set1 | set2}")                    # {1, 2, 3, 4, 5, 6, 7, 8}
print(f"Intersection: {set1 & set2}")             # {4, 5}
print(f"Difference: {set1 - set2}")               # {1, 2, 3}
print(f"Symmetric Difference: {set1 ^ set2}")     # {1, 2, 3, 6, 7, 8}

# Set methods
set1.add(6)
print(f"After add(6): {set1}")

set1.remove(1)  # Raises KeyError if element not found
print(f"After remove(1): {set1}")

set1.discard(10)  # No error if element not found
print(f"After discard(10): {set1}")

popped = set1.pop()  # Remove and return arbitrary element
print(f"Popped: {popped}, Set1: {set1}")

set1.clear()
print(f"After clear: {set1}")

# Set comparisons
setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}
setC = {1, 2, 3}

print(f"setA == setC: {setA == setC}")            # True
print(f"setA is subset of setB: {setA.issubset(setB)}")    # True
print(f"setB is superset of setA: {setB.issuperset(setA)}") # True
print(f"setA is disjoint with {6,7}: {setA.isdisjoint({6, 7})}") # True
```

### Practical Tuple and Set Examples

```python
# Tuple example: Returning multiple values from function
def get_student_info(student_id):
    """Return student name, grade, and status"""
    # Simulate database lookup
    student_data = {
        101: ("Alice", 85, "Pass"),
        102: ("Bob", 92, "Pass"),
        103: ("Charlie", 58, "Fail")
    }
    return student_data.get(student_id, ("Unknown", 0, "Unknown"))

# Using tuple unpacking with function return
name, grade, status = get_student_info(101)
print(f"Student: {name}, Grade: {grade}, Status: {status}")

# Set example: Finding common interests
def find_common_interests(person1_interests, person2_interests):
    """Find common interests between two people"""
    set1 = set(person1_interests)
    set2 = set(person2_interests)

    common = set1 & set2
    only_person1 = set1 - set2
    only_person2 = set2 - set1
    all_interests = set1 | set2

    return {
        "common": common,
        "only_person1": only_person1,
        "only_person2": only_person2,
        "all": all_interests
    }

alice_interests = ["reading", "hiking", "cooking", "movies"]
bob_interests = ["hiking", "gaming", "music", "cooking"]

result = find_common_interests(alice_interests, bob_interests)
print("\nInterest Analysis:")
print(f"Common interests: {result['common']}")
print(f"Only Alice's interests: {result['only_person1']}")
print(f"Only Bob's interests: {result['only_person2']}")
print(f"All interests: {result['all']}")

# Practical set usage: Removing duplicates
def remove_duplicates(data):
    """Remove duplicates while preserving some order"""
    seen = set()
    unique_data = []

    for item in data:
        if item not in seen:
            seen.add(item)
            unique_data.append(item)

    return unique_data

duplicate_numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 2, 6]
unique_numbers = remove_duplicates(duplicate_numbers)
print(f"\nOriginal: {duplicate_numbers}")
print(f"Unique: {unique_numbers}")
```

## Module 10: Zip() Method and Zipping Collections

### Understanding Zip Function

```python
# Basic zip usage
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "Boston", "Chicago"]

# Zip creates an iterator of tuples
zipped = zip(names, ages, cities)
print(f"Zipped object: {zipped}")

# Convert to list to see the tuples
zipped_list = list(zipped)
print(f"Zipped list: {zipped_list}")

# Iterating through zipped data
print("\nIterating through zipped data:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name} is {age} years old and lives in {city}")

# Zipping different length iterables
short_list = [1, 2, 3]
long_list = ['a', 'b', 'c', 'd', 'e']

# Zip stops at shortest iterable
result = list(zip(short_list, long_list))
print(f"\nZipping different lengths: {result}")

# Using zip with range
students = ["Alice", "Bob", "Charlie"]
for i, student in zip(range(1, len(students) + 1), students):
    print(f"  {i}. {student}")
```

### Practical Zip Applications

```python
# Creating dictionaries from two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

person_dict = dict(zip(keys, values))
print(f"Dictionary from zip: {person_dict}")

# Multiple students example
student_names = ["Alice", "Bob", "Charlie"]
student_grades = [85, 92, 78]
student_ids = [101, 102, 103]

# Create list of student dictionaries
students = []
for name, grade, id_num in zip(student_names, student_grades, student_ids):
    students.append({
        "id": id_num,
        "name": name,
        "grade": grade
    })

print("\nStudent records:")
for student in students:
    print(f"  ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}")

# Matrix operations with zip
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose matrix using zip
transposed = list(zip(*matrix))
print(f"\nOriginal matrix: {matrix}")
print(f"Transposed matrix: {transposed}")

# Calculating element-wise sums
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

sum_matrix = []
for row1, row2 in zip(matrix1, matrix2):
    sum_row = [a + b for a, b in zip(row1, row2)]
    sum_matrix.append(sum_row)

print(f"Matrix1: {matrix1}")
print(f"Matrix2: {matrix2}")
print(f"Sum: {sum_matrix}")
```

### Advanced Zip Techniques

```python
# Unzipping with zip(*)
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
names, ages = zip(*data)
print(f"Data: {data}")
print(f"Names: {names}")
print(f"Ages: {ages}")

# Using zip with enumerate for indexed iteration
fruits = ["apple", "banana", "cherry"]
prices = [1.20, 0.80, 2.50]

print("\nFruit prices with index:")
for i, (fruit, price) in enumerate(zip(fruits, prices)):
    print(f"  {i+1}. {fruit}: ${price:.2f}")

# Zipping with dictionary items
person1 = {"name": "Alice", "age": 25, "city": "NYC"}
person2 = {"name": "Bob", "age": 30, "city": "Boston"}

print("\nComparing people:")
for (k1, v1), (k2, v2) in zip(person1.items(), person2.items()):
    print(f"  {k1}: {v1} vs {k2}: {v2}")

# Custom zipping with different aggregation
def smart_zip(*iterables, aggregator=None):
    """Zip with custom aggregation function"""
    if aggregator is None:
        return zip(*iterables)

    result = []
    for values in zip(*iterables):
        result.append(aggregator(values))
    return result

# Example: zipping with sum aggregation
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]

sums = smart_zip(numbers1, numbers2, numbers3, aggregator=sum)
print(f"\nNumbers: {numbers1}, {numbers2}, {numbers3}")
print(f"Element-wise sums: {list(sums)}")

# Zipping with filter
def zip_with_filter(*iterables, condition=None):
    """Zip and filter based on condition"""
    if condition is None:
        return zip(*iterables)

    filtered = []
    for values in zip(*iterables):
        if condition(values):
            filtered.append(values)
    return filtered

# Example: Keep only tuples where sum > 10
data1 = [1, 2, 3, 4, 5]
data2 = [5, 6, 7, 8, 9]

filtered_pairs = zip_with_filter(data1, data2, condition=lambda x: sum(x) > 10)
print(f"\nData1: {data1}")
print(f"Data2: {data2}")
print(f"Pairs with sum > 10: {list(filtered_pairs)}")
```

### Real-World Zip Examples

```python
# Data processing pipeline
def process_sales_data(products, quantities, prices):
    """Process sales data and calculate totals"""
    sales_data = []
    total_revenue = 0

    for product, qty, price in zip(products, quantities, prices):
        revenue = qty * price
        total_revenue += revenue
        sales_data.append({
            'product': product,
            'quantity': qty,
            'price': price,
            'revenue': revenue
        })

    return sales_data, total_revenue

# Sample data
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
quantities = [10, 25, 15, 8]
prices = [999.99, 29.99, 79.99, 299.99]

sales, total = process_sales_data(products, quantities, prices)

print("Sales Report:")
for item in sales:
    print(f"  {item['product']}: {item['quantity']} units × ${item['price']} = ${item['revenue']:.2f}")
print(f"Total Revenue: ${total:.2f}")

# Student grade calculator
def calculate_student_grades(students, assignments, exams):
    """Calculate final grades based on assignments and exams"""
    final_grades = []

    for student, assignment_scores, exam_scores in zip(students, assignments, exams):
        # Weighted average: 40% assignments, 60% exams
        assignment_avg = sum(assignment_scores) / len(assignment_scores)
        exam_avg = sum(exam_scores) / len(exam_scores)
        final_grade = 0.4 * assignment_avg + 0.6 * exam_avg

        # Determine letter grade
        if final_grade >= 90:
            letter_grade = "A"
        elif final_grade >= 80:
            letter_grade = "B"
        elif final_grade >= 70:
            letter_grade = "C"
        elif final_grade >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"

        final_grades.append({
            'student': student,
            'final_grade': round(final_grade, 2),
            'letter_grade': letter_grade
        })

    return final_grades

# Sample data
students = ["Alice", "Bob", "Charlie"]
assignments = [[85, 90, 88], [78, 82, 80], [92, 95, 90]]
exams = [[88, 85], [75, 78], [96, 98]]

grades = calculate_student_grades(students, assignments, exams)

print("\nFinal Grades:")
for grade_info in grades:
    print(f"  {grade_info['student']}: {grade_info['final_grade']} ({grade_info['letter_grade']})")

# Creating parallel collections
def create_parallel_data_structures(names, ages, scores):
    """Create parallel lists and dictionaries from zipped data"""
    # List of tuples
    tuple_list = list(zip(names, ages, scores))

    # List of dictionaries
    dict_list = [{'name': n, 'age': a, 'score': s} for n, a, s in zip(names, ages, scores)]

    # Dictionary with names as keys
    name_dict = {name: {'age': age, 'score': score} for name, age, score in zip(names, ages, scores)}

    return tuple_list, dict_list, name_dict

# Test data
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
scores = [85, 92, 78]

tuples, dicts, named_dict = create_parallel_data_structures(names, ages, scores)

print(f"\nTuple list: {tuples}")
print(f"Dictionary list: {dicts}")
print(f"Named dictionary: {named_dict}")
```

This comprehensive guide covers all fundamental data structures and looping constructs in Python, providing detailed explanations and practical examples for each concept. The material progresses from basic conditional statements to advanced data structure operations, ensuring a solid foundation in Python programming.
