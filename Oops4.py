class Account:
    def __init__(self,title=None,account_balance=0):

        self.title = title
        self.account_balace = account_balance

class SavingsAccount(Account):
    def __init__(self,title = None,account_balance = 0,interest_rate=0):
        super().__init__(title,account_balance)
        self.interest_rate=interest_rate

account = SavingsAccount('Shailesh',5000,5)
print(account.title)
print(account.account_balace)
print(account.interest_rate)



