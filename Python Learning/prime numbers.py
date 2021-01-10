print('print prime numbers')
x=int(input('Enter upto what number we need prime number= '))
for num in range(2,x+1):
    for i in range(2,num):
        if (num%i==0):#not a prime number.
            break
    else: #print prime number
        print(num)
if x<2: print("wrong input")  
