# (c) drthpeters

import turtle as tu
import math

def bulge(h,h2,step):
    if step == 1:
        tu.left(45); tu.forward(h2)
        tu.right(90); tu.forward(h2)
        tu.right(90); tu.forward(h2)
        tu.left(45)
        
    else: 
        tu.left(45); passage(h,h2,step-1)
        tu.left(45); tu.forward(h2)
        for i in range(3):
            bulge(h,h2,step-1); tu.forward(h2)
        tu.left(45); passage(h,h2,step-1)
        tu.left(45)

def passage(h,h2,step):
    if step == 1:
        tu.forward(h2)
    else:
        passage(h,h2,step-1)
        tu.left(45); tu.forward(2*h)
        bulge(h,h2,step-1)
        tu.forward(2*h); tu.left(45)
        passage(h,h2,step-1)

# main program
print('Sierpinski Curve')
n = int(input('n = (1,...,6) '))

# preparations
h0 = 200
for i in range(n):
    h0 = h0*(4+math.sqrt(2))/(8+3*math.sqrt(2))
h = round(h0); h2 = round(math.sqrt(2)*h0)

tu.width(2) 
tu.speed(5)
tu.up(); tu.setpos(-100,60); tu.down()
tu.left(90)

for i in range(4):
    bulge(h,h2,n); tu.forward(2*h)

tu.up(); tu.hideturtle()
tu.setpos(-400,-300)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop()
tu.done() 