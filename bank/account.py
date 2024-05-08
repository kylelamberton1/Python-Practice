class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        return self.balance

    def withdraw(self, withdraw):
        self.balance -= withdraw
        if self.balance >= 0:
            return self.balance
        else:
            print ("Sorry, you do not have the funds to make the withdrawal")




