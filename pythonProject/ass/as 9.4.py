fname=input('Enter a file name:')

file=open(fname)
dict=dict()
list1=list()
for lines in file:
    if not lines.startswith('From:'):
        continue
    else:
        word=lines.split()
        list1.append(word[1])
for word in list1:
    dict[word]=dict.get(word,0)+1
##highest count word and higest count sent
hc=None
hcw=None
for emailid,sendtimes in dict.items():
    if hc is None or sendtimes>hc:
        hcw=word
        hc=sendtimes
print(hcw,hc)

    
