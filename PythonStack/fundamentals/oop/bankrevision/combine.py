class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(Accname="", interest = 0.02, balance = 0)

    def make_deposit(self, amount, Accname):
        self.account.deposit(amount, Accname)
        return self

    def make_withdraw(self, amount, Accname):
        self.account.withdraw(amount, Accname)
        return self

    def display_user_balance(self):
        # print(f"User: {self.name}, Balance: {self.account_balance}")
        print(f"User: {self.name}")
        self.account.display_account_info()
        return self
    
    def transfer_money(self, User2, amount):
        self.account.balance -= amount
        User2.account.balance += amount
        return self

    # def dodmg(self, name, attack_power, ability_power, speed, health)
    #     self.

class BankAccount:
    bank = "Coding Bank"
    def __init__(self, Accname="", interest = 0.02, balance = 0):
        self.Accname = Accname
        self.interest = interest
        self.balance = balance
        
    def deposit(self, amount, Accname):
        self.balance += amount
        return self
        
    def withdraw(self, amount, Accname):
        if BankAccount.nocashWdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging $5 fee")
            self.balance -= amount
            
        return self
    
    @staticmethod
    def nocashWdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
    
    
    def display_account_info(self):
        print(f"Account: {self.Accname}, Balance: {self.balance}")
        return self
    def yield_interest(self):
        self.balance *= (1+self.interest)
        return self
        
        
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
Tom = User("Tom Sq", "Tom@python.")
        
checking = BankAccount("Checking", 0, 0)
saving = BankAccount("Savings")

# checking.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()
# saving.deposit(1000).deposit(1000).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()



guido.make_deposit(100,checking).make_deposit(100,checking).make_deposit(100,checking).make_withdraw(50, checking).display_user_balance()
monty.make_deposit(50, checking).make_deposit(50, checking).make_withdraw(10, checking).make_withdraw(20, checking).display_user_balance()
Tom.make_deposit(1000, checking).make_withdraw(250, checking).make_withdraw(250, checking).make_withdraw(250, checking).display_user_balance()
# guido.transfer_money(Tom, 100).display_user_balance()
# # guido.display_user_balance()
# Tom.display_user_balance()