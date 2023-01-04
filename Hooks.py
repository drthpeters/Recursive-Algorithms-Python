# (c) drthpeters

import turtle as tu
import time

def draw(length, step):
    length /= 4
    if step == 0: 
        tu.forward(length)
        tu.right(90)
        tu.forward(length)
        tu.left(90)
        tu.forward(length)
        tu.left(90)
        tu.forward(length)
        tu.forward(length)
        tu.right(90)
        tu.forward(length) 
        tu.right(90)
        tu.forward(length) 
        tu.left(90)
        tu.forward(length)
    else:
        draw(length,step-1)
        tu.right(90)
        draw(length,step-1)
        tu.left(90)
        draw(length,step-1)
        tu.left(90)
        draw(length,step-1)
        draw(length,step-1)
        tu.right(90)
        draw(length,step-1)
        tu.right(90)
        draw(length,step-1)
        tu.left(90)
        draw(length,step-1)
        
# main program

for count in range(3):
    tu.up(); tu.setpos(-300,0); tu.down()
    tu.width(2)
    draw(600,count)
    time.sleep(3)
    tu.clearscreen()

#tu.up(); tu.setpos(-300,0); tu.down()
#draw(600,3) # looks nice but takes very much time!

tu.up(); tu.hideturtle()
tu.setpos(-300,-250)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop()
tu.done() 