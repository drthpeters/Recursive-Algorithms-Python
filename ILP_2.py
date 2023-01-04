# (c) drthpeters

import numpy as np
import scipy.optimize as scop

def read(filename):
    data = np.loadtxt(filename)
    print('data = '); print(data)
    obj = data[0][:-1]
    print(); print('obj = ',obj)
    A = [data[i][:-1] for i in range(1,len(data))]
    B = [data[i][-1] for i in range(1,len(data))]
    print('A = ',A); print('B = ',B)
    return obj, A, B

def solve_LP(obj, A, B):
    succ = True
    opt = scop.linprog(c=obj, A_ub=A, b_ub=B, method="highs")
    x = opt.x; y = opt.fun
    if opt.status > 0: succ = False
    return x,y,succ

def isInt(x):
    xlow = np.floor(x); xup = np.ceil(x)
    #print('xlow = ',xlow)
    #print('xup = ',xup)
    b = False
    if (abs(x-xlow) < epsilon) or (abs(xup - x) < epsilon): b = True
    return b

def allInt(x):
    b = True
    for i in range(len(x)):
        if isInt(x[i]) == False: b = False
    return b

def left(ind,x,A,B):
    A_ = [0 for i in range(len(x))]
    A_[ind] = 1
    A0 = A + [A_]; B0 = B + [np.floor(x[ind])]
    print('A0 = ',A0)
    print('B0 = ',B0)
    x0,y0,succ = solve_LP(obj,A0,B0)
    print('branch left: ',x0)
    print('value of the objective function: ',y0)
    print('success: ',succ); print()
    if succ == False: y0 = np.inf
    return x0,y0,A0,B0,succ
    
def right(ind,x,A,B):
    A_ = [0 for i in range(len(x))]
    A_[ind] = -1
    A1 = A + [A_]; B1 = B + [-np.ceil(x[ind])]
    print('A1 = ',A1)
    print('B1 = ',B1)
    x1,y1,succ = solve_LP(obj,A1,B1)
    print('branch right: ',x1)
    print('value of the objective function: ',y1)
    print('success: ',succ); print()
    if succ == False: y1 = np.inf
    return x1,y1,A1,B1,succ

def branch(ind,x,A,B,xList,yList):
    
    xl,yl,Al,Bl,succ = left(ind,x,A,B) 
    if succ:
        if allInt(xl):
            print('solution found x = ',xl,' y = ',yl); print()
            xList.append(xl); yList.append(yl)
        elif yl != np.inf: 
            i = 0
            while (i < len(xl)) & isInt(xl[i]) : i += 1
            branch(i,xl,Al,Bl,xList,yList)
        
    xr,yr,Ar,Br,succ = right(ind,x,A,B)
    if succ:
        if allInt(xr):
            print('solution found x = ',xr,' y = ',yr); print()
            xList.append(xr); yList.append(yr)
        elif yr != np.inf: 
            i = 0
            while (i < len(xr)) & isInt(xr[i]) : i += 1
            branch(i,xr,Ar,Br,xList,yList)
            
# main program ----------------------------------------------------------------
epsilon = 1e-6

xList, yList = [], []
obj, A, B = read('ILP1.txt')

x,y, succ = solve_LP(obj,A,B)
print(); print('LP relaxation : ',x)
print('value of the objective function: ',y)

if succ:
    if allInt(x): print('This is the optimal integer solution!')
    else:
        i = 0
        while (i < len(x)) & isInt(x[i]): i += 1
        found = branch(i,x,A,B,xList,yList)
        if found: 
            print('yList = ',yList)
            print('xList = ',xList)
        else:
            print('no solution of the current ILP!')
        
        if yList != []:
            ymin = min(yList)
            xmin = xList[np.argmin(yList)]; 
            print(); print('optimal integer solution: ')
            print('optimal objective value: ',ymin)
            ixmin = [int(xmin[i]) for i in range(len(xmin))]
            print('values of variables: ',ixmin)
else: print('The system is infeasible!')
