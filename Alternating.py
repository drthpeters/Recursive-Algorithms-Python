# (c) drthpeters

import numpy as np

def altrek(n):
    if n == 1: return 1
    elif (n % 2) == 0: return altrek(n-1) - 1/n 
    else: return altrek(n-1) + 1/n

print(); print('Alternating Series')
stn = input('n = '); n = int(stn)

print('A(',n,') = ',altrek(n))
print('Difference from ln 2: ',np.log(2) - altrek(n))