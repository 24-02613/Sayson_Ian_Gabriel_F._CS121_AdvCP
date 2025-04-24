from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, acc_number, balance):
        self._acc_number = acc_number
        self._balance = balance

    @property
    def account_number(self):
        return self._acc_number

    @property
    def balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = new_balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_account_type(self):
        pass

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.balance + amount)

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.set_balance(self.balance - amount)
        else:
            print("Not enough balance for withdrawal in Savings Account.")

    def display_account_type(self):
        return "Savings Account"

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.balance + amount)

    def withdraw(self, amount):
        if self.balance - amount >= -5000:
            self.set_balance(self.balance - amount)
        else:
            print("Overdraft limit reached in Current Account.")

    def display_account_type(self):
        return "Current Account"

def print_account_details(account):
    print("Account Number:", account.account_number)
    print("Balance:", account.balance)
    print("Account Type:", account.display_account_type())
    print()

s1 = SavingsAccount("SA123", 1000)
s2 = SavingsAccount("SA124", 500)

c1 = CurrentAccount("CA456", 0)
c2 = CurrentAccount("CA457", 100)

s1.deposit(200)
s1.withdraw(100)
s2.withdraw(100)  

c1.withdraw(200)  
c2.withdraw(1000)  

print_account_details(s1)
print_account_details(s2)
print_account_details(c1)
print_account_details(c2)        
