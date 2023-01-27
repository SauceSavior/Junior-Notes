import turtle as t 

wn=t.Screen()
courtHeight=600
courtWidth=1000
wn.screensize(courtHeight+50,courtWidth+50)


man=t.Turtle()
man.speed(0)
man.pensize(3)
def area():
    man.penup()
    man.goto(-courtHeight,courtWidth)
    man.pendown()
    man.degrees(90)
    man.forward(courtHeight)
    man.right(90)
    man.forward(courtWidth)
    man.right(90)
    man.forward(courtHeight)
    man.right(90)
    man.forward(courtWidth)
    
    
    
area() 
wn.mainloop()