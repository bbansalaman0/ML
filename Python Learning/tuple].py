str=input("Enter some elements: ").split(',')
lst=[int(i) for i in str]
tpl=tuple(lst)
print(tpl)
x=sorted(tpl)
print(x)
y=sorted(tpl,reverse=True)
print(y)
ele=int(input('enter a number to search: '))
try:
    pos=tpl.index(ele)
    print('found at position: ',pos+1)
except ValueError:
    print('Not found at any position')
