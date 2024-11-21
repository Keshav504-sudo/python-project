from bank_accounts import *

dave = bankaccounts(1000, "dave")
sara = bankaccounts(2000,"sara")

dave.getbalance()
sara.getbalance()

sara.deposit(500)
#dave.withdraw(10000)
dave.withdraw(10)

#dave.transfer(1000,sara)
#dave.transfer(100,sara)
#jim = Intrestrewardsacct(1000, "jim")
#jim.getbalance()
#jim.deposit(100)
#jim.transfer(100,dave)
blaze = savingsacct(1000,"blaze")
