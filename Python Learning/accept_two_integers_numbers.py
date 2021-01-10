x=int(input("enter x value="))
y=int(input("enter y value="))
print("1. u have entered:", x,y,x+y,x*y, sep="__")
print("""""sum of", x ,"and", y, "is", x+y,
"product of ", x, "and", y, "is", x*y""")
print("""""sum of", {} ,"and", {}, "is", {},
"product of ", {}, "and", {}, "is", {:5.3f}""".format(x,y,x+y,x,y,x*y))
print("""""sum of", %i,"and", %i, "is", %f,
"product of ", %i, "and", %i, "is", %5.3f"""%(x,y,x+y,x,y,x*y))

print()

x=int(input("enter x value="))
y=int(input("enter y value="))
print("1. u have entered:", x,y,x+y,x*y, sep="__")
print("sum of", x ,"and", y, "is", x+y,\
"product of ", x, "and", y, "is", x*y)
print('sum of {} and {} is {:f} \
product of {} and {} is {:5.3f}'.format(x,y,x+y,x,y,x*y))
print('sum of %i and %i is %f \
product of  %i and %i is %f'%(x,y,x+y,x,y,x*y))

