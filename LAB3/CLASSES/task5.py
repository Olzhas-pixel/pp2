class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")

# Example Usage:
acc = Account("Olzhas", 100)
acc.deposit(50)  # Output: Deposited: 50, New Balance: 150
acc.withdraw(30)  # Output: Withdrew: 30, New Balance: 120
acc.withdraw(200)  # Output: Insufficient funds
