import turtle as tu

def square(a):
    for i in range(4): tu.forward(a); tu.right(90)
    
def tree(width):
    if width > 3:
        x = tu.xcor()
        y = tu.ycor()
        if width > 10: tu.pencolor((0.85,0.55,0))
        else: tu.pencolor((0,0.85,0))
        tu.left(alpha)
        square(3*width)
        tu.forward(round(3*width))
        tree(round(0.6*width))
        tu.penup(); tu.back(round(3*width)); tu.pendown()
        if width > 10: tu.pencolor((0.85,0.55,0))
        else: tu.pencolor((0,0.85,0))
        tu.right(90)
        tu.forward(round(3*width))
        square(4*width)
        tu.forward(round(4*width))
        tree(round(0.8*width))
        tu.penup(); tu.setpos(x,y); tu.pendown()
        tu.left(90-alpha)
        
# constants
width = 30
alpha = 53
       
tu.penup()
tu.setx(-100)
tu.sety(-100)
tp = tu.pos()
tu.pendown(); tu.width(2); tu.pencolor((0.85,0.55,0))
square(5*width)
tu.setpos(tp)
tu.left(90)
tree(width)

tu.hideturtle(); tu.penup()
tu.setpos(-400,-330)
tu.pencolor((0,0,0))
tu.write('finished!',font = ("Arial",12,"normal"))
tu.mainloop(); tu.done()
