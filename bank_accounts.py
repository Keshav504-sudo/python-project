class balanceexception(Exception):
    pass

class bankaccounts:
    def __init__(self, initialamount, acctname):
        self.balance = initialamount
        self.name = acctname
        print(f"\n Account '{self.name}' created.\nbalance = ${self.balance:.2f}")
    
    def getbalance(self):
        print(f"\n Account '{self.name}' balance = ${self.balance:.2f}")
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n DEPOSIT COMPLETE.")
        self.getbalance()

    def viabletransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise balanceexception(f"\nsorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
    
    def withdraw(self, amount):
        try: 
            self.viabletransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getbalance()
        except balanceexception as error:
            print(f"\nwithdraw intrrupted: {error}")

    def transfer(self, amount, account):
        try:
            print('\n**********\n\n Begining transfer... 🚀')
            self.viabletransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete!\n\n**********')
        except balanceexception as error:
            print(f'\nTransfer intrrupted.{error}')

class Intrestrewardsacct(bankaccounts):
    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print("\ndeposit complete.")
        self.getbalance()

class savingsacct(Intrestrewardsacct):
    def __init__(self, initialamount, acctname):
        super().__init__(initialamount,acctname)
        self.fee = 5
    def withdraw(self, amount):
        try:
            self.viabletransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n Withdraw completed.")
            self.getbalance()
        except balanceexception as error:
            print(f"\nWithdraw interrupted: {error}")