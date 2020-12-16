print('for loop examples')
print("exp=1")
x="aman bansal"
for ch in x:
    print(ch)
print()
print()
print("exp=2")
x="amanbansal"
y=len(x)
for ch in range(y):
    print(ch)
print()
print()
print("exp=3")
x="aman bansal_suyashi bansal"
for ch in range(len(x)):
    print(ch+2)
print()
print()
print("exp=4")
for i in range(1,10,2):
    print(i)
print()
print()
print("exp=5")
for i in range(10,0,-2):
    print(i)
print()
print()
print("exp=6")
lst=['aman','bansal','suyashi','bansal']
for ch in lst:
    print(ch)
print()
print()
print("exp=7")
print('sum of list using for loop')
lst=[10,20,30,40,50,60,70,80,90,100]
sum=0 #initial sum of list is =0
for i in lst:
    print(i)
    sum+=i
print("sum of list is= ",sum)
print()
print()
print("exp=8")
print("sum of list using while loop")
lst=[10,20,30,40,50,60,70,80,90,100]
sum=0 #initial sum of list is =0
i=0 #initial zeroth position element of list is taken
while i<len(lst):
    print(lst[i])
    sum+=lst[i]
    i+=1
print("sum of list till is= ",sum)
print()
print()
print("exp=9")
print("sum of list using while loop")
lst=[10,20,30,40,50,60,70,80,90,100]
sum=0 #initial sum of list is =0
i=0 #initial zeroth position element of list is taken
while i<len(lst):
    print(lst[i])
    sum+=lst[i]
    i+=1
    print("sum of list till is= ",sum)
