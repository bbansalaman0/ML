def towers(n,a,c,b):
    if n==1:
        print('move disk {} from pole {} to pole {}'.format(n,a,c))
    else:
        towers(n-1,a,b,c)
        print('move disk {} from pole {} to pole {}'.format(n,a,c))
        towers(n-1,b,c,a)
n=int(input('enter no. of disks= '))
towers(n,'A','C','B')






  
