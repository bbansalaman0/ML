print('\nSingle Inheritance')

class Bank:
    cash=100000000

    @classmethod
    def available_cash(cls):
        print(cls.cash)


class Pnb(Bank):
    pass

class Sbi(Bank):
    cash=2000000000
    @classmethod
    def available_cash(cls):
        print(cls.cash + Bank.cash)

a=Pnb()
print('cash in Pnb= ',end='')
a.available_cash()

b=Sbi
print('cash in Sbi= ', end='')
b.available_cash()
print('\n\n')




print('Multiple Inheritance')

class A:
    def __init__(self):
        self.a="a"
        print(self.a)
        super(A, self).__init__()

class B:
    def __init__(self):
        self.b='b'
        print(self.b)
        super(B, self).__init__()
class C(A,B):
    def __init__(self):
        self.c='c'
        print(self.c)
        super(C, self).__init__()

o=C()






