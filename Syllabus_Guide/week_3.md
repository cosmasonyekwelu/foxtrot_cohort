# Python Functions & Methods - Comprehensive Guide

## Module 1: Function Declaration and Calling

### What are Functions?
Functions are reusable blocks of code that perform a specific task. They help in organizing code, reducing repetition, and making programs more modular and maintainable.

### Basic Function Syntax

```python
def function_name(parameters):
    """docstring - describes what the function does"""
    # function body
    # statements
    return value  # optional
```

### Simple Function Examples

```python
# Example 1: Basic function without parameters
def greet():
    """This function displays a greeting message"""
    print("Hello, welcome to Python programming!")

# Calling the function
greet()  # Output: Hello, welcome to Python programming!

# Example 2: Function with parameters
def greet_person(name):
    """Greet a specific person"""
    print(f"Hello {name}, welcome to Python programming!")

# Calling with argument
greet_person("Alice")  # Output: Hello Alice, welcome to Python programming!
greet_person("Bob")    # Output: Hello Bob, welcome to Python programming!

# Example 3: Function with multiple parameters
def introduce(name, age, city):
    """Introduce a person with their details"""
    print(f"Hi, I'm {name}, {age} years old from {city}")

# Calling with multiple arguments
introduce("Charlie", 25, "New York")
# Output: Hi, I'm Charlie, 25 years old from New York

# Example 4: Function with return value
def calculate_area(length, width):
    """Calculate area of a rectangle"""
    area = length * width
    return area

# Using return value
room_area = calculate_area(10, 5)
print(f"The area is: {room_area} square units")  # Output: The area is: 50 square units

# Example 5: Function call in expressions
def square(number):
    """Return the square of a number"""
    return number ** 2

# Using function in expressions
result = square(5) + square(3)
print(f"5² + 3² = {result}")  # Output: 5² + 3² = 34
```

### Function Documentation and Best Practices

```python
def calculate_compound_interest(principal, rate, time, compounds_per_year=1):
    """
    Calculate compound interest.
    
    Parameters:
    principal (float): Initial investment amount
    rate (float): Annual interest rate (as decimal, e.g., 0.05 for 5%)
    time (float): Time in years
    compounds_per_year (int): Number of times interest compounds per year
    
    Returns:
    float: Total amount after compound interest
    """
    amount = principal * (1 + rate/compounds_per_year) ** (compounds_per_year * time)
    return amount

# Using the well-documented function
investment = 1000
interest_rate = 0.05  # 5%
years = 3

final_amount = calculate_compound_interest(investment, interest_rate, years)
print(f"${investment} invested at {interest_rate*100}% for {years} years grows to ${final_amount:.2f}")

# Accessing function documentation
print(calculate_compound_interest.__doc__)
```

## Module 2: Return Statement

### Understanding the Return Statement
The `return` statement is used to exit a function and optionally pass back an expression to the caller. If no return statement is specified, the function returns `None`.

### Return Statement Examples

```python
# Example 1: Function without return statement
def say_hello(name):
    print(f"Hello, {name}!")

result = say_hello("Alice")
print(f"Return value: {result}")  # Output: Return value: None

# Example 2: Function with simple return
def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")  # Output: 5 + 3 = 8

# Example 3: Function with multiple return points
def check_number(number):
    """Check if number is positive, negative, or zero"""
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(10))   # Output: Positive
print(check_number(-5))   # Output: Negative
print(check_number(0))    # Output: Zero

# Example 4: Returning multiple values (as tuple)
def calculate_statistics(numbers):
    """Calculate mean and standard deviation"""
    if not numbers:
        return 0, 0  # Return zeros for empty list
    
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = variance ** 0.5
    
    return mean, std_dev  # Returns a tuple

# Unpacking returned values
data = [1, 2, 3, 4, 5]
average, deviation = calculate_statistics(data)
print(f"Average: {average:.2f}, Standard Deviation: {deviation:.2f}")

# Example 5: Early return
def process_user_input(user_input):
    """Process user input with validation"""
    if not user_input:
        return "Error: Empty input"  # Early return
    
    if not user_input.isdigit():
        return "Error: Input must be a number"  # Early return
    
    number = int(user_input)
    if number < 0:
        return "Error: Number must be positive"  # Early return
    
    # If all validations pass
    return f"Success: Processed number {number}"

print(process_user_input(""))        # Output: Error: Empty input
print(process_user_input("abc"))     # Output: Error: Input must be a number
print(process_user_input("-5"))      # Output: Error: Number must be positive
print(process_user_input("42"))      # Output: Success: Processed number 42

# Example 6: Returning complex data structures
def create_student_record(name, age, grades):
    """Create a student record dictionary"""
    return {
        'name': name,
        'age': age,
        'grades': grades,
        'average': sum(grades) / len(grades) if grades else 0,
        'status': 'Pass' if (sum(grades) / len(grades) if grades else 0) >= 60 else 'Fail'
    }

student = create_student_record("John Doe", 20, [85, 92, 78, 90])
print(student)
```

