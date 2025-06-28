# This module defines a simple BankAccount class that allows for deposits, withdrawals, and balance inquiries.
# It can be used in a command-line interface or imported into other Python scripts.
class BankAccount:
    def __init__(self, initial_balance=0):
        """Initializes the bank account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """Withdraws the specified amount from the account if sufficient funds are available."""
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be greater than zero.")
            return False

    def display_balance(self):
        """Prints the current account balance."""
        current_balance = self.account_balance
        if current_balance < 0:
            print("Warning: Your account is overdrawn!")
        print(f"Current balance: ${current_balance}")
