
# (c) drthpeters

import turtle as tu

def hexagon(a, red, blue):
    red *= 0.8; blue *= 1.25
    if blue > 1: blue = 1
    tu.pencolor(red,0,blue)
    tu.up()
    tu.setpos(-0.5*a,-0.866*a)
    tu.down()
    for i in range(6):
        tu.forward(a); tu.left(60)
    tu.up()
    tu.setpos(0,0)
    if a > 25:
        hexagon(a*0.8, red, blue)

# main program
red = 1; blue = 0.2
tu.pensize(width = 3)
hexagon(200,red, blue)
tu.up(); tu.hideturtle()
tu.setpos(-300,-250)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop()
tu.done()