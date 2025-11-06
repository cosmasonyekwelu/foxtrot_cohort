from model import Model



class ViewBalance(Model):
    def __init__(self):
        self.accounts = self.load_a_file(name_of_file="store.json")
        
    def run(self):
        print("Balance")