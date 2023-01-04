# (c) drthpeters

def Qrec(k):
    if k <= 2: y = 1
    else: y = Qrec(k-Qrec(k-1)) + Qrec(k-Qrec(k-2))
    return y

def Qiter(n): 
    Q = []
    for j in range(n+1):
        if j <= 2: Q.append(1)
        else: Q.append(Q[j-Q[j-1]] + Q[j-Q[j-2]])       
        if j > 0: print('Q(',j,') = ',Q[j])
               
# main program

print(); print("Hofstadter's Q-Function")
n = int(input('upper limit '))
ch = input('(r)ecursive or (i)terative ')
if ch in ['i','I']: Qiter(n)
else:
    for k in range(1,n+1):
        print('Q(',k,') = ',Qrec(k))