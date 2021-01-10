def factorial(n):
    fac=1
    while n>=1:
        fac=fac*n
        n-=1
    return fac
for i in range(1,15):
    print('factorial of {} is {}'.format(i,factorial(i)))
print()
print()
print('\n')



def factorial(n):
    if n==1:result=1
    else: result=n*factorial(n-1)
    return result
for i in range(1,15):
    print('factorial of {} is {}'.format(i,factorial(i)))
