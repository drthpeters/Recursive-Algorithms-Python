# (c) drthpeters

import turtle as tu
import random as rd

def fill(left,right,bottom,top,c):
    tu.setpos(left,bottom)
    tu.down()
    if c == 0: tu.fillcolor((0,0,0)) 
    elif c == 1: tu.fillcolor((1,0,0))
    elif c == 2: tu.fillcolor((0,0,1))
    else: tu.fillcolor((1,1,0))
    tu.begin_fill()
    tu.setpos(left,bottom)
    for i in range(2):
        tu.forward(top-bottom); tu.right(90)
        tu.forward(right-left); tu.right(90)
    tu.end_fill()
    tu.up()

def dye(left,right,bottom,top): 
    z = rd.randint(1,18)
    if z in colorset:
        fill(left,right,bottom,top,z)

def horizontal(left,right,bottom,top):
    span = top - bottom
    if span >= minspan:
        down = span//4 + bottom
        up = -span//4 + top
        if bottom < 0: middle = bottom
        else: middle = -1
        while (middle < down) or (middle > up):
            middle = bottom + rd.randint(1,span)
        fill(left,right,middle-half,middle+half,0)
        vertical(left,right,bottom,middle-half)
        vertical(left,right,middle+half,top)
    else: dye(left,right,bottom,top)
    
def vertical(left,right,bottom,top):
    span = right - left
    if span >= minspan:
        le = span//4 + left
        ri = -span//4 + right
        if left < 0: middle = left
        else: middle = -1
        while (middle < le) or (middle > ri):
            middle = left + rd.randint(1,span)
        fill(middle-half,middle+half,bottom,top,0)
        horizontal(left,middle-half,bottom,top)
        horizontal(middle+half,right,bottom,top)
    else: dye(left,right,bottom,top)

# main program 

minspan = 120; half = 5
colorset = {1,2,3}

tu.speed(8)
tu.up(); tu.hideturtle(); tu.left(90)
vertical(-300,300,-200,200)
tu.up()
tu.setpos(-300,-250)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop()
tu.done() 