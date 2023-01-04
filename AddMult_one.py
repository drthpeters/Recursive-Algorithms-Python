# (c) drthpeters

def f(n):
    if n == 1: return 1
    elif n % 2 == 0: return n+f(n-1)
    else: return n*f(n-1)

# main program
print('Add and multiply')
n = int(input('n = '))
print('value: ',f(n))
