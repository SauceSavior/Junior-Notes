import turtle as t 

wn=t.Screen()
courtHeight=600
courtWidth=1000

man=t.Turtle()
man.speed(0)
man.pensize(3)

def courtt():
    man.penup()
    man.goto(-courtWidth/2,courtHeight/2)
    man.pendown()
    man.forward(courtWidth)
    man.right(90)
    man.forward(courtHeight)
    man.right(90)
    man.forward(courtWidth)
    man.right(90)
    man.forward(courtHeight)
    man.right(90)
    man.forward(courtWidth/2)
    man.right(90)
    for i in range(15):
        man.forward(26)
        man.penup()
        man.forward(15)
        man.pendown()    
    
    
    
courtt()
wn.mainloop()