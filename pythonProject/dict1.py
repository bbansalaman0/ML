

dict= {'name':'aman','id':'Ue151012','salary':'25000'}
print(dict)
print('keys in dict:',dict.keys())
print('values in dict:',dict.values())
print('items in dict:',dict.items())
dict={values:keys for keys,values in dict.items()}
print(dict)
print(dict.get('aman',-1))
k='class'
v='btech'
dict.update({k:v})
print(dict)
print('\n')
y=dict.popitem()
print(y)
print(dict)
x=dict.pop('aman','banana')
print(x)
print(dict)


keys={'a','e','i','o','u'}
values='vowel'
vowels=dict.fromkeys(keys,values)
print(vowels)

# VOWELS KEYS
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = { key : list(value) for key in keys }
# you can also use { key : value[:] for key in keys }
print(vowels)

# UPDATING THE VALUE
value.append(2)
print(vowels)




colors={'r':'red','g':'green','b':'blue'}
for k in colors:
    print(k,colors[k])

for k,v in colors.items():
    print('keys="{}"  value="{}"'.format(k,v))
print(colors.get('red',0))

print('sorting using lambda function')
print()
colors={1:'red',5:'green',3:'blue'}
c1=sorted(colors.items(),key=lambda x:x[0])
print(c1)
c2=sorted(colors.items(),key=lambda x:x[1])
print(c2)
