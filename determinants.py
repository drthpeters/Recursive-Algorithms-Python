# (c) drthpeters

def enterMatrix():
    n = int(input('number of rows/columns: '))
    A = []
    print('enter coefficients line by line')
    for i in range(n):      
        Ai = []
        for j in range(n):
            st = 'a[' + str(i) + ',' + str(j) + '] = '
            Ai.append(float(input(st)))
        A.append(Ai)
    print('A = ',A)
    return A,n

def det(A,rank,column,ind):
    if rank == 2:
        # find correct indices
        k = list(ind)
        if k[0] > k[1]: x = k[0]; k.pop(0); k.append(x)
        # determinant with two rows
        res = A[k[0]][column]*A[k[1]][column+1] - A[k[1]][column]*A[k[0]][column+1]
    else:
        res = 0; count = 0; i = 0
        for i in range(n):
            if i in ind:
                # Zeile i entfernen!
                ind = ind - {i}
                res += (-1)**count*A[i][column]*det(A,rank-1,column+1,ind)
                count += 1
                ind = ind.union({i})
    return res

# main program
A,n = enterMatrix()
indices = {j for j in range(n)}
print('value of the determinant: ',det(A,n,0,indices))   