# (c) drthpeters

import turtle as tu
from time import sleep

def remove_disk(step,x,h):
    tu.up()
    if x == 0: tu.setpos(-300+15*(n-step),20*h)
    elif x == 1: tu.setpos(-50+15*(n-step),20*h)
    else: tu.setpos(200+15*(n-step),20*h)
    tu.down()
    tu.pencolor((1,1,1))
    tu.fillcolor('white')
    tu.begin_fill()
    for j in range(2):
        tu.forward(30*step)
        tu.left(90)
        tu.forward(20)
        tu.left(90)
    tu.end_fill()
    tu.up()

def disk(step,y,h):
    tu.up()
    if y == 0: tu.setpos(-300+15*(n-step),20*h)
    elif y == 1: tu.setpos(-50+15*(n-step),20*h)
    else: tu.setpos(200+15*(n-step),20*h) 
    tu.down()
    tu.fillcolor(clr[step])
    tu.begin_fill()
    for j in range(2):
        tu.forward(30*step)
        tu.left(90)
        tu.forward(20)
        tu.left(90)
    tu.end_fill()
    tu.up()
    
def shift(x,y,z,k,hList):
    hs = hList[0]; ht = hList[1]; ha = hList[2]
    if k == 1: 
        print('disk ',k,' ',x,' -> ',y)
        if x == 0: h = hs; hs -= 1
        elif x == 1: h = ht; ht -= 1
        else: h = ha; ha -= 1
        remove_disk(k,x,h)
        if y == 0: hs += 1; h = hs
        elif y == 1: ht += 1; h = ht
        else: ha += 1; h = ha 
        disk(k,y,h)
        sleep(slt)
        hList = [hs,ht,ha]
    else: 
        hList = shift(x,z,y,k-1,hList)
        hs = hList[0]; ht = hList[1]; ha = hList[2]
        print('disk ',k,' ',x,' -> ',y)
        if x == 0: h = hs; hs -= 1
        elif x == 1: h = ht; ht -= 1
        else: h = ha; ha -= 1
        remove_disk(k,x,h)
        if y == 0: hs += 1; h = hs
        elif y == 1: ht += 1; h = ht
        else: ha += 1; h = ha;
        disk(k,y,h)
        sleep(slt)
        hList = [hs,ht,ha]
        hList = shift(z,y,x,k-1,hList)
    return hList

#------------------------------------------------------------------------------
# main program
slt = 0 # sleeping time    
print(); print('Tower of Hanoi')
n = int(input('number of disk (<= 6): '))

clr = [' ', 'green', 'red', 'blue', 'orange', 'violet', 'cyan']
tu.speed(0)
tu.up(); tu.hideturtle()
tu.setpos(-300,-2); tu.down(); tu.forward(700); tu.up()
tu.setpos(-80,300); tu.write('Tower of Hanoi',font = ("Arial",16,"bold"))
tu.setpos(-280,200)
tu.write('source',font = ("Arial",12,"normal"))
tu.setpos(-25,200)
tu.write('target',font = ("Arial",12,"normal"))
tu.setpos(220,200)
tu.write('auxiliary',font = ("Arial",12,"normal"))
tu.pencolor((1,1,1))
for i in range(n): disk(i+1,0,n-i-1)

sleep(3)    
slt = 1
count = shift(0,1,2,n,[n-1,-1,-1])

tu.up(); tu.hideturtle()
tu.setpos(-300,-150)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop()
tu.done()   
   