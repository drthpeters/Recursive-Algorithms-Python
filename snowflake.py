# (c) drthpeters

import turtle as tu
import random as rd

def flake(x):
    red = rd.uniform(0,1)
    green = rd.uniform(0,1)
    blue = rd.uniform(0,1)
    tu.pencolor(red, green, blue)
    for i in range(n):
        tu.forward(x)
        if x > 20: flake(0.4*x)
        tu.back(x)
        tu.right(angle)
      
# main program
print(); print('Snowflakes') 
n = int(input('Number of rays (3..6): '))   
angle = 360/n
x = 600/n
tu.width(2)    
flake(x)
tu.up(); tu.hideturtle()
tu.setpos(-300,-150)
tu.pencolor((0,0,0))

tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop()
tu.done()      