### Return vs Print

```python
def calculate_with_print(a, b):
    """This function prints but doesn't return"""
    result = a + b
    print(f"The sum is: {result}")

def calculate_with_return(a, b):
    """This function returns but doesn't print"""
    result = a + b
    return result

# Using print function
calculate_with_print(5, 3)  # Output: The sum is: 8
print_result = calculate_with_print(5, 3)  # Still prints, but print_result is None

# Using return function
return_result = calculate_with_return(5, 3)  # No output, but stores result
print(f"Returned result: {return_result}")  # Output: Returned result: 8

# The key difference: return gives back a value that can be used elsewhere
total = calculate_with_return(10, 20) + calculate_with_return(5, 5)
print(f"Total: {total}")  # Output: Total: 40
```

## Module 3: Function Arguments

### Types of Function Arguments

#### 1. Positional Arguments
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"I have a {animal_type} named {pet_name}.")

# Positional arguments - order matters
describe_pet("dog", "Rex")      # Output: I have a dog named Rex.
describe_pet("cat", "Whiskers") # Output: I have a cat named Whiskers.

# Wrong order produces unexpected results
describe_pet("Rex", "dog")      # Output: I have a Rex named dog.
```

#### 2. Keyword Arguments
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"I have a {animal_type} named {pet_name}.")

# Keyword arguments - order doesn't matter
describe_pet(animal_type="hamster", pet_name="Harry")
describe_pet(pet_name="Harry", animal_type="hamster")

# Mixing positional and keyword arguments (positional first)
describe_pet("bird", pet_name="Polly")
```

#### 3. Default Parameters
```python
def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet with default type"""
    print(f"I have a {animal_type} named {pet_name}.")

# Using default parameter
describe_pet("Rex")             # Output: I have a dog named Rex.
describe_pet("Whiskers", "cat") # Output: I have a cat named Whiskers.

# Example with multiple default parameters
def create_user_profile(username, age=None, city="Unknown", is_active=True):
    """Create user profile with default values"""
    profile = {
        'username': username,
        'age': age,
        'city': city,
        'is_active': is_active
    }
    return profile

# Using different combinations
user1 = create_user_profile("alice")
user2 = create_user_profile("bob", age=25)
user3 = create_user_profile("charlie", city="New York", is_active=False)

print(user1)  # Output: {'username': 'alice', 'age': None, 'city': 'Unknown', 'is_active': True}
print(user2)  # Output: {'username': 'bob', 'age': 25, 'city': 'Unknown', 'is_active': True}
print(user3)  # Output: {'username': 'charlie', 'age': None, 'city': 'New York', 'is_active': False}
```

#### 4. Variable-length Arguments

```python
# *args for variable positional arguments
def print_scores(student_name, *scores):
    """Print student name and all their scores"""
    print(f"Student: {student_name}")
    print("Scores:", scores)
    if scores:
        average = sum(scores) / len(scores)
        print(f"Average: {average:.2f}")

print_scores("Alice", 85, 92, 78)
print_scores("Bob", 90, 88)
print_scores("Charlie")  # No scores provided

# **kwargs for variable keyword arguments
def build_car_profile(make, model, **car_info):
    """Build a car profile dictionary"""
    profile = {
        'make': make,
        'model': model'
    }
    # Add all additional keyword arguments
    for key, value in car_info.items():
        profile[key] = value
    return profile

car1 = build_car_profile("Toyota", "Camry", year=2022, color="blue", fuel_efficient=True)
car2 = build_car_profile("Ford", "Mustang", year=2023, color="red", convertible=True, horsepower=450)

print(car1)
print(car2)
```

