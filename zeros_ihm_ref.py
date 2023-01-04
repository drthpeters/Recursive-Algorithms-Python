# (c) drthpeters

def coeff():
    global n, a
    print('p(x) = a_0*x^0 + ... + a_n*x^n')
    n = int(input('degree of the polynomial: (<= 6) '))
    if n > 6: coeff()
    a = []
    for i in range(n+1):
        b = float(input('enter coefficient: '))
        a.append(b)

def polynomial():
    print('you entered')
    st = ''
    for i in range(n+1):
        st = st + str(a[i]) + '*x^' + str(i)
        if i < n: st += ' + '
    print(st)
    
def limit(n,a):
    global M
    M = 0
    for j in range(n+1):
        M += abs(a[j]/a[n])

def f(x):
    y = a[n]
    for j in range(n,0,-1): y = y*x + a[j-1]
    return y

def bisection(l,r): # interval halving method
    fl = f(l); fr = f(r)
    print('[',round(l,5),' , ',round(r,5),'] -> [',round(fl,6),' , ',round(fr,6),']')
    if r - l < epsilon:
        print(); print('A zero lies in the interval')
        print('[',l,',',r,'].'); print()
    else:
        if fl*f((l+r)/2) <= 0: bisection(l,(l+r)/2)
        else: bisection((l+r)/2,r)

def tov(n,a): # table of values
    print('Table of Values'); print()
    step = 0.1
    for i in range(round(-M/step),round(M/step)):
        print('  ',i*step,'  ->   ',round(f(i*step),3))
        if f(i*step)*f((i+1)*step) < -epsilon:
            print(); print('interval bisection')
            bisection(i*step,(i+1)*step)
        if abs(f(i*step)) < epsilon:
            print(); print('A zero detected at ',i*step)

# main program 
max = 6
epsilon = 1e-5
print(); print('Interval Halving Method')
ok = False
while not(ok):
    coeff() 
    polynomial()
    print(); ans = input('everything ok? (y/n) ')
    if ans in ['Y','y']: ok = True
limit(n,a)
tov(n,a)
       