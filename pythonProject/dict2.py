x='book my in my in go in go my'
dict={}
list1=[]

for i in x.split():
    list1.append(i)
    print(list1)
for j in list1:
    dict[j]=dict.get(j,0)+1
list1.sort(reverse=True)
print(list1)
print('\n')
for k,v in sorted(dict.items(),reverse= True):
    print(k,v)
print('"my" is repeated "',list1.count('my'),'" times')


n=int(input('enter a number= '))
countries=list()
cities=list()
d={}
for i in range(n):
    x=input('enter a country: ')
    countries.append(x)
    y=input('enter a city: ')
    cities.append(y)
    d.update({x:y})
z=zip(countries,cities)
print(countries,cities)
print(z)

print('{:15s}---{:15s}'.format('COUNTRY','CITY'))
print()
for k,v in d.items():
    print('{:15s}---{:15s}'.format(k,v))
print('\n')
for i in d:
    print('{:15s}---{:15s}'.format(i,d[i]))
