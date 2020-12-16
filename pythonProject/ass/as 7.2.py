fname=input('enter a file name: ')
file=open(fname)
c_count=0
c_big=0
c_big=float(c_big)
for lines in file.readlines():
    if lines.startswith('X-DSPAM-Confidence:'):
        a=float(lines[20:26])
        c_big+=a
        c_count+=1
b=c_big/c_count
print('Average spam confidence :',b)
