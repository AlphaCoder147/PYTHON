class BA:
    def __init__(self, owner, Balance):
        self.owner=owner
        self.Balance=Balance
        
    def deposit(self,amt):
        self.amt=amt
        self.Balance+=self.amt
        print("Your new balance is",self.Balance)
        
    def Withdraw(self,amt):
        self.amt=amt
        if self.amt > self.Balance:
            print("Insufficient Funds.")
        else:
            self.Balance-=self.amt
            print(self.amt,"Withdrawn.")
            print("New Balance is", self.Balance)
a=BA("Kapoor",15000)
b=input("Enter the operation you wish to perform. W/D:  ")
if b=="D":
    amount=float(input("Enter Amount to be Deposited: "))
    a.deposit(amount)
elif b=="W":
    amount=float(input("Enter Amount to be Withdrawn: "))
    a.Withdraw(amount)
else:
    print("Invalid Input")
                        