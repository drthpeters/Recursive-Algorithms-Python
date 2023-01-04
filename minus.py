
# (c) drthpeters

def minus(i):
    i -= 1
    print(i,end= ' ')
    if i > 0: minus(i)

def minus_2(i):
    i -= 1
    if i > 0: minus_2(i)
    print(i,end= ' ')

print(); print('M I N U S')
n = int(input('n = '))
minus(n)
print()
minus_2(n)
print()