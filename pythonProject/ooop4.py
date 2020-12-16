import sys
class Bank:

    def __init__(self, name='', balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self, amount):
        if amount> self.balance:
            print("Insufficient balance, can't withdraw")
        else:
            self.balance-=amount
        return self.balance

name=input('Enter Account holder name:')

b=Bank(name)

while True:
    print('d--Deposit  w--Withdraw  e--Exit')

    choice=input('Enter your choice:')

    if choice=='e' or choice=='E':
        sys.exit()

    amt=float(input('Enter amount= '))

    if choice=='d' or choice=='D':
        print(f'Your balance after deposit is: {b.deposit(amt)}')
    elif choice=='w' or choice=='W':
        print(f'Your balance after withdrawl is: {b.withdraw(amt)}')


