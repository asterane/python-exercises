class BankAccount:
    def __init__(self):
        self.balance = 0
        self.account_number = "010100"

    def withdrawal(self, amount):
        pass

    def deposit(self, amount):
        pass

class InterestAccount(BankAccount):
    def __init__(self, rate):
        pass
