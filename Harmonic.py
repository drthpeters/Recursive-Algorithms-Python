
# (c) drthpeters

gamma = 0.577215664901533
import math

def harmrek(n):
    if n == 1: return 1
    else: return harmrek(n-1) + 1/n

# main program
print(); print('Harmonic Series')
n = int(input('n = '))

print('H(',n,') = ',harmrek(n))

print()
print('approximated by',math.log(n)+gamma)
