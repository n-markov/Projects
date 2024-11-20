import locale
locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')

class BalanceException(Exception):
    pass

class BankAccount():
    def __init__(self, initalAmount, acctName):
        print("\n")
        self.balance = initalAmount
        self.name = acctName
        print(f"Account '{self.name}' created. \nBalance = {locale.currency(self.balance, grouping=True)}")

    def getBalance(self):
        return f"Account '{self.name}' has a balance of {locale.currency(self.balance, grouping=True)}\n"
    
    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit of {locale.currency(amount, grouping=True)} complete")
        print(self.getBalance())
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has {locale.currency(self.balance, grouping=True)}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete")
            print(self.getBalance())
        except BalanceException as error:
            print(f"\nWithdrawal interrupted: {error}.")

    def transfer(self, amount, account):
        try:
            print("\n***\nBeginning Transfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete\n***")
        except BalanceException as error:
            print(f"\nTransfer interrupted. {error}")
        
class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("\nDeposit Complete")
        print(self.getBalance())

class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initalAmount, acctName):
        super().__init__(initalAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdrawal Complete.")
            print(self.getBalance())
        except BalanceException as error:
            print(f"Withdrawal interrupted: {error}")  