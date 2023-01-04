# (c) drthpeters

import turtle as tu
import random as rd

def update(kk,x,y):
    tu.pencolor((1,1,1))
    tu.setpos(x,y)
    st = chr(9608)
    tu.write(st,font = ("Courier",12,"bold"))
    tu.setpos(x,y)
    tu.pencolor((0,0,0))
    tu.write(chr(a[kk]),font = ("Courier",12,"normal")) 
  
def merge(l, m, r, h, p):
    A = []
    L = a[l:m+1]
    R = a[m+1:r+1]
    
    while (L != []) or (R != []):
        if L == []: A += R; R = []
        elif R == []: A += L; L = []
        else:
            while (L != []) & (R != []):
                if L[0] < R[0]: A.append(L[0]); L.pop(0)
                else: A.append(R[0]); R.pop(0)
    
    for i in range(len(A)): a[l+i] = A[i]
    for i in range(l,r+1): update(i,p+13*i,260-50*h)
 
def mergeSort(l, r, h, p):
    if l < r:
        for i in range(l,r+1): update(i,p+13*i,260-50*h)
        m = (l+r)//2
        mergeSort(l, m, h+1,p-65//(2**h))
        mergeSort(m+1, r, h+1,p+65//(2**h))
        merge(l, m, r, h, p)
    else: update(l,p+13*l,260-50*h)
        

# main program    
tu.up(); tu.hideturtle()
tu.setpos(-120,310)
tu.pencolor((0,0,0))
tu.write('Mergesort - Array to be sorted',font = ("Courier",13,"bold"))  

n = 40; a = []
for i in range(n): a.append(rd.randint(65, 90))

tu.speed(1)
p = -26-13*len(a)//2
mergeSort(0,n-1,0,p)

tu.up(); tu.hideturtle()
tu.setpos(-300,-300)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))    
tu.mainloop()
tu.done()     
