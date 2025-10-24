# **Week 4 Summary — Python Functions**

## **Focus:**

Understanding how to create, use, and apply **functions** in Python — including advanced concepts like arguments, variable scope, decorators, and higher-order functions.

---

## **1. What Are Functions?**

A **function** is a block of reusable code designed to perform a specific task.
Instead of writing the same logic multiple times, functions allow you to define code once and call it whenever needed.

### **Benefits:**

1. **Modularity** – Breaks code into manageable parts.
2. **Reusability** – Use the same function across different programs.
3. **Readability** – Makes code cleaner and easier to understand.

### 🔹 **Basic Syntax:**

```python
def function_name():
    # block of code
    return result
```

### 🔹 **Example:**

```python
def addition():
    num_1 = 1
    num_2 = 2
    return num_1 + num_2
```

---

## **2. Return Values**

Functions can return **any data type**, including:

- String
- Integer
- Float
- Boolean
- List / Tuple / Dictionary / Set
- Function / Variable

Example:

```python
def introduction():
    return "Hi my name is Cosmas"
```

---

## **3. Variable Scope**

- **Global Variables:** Declared outside any function and accessible everywhere.
- **Local Variables:** Declared inside a function and accessible only within it.

```python
age = 12  # Global

def func():
    name = "Cosmas"  # Local
    return f"His Name is {name} and he is {age}"
```

---

## **4. Parameters & Arguments**

Parameters are variables in the function definition.
Arguments are the actual values passed when the function is called.

### Example:

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Cosmas"))  # Argument
```

---

## **5. Types of Function Arguments**

| Type                                       | Description                      | Example              |
| ------------------------------------------ | -------------------------------- | -------------------- |
| **Positional**                             | Must be in correct order         | `func(a, b, c)`      |
| **Keyword**                                | Passed by name                   | `func(x=1, y=2)`     |
| **Default**                                | Has a fallback value             | `def func(x=10)`     |
| **Variable-length (`*args`)**              | Takes multiple unnamed arguments | `def func(*args)`    |
| **Keyword Variable-length (`**kwargs`)\*\* | Takes multiple named arguments   | `def func(**kwargs)` |

### Examples:

```python
def game(mode="easy"):
    return f"Game on!!! mode {mode}"

def func_4(*colors):
    return colors  # Tuple

def func_5(**details):
    return details  # Dictionary
```

---

## **6. Practical Example — Food Ordering System**

```python
foods = [
    {"name": "Yam", "price": "1000"},
    {"name": "Rice and beans", "price": "1500"},
    {"name": "Spaghetti", "price": "1200"},
    {"name": "Fufu", "price": "2500"},
]
```

The program:

- Displays menu
- Allows user to search for food
- Calculates total bill
- Handles invalid entries

Demonstrates:

- Function reuse
- Loops
- Conditionals
- Type checking
- User input handling

---

## **7. Higher-Order Functions**

Functions that take **other functions as arguments** or return functions as results.

### Examples:

- `map()` – Applies a function to all items in an iterable.
- `filter()` – Selects items based on a condition.
- `reduce()` – Combines items to a single cumulative result.

```python
from functools import reduce

numbers = [1, 2, 3, 4]

map_result = list(map(lambda x: x * 2, numbers))
filter_result = list(filter(lambda x: x % 2 == 0, numbers))
reduce_result = reduce(lambda a, b: a + b, numbers)
```

---

## **8. Lambda Functions**

Anonymous (unnamed) functions defined with the `lambda` keyword.

```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

---

## **9. Nested Functions**

A **function defined inside another function**.

```python
def outer():
    def inner():
        return "Hello from inner function!"
    return inner()
```

---

## **10. List Comprehension**

A concise way to create lists in one line.

```python
numbers = [1, 2, 3, 4, 5, 6]
new_list = [n + 2 for n in numbers if n % 2 == 0]
```

---

## **11. Decorators**

Decorators modify or enhance another function **without changing its code**.
They use the `@decorator_name` syntax.

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello Team!")

say_hello()
```

---

## **12. Key Takeaways**

- Functions make code **clean, organized, and reusable**.
- Learn to use arguments effectively (`*args`, `**kwargs`).
- Understand **scope** (local vs global).
- Explore **higher-order functions** for efficient data handling.
- Use **decorators and lambdas** for advanced flexibility.
- Apply **list comprehensions** for cleaner loops.

---
