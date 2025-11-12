from model import Model


class Transfer(Model):
    def __init__(self):
        self.accounts = self.load_a_file("store.json")

    def run(self):
        sender_account = input("What is your account number: ")

        for sender_acc_in_database in self.accounts:
            if int(sender_account) == sender_acc_in_database['account_number']:
                receiver_account = input("Who do you want to send to?: ")

                for receiver_acc_in_database in self.accounts:
                    if int(receiver_account) == receiver_acc_in_database['account_number']:
                        amount = input("How much do you want to transfer?: ")

                        if sender_acc_in_database['account_balance'] < float(amount):
                            print(
                                f"{"==" * 24}\nInsufficient funds.\n{"==" * 24}")
                            return

                        sender_acc_in_database["account_balance"] -= float(
                            amount)
                        receiver_acc_in_database["account_balance"] += float(
                            amount)

                        self.save_a_file(
                            name_of_file="store.json", content=self.accounts)

                        print(
                            f"{"==" * 24}\nYou have transferred {amount} to {receiver_acc_in_database["account_number"]}.\nYour current balance is {sender_acc_in_database["account_balance"]}.\n{"==" * 24}")
                        return
                else:
                    print("No such account number was found.")

        else:
            print("outer: No such account number was found.")
