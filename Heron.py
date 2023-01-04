# (c) drthpeters

def Heron(x,i):
    i += 1
    x_new = 0.5*(x + a/x)
    print('step ',i,'[',a/x_new,',',x_new,']')
    if x_new - a/x_new > epsilon: Heron(x_new,i)

# main program
print("Computing Square Roots using Heron's Method")
a = float(input('radicant = '))
d = int(input('number of decimals: '))
epsilon = 10**(-d)
Heron(1,0)          