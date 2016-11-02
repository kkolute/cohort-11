'''
author : Kennedy kolute
class  : Andela bootcamp 11
'''
class BankAccount(object):
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 500
        self.CreditLine = 500

    def withdraw(self, amount):
        if (self.balance - amount < -self.CreditLine):
            return "Cannot withdraw beyond the current account balance"
        elif (self.balance < amount):
            return "Cannot withdraw beyond the current account balance"
        elif (amount < 0):
            return "Invalid withdraw amount"
        else:
            self.balance -= amount
            return self.balance

    def deposit(self, amount):

        if (amount < 0):
            return "Invalid deposit amount"
        else:
            self.balance += amount
            return self.balance


class CurrentAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if (amount < 0):
            return "Invalid deposit amount"
        else:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        if (self.balance < amount):
            return "Cannot withdraw beyond the current account balance"
        elif (amount < 0):
            return "Invalid withdraw amount"
        else:
            self.balance -= amount
            return self.balance


sa = SavingsAccount()

print(sa.withdraw(5000))
print(sa.balance)
sa.balance = 9
print(sa.balance)
