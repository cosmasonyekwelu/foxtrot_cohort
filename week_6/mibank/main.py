

class Main:
    def __init__(self, name, founded):
        self.name = name
        self.founded = founded

    def run(self):
        print(
            f"{'~' * 24}\n Welcome to {self.name} (Founded {self.founded})\n{'~' * 24}")

        while True:
            option = input(
                "1. Create an Account\n2. Withdraw Money\n3. View Balance\n4. Exit\nChoose an option (1-4): ")

            match option:
                case "1":
                    print("Account creation selected.")
                case "2":
                    print("Withdrawal option selected.")
                case "3":
                    print("Viewing balance...")
                case "4":
                    print("Exiting... Thank you for banking with us!")
                    break
                case _:
                    print("Invalid option. Please choose a number between 1 and 4.")


main = Main("MiBank", 2025)
main.run()
