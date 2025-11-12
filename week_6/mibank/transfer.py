from model import Model


class Transfer(Model):
    def __init__(self):
        self.accounts = self.load_a_file(name_of_file="store.json")

    def run(self):
        print("Intra-MiBank Transfer")
        sender = input("enter your account number: ")
        receiver = input("enter receiver account number: ")

        sender_found = False
        receiver_found = False

        for user in self.accounts:
            if int(sender.strip()) == user['account_number']:
                sender_user = user
                sender_found = True
            if int(receiver.strip()) == user['account_number']:
                receiver_user = user
                receiver_found = True

        if not sender_found:
            print(f"{'==' * 24}\nSender account not found.\n{'==' * 24}")
            return

        if not receiver_found:
            print(f"{'==' * 24}\nReceiver account not found.\n{'==' * 24}")
            return

        amount = input("Enter amount to transfer: ")

        if sender_user['account_balance'] < float(amount):
            print(f"{'==' * 24}\nInsufficient funds.\n{'==' * 24}")
            return

        sender_user['account_balance'] -= float(amount)
        receiver_user['account_balance'] += float(amount)

        self.save_a_file(name_of_file="store.json", content=self.accounts)

        print(
            f"{'==' * 24}\n{amount} has been transferred from {sender} to {receiver}.\n{'==' * 24}")
