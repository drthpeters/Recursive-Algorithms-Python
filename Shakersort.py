# (c) drthpeters
 
import turtle as tu
import random as rd
import math

def update(a,kk):
    i = kk % 60 
    j = math.floor(kk/60)
    tu.pencolor((1,1,1))
    tu.setpos(-400+14*i,120-16*j)
    st = chr(9608)
    tu.write(st,font = ("Courier",13,"bold"))
    tu.setpos(-400+14*i,120-16*j)
    tu.pencolor((0,0,0))
    tu.write(chr(a[kk]),font = ("Courier",13,"normal"))    

def back(a,l,r):
    k = r
    for j in range(r,l,-1):
        if a[j-1] > a[j]:
            x = a[j-1]; a[j-1] = a[j]; a[j] = x
            update(a,j-1); update(a,j)
            k = j
    if k < r: forward(a,k,r)
    
def forward(a,l,r):
    k = 0
    for j in range(l,r+1):
        if a[j-1] > a[j]:
            x = a[j-1]; a[j-1] = a[j]; a[j] = x
            update(a,j-1); update(a,j)
            k = j
    if l < k: back(a,l,k)
        
def shakersort(a,n):
    back(a,0,n-1)
                
# main program    
n = 60; a = []
tu.speed(6); tu.up(); tu.hideturtle()
tu.pencolor((0,0,0))

for i in range(n):
    a.append(rd.randint(65, 90))
    update(a,i) 
          
shakersort(a,n)
tu.up(); tu.hideturtle()
tu.setpos(-300,-150)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))    
tu.mainloop()
tu.done()     
