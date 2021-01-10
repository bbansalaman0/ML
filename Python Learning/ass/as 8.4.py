fname=input('enter a file name:')
file=open(fname)
list1=list()
for line in file:
    for word in line.split():
        if word in list1:
            continue
        else:
            list1.append(word)
list1.sort()
print(list1)
