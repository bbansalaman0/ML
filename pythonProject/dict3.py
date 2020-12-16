


dict={'name':'aman','id':'ue151012','salary':'25000',
      'names':'suyashi','ids':'ue151312','salarys':'256000'}
print('name of employee: ',dict['name'])
print('id of employee: ',dict['id'])
print('salary of employee: ',dict['salary'])


n=int(input('enter a number= '))
countries=list()
cities=list()
d={}
for i in range(n):
    x=input('enter a country: ')
    countries.append(x)
    y=input('enter a city: ')
    cities.append(y)

z=zip(countries,cities)
d=dict(z)
print(countries,cities)
print(z)
print(d)
