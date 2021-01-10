fname=input('enter a file name: ')
file=open(fname)
for lines in file.readlines():
    print(lines.upper().strip())

