## **Week 5 Summary — Python 100 Days of Code**

### **Theme:**

_Data Organization, Inventory Systems & Object-Oriented Programming (OOP)_

---

## ** Day 1: Market Seller Inventory System**

### **Objective:**

Build a simple **inventory management system** using lists and dictionaries to handle products dynamically through a console-based menu.

### **Core Concepts:**

- Working with **lists of dictionaries**
- Using **functions** for modular code
- Handling **user input and validation**
- Performing **CRUD operations** (Create, Read, Update-like Display)
- Implementing **search and calculation logic**
- String formatting with **f-strings**

### **Key Functions Explained:**

| Function            | Description                                                    |
| ------------------- | -------------------------------------------------------------- |
| `add_goods()`       | Prompts user to add new goods to the inventory list.           |
| `display_goods()`   | Displays all goods with their details in a formatted table.    |
| `calculate_goods()` | Sums up all product quantities to show total inventory count.  |
| `search_goods()`    | Allows searching goods by name or category (case-insensitive). |
| `main()`            | Provides a user menu to select different inventory options.    |

### **Data Structure Example:**

```python
goods = [
    {'name': 'phone', 'price': 50000, 'category': 'gadget', 'quantity': 12, 'date': '28-10-2025'},
    {'name': 'rice', 'price': 7000, 'category': 'food', 'quantity': 7, 'date': '28-10-2025'},
    {'name': 'book', 'price': 2000, 'category': 'confectionary', 'quantity': 10, 'date': '28-10-2025'},
]
```

### **Expected Output Example:**

```
============================
Market Seller Inventory.
============================
1. Add Goods
2. View Inventory
3. Calculate Total Number of Goods
4. Search by Name or Category
5. Exit
```

### **Skills Gained:**

- Data organization with lists & dictionaries
- Basic functional programming structure
- Control flow with `while` loops and conditional logic
- Use of `input()`, `print()`, and data type conversion

---

## ** Day 2: Object-Oriented Programming (OOP) Introduction**

### **Objective:**

Understand how to design programs using **classes and objects** — the foundation of object-oriented programming.

### **Core Concepts:**

- What is **OOP**?
  → A paradigm where we design programs around objects that model real-world entities.

- **Blueprints (Classes)** and **Instances (Objects)**

- **Attributes:** Variables that describe object properties

- **Methods:** Functions defined inside a class that perform actions

- **Constructors (`__init__`)**

- **Class vs Instance Attributes**

---

### **Code Summary Example:**

```python
class Person:  # Blueprint
    pass

# Creating Objects
Miracle = Person()
Clinton = Person()
Tivsue = Person()
```

---

### **Footballer Example Class:**

```python
class Footballer:
    # Class Attributes
    game = "football"
    ball = "sphere"

    # Instance Attributes
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    # Method
    def information(self):
        return f"{self.name} plays {Footballer.game}. The ball is {Footballer.ball}."


# Creating Objects
zinedine_zidane = Footballer("Zinedine Zidane", 34, "Attacking Midfielder")
cristiano_ronaldo = Footballer("Cristiano Ronaldo", 39, "Striker")

print(zinedine_zidane.information())
print(cristiano_ronaldo.information())
```

### **Expected Output:**

```
Zinedine Zidane plays football. The ball is sphere.
Cristiano Ronaldo plays football. The ball is sphere.
```

---

### **Key Takeaways:**

| Concept                      | Explanation                                                     |
| ---------------------------- | --------------------------------------------------------------- |
| **Class**                    | Blueprint that defines structure and behavior of objects.       |
| **Object / Instance**        | A real-world example of a class.                                |
| **Class Attribute**          | Shared across all instances of the class.                       |
| **Instance Attribute**       | Unique for each object.                                         |
| **Method**                   | Defines actions an object can perform.                          |
| **Constructor (`__init__`)** | Initializes new object instances with default or passed values. |

---

## ** Additional Resources & Learning Materials**

### **Videos:**

- [Python Object-Oriented Programming - Corey Schafer (YouTube)](https://www.youtube.com/watch?v=JeznW_7DlB0)
- [Python Data Structures Crash Course – freeCodeCamp](https://www.youtube.com/watch?v=WGJJIrtnfpk)

### **Docs & Tutorials:**

- [Python Classes — Official Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: Intro to OOP in Python](https://realpython.com/python3-object-oriented-programming/)

### **Practice Ideas:**

- Extend the inventory system to use classes (e.g., `class Product`, `class Inventory`).
- Add update & delete options in your menu.
- Create a `FootballTeam` class that manages multiple players.
- Combine Day 1 & Day 2 by saving goods as object instances instead of dictionaries.

---

## ** Week 5 Recap**

| Day   | Topic                       | Concepts Covered                              | Outcome                                       |
| ----- | --------------------------- | --------------------------------------------- | --------------------------------------------- |
| **1** | Market Seller Inventory     | Lists, Dictionaries, Functions, Loops, Search | Functional inventory app                      |
| **2** | Object-Oriented Programming | Classes, Objects, Attributes, Methods         | OOP basics implemented via `Footballer` class |

---
