# 🐍 Python Control Structures — Class Practice

## 📘 Overview

This project demonstrates how to use **control structures** in Python — specifically `if`, `elif`, and `else` statements — to make programs behave differently based on user input or specific conditions.

It combines **decision-making**, **user input handling**, and **data structures** to simulate real-world scenarios like course registration and supermarket sales.

These exercises are part of the Python class practice session designed to strengthen your understanding of how **logic flow** works in programming.

---

## 🎯 Learning Objectives

By the end of this practice, you should be able to:

- Understand and implement **conditional statements** (`if`, `elif`, `else`)
- Use **logical operators** like `and`, `or`, and `not`
- Handle **user input** effectively using `input()`
- Store and manipulate data with **lists** and **dictionaries**
- Format strings using **f-strings**
- Combine logic and data handling to build simple interactive programs

---

## 🧠 Concepts Covered

### 1. Conditional Logic

Conditional statements allow you to make decisions in your program.
For example:

```python
if condition:
    # Runs if condition is True
elif another_condition:
    # Runs if the first condition was False but this is True
else:
    # Runs if all previous conditions were False
```

You can also combine conditions using:

- `and` → both conditions must be true
- `or` → at least one condition must be true
- `not` → reverses the logical result

---

### 2. String Formatting with f-Strings

Python’s f-strings (`f"Hello {name}"`) make it easy to include variables in strings.

✅ Example:

```python
name = "Cosmas"
print(f"Hello {name}, welcome to Python class!")
```

⚠️ **Note:**
When using f-strings, don’t nest braces:

```python
# ❌ Wrong:
print(f"{"==" * 24}")

# ✅ Correct:
print("=" * 24)
```

---

### 3. User Input and Data Handling

The `input()` function lets you get user input as a string.
To use it as a number, convert it with `int()` or `float()` if needed.

Example:

```python
age = int(input("Enter your age: "))
```

You can then store user input in:

- **Lists** (`[]`) for groups of items or names
- **Dictionaries** (`{}`) for structured data like name–item pairs

---

## 💻 Code Implementation

Below is the full corrected version of your class exercise code.

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
        print("✅ Thank you for your purchase. Have a nice day!")
    elif option == "N":
        print("😐 No worries. Have a nice day!")
    else:
        print("⚠️ Invalid option. Please choose Y or N next time.")
else:
    print("❌ Sorry, we don't have that item in store.")

print("\n=== Updated Sales Record ===")
print(sales)
```

---

## 🧩 Explanation of Examples

### 🛣️ Destination Fee Example

Checks if your **transport fee** and **train availability** allow a successful trip:

- If train is available and cost is within budget → success
- If cost is okay but train unavailable → train not available
- Otherwise → unsuccessful

---

### 🧑‍💻 Course Registration Example

Simulates a registration system where:

- Users type their **name** and choose a course
- The chosen course list (UI/UX, Frontend, Backend) stores their name

This demonstrates list operations (`append`) and input validation.

---

### 🛒 Supermarket Example

Represents a mini-store system:

- Displays available items
- Records purchases in the sales list
- Handles invalid or declined purchases gracefully

This example combines conditionals, user input, and data storage using lists of dictionaries.

---

## 🏁 Summary — What You Learned

| Concept                  | Description                                               |
| ------------------------ | --------------------------------------------------------- |
| **if / elif / else**     | Controls which block of code executes based on conditions |
| **Logical operators**    | Combine or modify conditions (`and`, `or`, `not`)         |
| **f-Strings**            | Format output dynamically using variables                 |
| **User Input**           | Collect and process user responses                        |
| **Lists & Dictionaries** | Store and organize data efficiently                       |
| **Program Flow**         | How logic decisions shape user experience                 |

---
