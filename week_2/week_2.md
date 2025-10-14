Week 2: day 1 and 2

---

## 🐍 Week 2: Python Fundamentals — Comparison, Logical Operators, Strings & Data Structures

### 📅 Day 1: Comparison Operators, Logical Operators, and Strings

#### 🔹 Comparison Operators in Python

Comparison operators are used to compare two values or data.

| Operator | Meaning                  | Example    | Result  |
| -------- | ------------------------ | ---------- | ------- |
| `==`     | Is Equal                 | `5 == 5`   | ✅ True |
| `!=`     | Not Equal                | `5 != 4`   | ✅ True |
| `>`      | Greater Than             | `10 > 5`   | ✅ True |
| `<`      | Less Than                | `5 < 10`   | ✅ True |
| `>=`     | Greater Than or Equal To | `10 >= 10` | ✅ True |
| `<=`     | Less Than or Equal To    | `5 <= 8`   | ✅ True |

```python
stored_value = 10
search_input = 4

print("Is Equal:", stored_value == search_input)
print("Not Equal:", stored_value != search_input)
print("Greater Than:", stored_value > search_input)
print("Less Than:", stored_value < search_input)
print("Greater Than or Equal To:", stored_value >= search_input)
print("Less Than or Equal To:", stored_value <= search_input)
```

---

#### 🔹 Logical Operators in Python

Logical operators combine multiple conditions.

| Operator | Description                                | Example               | Result   |
| -------- | ------------------------------------------ | --------------------- | -------- |
| `and`    | True if **both** conditions are True       | `(5 > 2) and (3 < 4)` | ✅ True  |
| `or`     | True if **at least one** condition is True | `(5 > 10) or (3 < 4)` | ✅ True  |
| `not`    | Reverses the result (True → False)         | `not (5 > 2)`         | ❌ False |

```python
age = 20
nyse = "done"

print("AND:", age >= 20 and nyse == "done")
print("OR:", age >= 20 or nyse == "in_transit")
print("NOT:", not (age >= 20 and nyse == "done"))
```

---

#### 🔹 Strings in Python

A **string** is a sequence of characters enclosed in quotes.

```python
single_quote = 'Single quote string'
double_quote = "Double quote string"
triple_quote = '''Triple quotes
allow multi-line strings'''
```

**Special Characters in Strings:**

| Character | Function     |
| --------- | ------------ |
| `\n`      | New line     |
| `\t`      | Tab space    |
| `\\`      | Backslash    |
| `\'`      | Single quote |
| `\"`      | Double quote |

Example:

```python
sentence = "Hello!\nMy name is Cosmas.\tWelcome to Python class."
print(sentence)
```

**String Operations**

```python
# Concatenation
concat = "A string" + " is joined"

# Interpolation (f-string)
name = "Cosmas"
greeting = f"My name is {name}"

# Repetition
repeat = name * 3

# Membership
print("Book" in greeting)

# Common String Methods
sentence = " My name is John "
print(sentence.strip())      # Remove spaces
print(sentence.lower())      # Lowercase
print(sentence.upper())      # Uppercase
print(sentence.replace("John", "Doe"))  # Replace
```

---

### 📅 Day 2: Data Structures in Python

Data structures are ways to store and organize data in Python.

| Structure      | Ordered         | Mutable | Allows Duplicates | Syntax Example     |
| -------------- | --------------- | ------- | ----------------- | ------------------ |
| **List**       | ✅ Yes          | ✅ Yes  | ✅ Yes            | `[1, 2, 3]`        |
| **Tuple**      | ✅ Yes          | ❌ No   | ✅ Yes            | `(1, 2, 3)`        |
| **Set**        | ❌ No           | ✅ Yes  | ❌ No             | `{"a", "b"}`       |
| **Dictionary** | ❌ No (by keys) | ✅ Yes  | Keys unique       | `{"key": "value"}` |

---

#### 🔸 Dictionary

A collection of **key–value pairs**.

