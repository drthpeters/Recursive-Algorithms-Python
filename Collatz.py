# (c) drthpeters

def even(n):
    print(n,end = ' ')
    n = n //2
    if n % 2 == 0: even(n)
    else: odd(n)

def odd(n):
    if n == 1: print(1)
    else: 
        print(n,end = ' ')
        even(3*n+1)

print('Collatz Conjecture')
n = int(input('odd number n = '))
odd(n)
        