# ======== WEEK 3 SUMMARY: CONTROL STRUCTURES ========

"""
This week, I learned about:
Conditional Statements (if, elif, else)
Loops (while, for)
List Operations (append, remove)
Building interactive programs (Supermarket & Expense Tracker)
"""

# --- CONDITIONAL STATEMENTS ---
# Control the flow of your program by checking conditions.

destination_fee = 1000
transport_fee = 1900
train = "unavailable"

if transport_fee <= destination_fee and train == "available":
    print("Getting to destination Successful.")
elif transport_fee <= destination_fee and train != "available":
    print("Train Not Available.")
else:
    print("Getting to destination Unsuccessful.")


# --- LOOPS ---
# 1. While Loop: Runs repeatedly while a condition is True.
print("\n--- WHILE LOOP EXAMPLE ---")
num = 0
while num < 5:
    print("Number:", num)
    num += 1

# 2. For Loop: Used to iterate over a list or range.
print("\n--- FOR LOOP EXAMPLE ---")
people = ["John", "Peter", "Ade", "Oluadamilare", "King"]
for person in people:
    print("Hello", person)

# 3. Search Example (with break and else)
searched_name = "Peter"
for person in people:
    if person == searched_name:
        print("Found: {person}")
        break
else:
    print("Person not found.")


# --- LIST APPENDING EXAMPLES ---
print("\n--- APPENDING NUMBERS ---")
first_num = [1, 2, 3, 4, 5]
second_num = [6, 7, 8, 9, 10]

for num in second_num:
    first_num.append(num)
print("Combined List:", first_num)

# Doubling values
numbers = [1, 2, 3, 4, 5]
updated = []
for num in numbers:
    updated.append(num * 2)
print("Updated Numbers:", updated)

# Generating email list
print("\n--- EMAIL GENERATION ---")
email_users = []
for person in people:
    email_users.append(person + "@mail.com")
print("Email Users:", email_users)


# --- CASE-INSENSITIVE NAME DELETION ---
print("\n--- DELETE NAME EXAMPLE ---")
people = ["John", "Peter", "Ade", "Oluadamilare", "King"]
name = "john"
for person in people:
    if name.lower() == person.lower():
        people.remove(person)
        print(f"{person} Deleted.")
        break
else:
    print("The person is not found.")
print("Updated List:", people)


# --- COURSE ENROLLMENT PROGRAM ---
print("\n--- COURSE ENROLLMENT ---")
ui_ux_design = []
frontend_development = []
backend_development = []

name = "Cosmas"
course = "2"  # Pretend user chose 2

if course == "1":
    ui_ux_design.append(name)
elif course == "2":
    frontend_development.append(name)
elif course == "3":
    backend_development.append(name)
else:
    print("Invalid choice. Choose between 1, 2 or 3.")

print("UI/UX:", ui_ux_design)
print("Frontend:", frontend_development)
print("Backend:", backend_development)


# --- SUPERMARKET MINI PROJECT ---
print("\n--- MOKU SUPERMARKET ---")
items = ["Fanta", "Bread", "Milk", "Pillow", "Pan"]
sales = [{"name": "King", "item": "Bread"}, {"name": "Peter", "item": "Milk"}]

user_name = "David"
user_item = "Fanta"
if user_item in items:
    option = "Y"
    if option.upper() == "Y":
        sales.append({"name": user_name, "item": user_item})
        print("Purchase Successful")
    elif option.upper() == "N":
        print("Purchase Cancelled")
    else:
        print("Invalid Option")
else:
    print("Sorry, item not available")

print("Sales Record:", sales)


# --- EXPENSE TRACKER MINI PROJECT ---
print("\n--- EXPENSE TRACKER ---")

expenses = [
    {"expense": "Transportation", "price": 800},
    {"expense": "Food", "price": 850},
    {"expense": "Internet", "price": 900}
]

budget_limit = 1500

# Add a new expense
expense = "Electricity"
price = 1200
expense_dict = {"expense": expense, "price": price}

# Check budget
expense_dict["is_over_the_budget"] = price > budget_limit
expenses.append(expense_dict)

# Update all entries
for item in expenses:
    item["is_over_the_budget"] = item["price"] > budget_limit

# Print summary
print("\n=== Expense Summary ===")
for item in expenses:
    print(f"Expense: {item['expense']}")
    print(f"Price: {item['price']}")
    print(f"Over Budget: {item['is_over_the_budget']}")
    print("-" * 30)

print("Expense Tracker Completed Successfully!")
