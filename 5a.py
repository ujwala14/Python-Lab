'''Write a python program to simulate saving account processing in a
bank using constructors. Create Deposit and Withdraw with other member
functions and Check for Validation while withdrawing the amount and
depositing the amount by defining appropriate user defined exceptions.'''

class not_valid(Exception):
    def __init__(self,a):
        Exception.__init__(self)
        print("u are trying to withdraw Rs. ",a)
        print("u dont have that much!")

class sav_acc:
    def __init__(self,ano,nm,start_amt=0):
        self.acc_no=ano
        self.name=nm
        self.amt=start_amt
    def deposit(self,a):
        self.amt+=a
        print("Rs.",a,"deposited")
    def withdraw(self,a):
        if a>self.amt:
            raise not_valid(a)
        else:
            self.amt-=a
            print("Rs.",a,"withdrawn")
    def disp(self):
        print("-"*10 + " account statement " + '-'*10)
        print(self.acc_no," : ",self.name)
        print("Balance : Rs " ,self.amt)
        print("-"*40)

x,y,z=input("Enter acc_no,name & start amt: ").split()
p1=sav_acc(int(x),y,int(z))
while 1:
    try:
        print("\n1:deposit\t2:withdraw\t3:exit")
        n=int(input("Enter choice: "))
        if n==1:
            a=int(input("Enter amt to deposit: "))
            p1.deposit(a)
        elif n==2:
            a=int(input("Enter amt to withdraw: "))
            p1.withdraw(a)
        else:
            exit()
        p1.disp()
    except not_valid:
        print('invalid!')
