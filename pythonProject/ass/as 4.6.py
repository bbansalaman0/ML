def computepay(h,r):
    if h>40:
        pay=h*r+((h-40)*(r*0.5))
    else:
        pay=h*r
    return pay
hours=input('enter hours:')
rate=input('enter rate:')
h=float(hours)
r=float(rate)
tp=computepay(h,r)
print('Pay',tp)
