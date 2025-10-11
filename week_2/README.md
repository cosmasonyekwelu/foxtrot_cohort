# Week 2 - Python Fundamentals Readme

## Overview

This week covered essential Python programming concepts including comparison operators, logical operators, string operations, and data structures. The material was divided into Day 1, Day 2, and Classwork sessions.

## Day 1 Topics

### Comparison Operators

Comparison operators are used to compare two values and return Boolean results (True/False).

**Operators:**

- `==` : Is Equal
- `!=` : Not Equal
- `>` : Greater Than
- `<` : Less Than
- `>=` : Greater Than or Equal To
- `<=` : Less Than or Equal To

**Example:**

```python
stored_value = 10
search_input = 4
is_equal = stored_value == search_input  # Returns False
```

### Logical Operators

Logical operators combine multiple comparisons and return Boolean results.

**Operators:**

- `and` : Both comparisons must be True
- `or` : At least one comparison must be True
- `not` : Reverses the Boolean result

**Example:**

```python
age = 20
nyse = "done"
is_all_true = age >= 20 and nyse == "done"  # Returns True
```

### String Operations

Strings are sequences of characters enclosed in quotes.

**String Declaration Methods:**

- Single quotes: `'Hello'`
- Double quotes: `"Hello"`
- Triple quotes (multi-line): `'''Hello\nWorld'''`

**Special Characters:**

- `\n` : New line
- `\t` : Tab
- `\\` : Backslash
- `\b` : Backspace
- `\'` : Single quote
- `\"` : Double quote

**String Operations:**

- **Concatenation**: `str1 + str2`
- **Repetition**: `str1 * 3`
- **Interpolation**: `f"My name is {name}"`
- **Membership**: `"text" in string`

**String Methods:**

- `.replace()` : Replace substring
- `.strip()` : Remove whitespace
- `.lower()` : Convert to lowercase
- `.upper()` : Convert to uppercase
- `.title()` : Convert to title case
- `.find()` : Find substring position
- `.split()` : Split into list

## Day 2 Topics

### Data Structures

Python provides four built-in data structures for storing collections of data.

#### 1. Dictionary

- Unordered collection of key-value pairs
- Mutable (can be changed)
- Keys must be unique

```python
person = {
    "first_name": "Justice",
    "last_name": "Rivers",
    "age": 28
}
```

**Dictionary Operations:**

- Access: `person["first_name"]`
- Update: `person["age"] = 29`
- Add: `person["club"] = "Liverpool"`
- Delete: `del person["age"]`
- Methods: `.get()`, `.pop()`, `.clear()`

#### 2. List

- Ordered, mutable collection
- Allows duplicates
- Can contain mixed data types

```python
datas = ["paul", 22, False, 14.5]
```

**List Operations:**

- Access: `datas[0]`
- Update: `datas[0] = "John"`
- Add: `.append()`, `.insert()`
- Remove: `.pop()`, `.remove()`, `del`
- Concatenation: `list1 + list2`
- Repetition: `list1 * 3`
- Membership: `element in list`

#### 3. Tuple

- Ordered, immutable collection
- Faster than lists
- Use for fixed data

```python
colors = ("red", "blue", "yellow")
```

**Tuple Operations:**

- Access: `colors[0]`
- Concatenation: `tuple1 + tuple2`
- Repetition: `tuple1 * 2`
- Membership: `element in tuple`
- Methods: `.count()`, `.index()`

#### 4. Set

- Unordered collection of unique elements
- Mutable but elements must be immutable
- No indexing

```python
top_4_clubs = {"Arsenal", "Liverpool", "Tottenham"}
```

**Set Operations:**

- Union: `set1.union(set2)` or `set1 | set2`
- Intersection: `set1.intersection(set2)` or `set1 & set2`
- Difference: `set1.difference(set2)` or `set1 - set2`

## Classwork Exercises

The classwork reinforced these concepts through practical exercises:

1. **Comparison Operators**: Practiced using all comparison operators with various values
2. **Variable Comparison**: Compared stored values with user inputs
3. **Logical Conditions**: Combined multiple conditions using logical operators
4. **String Manipulation**: Created strings using different quote styles and special characters
5. **String Methods**: Applied various string methods for formatting and searching
6. **Data Structure Operations**: Performed CRUD operations on dictionaries, lists, tuples, and sets

## Key Concepts Mastered

- **Boolean Logic**: Understanding True/False evaluations
- **Operator Precedence**: Knowing which operations execute first
- **String Formatting**: Multiple ways to create and manipulate strings
- **Data Structure Selection**: Choosing the right structure for different use cases
- **Mutability**: Understanding which data structures can be modified
- **Nested Structures**: Working with complex, nested data organizations

## Practical Applications

These fundamentals are essential for:

- Data validation and conditional logic
- Text processing and formatting
- Organizing and accessing complex data
- Building more advanced algorithms and applications

This week provided a solid foundation in Python's core concepts that will be built upon in subsequent weeks.
