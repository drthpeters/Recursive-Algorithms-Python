# (c) drthpeters

import math

def f(x):
    return math.sin(2*x)

def regula(l,r,count): 
    fl = f(l); fr = f(r)
    print('[',round(l,5),' , ',round(r,5),'] -> [',round(fl,6),' , ',round(fr,6),']')
    xm = (l*fr - r*fl)/(fr - fl) 
    print('xm = ',xm)
    if abs(f(xm)) < epsilon:
        print()
        print('approximate solution: ',xm)
    else:
        if fl*f(xm) <= -epsilon: regula(l,xm,count+1)
        else: regula(xm,r,count+1)

# main program 
epsilon = 1e-12
print(); print('Regula Falsi')
left = float(input('left border: '))
right = float(input('right border: '))
regula(left,right,0)
       