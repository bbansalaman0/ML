print('positin argument')
def attach(a,b):
    c=a+b
    print('total string= '+c)
attach('aman','bansal')
print()
print('keyword argument')
def grocery(item,price):
    print('item= {}'.format(item))
    print('price= %.2f'%price)
grocery(item='apple',price=20.50)
grocery(price=50.9,item='mango')
print()
print()
print('default argument')
def grocery(item,price=90):
    print('item= {}'.format(item))
    print('price= %.2f'%price)
grocery(item='mango',price=20.50)
grocery(item='mango')
print()
print()
print('variable length argument')

def add(fargs,*args):
    print('formal argument= ',fargs)

    sum=0
    for i in args:
        sum+=i
    print('sum of all numbers= ',(fargs+sum))
add(5, 20)
add(5,12,23,34,54,67)
print()
print()
print()
def display(fargs,**kwargs):
    print('formal argument= ',fargs)
    for x,y in kwargs.items():
        print('key={}, value={}'.format(x,y))
display(5,rno=20)
print()
display(5,rno=20,name='aman bansal')

print()
print()
a=2
def myfunction():
    x=globals()['a']
    print(x)
    a=1
    print(a)
    
myfunction()
print(a)
