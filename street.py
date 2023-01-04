# (c) drthpeters

import turtle as tu
import random as rd

def house(x):
    gray = rd.uniform(0.4,0.9)
    red = gray; green = gray; blue = gray
    tu.fillcolor((red, green, blue))
    tu.begin_fill()
    tu.pencolor('black')
    tu.forward(2*x); tu.left(90)
    tu.forward(x); tu.left(45)
    tu.pencolor('red')
    tu.forward(x); tu.left(90)
    tu.forward(x); tu.left(45)
    tu.pencolor('black')
    tu.forward(x); tu.left(90); tu.forward(x)
    tu.end_fill()
    if tu.xcor() < 200: house(20*rd.randint(3,10))
    
# main program
print(); print('Street')
tu.width(2) 
tu.up(); tu.hideturtle()
tu.setpos(-450,-200)
tu.down(); tu.forward(900); tu.setpos(-450,-200)
house(7*rd.randint(3,7))

tu.pencolor((0,0,0))
tu.up(); tu.hideturtle()
tu.setpos(-300,-300)

tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop()
tu.done()      