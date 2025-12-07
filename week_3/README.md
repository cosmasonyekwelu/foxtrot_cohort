
# Python Control Structures — Class Practice

## Overview

This project demonstrates how to use conditional statements in Python (`if`, `elif`, and `else`) to control how a program responds to user input or specific conditions.

The exercises combine decision-making, input handling, and basic data structures to simulate real-world examples such as course registration and supermarket transactions.

The goal is to help you understand how logic flow works in programming.

---

## Learning Objectives

By completing this practice, you should be able to:

* Use conditional statements (`if`, `elif`, `else`)
* Apply logical operators (`and`, `or`, `not`)
* Collect and process user input using `input()`
* Store and organize information using lists and dictionaries
* Format strings using f-strings
* Combine data input and conditional logic to build interactive programs

---

## Concepts Covered

### 1. Conditional Logic

Conditional statements allow a program to behave differently depending on circumstances:

```python
if condition:
    # Code runs when condition is True
elif another_condition:
    # Runs if the first condition is False and this one is True
else:
    # Runs when all previous conditions are False
```

Logical operators include:

* `and` — both conditions must be True
* `or` — at least one condition must be True
* `not` — reverses a condition’s logical value

---

### 2. String Formatting Using f-Strings

f-Strings allow variables to be easily inserted into strings:

```python
name = "Cosmas"
print(f"Hello {name}, welcome to Python class!")
```

Avoid placing f-strings inside f-strings:

```python
# Incorrect
print(f"{"==" * 24}")

# Correct
print("=" * 24)
```

---

### 3. User Input and Data Handling

User input is collected using the `input()` function. Input is always read as a string, so convert it to numbers when needed:

```python
age = int(input("Enter your age: "))
```

Data may be stored in:

* Lists (`[]`) — useful for storing collections of values
* Dictionaries (`{}`) — ideal for storing structured key–value data

---

## Code Implementation

Below is the complete corrected version of the class exercise:

```python
# ======== CONTROL STRUCTURE ========

destination_fee = 1000
transport_fee = 1900
train = "unavailable"

# Example: Nested if/elif/else
if transport_fee <= destination_fee and train == "available":
    print("=" * 24)
    print("Getting to destination Successful.")
    print("=" * 24)
elif transport_fee <= destination_fee and train != "available":
    print("=" * 24)
    print("Train Not Available.")
    print("=" * 24)
else:
    print("=" * 24)
    print("Getting to destination Unsuccessful.")
    print("=" * 24)

# ==========================================
# Course Registration Example
# ==========================================

ui_ux_design = []
frontend_development = []
backend_development = []

print("\nWelcome to Univelcity")
name = input("What is your name? ")

course = input(
    "What course are you planning to take?\n"
    "1. UI/UX Design\n"
    "2. Frontend Development\n"
    "3. Backend Development\n"
    "(Choose one: 1/2/3): "
)

if course == "1":
    ui_ux_design.append(name)
elif course == "2":
    frontend_development.append(name)
elif course == "3":
    backend_development.append(name)
else:
    print("You chose the wrong option. Please choose between 1, 2, or 3.")

print("\n=== Course Enrollment ===")
print("UI/UX Design:", ui_ux_design)
print("Frontend Development:", frontend_development)
print("Backend Development:", backend_development)

# ==========================================
# Supermarket Sales Example
# ==========================================

items = ["Fanta", "Bread", "Milk", "Pillow", "Pan"]
sales = [
    {"name": "King", "item": "Bread"},
    {"name": "Peter", "item": "Milk"}
]

print("\n" + "=" * 24)
print("Welcome to Moku Supermarket")
print("=" * 24)

name = input("Please tell us your name: ")
user_item = input(
    f"Hello {name}. What do you want to buy?\nAvailable items: {items}\nWrite the name of what you want: "
)

if user_item in items:
    option = input(f"You selected {user_item}. Do you want to buy it? (Choose Y/N): ").upper()
    if option == "Y":
        sales.append({"name": name, "item": user_item})
        print("Thank you for your purchase. Have a nice day!")
    elif option == "N":
        print("No worries. Have a nice day!")
    else:
        print("Invalid option. Please choose Y or N next time.")
else:
    print("Sorry, we don't have that item in store.")

print("\n=== Updated Sales Record ===")
print(sales)
```

---

## Explanation of Examples

### Destination Fee Example

Checks whether the transport cost is within budget and whether the train is available. The result depends on both conditions.

---

### Course Registration Example

Simulates a simple registration system:

* Collects a name
* Accepts a course option
* Stores the name in a corresponding course list

Demonstrates list operations and input validation.

---

### Supermarket Example

Models a small store interaction:

* Displays available items
* Accepts purchase decisions
* Stores sales in a list of dictionaries

Demonstrates combining input, conditionals, and data storage.

---

## Summary of What You Learned

| Concept                | Description                                       |
| ---------------------- | ------------------------------------------------- |
| Conditional Statements | Code branches based on logical conditions         |
| Logical Operators      | Combine or modify conditions (`and`, `or`, `not`) |
| f-Strings              | Format strings using variables                    |
| User Input             | Read, process, and validate user responses        |
| Lists & Dictionaries   | Store and organize program data                   |
| Program Flow           | Decisions change how the program behaves          |

---
