import sys
from numpy import *
r1,c1=[int(i) for i in input('enter row and column nos. of matrix 1= ').split(' ')]
r2,c2=[int(i) for i in input('enter row and column nos. of matrix 2= ').split(" ")]
if c1!=r2:
    print('multiplication could not happen')
    exit()
matrix_1=input('enter elements of matrix 1= ')
matrix_2=input('enter elements of matrix 2= ')
x=reshape(matrix(matrix_1),(r1,c1))
y=reshape(matrix(matrix_2),(r2,c2))
print('the product of matrix= ')
z=x*y
print(x,'*',y,'=',x)
