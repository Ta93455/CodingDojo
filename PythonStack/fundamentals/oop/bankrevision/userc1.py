class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(Accname='', interest = 0.02, balance = 0)

    def make_deposit(self):
        self.account.deposit(100)
        return self

    def make_withdraw(self):
        self.account.withdraw(100)
        return self

    def display_user_balance(self):
        # print(f"User: {self.name}, Balance: {self.account_balance}")
        print(f"User: {self.name}, Balance: {self.account.display_account_info}")
        return self
    
    def transfer_money(self, User2, amount):
        self.account_balance -= amount
        User2.account_balance += amount
        return self
        

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
Tom = User("Tom Sq", "Tom@python.")



guido.make_deposit(100).make_deposit(100).make_deposit(100).make_withdraw(50).display_user_balance()
monty.make_deposit(50).make_deposit(50).make_withdraw(10).make_withdraw(20).display_user_balance()
Tom.make_deposit(1000).make_withdraw(250).make_withdraw(250).make_withdraw(250).display_user_balance()
guido.transfer_money(Tom, 100).display_user_balance()
# guido.display_user_balance()
Tom.display_user_balance()