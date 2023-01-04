# (c) drthpeters 

import turtle as tu
import random as rd

def chooseColor():
    red = rd.uniform(0,0.9)
    green = rd.uniform(0,0.9)
    blue = rd.uniform(0,0.9)
    return (red, green, blue)
    
def dragon(size,step):
    
    if step == 0: tu.forward(size)
    else:
        size = round(size*0.707)
        tu.left(45)
        dragon(size,step-1)
        tu.right(90)
        dragon(size,step-1)
        tu.left(45)

# main program
tu.width(2) 

for step in range(6):
    tu.pencolor(chooseColor())
    tu.up()
    tu.setpos(-160,-50)
    tu.down()
    dragon(270,step)

tu.up(); tu.hideturtle()
tu.setpos(-300,-150)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop()
tu.done()         