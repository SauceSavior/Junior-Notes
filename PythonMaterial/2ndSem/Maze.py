import turtle as t

wn=t.Screen()

mazeMan=t.Turtle()
mazeMan.pensize(5)
# mazeMan.pencolor("blue")
mazeMan.speed(0)

x=10
for i in range(20):
    mazeMan.hideturtle()
    mazeMan.forward(x)
    mazeMan.left(90)
    for j in range (2):
        mazeMan.penup()
        mazeMan.forward(40)
        mazeMan.pendown()
        mazeMan.left(90)
        mazeMan.forward(30)
        mazeMan.right(90)
        for k in range(2):
            mazeMan.forward(20)
            mazeMan.penup()
            mazeMan.forward(30)
            mazeMan.pendown()

    # for every x in x pen up then pen down after y
    x+=15


wn.mainloop() 
