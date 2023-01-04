# (c) drthpeters

import turtle as tu

def snail(wid,situ,red,green, blue):
    red *= 0.85; green *= 1.05; blue *= 1.07
    if blue > 1: blue = 1
    if green > 1: green = 1   
    tu.pencolor((red, green, blue))
    tu.fillcolor((red, green, blue))
    tu.begin_fill()
    tu.up()
    tu.down()
    for i in range(2):
        tu.forward(round(wid)); tu.left(90)
        tu.forward(round(wid)); tu.left(90)
    tu.end_fill()
    if wid > 20:
        tu.right(18)
        snail(wid*0.95, situ+2,red, green, blue)

# main program
x0 = -100; y0 = 100    
red = 1; green = 0.1; blue = 0.1
tu.pensize(width = 2); tu.setheading(90)
snail(200,0,red, green, blue)
tu.up(); tu.hideturtle()
tu.setpos(-250,-250)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop()
tu.done()