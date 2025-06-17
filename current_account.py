from account import Account

class CurrentAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        super().withdraw(amount)  # Calling the base class method to handle withdrawal

    def deposit(self, amount):
        super().deposit(amount)  # Calling the base class method to handle deposit
