# (c) drthpeters

import turtle as tu
import random as rd
import time

def chooseColor():
    red = rd.uniform(0,0.99)
    green = rd.uniform(0,0.99)
    blue = rd.uniform(0,0.99)
    clrtup = (red, green, blue)
    return clrtup

def hexagon():
    tu.setpos(rd.randint(-400,400),rd.randint(-300,300))
    a = 30+rd.randint(0,45)
    tu.right(rd.randint(0,45))
    tu.down()
    tu.fillcolor(chooseColor()) 
    tu.begin_fill()
    for i in range(6):
        tu.forward(a); tu.left(60)
    tu.end_fill()
    tu.up()
    htime = time.time()
    if htime-start < tlim: rectangle()

def rectangle():
    tu.setpos(rd.randint(-400,400),rd.randint(-300,300))
    a = 20 + rd.randint(0,20)
    b = 20 + rd.randint(0,50)
    tu.right(rd.randint(0,45))
    tu.down()
    tu.fillcolor(chooseColor()) 
    tu.begin_fill()
    for i in range(2):
        tu.forward(a); tu.right(90)
        tu.forward(b); tu.right(90)
    tu.end_fill()
    tu.up()
    rtime = time.time()
    if rtime-start < tlim: triangle()

def triangle():
    tu.setpos(rd.randint(-400,400),rd.randint(-300,300))
    a = 30 + rd.randint(0,40)
    tu.right(rd.randint(0,45))
    tu.down()
    tu.fillcolor(chooseColor()) 
    tu.begin_fill()
    for i in range(3):
        tu.forward(a); tu.right(120)
    tu.end_fill()
    tu.up()
    ttime = time.time()
    if ttime-start < tlim: hexagon()
        
# main program        
tlim = 25
tu.width(2) 
tu.speed(5)
tu.up()
tu.left(90)

start = time.time()
hexagon()

tu.up(); tu.hideturtle()
tu.setpos(-400,-330)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop()
tu.done()         