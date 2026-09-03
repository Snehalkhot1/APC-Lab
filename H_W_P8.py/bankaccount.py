# BankAccount Class

class BankAccount:

    # Class-level counter for unique account numbers
    account_counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(amount, "deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    # Display balance
    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)

    # Transfer money
    def transfer(self, amount, other_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(amount, "transferred successfully.")
        else:
            print("Insufficient balance or invalid amount.")


# Main program

# Creating two BankAccount objects
account1 = BankAccount("Snehal")
account2 = BankAccount("Rahul")

# Display initial balances
print("----- Initial Balances -----")
account1.display_balance()
account2.display_balance()

# Deposits
print("\n----- Deposits -----")
account1.deposit(5000)
account2.deposit(3000)

# Display balances
account1.display_balance()
account2.display_balance()

# Withdrawal
print("\n----- Withdrawal -----")
account1.withdraw(1000)

# Transfer
print("\n----- Transfer -----")
account1.transfer(2000, account2)

# Final balances
print("\n----- Final Balances -----")
account1.display_balance()
account2.display_balance()