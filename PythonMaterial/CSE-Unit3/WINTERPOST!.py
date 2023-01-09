 # matt.goto(380,325) top right
# matt.goto(-380,-315) bottom left
from turtle import Screen, Turtle
import random
matt = Turtle()
screen = Screen()

def background():
    COLOR = (0.502,0.898,1.0)  # (154, 0, 254)
    TARGET = (1,1,1)  # (221, 122, 80)
    screen.tracer(False)
    WIDTH, HEIGHT = screen.window_width(), screen.window_height()
    deltas = [(hue - COLOR[index]) / HEIGHT for index, hue in enumerate(TARGET)]
    matt.color(COLOR)
    matt.penup()
    matt.goto(-WIDTH/2, HEIGHT/2)
    matt.pendown()
    direction = 1
    for distance, y in enumerate(range(HEIGHT//2, -HEIGHT//2, -1)):
        matt.forward(WIDTH * direction)
        matt.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
        matt.sety(y)
        direction *= -1

    #https://stackoverflow.com/questions/63999474/how-do-i-make-a-linear-gradient-with-python-turtle

def trunk():
    print(matt.xcor(),matt.ycor())
    matt.showturtle()
    matt.fillcolor("brown")
    matt.color("brown")
    matt.begin_fill()
    matt.forward(30)
    matt.left(90)
    matt.forward(50)
    matt.left(90)
    matt.forward(30)
    matt.left(90)
    matt.forward(50)
    matt.end_fill()

def leaf():
    matt.fillcolor("green")
    matt.color("green")
    matt.begin_fill()
    matt.right(180)
    matt.forward(60)
    matt.right(120)
    matt.forward(90)
    matt.right(120)
    matt.forward(90)
    matt.right(120)
    matt.forward(60)
    matt.end_fill()

def star():
    matt.fillcolor("gold")
    matt.color("gold")
    matt.begin_fill()
    matt.forward(30)
    matt.right(144)
    matt.forward(30)
    matt.right(144)
    matt.forward(30)
    matt.right(144)
    matt.forward(30)
    matt.right(144)
    matt.forward(30)
    matt.right(144)
    matt.end_fill()

def tree():
    trunk()
    matt.backward(50)
    matt.left(90)
    matt.forward(30)
    leaf()
    matt.forward(30)
    matt.right(120)
    matt.forward(50)
    matt.right(60)
    matt.forward(35)
    leaf()
    matt.forward(30)
    matt.right(120)
    matt.forward(75)
    matt.left(10)
    matt.penup()
    matt.left(70)
    matt.forward(3)
    matt.right(70)
    matt.pendown()
    star()

def forest():
    matt.penup()
    matt.goto(random.randint(-300,300), random.randint(300,300))
    matt.pendown()

background()
for i in range(10):
    forest()
    tree()




screen.tracer(True)
screen.exitonclick() 

screen.mainloop()