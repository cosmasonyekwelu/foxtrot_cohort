from register import Register

class Transfer:
    def __init__(self):
        self.accounts = Register.accounts

    def run(self):
        print("Intra-Transfer")
        sender = input("Enter your account number: ")
        receiver = input("Enter receiver's account number: ")

        if sender not in self.accounts:
            print("Sender account not found.")
            return

        if receiver not in self.accounts:
            print("Receiver account not found.")
            return

        try:
            amount = float(input("Enter amount to transfer: "))
        except ValueError:
            print("Invalid amount.")
            return


        if self.accounts[sender]["balance"] < amount:
            print("Insufficient funds.")
            return

        self.accounts[sender]["balance"] -= amount
        self.accounts[receiver]["balance"] += amount

        print(f"Transfer successful. {amount}  to {receiver}.")
