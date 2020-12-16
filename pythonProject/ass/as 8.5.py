fname=input('enter a file name: ')
file=open(fname)
count=0
for lines in file:
    if not lines.startswith('From:'):
        continue
    else:
        count+=1
        list=lines.split()
        print(list[1])
print('There were',count,'lines in the file with From as the first word')
