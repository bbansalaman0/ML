x,n=[int(i) for i in input('enter an angle value, no. of iterations(seperated by comma:').split(',')]
print('convert angle(degree) into radian')
r=(x*3.14159)/180
#this becomes the first term
t=r
#till now sum
sum=r
#display iteration and sum
print('iteration=%d\tSum=%f'%(1,sum))
i=2
for j in range(2,n+1):
    t=(-1)*t*r*r/(i*(i+1))
    sum=sum+t
    print('iteration=%d\tSum=%f'%(j,sum))
    i+=2
