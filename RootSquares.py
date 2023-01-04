# (c) drthpeters

import math

def root(n):
    if n > 1:
        return math.sqrt(n + square(n-1))
    else: return 1

def square(n):
    return (n + root(n-1))**2    

# main program
print('Roots and Squares')
n = int(input('n = '))

y = root(n) if n % 2 == 1 else square(n)
print('result: ',y)
