# (c) drthpeters

import turtle as tu

def rectangle(a,b):
    tu.down()
    for i in range(2):
        tu.forward(a); tu.right(90)
        tu.forward(b); tu.right(90)
    tu.up()
    triangle(a,b)

def triangle(a,b):
    tu.down()
    tu.right(30)
    for i in range(3):
        tu.forward(b); tu.right(120)
    tu.left(30)
    tu.up()
    x = tu.xcor(); y = tu.ycor()
    tu.setpos(x+b*0.25,y)
    if b > minlength:
        rectangle(a//2,b//2)
        
# main program        
minlength = 100
tu.width(2) 
tu.speed(5)
tu.up(); tu.setpos(-200,-250)
tu.left(90)

rectangle(520,600)

tu.up(); tu.hideturtle()
tu.setpos(-400,-300)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop()
tu.done()         