print('exp=1')
for i in range(3):
    for j in range(4):
        print('i=',i,'\t','j=',j,'\n')
print()
print()



print("exp=2")
for i in range(1,11):
    for j in range(1,i+1):
        print("* ",end=" ")
    print()
print()
print()



print("exp=2.2")
for i in range(1,11):
    print("*  "*(i))
print()
print()



print("exp=3")
n=40
for i in range(1,11):
    print(" "*n,end=" ")
    print("* "*i)
    n-=1
print()
print()




print("exp=3.5")
n=40
for i in range(1,11):
    print(" "*(n-i) + '* '*i)
print()
print()



print('exp=4')
for i in range(1,11):
    for j in range(1,11):
        print(('%8d')%(i*j),end=" ")
    print()
print()
print()



print('exp=5')
for i in range(1,11):
   for j in range(11,21):
        print("%8d"%(i*j),end=" ")
   print()

print(" ")
print(" ")

n=10
for i in range(n):
    # for j in range(1,i+1):
    print((n-i)*'  ' + (2*i+1)*' *')


for i in range(n,-1,-1):
# for j in range(1,i+1):
    print((n-i)*'  ' + (2*i+1)*' *')



print(" ")
print(" ")

n = 5

for i in range(n):
    print(' ' * (n - i) + '*' * ((2 * i) + 1))

for i in range(n, -1, -1):
    print(' ' * (n - i) + '*' * ((2 * i) + 1))


print(" ")
print(" ")

i = 1
result = 1

while i < 7:
    i += 1
    if i % 2 == 0:
        print('Skipping {}'.format(i))
        continue
    print('Multiplying with {}'.format(i))
    result = result + i

print('i:', i)
print('result:', result)

print(" ")
print(" ")


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in weekdays:
    print(day)
print(" ")
print(" ")

persons = [{'name': 'John', 'sex': 'Male'}, {'name': 'Jane', 'sex': 'Female'}]

for person in persons:
    for key in person:
        print(key, ":", person[key])
    print(" ")

