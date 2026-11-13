class Bank:
    def __init__(self,acc_no,name,type,bal):
        self.acc_no=acc_no
        self.name=name
        self.type=type
        self.bal=bal
    def deposit(self,amt):
        if amt<=0:
            print("It should be an positive number")
        else:
            self.bal+=amt
            print("Your current balance is",self.bal)
    def withdraw(self,amt):
        if amt<=0:
            print("It should be an positive number")
        elif amt>self.bal:
            print("Insufficient balance")
        else:
            self.bal-=amt
            print("Your current balance is",self.bal)
    def display(self):
        print(f"Sccount number:{self.acc_no}")
        print(f"Account holder:{self.name}")
        print(f"Account type:{self.type}")
        print(f"Current balance:{self.bal}")

no=int(input("Enter the account number:"))
name=input("Enter your name:")
type=input("Enter the account type:")
bal=int(input("Enter your balance:"))
usrl=Bank(no,name,type,bal)
while True:
    print("\n1)DEPOSIT\n2)WITHDRAW\n3)ACCOUNT INFORMATION\n4)EXIT\n")
    opt=int(input("Enter the option:"))
    if opt==1:
        amt=int(input("Enter your amount:"))
        usrl.deposit(amt)
    elif opt==2:
        amt=int(input("Enter your withdrawal amount:"))
        usrl.withdraw(amt)
    elif opt==3:
        usrl.display()
    elif opt==4:
        exit(0)
    else:
        print("Invalid option")