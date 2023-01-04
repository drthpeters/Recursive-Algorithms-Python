# (c) drthpeters

import numpy as np
import scipy.optimize as scop

def read(filename):
    data = np.loadtxt(filename)
    obj = data[0][:-1]
    A = [data[i][:-1] for i in range(1,len(data))]
    B = [data[i][-1] for i in range(1,len(data))]
    return obj, A, B

def solve_LP(obj, A, B):
    succ = True
    opt = scop.linprog(c=obj, A_ub=A, b_ub=B, method="highs")
    x = opt.x; y = opt.fun
    if opt.status > 0: succ = False
    return x,y,succ
    
def isInt(x):
    xlow = np.floor(x); xup = np.ceil(x)
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
    x0,y0,succ = solve_LP(obj,A0,B0)
    if succ == False: y0 = np.inf
    return x0,y0,A0,B0,succ
    
def right(ind,x,A,B):
    A_ = [0 for i in range(len(x))]
    A_[ind] = -1
    A1 = A + [A_]; B1 = B + [-np.ceil(x[ind])]
    x1,y1,succ = solve_LP(obj,A1,B1)
    if succ == False: y1 = np.inf
    return x1,y1,A1,B1,succ

def branch(ind,x,A,B,xList,yList):
    found_l = False; found_r = False
    
    xl,yl,Al,Bl,succ = left(ind,x,A,B)
    if succ:
        if allInt(xl) & (yl != np.inf):
            xList.append(xl); yList.append(yl)
            found_l = True
        
    xr,yr,Ar,Br,succ = right(ind,x,A,B)
    if succ:
        if allInt(xr) & (yr != np.inf):
            xList.append(xr); yList.append(yr)
            found_r = True
    
    bound = min(yl,yr)
    if (yl <= bound) & (yl != np.inf) & (found_l == False):
        i = 0
        while (i < len(xl)-1) & isInt(xl[i]) : i += 1
        if i < len(xl): found_l = branch(i,xl,Al,Bl,xList,yList)
    if (yr <= bound) & (yr != np.inf) & (found_r == False):
        i = 0
        while (i < len(xr)-1) & isInt(xr[i]) : i += 1
        if i < len(xr): found_r = branch(i,xr,Ar,Br,xList,yList)
    
    y2 = np.inf; found2 = False
    if yl > bound: y2 = yl; x2 = xl; A2 = Al; B2 = Bl
    if yr > bound: y2 = yr; x2 = xr; A2 = Ar; B2 = Br
    if (y2 != np.inf) & (found_l == False) & (found_r == False):
        i = 0
        while (i < len(x2)-1) & isInt(x2[i]) : i += 1
        if i < len(x2): found2 = branch(i,x2,A2,B2,xList,yList)
    
    return found_l or found_r or found2
             
# main program ----------------------------------------------------------------
epsilon = 1e-6

xList, yList = [], []
obj, A, B = read('ILP1.txt')

x,y, succ = solve_LP(obj,A,B)
print(); print('LP relaxation : ',x)
print('value of the objective function: ',y); print()

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
            print('no solution of the ILP!')
        
        if yList != []:
            ymin = min(yList)
            xmin = xList[np.argmin(yList)]; 
            print(); print('optimal integer solution: ')
            print('optimal objective value: ',ymin)
            ixmin = [int(xmin[i]) for i in range(len(xmin))]
            print('values of variables: ',ixmin)
else: print('The system is infeasible!')
