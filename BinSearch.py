
# (c) drthpeters 

namesList = []
with open('names_sort.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    namesList.append(lines[i][:-1]) 

#------------------------------------------------------------------------------
def search(l,r):
    found = False
    m = round((l+r)/2)
    print(' Name[',m,'] = ',namesList[m])
    if na == namesList[m]: found = True
    if (na < namesList[m]) & (l < m): found,m = search(l,m-1)
    if (na > namesList[m]) & (m < r): found,m = search(m+1,r)
    return found, m

# main program ----------------------------------------------------------------
n = len(namesList)
print()  
print('Binary Search of Names ',n,' first names'); print()
na = input('Name: '); print()
found, m = search(0,n-1)
print()
if found: print(na + ' is number '+ str(m))
else: print(na + ' is not in the list of names')