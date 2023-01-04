# (c) drthpeters

def multiply(i):
    if i > 1: return i*add(i-1)
    else: return 1

def add(i):
    return i + multiply(i-1)

# main program
print('Add and multiply')
n = int(input('n = '))
if n % 2 == 0: value = add(n)
else: value = multiply(n)
print('value: ',value)