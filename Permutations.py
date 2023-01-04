# (c) drthpeters

def swap(p,i,j):
    x = p[i]; p[i] = p[j]; p[j] = x
    return p

def perm(n):
    if n == 2: 
        print(p)        
        swap(p,pmax-2,pmax-1)
        print(p)       
        swap(p,pmax-2,pmax-1)
    else:
        perm(n-1)       
        for i in range(pmax-n+1,pmax):
            swap(p,pmax-n,i)
            perm(n-1)
        for i in range(pmax-n+1,pmax): swap(p,i-1,i)
        
#- main program ---------------------------------------------------------------

print('Permutations')
pmax = int(input('Enter the order (2..6) '))
p = [i+1 for i in range(pmax)]
perm(pmax)
    