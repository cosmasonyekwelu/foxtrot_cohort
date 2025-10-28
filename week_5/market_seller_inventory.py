goods = [
    {"name": "Milk", "price": 500, "category": "Beverages",
        "date_of_arrival": "25-03-2025", "quantity": 12},
    {"name": "Soap", "price": 400, "category": "Toiletries",
        "date_of_arrival": "26-03-2025", "quantity": 10},
    {"name": "Star", "price": 800, "category": "Beer",
        "date_of_arrival": "27-03-2025", "quantity": 8}
]


def add_goods():
    name = input("Enter product name: ").strip()
    category = input("Enter category: ").strip()
    price = float(input("Enter price: "))
    date_of_arrival = input("Enter date of arrival (dd-mm-yyyy): ")
    quantity = int(input("Enter quantity: "))

    goods.append({
        "name": name,
        "price": price,
        "category": category,
        "date_of_arrival": date_of_arrival,
        "quantity": quantity
    })

    print(name + " added successfully!\n")


def display_goods():
    print(f"{"==" * 15}\nMarket Seller Inventory Menu.\n{"==" * 15}")
    for good in goods:
        print("Name:", good["name"],
              "| Price: " + str(good["price"]),
              "| Category:", good["category"],
              "| Date:", good["date_of_arrival"],
              "| Quantity:", good["quantity"])


def calculate_goods():
    total = sum(good["quantity"] for good in goods)
    print("Total number of good in inventory", total)


def search_goods():
    keyword = input("Enter name or category to search: ").strip().lower()
    print(f"{"==" * 10}\nSearch Results\n{"==" * 10}")

    found = False
    for good in goods:
        if keyword in good["name"].lower() or keyword in good["category"].lower():
            print("Name:", good["name"],
                  "| Category:", good["category"],
                  "| Price: ₦" + str(good["price"]),
                  "| Date:", good["date_of_arrival"],
                  "| Quantity:", good["quantity"])
            found = True

    if not found:
        print("No matching goods found.")


def main():
    print(f"{"==" * 12}\nMarket Seller Inventory.\n{"==" * 12}")
    while True:
        print(f"1. Add Goods \n2. View Inventory\n3. Calculate Total Number of Goods \n4. Search by Name or Category \n5. Exit")
        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            add_goods()
        elif choice == "2":
            display_goods()
        elif choice == "3":
            calculate_goods()
        elif choice == "4":
            search_goods()
        elif choice == "5":
            print("Exiting... Goodbye!\n")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.\n")


main()
