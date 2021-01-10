group=[1,2,3,4,5,6]
search=int(input('enter a element to search='))
for i in group:
    if search==i:
        print('element is found in group')
        break
else: print("element not found in group")