### Advanced Argument Examples

```python
def complex_calculation(a, b, c=1, d=2, *args, **kwargs):
    """
    Demonstrate all types of function arguments
    
    Parameters:
    a, b: required positional
    c, d: optional with defaults
    *args: variable positional
    **kwargs: variable keyword
    """
    result = a + b + c + d
    
    # Add all args
    for arg in args:
        result += arg
    
    # Process kwargs
    print("Additional parameters:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")
        if isinstance(value, (int, float)):
            result += value
    
    return result

# Using all argument types
total = complex_calculation(
    10, 20,           # a, b (required)
    c=5,              # c (default overridden)
    # d uses default (2)
    30, 40,           # *args
    bonus=100,        # **kwargs
    multiplier=2,     # **kwargs (not added to result)
    name="test"       # **kwargs (not added to result)
)

print(f"Total: {total}")  # Output: Total: 207 (10+20+5+2+30+40+100)
```

## Module 4: Function Nesting

### Nested Functions (Inner Functions)

```python
# Example 1: Basic nested function
def outer_function(message):
    """Outer function containing an inner function"""
    
    def inner_function():
        """Inner function that uses outer function's variable"""
        print(f"Message from outer: {message}")
    
    # Call the inner function
    inner_function()

outer_function("Hello from outer!")  # Output: Message from outer: Hello from outer!

# Example 2: Returning inner function (closure)
def create_greeter(greeting):
    """Create a greeter function with custom greeting"""
    
    def greet(name):
        """Inner function that remembers the greeting"""
        return f"{greeting}, {name}!"
    
    return greet  # Return the inner function without calling it

# Create specialized greeters
hello_greeter = create_greeter("Hello")
goodbye_greeter = create_greeter("Goodbye")
formal_greeter = create_greeter("Good day")

# Use the specialized greeters
print(hello_greeter("Alice"))     # Output: Hello, Alice!
print(goodbye_greeter("Bob"))     # Output: Goodbye, Bob!
print(formal_greeter("Charlie"))  # Output: Good day, Charlie!

# Example 3: Practical use case - calculator with operations
def calculator():
    """Calculator with nested operation functions"""
    
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
    
    # Return all operations as a dictionary
    return {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

# Using the calculator
calc = calculator()
print(calc['add'](5, 3))        # Output: 8
print(calc['multiply'](4, 7))   # Output: 28
print(calc['divide'](10, 2))    # Output: 5.0

# Example 4: Nested functions for data validation
def process_user_data(username, email, age):
    """Process user data with nested validation functions"""
    
    def validate_username(name):
        if len(name) < 3:
            return False, "Username must be at least 3 characters"
        if not name.isalnum():
            return False, "Username must be alphanumeric"
        return True, "Username is valid"
    
    def validate_email(email_addr):
        if '@' not in email_addr or '.' not in email_addr:
            return False, "Invalid email format"
        return True, "Email is valid"
    
    def validate_age(user_age):
        if not isinstance(user_age, int) or user_age < 0 or user_age > 150:
            return False, "Age must be a positive integer between 0 and 150"
        return True, "Age is valid"
    
    # Perform all validations
    validations = [
        validate_username(username),
        validate_email(email),
        validate_age(age)
    ]
    
    # Check if all validations passed
    errors = [error for is_valid, error in validations if not is_valid]
    
    if errors:
        return False, errors
    else:
        return True, "All data is valid"

# Test the validation
result, message = process_user_data("john123", "john@example.com", 25)
print(f"Success: {result}, Message: {message}")

result, errors = process_user_data("jo", "invalid-email", 200)
print(f"Success: {result}, Errors: {errors}")
```

### Nonlocal Keyword

