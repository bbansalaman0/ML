def prime(num):
    x=1 ##if prime
    for i in range(2,num):
        if num%i==0:
            
            x=0 # if not prime
            break
        
        else:x=1
    return x
num=int(input('enter a number= '))
result=prime(num)
if result==1:
    print(num,'is a prime')
else:print('not a prime')
print()
print()

def prime(n):
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:x=1
    return x
n=int(input('enter a number= '))
i=2
c=1
while True:
    if prime(i):
        print(i)
        c+=1
    i+=1
    if c>n:break
    
    
