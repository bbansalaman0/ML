hours=input('enter total hours:')
rate=input('enter rate:')
h=float(hours)
r=float(rate)
if h>40:
    total_pay=h*r+((h-40)*(r*0.5))
else:total_pay=h*r
print(total_pay)
