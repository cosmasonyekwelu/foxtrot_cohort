import random
from model import Model


class Register(Model):
    def __init__(self):
        self.accounts = self.load_a_file(name_of_file="store.json")

    def run(self):
        name = input("What is your name: ")
        email = input("What is your email address: ")

        # Generate account nummber
        account_no = random.randint(1000000000, 9999999999)

        user = {"name": name, "email": email,
                "account_number": account_no, "account_balance": 0}
        self.accounts.append(user)

        self.save_a_file(name_of_file="store.json", content=self.accounts)

        print(
            f"{"==" * 24}\nYour account is created.\nYour account number is {account_no}\n{"==" * 24}")
