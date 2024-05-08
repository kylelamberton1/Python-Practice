from account import Account

acct1 = Account('Jose', 100)
print(acct1)
print(acct1.balance)
acct1.deposit(50)
print(acct1.balance)
acct1.withdraw(200)
print(acct1.balance)


