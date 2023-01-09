import turtle as t 
import random as r

wn=t.Screen()
bob=t.Turtle()
bob.shape("turtle")
bob.shapesize(2)
bob.fillcolor("purple")
bob.speed(0)
bob.penup()

timer=5
fontStuff=font=("Comic Sans",30,"normal")
interval=1000
timekeeper=t.Turtle()
timekeeper.penup()
timekeeper.hideturtle()
timekeeper.goto(-100,200)
timekeeper.pendown()
timekeeper.speed(0)

wn=t.Screen()
scorekeeper=t.Turtle()
scorekeeper.penup()
scorekeeper.hideturtle()
scorekeeper.goto(100,200)
scorekeeper.pendown()
scorekeeper.speed(0)
fontStuff=font=("Comic Sans",30,"normal")


def updatetimer():
    global timer
    timekeeper.clear()
    if timer<=0:
        timekeeper.write("Times Up!",font=fontStuff)
    else:
        timer-=1
        timekeeper.write(f"Timer: {timer}",font=fontStuff)
        timekeeper.getscreen().ontimer(updatetimer,interval)


def bobClicked(x,y):
    if timer<=0:
        timekeeper.write(f"Timer: {timer}",font=fontStuff)
    else:
        print("bob was clicked")
        print(x,y)
        moveBob()

def moveBob():
    newX=r.randint(-300,300)
    newY=r.randint(-300,300)
    bob.goto(newX,newY)

score=0
def updateScore(x,y):
    global score
    score+=1
    scorekeeper.clear()
    scorekeeper.write(f"score: {score}",font=fontStuff)
wn.onscreenclick(updateScore)




bob.onclick(bobClicked)

wn.ontimer(updatetimer,interval)


wn.mainloop()