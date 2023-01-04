
# (c) drthpeters

import turtle as tu
import random as rd

def shape(count,x):
    red = rd.uniform(0,1)
    green = rd.uniform(0,1)
    blue = rd.uniform(0,1)
    tu.pencolor((red,green,blue))
    for i in range(n):
        tu.forward(x)
        tu.right(angle)
    tu.right(7)
    if count < 360/7: shape(count+1,x)
    
# main program
print(); print('Rosette') 
n = int(input('Number of edges (3..6): '))   
angle = 360/n
tu.width(2)    
shape(0,600/n)
tu.up(); tu.hideturtle()
tu.setpos(-300,-150)
tu.pencolor((0,0,0))

tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop()
tu.done()      