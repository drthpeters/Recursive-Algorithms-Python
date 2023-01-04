
# (c) drthpeters

def gcd(x,y):
    if x < 0: x = -x
    if y < 0: y = -y
    r = 1
    while r > 0:
        r = x % y; x = y; y = r
    print('The GCD is ',x)
    z = int(input('next number: '))
    if z != 0: gcd(x,z) 

# main program
print(); print('Greatest Common Divisor')
print('Enter numbers, end = 0')
a, b = 0, 0
while a == 0: a = int(input('first number: '))
while b == 0: b = int(input('second number: '))
gcd(a,b)