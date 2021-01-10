print("exp=1")
x=int(input("enter a element= "))
while x>=1 and x<=20:
    print('x= ',2**x)
    x+=1
print('out of loop')
print()
print()
print('exp=2')
x=int(input("enter a element= "))
while x>=1:
    print('x= ',x)
    x-=1
    if x==5:
        break
print('out of loop')
print()
print()
print('exp=3')
x=int(input("enter a element= "))
while x>=1 and x<=20:
    print('x= ',2**x)
    x+=1
    if x==20:
        break
print('out of loop')
print()
