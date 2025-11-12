# Title: Expense Tracker Program

# 1. Create a list called expenses. It's going to be a list of dictionary in this format e.g [{"expense": "Transportation", "price": 400}].
expenses = [
    {"expense": "Transportation", "price": 800},
    {"expense": "Food", "price": 850},
    {"expense": "Internet", "price": 900}
]

# 2. create inputs: expense, price
# 3. Create a dictionary with the keys and values of expense and price.

while True:
    expense_name = input("Enter the expense name: ")
    expense_price = float(input("Enter the expense price: "))

    new_expense = {"expense": expense_name, "price": expense_price}
# 4. Write an if else statement. If price is greater than (put your price), update the dictionary with the key "is_over_the_budget", set True and append to expenses.
#    Else add the same type of key "is_over_the_budget", set to False and append to expenses.
    budget_limit = 600

    if expense_price > budget_limit:
        new_expense["is_over_the_budget"] = True
    else:
        new_expense["is_over_the_budget"] = False

    expenses.append(new_expense)

# 5. Debug at the end to check if your code is working as expected.
    print(f"{expense_name} has been added")

    option = input("Do you want to continue? (Choose y/n)")

    if option == "y":
        continue
    if option == "n":
        for item in expenses:
            print(f"Expense: {item["expense"]},Price:{expense_price}")
        break
    else:
        print("Invalid Option")
