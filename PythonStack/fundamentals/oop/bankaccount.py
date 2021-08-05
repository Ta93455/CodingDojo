class BankAccount:
    bank = "Coding Bank"
    def __init__(self, name, interest = 0.01, balance = 0):
        self.name = name
        self.interest = interest
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds: Charging $5 fee")
            self.balance = self.balance - 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Account: {self.name}, Balance: {self.balance}")
        return self
    def yield_interest(self):
        self.balance *= (1+self.interest)
        return self
        
    @staticmethod
    def nocashWdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
        
    @classmethod
    def getinstance(cls, name):
        cls.bank = name
        
checking = BankAccount('Checking', balance = 100)
saving = BankAccount('Savings', balance=1000)

print(f"Amount: {checking.balance}")
print(f"Amount: {saving.balance}")
checking.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()
saving.deposit(1000).deposit(1000).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()

