# Bank Account System

class BankAccount:
    def __init__(self, name, balance):
        # Store account holder name and balance
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        # Add money to the account
        self.balance = self.balance + amount
        print("Amount Deposited Successfully")

    def withdraw(self, amount):
        # Withdraw money if balance is sufficient
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        # Display current balance
        print("Current Balance:", self.balance)

    def display(self):
        # Display account details
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


acc1 = BankAccount("Sawan", 1000)

acc1.deposit(500)
acc1.withdraw(200)
acc1.check_balance()
acc1.display()
