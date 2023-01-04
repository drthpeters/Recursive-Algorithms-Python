# (c) drthpeters

weight = [7,4,6,8,6]
value = [4,4,5,4,6]
maxweight = 13 # of knapsack

#weight = [6,8,7]
#value = [5,6,8]
#maxweight = 13

#weight = [12,2,1,1,4]
#value = [4,2,2,1,10]
#maxweight = 15

#weight = [5, 7, 6, 8, 10, 11, 12, 15, 17, 30, 18]  
#value = [8, 9, 6, 5, 10, 5, 10, 17, 19, 20, 13]  
#maxweight = 33


def find(x):
    posi = -1
    for j in range(n-1,x,-1):
        if (not marked[j]): posi = j
    return posi

def clean(x):
    y = x + 1
    while y <= n-1: 
        marked[y] = False
        y += 1
        
def search(current):
    global count, base, optival, optiList
    y = find(current)
    if y >= 0:
        count += 1; current = y
        indList.append(current)
        wtList.append(weight[current]); valList.append(value[current])
        if (sum(wtList) <= maxweight) & (sum(valList) > optival):
            optival = sum(valList); optiList = indList.copy()
        if sum(wtList) > maxweight:
            for ii in range(current+1,n): marked[ii] = True
        print('count = ',count,' optival = ',optival,' indList = ',indList)
        search(current)
    else: # backtracking
        marked[current] = True
        clean(indList[-1])
        indList.pop(-1); wtList.pop(-1); valList.pop(-1)
        if indList != []: current = indList[-1]
        else: 
            current = -1 + base; base += 1
        if base < n: search(current)
        
# main program        
n = len(weight)
indList, optiList, valList, wtList = [], [], [], []
marked = [False for i in range(n)]
base, count, optival = 0, 0, 0
search(-1)
print()
print('optimal value: ',optival)
print('optimal objects: ',optiList)  
print('number of checks: ',count) 
        