# (c) drthpeters

def fibo_p(k):
    if k == p: y = 1
    elif k < p: y = 0
    else: 
        y = 0
        for j in range(p+1): y += fibo_p(k-1-j)
    return y

def fibopiter(n): 
    fibop = []
    for j in range(n+1):
        if j == p: fibop.append(1)
        elif j < p: fibop.append(0)
        else:
            y = 0
            for i in range(p+1): y += fibop[j-1-i]  
            fibop.append(y)
        print('fibo_p(',j,') = ',fibop[j])
        
# main program
print(); print("Fibonacci Function of Order p")
p = int(input('order p = '))
n = int(input('upper limit '))
ch = input('(r)ecursive or (i)terative ')
if ch in ['i','I']: fibopiter(n)
else:
    for k in range(1,n+1):
        print('fibo_p(',k,') = ',fibo_p(k))
