# -*- coding: utf"-8 -"*-
""""
Created on Sun Sep 10 10:00:35 2023

@author: Tommy
"""

import turtle as tu
import time

# given sets A,B, arcs, predefined matching M
A = ['a','b','c','d','e']
B = ['f','g','h','j','k']
arcs = [['a','f'],['a','h'],['b','f'],['b','g'],['c','g'],['d','h'],
         ['d','j'],['e','j'],['e','k']]
M = [['b','f'],['a','h']]


Aplot = A.copy(); Bplot = B.copy()
arcs0 = arcs.copy()
M0 = M.copy()

#-- functions -----------------------------------------------------------------

def updateArcs(arcs,M):
    for i in range(len(arcs)):
        if (arcs[i][0] in B) and (arcs[i][1] in A): 
            arcs[i] = [arcs[i][1],arcs[i][0]]
    for i in range(len(arcs)):
        for j in range(len(M)):
            if arcs[i] == M[j]:
                arcs[i] = [M[j][1],M[j][0]]
    return arcs

def getUM(M):
    UM = [] 
    for i in range(len(M)): 
        for j in range(2):
            if (M[i][j] in A) or (M[i][j] in B): UM.append(M[i][j])
    return UM

def addPath(arcs,P): # in B
    for i in range(len(arcs)):
        if P != []:
            if (P[-1] == arcs[i][0]) and (not(arcs[i][1] in P)): 
                P.append(arcs[i][1]); 
                if P[-1] in A: addB(arcs,P)
    return P

def addB(arcs,P): # in A
    i = 0
    while (i < len(B)) and (not([P[-1],B[i]] in arcs)): i += 1
    if (i < len(B)) and (not(B[i] in P)): 
        P.append(B[i]) 
        P = addPath(arcs,P)
    return P
    
def makePath(arcs,AM,BM,P):    
    P = addB(arcs,P)
    while (P != []) and (not(P[-1] in BM)): P.pop(-1)
    if (P != []) and (BM != []):
        if P[-1] in BM:
            for j in range(len(BM)): 
                if BM[j] == P[-1]: BM.pop(j); break
    return P,BM
    
def matching(arcs,M,AM,BM):
    arcs = updateArcs(arcs,M)
    P = [AM[0]]
    P,BM = makePath(arcs,AM,BM,P)
    E = [] # edges of P
    for i in range(len(P)-1):
        if i % 2 == 0: E.append([P[i],P[i+1]])
        else: E.append([P[i+1],P[i]])
    M1, M2, M_new  = [], [], []
    for j in range(len(M)): 
        if not(M[j] in E): M1.append(M[j])
    for j in range(len(E)):
        if not(E[j] in M): M2.append(E[j])
    M_new = M1 + M2    
    AM.pop(0)
    if len(AM) > 0: M_new = matching(arcs,M_new,AM,BM) 
    return M_new

def drawLine(X,Y):
    x, y = -1, -1
    if (X in Bplot) and (Y in Aplot): X,Y = Y,X
    for i in range(len(Aplot)): 
        if X == Aplot[i]: x = Apos[i]
    for i in range(len(B)): 
        if Y == Bplot[i]: y = Bpos[i]
    tu.setpos(x,200); tu.down(); tu.showturtle()
    tu.setpos(y,10); tu.up(); tu.hideturtle()
    
def drawLine2(X,Y):
    x, y = -1, -1
    for i in range(len(Aplot)): 
        if X == Aplot[i]: x = Apos[i]
    for i in range(len(B)): 
        if Y == Bplot[i]: y = Bpos[i]
    tu.setpos(y,10); tu.down()
    tu.setpos(x,200); tu.up()  
    x, y = -1, -1
    

def clearWriting(x,y,l):
    tu.pencolor((1,1,1))
    tu.hideturtle(); tu.setpos(x,y-1)
    stc = ''
    for i in range(l): stc += chr(9608)
    tu.write(stc,font = ("Courier",14,"bold"))
    tu.setpos(x+2,y-1)
    tu.write(stc,font = ("Courier",14,"bold"))

