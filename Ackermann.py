# (c) drthpeters

def A(m,n):
    if m == 0: y = n+1
    else: 
        if n == 0: y = A(m-1,1)
        else: y = A(m-1,A(m,n-1))
    return y

# main program
print(); print('Ackermann Function')
m = int(input('m =  '))
n = int(input('n =  '))    
print()
print('A(',m,',',n,') = ',A(m,n))
