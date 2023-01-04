# (c) drthpeters

def work(k):
    print(st[k],end = '')
    if st[k] != ' ': work(k+1)

def work2(k):
    if st[k] != ' ': work2(k+1)
    print(st[k],end = '')
    
# main program
st = input('enter a word, then press enter ') 
st += ' '
work(0)  
print()
work2(0)
print()
 