````
Foxtrot Cohort:  Day 2
Date: 02 October 2025

## Python Basics — Comments, Variables, Data Types, and Operators.

### 1. Comments in Python
- **Single-line comment** uses `#` symbol.
  ```python
  # This is a single line comment
````

- **Multi-line comment / documentation string** uses triple quotes (`'''` or `"""`).

  ```python
  '''
  This is a multi-line comment
  that spans multiple lines
  and is often used for documentation.
  '''
  ```

### 2. Variables and Data Types

- Variables are names used to store values.
- Python uses **snake_case** naming convention.

Examples:

```python
bottle = "water"          # string
first_name = "Cosmos"     # string
world = "Hello World!"    # string variable
```

**Basic Data Types in Python:**

- String: `"qwerty1234567890@#$%^&*()_+"`
- Integer: `1234567890`
- Float: `123.4567890`
- Boolean: `True`, `False`

```python
print(world)   # Displays: Hello World!
```

### 3. Arithmetic Operators

Operators are used to perform calculations:

```
+  Addition (integers, floats, strings → concatenation)
-  Subtraction (integers, floats)
*  Multiplication (integers, floats, strings → repetition)
/  Division (integers, floats)
// Floor Division (rounding down values)
```

Examples:

```python
first_number = 4
second_number = 6

add = first_number + second_number
subtract = first_number - second_number
multiply = first_number * second_number
divide = first_number / second_number

print("Addition:", add)
print("Subtraction:", subtract)
print("Multiplication:", multiply)
print("Division:", divide)

# Display type of each result
print("Addition:", add, "Type:", type(add))
print("Subtraction:", subtract, "Type:", type(subtract))
print("Multiplication:", multiply, "Type:", type(multiply))
print("Division:", divide, "Type:", type(divide))
```

**String Operations:**

```python
concatenation = "Hello" + " " + "Cosmas"    # "Hello Cosmas"
repetition = "Hurray" * 3                   # "HurrayHurrayHurray"
```

### 4. Type Casting

Type casting means converting one data type into another.

- `int()` → convert to integer
- `str()` → convert to string
- `float()` → convert to float
- `bool()` → convert to boolean

Examples:

```python
convert_to_string = str(add)
print("Converting addition to string:", convert_to_string, type(convert_to_string))

convert_to_float = float(subtract)
print("Converting subtraction to float:", convert_to_float, type(convert_to_float))

convert_to_boolean = bool(multiply)
print("Converting multiplication to boolean:", convert_to_boolean, type(convert_to_boolean))

convert_to_int = int(divide)
print("Converting divide to integer:", convert_to_int, type(convert_to_int))
```

### 5. Re-assigning Variables

Variables can be re-assigned new values:

```python
nationality = "United States Of America"
nationality = "Nigerian"
nationality = "France"
print(nationality)   # Output: France
```

Example of string concatenation with variables:

```python
introduction = "Hello, My name is " + first_name + " I am from " + nationality
print(introduction)
```

---

✅ **Day 2 Summary**:

- Learned how to write comments in Python.
- Explored variables, naming conventions, and data types.
- Practiced arithmetic and string operators.
- Performed type casting (int, str, float, bool).
- Understood variable reassignment and string concatenation.

---
