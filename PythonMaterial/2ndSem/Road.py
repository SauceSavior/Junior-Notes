import turtle as t

timmy=t.Turtle()
jeff=t.Turtle()

t.Screen().bgcolor("gray")
timmy.speed(10)
jeff.speed(10)
def white():     
    for i in range (8):
        jeff.forward(10)
        jeff.penup()
        jeff.forward(10)
        jeff.pendown



timmy.penup()
timmy.goto(-350,0)
timmy.pendown()
for i in range(4):
    timmy.forward(200)
    timmy.left(90)
    timmy.forward(200)
    timmy.right(90)
    timmy.forward(200)
    timmy.right(90)
white()


