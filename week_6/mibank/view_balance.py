from model import Model


class ViewBalance(Model):
    def __init__(self):
        self.accounts = self.load_a_file(name_of_file="store.json")

    def run(self):
        account_no = input("What is your account number: ")

        for user in self.accounts:
            if int(account_no) == user['account_number']:
                print(
                    f"{"==" * 24}\nYour account balance is {user['account_balance']}.\n{"==" * 24}")
                break
        else:
            print("No such account number was found.")

