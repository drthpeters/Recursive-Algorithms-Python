# (c) drthpeters

def Perm(m):
    if m == 1:
        print(A)
    for i in range(m):
        Perm(m-1)
        if m % 2 == 1:
            x = A[0]; A[0] = A[m-1]; A[m-1] = x
        else:
            x = A[i]; A[i] = A[m-1]; A[m-1] = x

# main program
n = int(input('n = '))
A = [i+1 for i in range(n)]
print('A = ',A); print()
Perm(n)