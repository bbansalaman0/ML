print('exp=1')
print()
print('assert statement')
x=int(input('enter a number greater than zero= '))
assert x>0
print('u entered= ',x)
print()
print()
print('exp=2')
print("assetion using try and except method")
x=int(input('enter a number greater than zero= '))
try:
    assert(x>0)
    print("u entered: ",x)
except AssertionError:
    print("wrong input entered") #this is executed in case of exception.
