# `get_funds()` Return account balance
# `deposit(amount)` Deposit to the account
# `check_withdrawal(amount)` Return `True` if large enough balance for a withdrawal
# `withdraw(amount)` Withdraw an allowed amount; raise a `ValueError` if insufficent balance
# `calc_interest()` Calculate and return interest on the current account balance

class Account():
    def __init__(self, balance, account_type):
        self.balance = balance
        self.account_type = account_type

    def get_funds(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance - amount <= 0:
            raise ValueError
        else:
            self.balance -= amount
            return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def check_withdraw(self, amount):
        if self.balance - amount <= 0:
            return False
        else:
            return True

    def get_standing(self):
        if self.balance >= 1000:
            return True
        else:
            return False

    def from_csv_string(record):
        record = record.split(',')
        return Account(float(record[1]), record[2])
