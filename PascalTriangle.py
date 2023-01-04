# (c) drthpeters

def bc(b,a):
    if (a == 0) or (a == b): return 1
    elif b == 1: return 1 
    else: return bc(b-1,a-1)+bc(b-1,a)
        
# main program
print(); print("Pascal's triangle")
n = int(input('Number of rows: '))  
for k in range(1,n+1): 
    for j in range(k+1):
        print(bc(k,j),' ',end = ' ')
    print()    