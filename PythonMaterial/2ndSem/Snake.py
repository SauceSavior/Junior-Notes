import turtle as t 
import time
import random

wn=t.Screen()
wn.bgcolor("green")
wn.setup(width=600,height=600)

delay=.1
bodyParts=[]

head=t.Turtle(shape="square")
head.speed(1)
head.penup()
head.direction="stop"
head.color("black")

food=t.Turtle()
food.speed(0)
food.shape("turtle")
food.shapesize(.5,.5)
food.color("red")
food.penup()
food.goto(100,100)

def up():
    if head.direction != "down":
        head.direction="up"
def right():
    if head.direction != "left":
        head.direction="right"
def down():
    if head.direction != "up":
        head.direction="down"
def left():
    if head.direction != "right":
        head.direction="left"
def move():
    if head.direction=="up":
        head.sety(head.ycor()+20)
    if head.direction=="down":
        head.sety(head.ycor()-20)
    if head.direction=="left":
        head.setx(head.xcor()-20)
    if head.direction=="right":
        head.setx(head.xcor()+20)
def hideTheBodyParts():
    global bodyParts
    head.goto(0,0)
    head.direction="stop"
    for eachPart in bodyParts:
        eachPart.goto(1000,1000)
    bodyParts=[]
wn.onkeypress(up,"w")
wn.onkeypress(right,"d")
wn.onkeypress(down,"s")
wn.onkeypress(left,"a")
wn.listen()

while True:
    wn.update()
    if head.distance(food)<20:
        food.goto(random.randint(-280,280),random.randint(-280,280))
        part=t.Turtle(shape="circle")
        part.color("black")
        part.speed(0)
        part.penup()
        bodyParts.append(part)
    if len(bodyParts)>0:    
        x=head.xcor()
        y=head.ycor()
        bodyParts[0].goto(x,y)
    for i in range(len(bodyParts)-1,0,-1):
        x=bodyParts[i-1].xcor()
        y=bodyParts[i-1].ycor()
        bodyParts[i].goto(x,y)
    move()
    if head.xcor()>=300 or head.xcor()<=-300 or head.ycor()>=300 or head.ycor()<=-300:
        head.goto(0,0)
        for eachPart in bodyParts:
            eachPart.goto(1000,1000)
            bodyParts=[]
    for part in bodyParts:
        if part.distance(head)<10:
            hideTheBodyParts()
    
    time.sleep(delay)
wn.mainloop()