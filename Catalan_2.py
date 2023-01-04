# (c) drthpeters

def Cat(n,CatList):
    if n in [0,1]: return 1
    else:
        su = 0
        for j in range(n): 
            su += CatList[j]*CatList[n-1-j]
        return su

# main program
print(); print('Catalan Numbers')
n = int(input('limit = '))

CatList = []
for i in range(n+1):
    CatList.append(Cat(i,CatList))
    print('C(',i,') = ',round(CatList[i]))
