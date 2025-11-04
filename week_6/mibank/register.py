import random
from model import Model


class Register(Model):
    def __init__(self):
        self.accounts = []

    def run(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        account_no = random.randint(1000000000, 9999999999)

        user = {"name": name, "email": email,
                "account_number": account_no, "account_balance": 0}
        self.accounts.append(user)

        self.create_a_file(name_of_file="store.json", content=self.accounts)

        print(f"{"==" * 24}\nAccount created successfully! Your account number is {account_no}\n{"==" * 24}")
