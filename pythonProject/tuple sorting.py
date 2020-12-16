emp=((10,'aman',10000),(40,'suyashi',20000),(30,'spbansal',40000))

print(sorted(emp))

print(sorted(emp,reverse=True))

print(sorted(emp,reverse=False, key=lambda x:x[1]))

print(sorted(emp,reverse=True, key=lambda x:x[2]))



##insertion of element  

str=(input('enter some names: ').split(','))
print(str)
name=[input('enter a new name: ')]
print(name)
place=int(input('enter a position: '))
names1=str[0:place-1]
names=names1+name+str[place-1:]
print(names)


##deletion of element


str=(input('enter some names: ').split(','))
print(str)

place=int(input('enter a position to be deleted: '))
print(place)
names1=str[0:place-1]
names=names1+str[place:]
print(names)
