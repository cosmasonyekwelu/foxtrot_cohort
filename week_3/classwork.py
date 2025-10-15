# Title: Expense Tracker Program

# 1. Create a list called expenses. It's going to be a list of dictionary in this format e.g [{"expense": "Transportation", "price": 400}].
expenses = [
    {"expense": "Transportation", "price": 800},
    {"expense": "Food", "price": 850},
    {"expense": "Internet", "price": 900}
]

# 2. create inputs: expense, price.
expense = input("Enter the expense name: ")
price = float(input("Enter the expense price: "))

# 3. Create a dictionary with the keys and values of expense and price.
expense_dict = {"expense": expense, "price": price}

# 4. Write an if else statement. If price is greater than (put your price), update the dictionary with the key "is_over_the_budget", set True and append to expenses.
#    Else add the same type of key "is_over_the_budget", set to False and append to expenses.
budget_limit = 1500

if price > budget_limit:
    expense_dict["is_over_the_budget"] = True
else:
    expense_dict["is_over_the_budget"] = False

expenses.append(expense_dict)

for item in expenses:
    item["is_over_the_budget"] = item["price"] > budget_limit

# 5. Debug at the end to check if your code is working as expected.
print("\n=== Expense Summary ===")
for item in expenses:
    print(f"Expense: {item['expense']}")
    print(f"Price: {item['price']}")
    print(f"Over Budget: {item['is_over_the_budget']}")
    print("-" * 30)

print("Expense added successfully!")
print("All expenses:", expenses)
