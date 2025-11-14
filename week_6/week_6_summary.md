# Week 6 Summary

This week focused on learning Python fundamentals through practical, real-world examples. Below is a structured summary of everything covered:

---

## 1. **JSON Handling in Python**
- Converting JSON strings to Python dictionaries using `json.loads()`.
- Writing Python objects to JSON files using `json.dumps()`.
- Reading JSON content back into Python.

**Example learned:**
```python
import json
x = {"name": "Alice", "age": 30, "city": "New York"}
with open("store.json", "w") as store:
    store.write(json.dumps(x))
```

---

## 2. **File Handling**
I learned the different file modes in Python:

| Mode | Meaning |
|------|---------|
| `r` | Read (default) |
| `a` | Append |
| `w` | Write |
| `x` | Exclusive Create |
| `t` | Text mode (default) |
| `b` | Binary mode |

I practiced opening, reading, and writing files.

---

## 3. **Object-Oriented Programming (OOP)**
I explored:
- Instance methods
- Class methods
- Static methods
- The concept of composition in OOP

**Composition Example:**
```python
class A:
    def __init__(self):
        self.name = "This is class A"

class B:
    def __init__(self):
        self.name = "This is class B"
        self.a = A()  # B contains A
```

---

## 4. **Decorators**
I learned the concept of decorators and how they wrap function behavior.

Example learned:
```python
def decor(func):
    def wrapper():
        print("Check if logged in")
        func()
    return wrapper
```

---

## 5. **Building a Mini Banking System (Project)**
This was the biggest part of the week. We created a **full banking application using Python OOP and JSON as storage**.

### **Project Architecture**
The project followed a modular structure:

- `Main` — central app controller
- `Model` — handles file I/O (save & load JSON)
- `Register` — creates bank accounts
- `Deposit` — deposit money
- `Withdraw` — withdraw money
- `Transfer` — send money between accounts
- `ViewBalance` — check account balance

All account data is stored inside **store.json**.

---

## 6. **Model Class for Reusable File Handling**
```python
class Model:
    @staticmethod
    def save_a_file(name_of_file, content):
        with open(name_of_file, "w") as store:
            store.write(json.dumps(content))

    @staticmethod
    def load_a_file(name_of_file):
        with open(name_of_file) as store:
            return json.loads(store.read())
```

This allowed every feature (Deposit, Register, Transfer, etc.) to share the same storage logic.

---

## 7. **Account Registration**
- Auto-generates a 10-digit account number
- Saves users to JSON

```python
user = {"name": name, "email": email,
        "account_number": account_no, "account_balance": 0}
```

---

## 8. **Deposit Feature**
- Searches for user by account number
- Updates account balance
- Saves new state to JSON

---

## 9. **Withdraw Feature**
- Checks insufficient funds
- Subtracts from balance
- Saves updated store

---

## 10. **Transfer Feature**
- Finds both sender and receiver
- Validates balance
- Deducts and adds accordingly
- Saves new balances to file

---

## 11. **View Balance Feature**
Simple account number lookup that prints the current balance.

---

## 12. **Main Menu Controller**
Runs an interactive prompt:
```
1. Create account
2. Deposit
3. Withdraw
4. View balance
5. Transfer
6. Exit
```
Uses Python's `match-case` for clean logic.

---

# **Conclusion**
Week 6 was about understanding Python deeper through **files, JSON, OOP, decorators, and a complete mini banking system**. I practiced:
- Clean project structure
- Real-world logic
- Reusable models
- Input validation and file persistence

This week significantly strengthened my backend development skills in Python.

---

