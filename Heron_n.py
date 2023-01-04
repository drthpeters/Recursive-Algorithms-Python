# (c) drthpeters

def Heron(x,i):
    i += 1
    x_new = (1-1/k)*x + a/(k*x**(k-1))
    print('step ',i,' approximation ',x_new)
    if abs(x_new - x) > epsilon: Heron(x_new,i)

# main program
print("Computing Square Roots using Heron's Method")
a = float(input('radicant: '))
k = int(input('root exponent: '))
d = int(input('number of decimals: '))
epsilon = 10**(-d)
Heron(1,0)          