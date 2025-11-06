from model import Model


class Deposit(Model):
    def __init__(self):
        self.accounts = self.load_a_file(name_of_file="store.json")

    def run(self):
        account_no = input("What is your account number: ")

        for user in self.accounts:
            if int(account_no) == user['account_number']:
                amount = input("How much do you want to deposit?: ")
                user['account_balance'] += float(amount)
                self.save_a_file(name_of_file="store.json",
                                 content=self.accounts)
                print(
                    f"{"==" * 24}\n{amount} has been added to your account.\n{"==" * 24}")
                break
        else:
            print("No such account number was found.")
