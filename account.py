class Account:
    def __init__(self, balance):  # Corrected the constructor
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:  # Checking if the balance is sufficient
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def deposit(self, amount):
        self.balance += amount