def matchingTu(arcs,M,AM,BM):
    arcs = updateArcs(arcs,M)
    #print('matchingTu arcs = ',arcs)
    P = [AM[0]]
    P,BM = makePath(arcs,AM,BM,P)
    #print('matchingTu P = ',P,' BM = ',BM)
    E = [] # edges of P
    for i in range(len(P)-1):
        if i % 2 == 0: E.append([P[i],P[i+1]])
        else: E.append([P[i+1],P[i]])
    for i in range(len(E)):
        tu.speed(1)
        if i % 2 == 0: 
            tu.pencolor((0,0.85,0)); drawLine(E[i][0],E[i][1])
        else: 
            tu.pencolor((0.85,0,0)); drawLine2(E[i][0],E[i][1])      
        tu.speed(5)
    tu.pencolor((0,0,0)); tu.setpos(-150,-130); 
    Pstr = ''
    for j in range(len(P)): Pstr += P[j] + '  '
    if len(P) == 0: Pstr = 'not found'
    tu.write('new Path:  ' + Pstr,font = ("Arial",12,"normal"))
    time.sleep(2+len(P)); clearWriting(-150,-130,60)
    M1, M2, M_new  = [], [], []
    for j in range(len(M)): 
        if not(M[j] in E): M1.append(M[j])
    for j in range(len(E)):
        if not(E[j] in M): M2.append(E[j])
    M_new = M1 + M2    
    AM.pop(0)
    if len(AM) > 0: M_new = matchingTu(arcs,M_new,AM,BM) 
    return M_new

# main program ----------------------------------------------------------------

arcs = updateArcs(arcs,M)
UM = getUM(M)
AM = list(set(A) - set(UM)); nAM = len(AM)
BM = list(set(B) - set(UM)); nBM = len(BM); nB = len(B); B0 = B.copy()
MList = []

for na in range(nAM):
    for np in range(nB): 
        UM = getUM(M)
        AM0 = list(set(A) - set(UM))
        B1 = B0[np:]; B2 = B0[:np]
        AM1 = AM0[na:]; AM2 = AM0[:na]
        AM = AM1 + AM2; B = B1 + B2; AMplot = AM.copy()
        BM = list(set(B) - set(UM)); BMplot = BM.copy()
        M_new = matching(arcs,M,AM,BM)  
        MList.append(M_new)
        if len(M_new) == min(len(A),len(B)): break
    if len(M_new) == min(len(A),len(B)): break

maxlen = 0; ind = -1
for i in range(len(MList)):
    if len(MList[i]) > maxlen: maxlen = len(MList[i]); ind = i

print('\nmaxlen = ',maxlen)
print('maximal matching: ',MList[ind])

#-- turtlegraphics ------------------------------------------------------------

#-- vertices, arcs
Apos, Bpos = [], []
print('Aplot = ',Aplot)
print('Bplot = ',Bplot)
tu.speed(8)
tu.hideturtle(); tu.width(3); tu.up(); 
for i in range(len(Aplot)):
    tu.setpos(-250+i*100,200);
    Apos.append(-250+i*100)
    tu.down(); tu.circle(5); tu.up()
    tu.setpos(-250+i*100,220);
    tu.write(str(Aplot[i]),font = ("Arial",12,"normal"))
for i in range(len(Bplot)):
    tu.setpos(-250+i*100,0); 
    Bpos.append(-250+i*100)
    tu.down(); tu.circle(5); tu.up()
    tu.setpos(-250+i*100,-25);
    tu.write(str(Bplot[i]),font = ("Arial",12,"normal"))

tu.width(1); tu.speed(3)

# initial arcs
print('arcs0 = ',arcs0)
for i in range(len(arcs0)): drawLine(arcs0[i][0],arcs0[i][1])
tu.width(2)

if M != []:
    # initial matching
    tu.setpos(-100,-130)
    tu.write('green: given matching',font = ("Arial",12,"normal"))
    tu.pencolor((0,0.85,0)) # green
    for i in range(len(M0)): drawLine(M0[i][0],M0[i][1])
    time.sleep(4)
    clearWriting(-100,-130,15)

# new matching
M_new = matchingTu(arcs0,M0,AMplot,BMplot)
Mstr = ''
for i in range(len(M_new)):
    Mstr += '('+M_new[i][0]+','+M_new[i][1]+')  '
tu.setpos(-200,-130); tu.pencolor((0,0,0))
tu.write('Matching:  '+ Mstr,font = ("Arial",12,"normal"))
                           
tu.hideturtle()
tu.setpos(-400,-300)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop(); tu.done()
