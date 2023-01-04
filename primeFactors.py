# (c) drthpeters

def findPF(n,x):
    if n % x == 0: 
        print(x,' ',end = '')
        n = n / x
    else: x += 1
    if n >= x: findPF(n,x)

# main program
print('Prime Factors')
n = int(input('n = '))
findPF(n,2)