from numpy import *
arr1=array([1,2,3,4,5,6,7,8,9])
print(arr1)
print()
arr2=array([2,
            3,
            4,
            5])
print(arr2)
print()
arr3=array([[1,2,3,4,5,6],
           [7,8,9,0,1,2.1],dtype(int)])
print(arr3)
print()
arr4=array([[[1,2,3],[4,5,6]],
            [[7,8,9],[1.0,1.1,1.2]]])
print(arr4)
print()
print('ndim')
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)
print('shape')
print(arr1.shape)
print(arr2.shape)
print(arr3.shape)
print(arr4.shape)
print('size')
print(arr1.size)
print(arr2.size)
print(arr3.size)
print(arr4.size)
print('itemsize')
print(arr1.itemsize)
print(arr2.itemsize)
print(arr3.itemsize)
print(arr4.itemsize)
print('dtype')
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)
print('nbytes')
print(arr1.nbytes)
print(arr2.nbytes)
print(arr3.nbytes)
print(arr4.nbytes)
print('reshape')
arr5=arange(10)
print(arr5.reshape(5,2))
print(arr5.reshape(2,5))

print('flatten')
arr6=array([[arange(4)],[arange(4,8)]])
print(arr6)
print(arr6.flatten())
print('zeros matrix')
a=zeros((2,4),int)
print(a)
a=zeros((2,4),float)
print(a)
a=zeros((2,4),complex)
print(a)
print('ones matrix')
b=ones((3,6),int)
print(b)
b=ones((3,6),float)
print(b)
b=ones((3,6),complex)
print(b)
print('eye function')
print(eye(4,dtype=int))
print(eye(5,dtype=float))
print(eye(2,dtype=complex))  
c=arange(12)
print(c.reshape(4,3))
print()
print()
d=c.reshape(2,3,2)
print(d)
print(c)
print(d.flatten())
print(type(d))
print('\n')
print('\n')
print('program-1')
a=arange(9)
print(a)
b=a.reshape(3,3)
print(b)
for i in range(len(b)):
    print('c= ',b[i])
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j],end=',  ')
print()
print('slicing')
c=reshape(arange(11,36),(5,5))
print(c)
print(c[0:3,0:2])
print(c[2:4,3:])
print('\n')
print('\n')
print('matrices using numpy')
str='1 2;3,4;5 6;7 8;9 0.2'
print(matrix(str))
print('\n')
str='1 2 7;3,4,8;5 6 9'
print('str= ',matrix(str))
print()
print('diaginal matrix= ',diagonal(matrix(str)))
print('max= ',(matrix(str)).max())
print('min= ',(matrix(str)).min())
print('sum and mean of matrics')
a=matrix(arange(56).reshape(7,8))
print(a)
print(a.sum())
print(a.mean())
print()
print('prod(0)=\n',a.prod(0))
print()
print('prod(1)=\n',a.prod(1))
print('\n')
a='10,2;35,5.5;9.2,5;5,10'
b= matrix(a)
print(b)
print()
print(sort(b))
print()
print(sort(b,axis=0))
print()
print('transpose of a matrix')
print(b)
print()
print(b.transpose())
print()
print(b.getT())
a=matrix((arange(1,17)).reshape(4,4))
b=matrix((arange(16,32).reshape(4,4)))
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(b*a)
print(b/a) 
