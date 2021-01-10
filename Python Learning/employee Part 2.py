
from employee import *
##this is main program
basic=float(input('enter basic salary: '))

##calculate gross salary
gross=basic+hra(basic)+da(basic)
print('Your gross salary is: {:10.2f}'.format(gross))

##calculate net salary
net=gross-itax(gross)-pf(basic)
print('Your net salary is: {:10.2f}'.format(net))
