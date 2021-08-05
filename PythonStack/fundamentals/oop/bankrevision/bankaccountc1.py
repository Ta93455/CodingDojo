class BankAccount:
    bank = "Coding Bank"
    def __init__(self, Accname, interest = 0.02, balance = 0):
        self.Accname = Accname
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
        print(f"Account: {self.Accname}, Balance: {self.balance}")
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
        
        
checking = BankAccount('Checking', balance = 100)
saving = BankAccount('Savings', balance=1000)

print(f"Amount: {checking.balance}")
print(f"Amount: {saving.balance}")
checking.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()
saving.deposit(1000).deposit(1000).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()

