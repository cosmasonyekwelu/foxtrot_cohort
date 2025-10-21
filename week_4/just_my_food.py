import time
foods = [
    {"name": "Yam", "price": "1000"},
    {"name": "Rice and beans", "price": "1500"},
    {"name": "spagetti", "price": "1200"},
    {"name": "Fufu", "price": "2500"},
]


def display_food():
    print("Just My Food Menu")
    for food in foods:
        print(f"Name: {food['name']}, Price: {food['price']}")
        time.sleep(1)


def search_for_food(Searched_food):
    for food in foods:
        if food["name"].lower().replace(" ", "") == Searched_food.lower().replace(" ", ""):
            return food
    else:
        return False


def main():
    bill = 0
    while True:
        display_food()
        options = input("What do you want to buy \n Write the name of food: ")

        is_food = search_for_food(options)

        if type(is_food) == dict:
            purchase = input(
                f"The price of this food is {is_food["price"]}. Do you want to buy it (y/n):")

            if purchase == "y":
                bill = bill + float(is_food["price"])

                option_two = input(
                    f"Your bill is {bill}. Do you want to buy more? (y/n)")

                if option_two == "y":
                    continue
                else:
                    print(f"Thank You for your purchased. Total Bill :{bill}")
                    break
        else:
            print("Sorry we don't have the requested food.")
            time.sleep(3)


main()