```python
def counter_factory():
    """Create a counter with nested functions"""
    count = 0
    
    def increment():
        nonlocal count  # Allows modifying the outer variable
        count += 1
        return count
    
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    def get_count():
        return count
    
    def reset():
        nonlocal count
        count = 0
        return count
    
    return {
        'increment': increment,
        'decrement': decrement,
        'get_count': get_count,
        'reset': reset
    }

# Using the counter
counter = counter_factory()
print(counter['increment']())  # Output: 1
print(counter['increment']())  # Output: 2
print(counter['decrement']())  # Output: 1
print(counter['get_count']())  # Output: 1
print(counter['reset']())      # Output: 0
```

## Module 5: Recursion - How & When to Use

### Understanding Recursion
Recursion is a programming technique where a function calls itself to solve a smaller version of the same problem. Every recursive function needs:
1. **Base case**: The condition that stops the recursion
2. **Recursive case**: The part where the function calls itself

### Basic Recursion Examples

```python
# Example 1: Factorial calculation
def factorial(n):
    """
    Calculate factorial using recursion
    n! = n * (n-1) * (n-2) * ... * 1
    0! = 1 (base case)
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(f"5! = {factorial(5)}")   # Output: 5! = 120
print(f"0! = {factorial(0)}")   # Output: 0! = 1

# Visualizing factorial(5):
# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1 (base case)
# Then unwinding: 1 * 2 * 3 * 4 * 5 = 120

# Example 2: Fibonacci sequence
def fibonacci(n):
    """
    Calculate nth Fibonacci number
    Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...
    Each number is sum of two preceding ones
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# Example 3: Sum of digits
def sum_digits(n):
    """
    Calculate sum of digits of a number using recursion
    """
    # Base case: single digit
    if n < 10:
        return n
    # Recursive case: last digit + sum of remaining digits
    else:
        return n % 10 + sum_digits(n // 10)

print(f"Sum of digits in 12345: {sum_digits(12345)}")  # Output: 15

# Example 4: Power calculation
def power(base, exponent):
    """
    Calculate base raised to exponent using recursion
    """
    # Base cases
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    # Recursive case for positive exponent
    elif exponent > 0:
        return base * power(base, exponent - 1)
    # Recursive case for negative exponent
    else:
        return 1 / power(base, -exponent)

print(f"2^5 = {power(2, 5)}")    # Output: 32
print(f"2^-3 = {power(2, -3)}")  # Output: 0.125
```

### Practical Recursion Examples

```python
# Example 1: Directory tree traversal
import os

def list_files(startpath, max_depth=3, current_depth=0):
    """
    Recursively list files and directories with indentation
    """
    if current_depth > max_depth:
        return
    
    # Indentation for visual hierarchy
    indent = "  " * current_depth
    
    try:
        for item in os.listdir(startpath):
            item_path = os.path.join(startpath, item)
            
            if os.path.isdir(item_path):
                print(f"{indent}📁 {item}/")
                # Recursive call for subdirectory
                list_files(item_path, max_depth, current_depth + 1)
            else:
                print(f"{indent}📄 {item}")
    except PermissionError:
        print(f"{indent}🚫 Permission denied: {startpath}")

# Usage (be careful with the path!)
# list_files(".", max_depth=2)

# Example 2: Binary search (recursive)
def binary_search(arr, target, low=0, high=None):
    """
    Perform binary search recursively on sorted array
    Returns index of target if found, else -1
    """
    if high is None:
        high = len(arr) - 1
    
    # Base case: element not found
    if low > high:
        return -1
    
    # Calculate middle index
    mid = (low + high) // 2
    
    # Base case: element found
    if arr[mid] == target:
        return mid
    
    # Recursive cases
    elif arr[mid] > target:
        # Search left half
        return binary_search(arr, target, low, mid - 1)
    else:
        # Search right half
        return binary_search(arr, target, mid + 1, high)

# Test binary search
sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
result = binary_search(sorted_numbers, target)
print(f"Found {target} at index {result}")  # Output: Found 11 at index 5

# Example 3: Tower of Hanoi
def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Solve Tower of Hanoi puzzle recursively
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, auxiliary, destination)
    
    # Move nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n-1, auxiliary, destination, source)

print("Tower of Hanoi solution for 3 disks:")
tower_of_hanoi(3, 'A', 'C', 'B')
```

### When to Use Recursion

**Use recursion when:**
- Problem can be broken down into smaller identical problems
- Tree-like data structures or hierarchical data
- Problems with natural recursive definition (factorial, Fibonacci)

