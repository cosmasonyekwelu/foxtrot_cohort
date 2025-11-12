# Week 3 Summary: Control Structures in Python

## Table of Contents

1. [Conditional Statements](#conditional-statements)
2. [Loops](#loops)
3. [Practical Applications](#practical-applications)
4. [Key Concepts](#key-concepts)

## Conditional Statements

### Basic If-Else Structure

```python
if condition:
    # code to execute if condition is True
else:
    # code to execute if condition is False
```

### Examples

```python
# Simple if-else
if transport_fee <= destination_fee:
    print("Getting to destination Successful.")
else:
    print("Getting to destination Unsuccessful.")

# Multiple conditions with AND
if transport_fee <= destination_fee and train == "available":
    print("Getting to destination Successful.")
elif transport_fee <= destination_fee and train != "available":
    print("Train Not Available.")
else:
    print("Getting to destination Unsuccessful.")
```

### Key Points:

- Use `if`, `elif` (else if), and `else` for decision making
- Conditions can be combined with `and`, `or`, `not`
- Indentation is crucial for code blocks

## Loops

### While Loop

```python
# Basic while loop
num = 0
while num < 10:
    print(num)
    num = num + 1

# Infinite while loop (use with caution)
while True:
    print("Hello World!")
    # Typically includes a break condition
```

### For Loop

```python
# Iterating through lists
people = ["John", "Peter", "Ade", "Oluadamilare", "King"]
for person in people:
    print(person)

# For-else structure
for person in people:
    if person == searched_name:
        print(f"Person found: {person}")
        break
else:
    print("The person is not found.")
```

## Practical Applications

### List Manipulation

```python
# Combining lists
first_num = [1, 2, 3, 4, 5]
second_num = [6, 7, 8, 9, 10]
for num in second_num:
    first_num.append(num)

# Modifying list elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
updated = []
for num in numbers:
    num = num * 2
    updated.append(num)
```

### Data Processing

```python
# Creating email addresses from names
people = ["John", "Peter", "Ade", "Oluadamilare", "King"]
email_users = []
for person in people:
    email_address = person + "@mail.com"
    email_users.append(email_address)
```

### User Input Handling

```python
# Removing items with user input (case-insensitive)
people = ["John", "Peter", "Ade", "Oluadamilare", "King"]
name = input("Who do you want to delete: ").strip()
for person in people:
    if name.lower() == person.lower():
        people.remove(person)
        print(f"{person} Deleted.")
        break
else:
    print("The person is not found.")
```

### Program Examples

#### Course Registration System

```python
ui_ux_design = []
frontend_development = []
backend_development = []

print("Welcome to Univelcity")
name = input("What is your name")
course = input("What course are you planning to take?\n1. UI/UX design.\n2. Frontend Development\n3. Backend Development\n(Choose one 1/2/3): ")

if course == "1":
    ui_ux_design.append(name)
elif course == "2":
    frontend_development.append(name)
elif course == "3":
    backend_development.append(name)
else:
    print("You chose the wrong option. You are to choose between 1, 2 or 3.")
```

#### Supermarket System

```python
items = ["Fanta", "Bread", "Milk", "Pillow", "Pan"]
sales = [
    {"name": "King", "item": "Bread"},
    {"name": "Peter", "item": "Milk"}
]

print(f"Welcome to Moku Supermarket")
name = input("Please tell us your name:")
user_item = input(f"Hello {name}. What do you want to buy?\n{items}\nWrite the name of what you want:")

if user_item in items:
    option = input(f"You selected {user_item}. Do you want to buy?\n(Choose Y/N):")
    if option == "Y":
        sales.append({"name": name, "item": user_item})
        print("Thank you. Have a nice day")
    elif option == "N":
        print("I'm sorry. Have a nice day ")
    else:
        print("You choose the wrong option")
else:
    print("Sorry, we don't have that in store")
```

#### Expense Tracker

```python
expenses = [
    {"expense": "Transportation", "price": 800},
    {"expense": "Food", "price": 850},
    {"expense": "Internet", "price": 900}
]

while True:
    expense_name = input("Enter the expense name: ")
    expense_price = float(input("Enter the expense price: "))

    new_expense = {"expense": expense_name, "price": expense_price}
    budget_limit = 600

    if expense_price > budget_limit:
        new_expense["is_over_the_budget"] = True
    else:
        new_expense["is_over_the_budget"] = False

    expenses.append(new_expense)
    print(f"{expense_name} has been added")

    option = input("Do you want to continue? (Choose y/n)")
    if option == "n":
        for item in expenses:
            print(f"Expense: {item['expense']}, Price: {item['price']}")
        break
```

## Key Concepts

### 1. **Control Flow**

- Programs execute sequentially unless directed by control structures
- Conditions and loops change the execution path

### 2. **Boolean Logic**

- `and`, `or`, `not` operators for complex conditions
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`

### 3. **Loop Control**

- `break`: Exit loop immediately
- `continue`: Skip to next iteration
- `else` in loops: Executes when loop completes normally (no break)

### 4. **String Methods**

- `.strip()`: Remove whitespace
- `.lower()`: Convert to lowercase for case-insensitive comparisons

### 5. **List Operations**

- `.append()`: Add items to list
- `.remove()`: Remove items from list
- List comprehension (implicit in examples)

### 6. **Data Structures**

- Lists: Ordered, mutable collections
- Dictionaries: Key-value pairs for structured data
- Lists of dictionaries for complex data storage

### 7. **Input Validation**

- Always validate user input
- Handle edge cases and unexpected inputs
- Use appropriate data type conversions

### 8. **Debugging Techniques**

- Print statements for variable inspection
- Step-through execution mentally
- Test with different input values

This week focused on making programs dynamic and interactive through conditional logic and repetition, which are fundamental concepts in programming.
