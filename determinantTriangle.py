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

def triangle(A,rank):
    if rank > 1:
        det = A[0][0]
        for k in range(1,rank):
            y = A[k][0]/A[0][0]
            for j in range(rank):               
                A[k][j] = A[k][j] - y*A[0][j]
        A1 = []
        for k in range(1,rank):
            a = [A[k][j] for j in range(1,rank)]
            A1.append(a)
        det *= triangle(A1,rank-1)
        return det
    else: return A[0][0]
                
# main program
A,n = enterMatrix() 
D = triangle(A,n)
print('value of the determinant = ',D)