**Avoid recursion when:**
- Simple iterative solution exists
- Deep recursion might cause stack overflow
- Performance is critical

```python
# Example: Comparing recursive vs iterative factorial
def factorial_recursive(n):
    """Recursive factorial"""
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """Iterative factorial"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Both produce same result
print(f"Recursive: 5! = {factorial_recursive(5)}")  # Output: 120
print(f"Iterative: 5! = {factorial_iterative(5)}")  # Output: 120
```

## Module 6: *Args and **Kwargs (Argument Types)

### Understanding *Args and **Kwargs

#### *Args (Variable Positional Arguments)
```python
# Basic *args example
def print_numbers(*args):
    """Accept any number of positional arguments"""
    print(f"Type of args: {type(args)}")  # Always a tuple
    print(f"Number of arguments: {len(args)}")
    print("Arguments:", args)
    
    # Process each argument
    for i, arg in enumerate(args, 1):
        print(f"Argument {i}: {arg} (type: {type(arg)})")

print_numbers(1, 2, 3)
print_numbers("hello", "world", 42, [1, 2, 3])

# Practical example: Calculator with *args
def calculate_average(*numbers):
    """Calculate average of any number of values"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max_min(*values):
    """Find maximum and minimum of given values"""
    if not values:
        return None, None
    return max(values), min(values)

# Using the functions
avg1 = calculate_average(85, 92, 78, 90)
avg2 = calculate_average(100, 95)
print(f"Average 1: {avg1:.2f}")  # Output: Average 1: 86.25
print(f"Average 2: {avg2:.2f}")  # Output: Average 2: 97.50

max_val, min_val = find_max_min(5, 2, 8, 1, 9, 3)
print(f"Max: {max_val}, Min: {min_val}")  # Output: Max: 9, Min: 1

# Combining *args with regular parameters
def create_sentence(subject, verb, *objects):
    """Create a sentence with subject, verb, and any number of objects"""
    sentence = f"{subject} {verb}"
    if objects:
        sentence += " " + " ".join(objects)
    return sentence + "."

print(create_sentence("The cat", "chased", "the", "mouse"))  # Output: The cat chased the mouse.
print(create_sentence("I", "like", "python", "programming")) # Output: I like python programming.
```

#### **Kwargs (Variable Keyword Arguments)
```python
# Basic **kwargs example
def print_student_info(**kwargs):
    """Accept any number of keyword arguments"""
    print(f"Type of kwargs: {type(kwargs)}")  # Always a dictionary
    print(f"Number of keyword arguments: {len(kwargs)}")
    
    # Process keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_student_info(name="Alice", age=20, major="Computer Science", gpa=3.8)

# Practical example: User registration
def register_user(username, password, **profile_info):
    """Register user with required credentials and optional profile info"""
    user = {
        'username': username,
        'password': password,  # In real apps, hash this!
        'profile': profile_info
    }
    return user

# Creating user accounts with different profile information
user1 = register_user("alice123", "securepass", email="alice@example.com", age=25)
user2 = register_user("bob456", "mypassword", full_name="Bob Smith", city="New York", occupation="Engineer")
user3 = register_user("charlie789", "test123")  # No additional info

print("User 1:", user1)
print("User 2:", user2)
print("User 3:", user3)

# Combining regular, *args, and **kwargs
def comprehensive_function(required1, required2, *args, **kwargs):
    """Function with all types of parameters"""
    print(f"Required 1: {required1}")
    print(f"Required 2: {required2}")
    print(f"Additional args: {args}")
    print(f"Additional kwargs: {kwargs}")

comprehensive_function("hello", "world", 1, 2, 3, name="Alice", age=25)
```

### Advanced *Args and **Kwargs Usage

