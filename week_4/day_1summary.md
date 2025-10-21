# Python Functions - Comprehensive Guide

## Table of Contents

1. [Introduction to Functions](#introduction-to-functions)
2. [Function Definition and Syntax](#function-definition-and-syntax)
3. [Return Statements](#return-statements)
4. [Variable Scope](#variable-scope)
5. [Parameters and Arguments](#parameters-and-arguments)
6. [Types of Arguments](#types-of-arguments)
7. [Advanced Function Concepts](#advanced-function-concepts)
8. [Practical Example: Food Ordering System](#practical-example-food-ordering-system)

---

## Introduction to Functions

### What are Functions?

Functions are blocks of code that perform specific tasks. They help organize code into manageable, reusable sections.

### Benefits of Using Functions

1. **Modularity**: Break down complex problems into smaller, manageable pieces
2. **Reusability**: Write once, use multiple times
3. **Readability**: Make code easier to understand and maintain
4. **Debugging**: Easier to test and fix individual components

## Function Definition and Syntax

### Basic Function Structure

```python
def function_name():
    # code block
    return value
```

### Example 1: Simple Addition Function

```python
def addition():  # Function definition
    num_1 = 1
    num_2 = 2
    sum = num_1 + num_2
    return sum  # Return the result

output = addition()  # Function call
print(output)  # Output: 3
```

### Example 2: Subtraction Function

```python
def subtraction():
    return 2 - 1  # Direct return

output = subtraction()
print(output)  # Output: 1
```

## Return Statements

### What Can Functions Return?

Functions can return any data type in Python:

- Strings
- Booleans
- Integers
- Floats
- Lists
- Tuples
- Dictionaries
- Sets
- Other functions
- Variables

### Example: String Return

```python
def introduction():
    return "Hi my name is Cosmas"

print(introduction())  # Output: Hi my name is Cosmas
```

### Important Note about Return

Code after a return statement is unreachable:

```python
def example():
    return "This will be returned"
    print("This will never execute")  # Unreachable code
```

## Variable Scope

### Local vs Global Variables

- **Local Variables**: Defined inside a function, accessible only within that function
- **Global Variables**: Defined outside functions, accessible throughout the program

### Example: Variable Scope

```python
age = 12  # Global Variable

def func():
    name = "Cosmas"  # Local Variable
    return "His Name is " + name + " and he is " + str(age)

print(func())  # Output: His Name is Cosmas and he is 12
```

## Parameters and Arguments

### Definitions

- **Parameters**: Variables in the function definition
- **Arguments**: Actual values passed to the function when called

### Example: Function with Parameters

```python
def func_1(words):  # 'words' is a parameter
    return words

print(func_1("This is an argument"))  # "This is an argument" is an argument
```

### Practical Example: Reusable Addition

```python
def reusable_addition(num_one, num_two):
    return num_one + num_two

output_one = reusable_addition(14, 2)    # Output: 16
output_two = reusable_addition(4, 4)     # Output: 8
output_three = reusable_addition(16, 18) # Output: 34
```

## Types of Arguments

### 1. Positional/Required Arguments

Arguments must be passed in correct order and quantity.

```python
def func_2(pos1, pos2, pos3):
    return pos1, pos2, pos3

result = func_2("first value", "second value", "Third Value")
print(result)  # Output: ('first value', 'second value', 'Third Value')
```

### 2. Keyword Arguments

Arguments identified by parameter name, can be in any order.

```python
def func_2(pos1, pos2, pos3):
    return pos1, pos2, pos3

result = func_2(pos1="first value", pos3="third value", pos2="second value")
print(result)  # Output: ('first value', 'second value', 'third value')
```

### 3. Default Arguments

Parameters with default values if no argument is provided.

```python
def game(mode="easy"):
    return f"Game on!!! mode {mode}"

print(game())          # Output: Game on!!! mode easy
print(game("hard"))    # Output: Game on!!! mode hard
```

### 4. Variable-length Arguments (\*args)

Allows function to accept any number of positional arguments.

```python
def func_4(*param):  # *param collects all arguments as a tuple
    return param

print(func_4("red", "blue", "yellow", "green"))
# Output: ('red', 'blue', 'yellow', 'green')
```

### 5. Keyword Arguments (\*\*kwargs)

Allows function to accept any number of keyword arguments.

```python
def func_5(**param):  # **param collects all keyword arguments as a dictionary
    return param

result = func_5(
    name="Miracle",
    email="miracle@mail.com",
    availability=True,
    rating=8.0
)
print(result)
# Output: {'name': 'Miracle', 'email': 'miracle@mail.com', 'availability': True, 'rating': 8.0}
```

## Advanced Function Concepts

### Combining Different Argument Types

```python
def complex_function(req_param, def_param="default", *args, **kwargs):
    print(f"Required: {req_param}")
    print(f"Default: {def_param}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

complex_function("required", "custom", "arg1", "arg2", key1="value1", key2="value2")
```

## Practical Example: Food Ordering System

```python
import time

# Food database
foods = [
    {"name": "Yam", "price": "1000"},
    {"name": "Rice and beans", "price": "1500"},
    {"name": "spagetti", "price": "1200"},
    {"name": "Fufu", "price": "2500"},
]

def display_food():
    """Display all available food items"""
    print("Just My Food Menu")
    for food in foods:
        print(f"Name: {food['name']}, Price: {food['price']}")
        time.sleep(1)

def search_for_food(searched_food):
    """Search for food in the database"""
    for food in foods:
        # Normalize strings for comparison (remove spaces and convert to lowercase)
        if food["name"].lower().replace(" ", "") == searched_food.lower().replace(" ", ""):
            return food
    return False  # Food not found

def main():
    """Main program logic"""
    bill = 0
    while True:
        display_food()
        options = input("What do you want to buy \n Write the name of food: ")

        is_food = search_for_food(options)

        if type(is_food) == dict:
            purchase = input(
                f"The price of this food is {is_food['price']}. Do you want to buy it (y/n):")

            if purchase == "y":
                bill = bill + float(is_food["price"])

                option_two = input(
                    f"Your bill is {bill}. Do you want to buy more? (y/n)")

                if option_two == "y":
                    continue
                else:
                    print(f"Thank You for your purchased. Total Bill :{bill}")
                    break
        else:
            print("Sorry we don't have the requested food.")
            time.sleep(3)

# Start the program
main()
```

## Key Takeaways

1. **Functions organize code** into reusable blocks
2. **Parameters define what a function needs**, arguments provide the actual values
3. **Return statements** send data back from functions
4. **Variable scope** determines where variables can be accessed
5. **Different argument types** provide flexibility in function calls
6. **Practical applications** like the food system demonstrate real-world usage

Practice these concepts regularly to build strong programming fundamentals!
