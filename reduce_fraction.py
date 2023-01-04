# (c) drthpeters

def search_prime(prime, num, den):
    possible = True; success = False
    if (num % prime != 0) or (den % prime != 0):
        prime += 1
        if (num < prime) or (den < prime): possible = False
        if possible: 
            prime, success = search_prime(prime, num, den)
    else: success = True
    return prime, success

def reduce(prime, num, den):
    prime, success = search_prime(prime, num, den)
    if success:
        num = num // prime
        den = den // prime
        print(' = ',num,'/',den,end = ' ')
        reduce(prime, num, den)

# main program
print(); print('Reduce a fraction')
possible = True; prime = 2
num = int(input('numerator: '))
den = int(input('denominator: '))
print()
print(num,'/',den,end = ' ')
reduce(prime, num, den)       