```python
# Unpacking with * and **
def function_with_three_params(a, b, c):
    """Function that requires exactly three parameters"""
    return a + b + c

# Normal call
result1 = function_with_three_params(1, 2, 3)

# Unpacking list/tuple with *
numbers = [4, 5, 6]
result2 = function_with_three_params(*numbers)  # Equivalent to function_with_three_params(4, 5, 6)

# Unpacking dictionary with **
params = {'a': 7, 'b': 8, 'c': 9}
result3 = function_with_three_params(**params)  # Equivalent to function_with_three_params(7, 8, 9)

print(f"Result 1: {result1}")  # Output: 6
print(f"Result 2: {result2}")  # Output: 15
print(f"Result 3: {result3}")  # Output: 24

# Practical example: Configuration system
def configure_application(main_setting, *plugins, **settings):
    """Configure application with main setting, plugins, and various settings"""
    configuration = {
        'main_setting': main_setting,
        'plugins': list(plugins),
        'settings': settings
    }
    return configuration

# Using unpacking for configuration
plugin_list = ['auth_plugin', 'cache_plugin', 'logging_plugin']
app_settings = {
    'debug': True,
    'port': 8080,
    'database_url': 'sqlite:///app.db'
}

config = configure_application('production', *plugin_list, **app_settings)
print("Application configuration:")
for key, value in config.items():
    print(f"  {key}: {value}")

# Decorator with *args and **kwargs
def debug_decorator(func):
    """Decorator to debug function calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@debug_decorator
def multiply_numbers(a, b, c=1):
    return a * b * c

# The decorator works with any arguments
multiply_numbers(2, 3)
multiply_numbers(2, 3, c=4)
multiply_numbers(a=5, b=6)
```

## Module 7: Lambda Functions

### Understanding Lambda Functions
Lambda functions are small, anonymous functions defined with the `lambda` keyword. They can have any number of arguments but only one expression.

### Basic Lambda Syntax
```python
# Syntax: lambda arguments: expression

# Equivalent regular function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

print(square(5))           # Output: 25
print(square_lambda(5))    # Output: 25

# Lambda with multiple parameters
add = lambda a, b: a + b
multiply = lambda x, y, z: x * y * z

print(add(3, 7))           # Output: 10
print(multiply(2, 3, 4))   # Output: 24

# Lambda with no parameters
get_pi = lambda: 3.14159
get_message = lambda: "Hello, World!"

print(get_pi())            # Output: 3.14159
print(get_message())       # Output: Hello, World!
```

### Common Use Cases for Lambda Functions

#### 1. With `map()` function
```python
# map(function, iterable) applies function to each item

numbers = [1, 2, 3, 4, 5]

# Using lambda with map
squared = list(map(lambda x: x ** 2, numbers))
cubed = list(map(lambda x: x ** 3, numbers))

print(f"Numbers: {numbers}")        # Output: Numbers: [1, 2, 3, 4, 5]
print(f"Squared: {squared}")        # Output: Squared: [1, 4, 9, 16, 25]
print(f"Cubed: {cubed}")            # Output: Cubed: [1, 8, 27, 64, 125]

# Practical example: Processing strings
names = ["alice", "bob", "charlie"]
capitalized = list(map(lambda name: name.title(), names))
print(f"Capitalized: {capitalized}")  # Output: Capitalized: ['Alice', 'Bob', 'Charlie']
```

#### 2. With `filter()` function
```python
# filter(function, iterable) keeps items where function returns True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Filter numbers greater than 5
large_numbers = list(filter(lambda x: x > 5, numbers))

print(f"Numbers: {numbers}")           # Output: Numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Even numbers: {evens}")        # Output: Even numbers: [2, 4, 6, 8, 10]
print(f"Numbers > 5: {large_numbers}") # Output: Numbers > 5: [6, 7, 8, 9, 10]

# Practical example: Filtering valid emails
emails = [
    "user@example.com",
    "invalid-email",
    "test@domain.org",
    "another@company.com",
    "bad_email"
]

valid_emails = list(filter(lambda email: '@' in email and '.' in email, emails))
print(f"Valid emails: {valid_emails}")
```

