#kata
#https://www.codewars.com/kata/5a03af9606d5b65ff7000009/train/python

class User:
    def __init__(self, name: str, balance: int, checking_account: bool):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    def withdraw(self, amount: int) -> str:
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative")
        if amount > self.balance:
            raise ValueError(f"{self.name} has insufficient funds: only {self.balance}")
        self.balance -= amount
        return f"{self.name} has {self.balance}."
    def add_cash(self, amount):
        self.balance += amount
        return f"{self.name} has {self.balance}."
    def check(self, issuer, amount):
        if not issuer.checking_account:
            raise ValueError(f"{issuer.name} does not have a checking account")
        if amount > issuer.balance:
            raise ValueError(f"{issuer.name} has insufficient funds to issue a check")
        issuer.balance -= amount
        self.balance += amount
        return f"{self.name} has {self.balance} and {issuer.name} has {issuer.balance}."
        























class User:
    
    def __init__(self, name: str, balance: int, checking_account: bool):
        # the account holder's name
        self.name = name
        # the initial balance
        self.balance = balance
        # whether this user can issue checks to others
        self.checking_account = checking_account
    
    def withdraw(self, amount):
        """Withdraw `amount` from this account, if balance is sufficient"""
        try:
            if amount<self.balance:
                self.balance-=amount
                return f"{self.name} has {self.balance}."
        except ValueError:
            pass
    
    def add_cash(self, amount):
        """Deposit `amount` into this account"""
        self.balance+=amount
        return f"{self.name} has {self.balance}."
        pass  # implement me
    
    def check(self, issuer, amount):
        """Receive a check from `issuer` over `amount`, if possible
        
        `issuer` is the User issuing the check, i.e. the account the `amount` will be taken from
        `self` is the User receiving the check, i.e. the account the `amount` will be added to
        """
        try:
            
            issuer.checking_account==True
        except ValueError:
            print("checkingamountfalse")
                
        try:
            if issuer.balance>amount:
                issuer.balance-=amount
                self.balance+=amount
                return f"{self.name} has {self.balance} and {issuer.name} has {issuer.balance}."
            
        except ValueError:
            print("insufficiantamount")
         # implement me