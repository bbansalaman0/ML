##def da(basic):
def da(basic):
    da=basic*80/100
    return da

##def hra(basic):
def hra(basic):
    hra=basic*15/100
    return hra

##def pf(basic):
def pf(basic):
    pf=basic*12/100
    return pf

##def itax(gross):
def itax(gross):
    tax=gross*0.1
    return tax
##this is main program
basic=float(input('enter basic salary: '))

##calculate gross salary
gross=basic+hra(basic)+da(basic)
print('Your gross salary is: {:10.2f}'.format(gross))

##calculate net salary
net=gross-itax(gross)-pf(basic)
print('Your net salary is: {:10.2f}'.format(net))
