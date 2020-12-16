fname=input('Enter a file name:')
file=open(fname)
list1=list()
count=0
dict=dict()
for lines in file:
    if not lines.startswith('From '):
        continue
    else:
        count+=1
        word=lines.split()
    
        str1=''.join(word[5])
        
        list1.append(str1[0:2])
       
for word in list1:
    dict[word]=dict.get(word,0)+1
for k,v in sorted(dict.items()):
    print(k,v)