```python
person = {
    "first_name": "Justice",
    "last_name": "Rivers",
    "age": 28,
    "gender": "Male",
    "profession": "Pet Engineer",
    "tags": ["a", "ab"],
    "nationality": {
        "nation": "Nigeria",
        "nin": 3456789023,
        "tax": "all paid in full"
    }
}

introduction = f"Hello {person['first_name']} {person['last_name']} from {person['nationality']['nation']}."
print(introduction)
```

**Dictionary Operations**

```python
person["profession"] = "Software Engineer"  # Update
person["club"] = "Liverpool"                # Add new key
del person["gender"]                        # Delete key

print(person.get("first_name", "Unknown"))  # Safe get
```

---

#### 🔸 List

Lists store multiple items in a single variable.

```python
datas = ["paul", 22, False, 14.5, person, [1, 2, 3, 4, 5]]
datas[0] = "John"
del datas[5]

numbers = [1, 2, 3, 4, 5]
numbers.append(11)
numbers.insert(2, 100)
numbers.remove(5)
numbers.pop(1)
print(numbers)
```

**Nested List Example (Classwork)**

```python
nested_number = [2, 46, 33, 1, 6, 3, ["twenty", "Yes", 5, 6, {"another": [3, 55, 6, "middle", 17]}, 7], 55, 2, 4]

# Locate "Yes"
print(nested_number[6][1])

# Add "end" to the 'another' list
nested_number[6][4]["another"].append("end")

# Delete the number 7
nested_number[6].remove(7)
```

---

#### 🔸 Tuple

Tuples are **immutable lists**.

```python
colors = ("red", "blue", "yellow", "red")

print(colors.count("red"))        # Count
print("blue" in colors)           # Membership
concat_tuple = colors + ("green", "orange")
print(concat_tuple)
```

---

#### 🔸 Set

Sets are **unordered collections** with **unique elements**.

```python
top_4_clubs = {"Arsenal", "Liverpool", "Tottenham", "Bournemouth"}
regulars = {"Fulham", "Bournemouth", "Burnley", "Wolves"}

intersect = top_4_clubs.intersection(regulars)  # Common
union = top_4_clubs.union(regulars)              # Combine
difference = top_4_clubs.difference(regulars)    # Unique to top_4_clubs
print(difference)
```

---

### 🧩 Classwork Recap

```python
# 1. Comparison Examples
print(10 == 10)
print(10 >= 5)
print(10 <= 5)

# 2. Equality Check
stored_value = 12
search_input = 12
print(stored_value == search_input)

# 3. Greater/Less Than
print(5 > 10)
print(15 <= 20)

# 4. Logical AND
age = 24
driver_license = "yes"
print(age >= 18 and driver_license == "yes")

# 5. Logical OR
temperature = 35
raining = False
print(temperature > 30 or raining == True)

# 6. NOT Operator
is_tired = False
print(not is_tired)

# 7. String Types
single = 'Single quotes Example'
double = "Double quotes Example"
triple_single = '''Triple single quotes Example'''
triple_double = """Triple double quotes Example"""
print(single, double, triple_single, triple_double)

# 8. Escape Characters
print("Hello!\nMy name is Cosmas.\tWelcome to Python Backend class.")

# 9. String Methods
name = " miracle "
print(name.strip())
print(name.upper())
print(name.lower())

# 10. Concatenation, f-string & Repetition
text_one = "Python"
text_two = " Programming"
print(text_one + text_two)
print(f"My name is Cosmas")
print("Univelcity" * 3)
```

---

### ✅ Summary

By the end of Week 2, I learned:

- How to compare values using **comparison operators**
- How to make logical decisions using **and**, **or**, **not**
- How to manipulate and format **strings**
- How to store and manage data using **lists**, **tuples**, **sets**, and **dictionaries**

---

### 📘 Suggested Next Steps

- Practice **nested data structures** (lists inside dictionaries, etc.)
- Try **looping** through lists and dictionaries
- Start exploring **conditional statements (if / else)** in Week 3

---
