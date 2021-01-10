def sum(a,b):
    c=a*b
    return c
    
c=sum(2,3)
print(c)
print()
print()
print()
def subtract_add_multiplication_divide(a,b):
    q=a-b
    w=a+b
    e=a*b
    r=a/b
    return q,w,e,r
t=subtract_add_multiplication_divide(5,30)
print('the results are= ')
print(t)
for i in t:
    print(i)
print()
print()
def even_odd(a):
    if a%2==0:print(a,'is even')
    else:print(a,'is odd')
even_odd(12)
even_odd(13)
print()
print()
def modify(x):
    x=25
    print(x,id(x))

x=10
modify(x)
print(x,id(x))
print()
def modify(lst):
    lst.append(9)
    print(lst,id(lst))
lst=[1,2,3,4,5,6]
modify(lst)
print(lst,id(lst))
print()
print()
def modify(lst):
    lst=[4,5,6743,684,34,4]
    print(lst,id(lst))
lst=[1,2,3,4,5,6]
modify(lst)
print(lst,id(lst))
