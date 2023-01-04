# (c) drthpeters

def Cat(n):
    if n == 0: return 1
    else:
        su = 0
        for j in range(n): 
            su += Cat(j)*Cat(n-1-j)
        return su

# main program
print(); print('Catalan Numbers')
n = int(input('limit = '))

for i in range(n+1):
    print('C(',i,') = ',round(Cat(i)))
