class BankAccount:
    account_number = 1001

    def __init__(self, holder):
        self.holder = holder
        self.balance = 0
        self.acc_no = BankAccount.account_number
        BankAccount.account_number += 1

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("\nAccount Number:", self.acc_no)
        print("Account Holder:", self.holder)
        print("Balance:", self.balance)

    def transfer(self, other, amount):
        if amount <= self.balance:
            self.balance -= amount
            other.balance += amount
            print("Transfer Successful")
        else:
            print("Insufficient Balance")


acc1 = BankAccount("Sneha")
acc2 = BankAccount("Rahul")

acc1.deposit(5000)
acc1.withdraw(1000)
acc1.transfer(acc2, 2000)

print("\nAccount 1")
acc1.display()

print("\nAccount 2")
acc2.display()