#### 3. With `sorted()` function
```python
# Using lambda as key function for sorting

# Sorting numbers
numbers = [5, 2, 8, 1, 9, 3]
sorted_numbers = sorted(numbers)
reverse_sorted = sorted(numbers, reverse=True)

print(f"Original: {numbers}")         # Output: Original: [5, 2, 8, 1, 9, 3]
print(f"Sorted: {sorted_numbers}")    # Output: Sorted: [1, 2, 3, 5, 8, 9]
print(f"Reverse: {reverse_sorted}")   # Output: Reverse: [9, 8, 5, 3, 2, 1]

# Sorting by custom criteria
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78},
    {'name': 'Diana', 'grade': 95}
]

# Sort by grade (ascending)
by_grade = sorted(students, key=lambda student: student['grade'])
# Sort by grade (descending)
by_grade_desc = sorted(students, key=lambda student: student['grade'], reverse=True)
# Sort by name
by_name = sorted(students, key=lambda student: student['name'])

print("By grade:")
for student in by_grade:
    print(f"  {student['name']}: {student['grade']}")

print("By name:")
for student in by_name:
    print(f"  {student['name']}: {student['grade']}")

# Sorting strings by length
words = ["python", "java", "c", "javascript", "go"]
by_length = sorted(words, key=lambda word: len(word))
print(f"Words by length: {by_length}")  # Output: Words by length: ['c', 'go', 'java', 'python', 'javascript']
```

#### 4. Inline usage and practical examples
```python
# Immediate invocation
result = (lambda x, y: x * y)(5, 3)
print(f"Immediate result: {result}")  # Output: 15

# Using lambda in list comprehensions
operations = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x - 5
]

number = 10
results = [op(number) for op in operations]
print(f"Operations on {number}: {results}")  # Output: [11, 20, 100, 5]

# Calculator with lambda functions
calculator = {
    'add': lambda a, b: a + b,
    'subtract': lambda a, b: a - b,
    'multiply': lambda a, b: a * b,
    'divide': lambda a, b: a / b if b != 0 else "Error: Division by zero",
    'power': lambda a, b: a ** b
}

# Using the calculator
a, b = 10, 3
for operation, func in calculator.items():
    result = func(a, b)
    print(f"{a} {operation} {b} = {result}")

# Conditional lambda
categorize_age = lambda age: "Child" if age < 13 else "Teen" if age < 20 else "Adult"

ages = [8, 15, 25, 70, 12]
categories = [categorize_age(age) for age in ages]
print(f"Ages: {ages}")           # Output: Ages: [8, 15, 25, 70, 12]
print(f"Categories: {categories}") # Output: Categories: ['Child', 'Teen', 'Adult', 'Adult', 'Child']
```

### Limitations of Lambda Functions
- Only one expression allowed
- No statements (if, for, while, etc.) - only expressions
- No documentation strings
- Less readable for complex operations

```python
# When NOT to use lambda (use regular function instead)

# Complex logic - use regular function
def process_data(data):
    """Process data with multiple steps"""
    # Multiple operations
    cleaned = data.strip().lower()
    if len(cleaned) < 5:
        return "Too short"
    elif len(cleaned) > 50:
        return "Too long"
    else:
        return cleaned.title()

# Don't try to cram this into a lambda!
# This would be very hard to read and maintain
```

## Module 8: Pythonic Decorators Are Fun

### Understanding Decorators
Decorators are functions that modify the behavior of other functions. They provide a way to add functionality to existing code without modifying the original function.

### Basic Decorator Syntax

```python
# Example 1: Simple decorator
def my_decorator(func):
    """A simple decorator that adds functionality"""
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Using the decorated function
say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# Without decorator syntax (equivalent)
def say_hello():
    print("Hello!")

decorated_hello = my_decorator(say_hello)
decorated_hello()
```

### Decorators with Arguments

```python
# Decorator for functions with arguments
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@decorator_with_args
def add_numbers(a, b):
    return a + b

@decorator_with_args
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Using decorated functions
result1 = add_numbers(5, 3)
result2 = greet("Alice", greeting="Hi")
result3 = greet("Bob")

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}")
```

### Practical Decorator Examples

#### 1. Timing Decorator
```python
import time

def timer(func):
    """Decorator that measures function execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    """Simulate a slow function"""
    time.sleep(2)
    return "Done!"

@timer
def fast_function():
    """A fast function"""
    return "Quick result!"

# Test the timer
print(slow_function())
print(fast_function())
```

