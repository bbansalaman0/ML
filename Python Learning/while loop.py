x=1
while x<+10:
    print(x)
    x+=1
print('end')
print()
print()
x=1
while x<+10:
    print(x)
    x+=1
    print('end')
print()
print("enter a range")
x=100
while x>=100 and x<=200:
    print(x)
    x+=5
print('end')
print()
print("find even no. in range")
m,n=[int(i) for i in input("enter minimum and maximum range (seperated by (,):").split(',')]
x=m
if x%2!=0:
    x=x+1
while x>=m and x<=n:
    print(x)
    x+=2
print()
print("find odd no. in range")
m,n=[int(i) for i in input("enter minimum and maximum range (seperated by (,):").split(',')]
x=m
if x%2==0:
    x=x+1
while x>=m and x<=n:
    print(x)
    x+=2

