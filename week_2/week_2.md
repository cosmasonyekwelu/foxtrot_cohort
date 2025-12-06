# Week 2 — Python Fundamentals

**(Comparison Operators, Logical Operators, Strings, and Data Structures)**

---

## Day 1 — Comparison Operators, Logical Operators, and Strings

### Comparison Operators

Used to compare values.

| Operator | Meaning                  | Example    | Result |
| -------- | ------------------------ | ---------- | ------ |
| `==`     | Equal                    | `5 == 5`   | True   |
| `!=`     | Not Equal                | `5 != 4`   | True   |
| `>`      | Greater Than             | `10 > 5`   | True   |
| `<`      | Less Than                | `5 < 10`   | True   |
| `>=`     | Greater Than or Equal To | `10 >= 10` | True   |
| `<=`     | Less Than or Equal To    | `5 <= 8`   | True   |

```python
stored_value = 10
search_input = 4

print(stored_value == search_input)
print(stored_value != search_input)
print(stored_value > search_input)
print(stored_value < search_input)
print(stored_value >= search_input)
print(stored_value <= search_input)
```

---

### Logical Operators

Used to evaluate multiple conditions.

| Operator | Meaning                                   | Example               | Result |
| -------- | ----------------------------------------- | --------------------- | ------ |
| `and`    | True if both conditions are True          | `(5 > 2) and (3 < 4)` | True   |
| `or`     | True if at least one condition is True    | `(5 > 10) or (3 < 4)` | True   |
| `not`    | Reverses boolean result (True becomes No) | `not (5 > 2)`         | False  |

```python
age = 20
status = "done"

print(age >= 20 and status == "done")
print(age >= 20 or status == "in_transit")
print(not (age >= 20 and status == "done"))
```

---

### Strings

A string is text enclosed in quotes.

```python
single_quote = 'Single quoted string'
double_quote = "Double quoted string"
multi_line = '''Multiline
string using triple quotes'''
```

**Common Escape Characters**

| Character | Meaning      |
| --------- | ------------ |
| `\n`      | New line     |
| `\t`      | Tab space    |
| `\\`      | Backslash    |
| `\'`      | Single quote |
| `\"`      | Double quote |

Example:

```python
sentence = "Hello!\nWelcome to Python.\tLet's learn."
print(sentence)
```

**String Operations**

```python
# Concatenation
msg = "Hello" + " World"

# f-string
name = "Cosmas"
greeting = f"My name is {name}"

# Repetition
print(name * 3)

# Membership
print("Cos" in greeting)

# Useful methods
text = " Python Developer "
print(text.strip())
print(text.lower())
print(text.upper())
print(text.replace("Developer", "Engineer"))
```

---

## Day 2 — Data Structures Overview

These are ways of organizing data for efficient use.

| Structure  | Ordered | Mutable | Allows Duplicates | Example            |
| ---------- | ------- | ------- | ----------------- | ------------------ |
| List       | Yes     | Yes     | Yes               | `[1, 2, 3]`        |
| Tuple      | Yes     | No      | Yes               | `(1, 2, 3)`        |
| Set        | No      | Yes     | No                | `{"a", "b"}`       |
| Dictionary | No      | Yes     | Keys unique       | `{"key": "value"}` |

---

### Dictionary

Stores data as key–value pairs.

```python
person = {
    "first_name": "Justice",
    "last_name": "Rivers",
    "age": 28,
    "profession": "Pet Engineer",
    "tags": ["a", "ab"],
    "nationality": {
        "nation": "Nigeria",
        "nin": 3456789023
    }
}

intro = f"Hello {person['first_name']} from {person['nationality']['nation']}"
print(intro)
```

**Dictionary operations**

```python
person["profession"] = "Software Engineer"
person["club"] = "Liverpool"
del person["age"]

print(person.get("first_name", "Unknown"))
```

---

### List

Lists hold multiple values.

```python
data = ["paul", 22, False, 14.5, person]
data[0] = "John"
del data[4]

numbers = [1, 2, 3, 4, 5]
numbers.append(11)
numbers.insert(2, 100)
numbers.remove(5)
numbers.pop(1)
print(numbers)
```

**Nested List Example**

```python
nested = [1, 2, 3, ["Yes", 5, {"info": [4, 5, 6]}], 7]

# Access "Yes"
print(nested[3][0])

# Add "end"
nested[3][2]["info"].append("end")

# Remove 7
nested.remove(7)
```

---

### Tuple

Immutable (cannot be changed) ordered collection.

```python
colors = ("red", "blue", "yellow", "red")
print(colors.count("red"))
print("blue" in colors)
combined = colors + ("green",)
print(combined)
```

---

### Set

Unordered, unique values.

```python
clubs1 = {"Arsenal", "Liverpool", "Tottenham"}
clubs2 = {"Fulham", "Liverpool", "Wolves"}

print(clubs1.intersection(clubs2))  # Common values
print(clubs1.union(clubs2))         # Combined
print(clubs1.difference(clubs2))    # Unique values
```

---

## Classwork Recap (Selected Examples)

```python
# Comparison
print(10 == 10)
print(10 >= 5)

# Logical
age = 24
driver = "yes"
print(age >= 18 and driver == "yes")

# Strings
print("Hello\nWelcome to Python!")

# String methods
name = " miracle "
print(name.strip())
print(name.upper())

# Lists and dictionary
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
```

---

## Week Summary

By the end of Week 2, you should understand:

- Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Logical operators (`and`, `or`, `not`)
- String formatting, methods, and escape sequences
- Storing and modifying data using lists, tuples, sets, and dictionaries

---

## Suggested Practice

- Try working with nested structures
- Loop through lists and dictionaries
- Prepare for conditions (`if`, `elif`, `else`) in Week 3

---
