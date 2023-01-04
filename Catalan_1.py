
# (c) drthpeters

def fakrek(n):
    if n == 0: return 1
    else: return n*fakrek(n-1)

# main program
print(); print('Catalan Numbers')
n = int(input('limit = '))

for k in range(n+1):
    C = fakrek(2*k)/(fakrek(k+1)*fakrek(k))
    print('C(',k,') = ',round(C))