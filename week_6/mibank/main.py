from register import Register
from deposit import Deposit
from withdraw import Withdraw
from view_balance import ViewBalance
from transfer import Transfer


class Main:
    def __init__(self, name, founded):
        self.name = name
        self.founded = founded

        # Composition
        self.register = Register()
        self.deposit = Deposit()
        self.withdraw = Withdraw()
        self.view_balance = ViewBalance()
        self.transfer = Transfer()

    def run(self):
        print(
            f"{"~~" * 24}\nWelcome to {self.name}. What do you want to do today?\n{"~~" * 24}")
        while True:
            options = input(
                "1. Create an account.\n2. Deposit money\n3. Withdraw money. \n4. View balance.\n5. Exit.\nChoose(1|2|3|4|5|6):")

            match options:
                case "1":
                    self.register.run()
                case "2":
                    self.deposit.run()
                case "3":
                    self.withdraw.run()
                case "4":
                    self.view_balance.run()
                case "5":
                    self.transfer.run()
                case "6":
                    break
                case _:
                    print("Wrong option. Choose between 1 to 6.")


main = Main(name="Mibank", founded=2025)
main.run()
