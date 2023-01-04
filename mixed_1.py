# (c) drthpeters

import turtle as tu

def square(length):
    tu.down()
    for i in range(4):
        tu.forward(length)
        tu.right(90)
    tu.up()
    x = tu.xcor(); y = tu.ycor()
    tu.setpos(x+length//10,y+length//10)
    triangle(round(length*0.8))

def triangle(length):
    tu.down()
    tu.right(30)
    for i in range(3):
        tu.forward(length); tu.right(120)
    tu.left(30)
    tu.up()
    x = tu.xcor(); y = tu.ycor()
    tu.setpos(x+length*0.3,y+length//10)
    if length > minlength:
        square(round(length*0.4))
        
# main program        
minlength = 40
tu.width(2) 
tu.speed(5)
tu.up(); tu.setpos(-200,-250)
tu.left(90)

square(600)

tu.up(); tu.hideturtle()
tu.setpos(-400,-300)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop()
tu.done()         