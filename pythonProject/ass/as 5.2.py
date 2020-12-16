n=0
largest=-1
smallest=None
while True:
    n=input('enter in input:')
    if n=='done':
        break
    try:
        num=int(n)
    except: print('Invalid input')
    if num>largest:
        largest=num
        
    elif smallest is None:
        smallest=num
    elif num<smallest:
        smallest=num
       
print('Maximum is',largest)
print('Minimum is',smallest)
        
    
        