#### 2. Debugging Decorator
```python
def debug(func):
    """Decorator that prints function call details"""
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        
        result = func(*args, **kwargs)
        
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@debug
def make_greeting(name, age=None, city=None):
    greeting = f"Hello, {name}"
    if age:
        greeting += f", age {age}"
    if city:
        greeting += f" from {city}"
    return greeting + "!"

# Test debug decorator
make_greeting("Alice")
make_greeting("Bob", age=25)
make_greeting("Charlie", city="New York", age=30)
```

#### 3. Validation Decorator
```python
def validate_positive_numbers(func):
    """Decorator that validates all numeric arguments are positive"""
    def wrapper(*args, **kwargs):
        # Check positional arguments
        for i, arg in enumerate(args):
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument {i} must be positive, got {arg}")
        
        # Check keyword arguments
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"Argument '{key}' must be positive, got {value}")
        
        return func(*args, **kwargs)
    return wrapper

@validate_positive_numbers
def calculate_area(length, width):
    return length * width

@validate_positive_numbers
def create_rectangle(length, width, color="blue"):
    return {
        'length': length,
        'width': width,
        'color': color,
        'area': length * width
    }

# Test validation
try:
    print(calculate_area(5, 3))  # Works fine
    print(calculate_area(-2, 3)) # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

try:
    print(create_rectangle(4, 6, color="red"))  # Works fine
    print(create_rectangle(4, -1))              # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
```

### Decorators with Parameters

```python
# Decorator that accepts parameters
def repeat(num_times):
    """Decorator that repeats function execution"""
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(num_times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    return f"Hello, {name}!"

@repeat(num_times=5)
def roll_dice():
    import random
    return random.randint(1, 6)

print(greet("Alice"))
print(roll_dice())

# Conditional execution decorator
def conditional_execute(condition=True):
    """Decorator that conditionally executes function"""
    def decorator_conditional(func):
        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                print(f"Execution of {func.__name__} skipped")
                return None
        return wrapper
    return decorator_conditional

@conditional_execute(condition=True)
def important_function():
    return "This ran!"

@conditional_execute(condition=False)
def skipped_function():
    return "This won't run!"

print(important_function())  # Output: This ran!
print(skipped_function())    # Output: Execution of skipped_function skipped\nNone
```

### Class-Based Decorators

```python
# Decorator as a class
class CountCalls:
    """Decorator that counts how many times a function is called"""
    
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

@CountCalls
def say_goodbye():
    print("Goodbye!")

# Test class-based decorator
say_hello()
say_hello()
say_goodbye()
say_hello()
print(f"say_hello was called {say_hello.num_calls} times")
print(f"say_goodbye was called {say_goodbye.num_calls} times")

# Cache decorator using class
class CacheResults:
    """Decorator that caches function results"""
    
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args, **kwargs):
        # Create a key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in self.cache:
            print(f"Cache hit for {self.func.__name__}{args}")
            return self.cache[key]
        else:
            print(f"Computing {self.func.__name__}{args}")
            result = self.func(*args, **kwargs)
            self.cache[key] = result
            return result

@CacheResults
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test cache decorator
print(f"fibonacci(10) = {fibonacci(10)}")
```

### Multiple Decorators

```python
def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

def underline(func):
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"
    return wrapper

# Multiple decorators - applied from bottom to top
@bold
@italic
@underline
def hello(name):
    return f"Hello, {name}!"

print(hello("Alice"))  # Output: <b><i><u>Hello, Alice!</u></i></b>

# Equivalent to: bold(italic(underline(hello)))("Alice")
```

### Preserving Function Metadata

```python
from functools import wraps

def preserve_metadata(func):
    """Decorator that preserves the original function's metadata"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function docstring"""
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@preserve_metadata
def calculate_sum(a, b):
    """Calculate the sum of two numbers"""
    return a + b

# Without @wraps, metadata would be lost
print(f"Function name: {calculate_sum.__name__}")      # Output: calculate_sum
print(f"Function doc: {calculate_sum.__doc__}")       # Output: Calculate the sum of two numbers
print(f"Function module: {calculate_sum.__module__}") # Output: __main__

# Test the function
result = calculate_sum(5, 3)
print(f"Result: {result}")  # Output: Result: 8
```

This comprehensive guide covers all aspects of Python functions and methods, from basic declaration to advanced decorators. Each concept is explained with practical examples that demonstrate real-world usage scenarios.