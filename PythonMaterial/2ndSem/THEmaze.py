#---- powershelll config
#cd .\Documents\22-23_am_notes\Python_Material\TMNT\Section2\MazeRunner\
#---- imports
import turtle as t
import random as r
import time
#---- global variables
wn=t.Screen()
wallLength=15
numberOfWalls=25
pathWidth=15
barrier=15
#---- initialize turtles
timer=t.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(250,-140)
timer.pensize(20)
timer.pendown()
timeLeft=0
mazeDrawer = t.Turtle()
enemyRunner=t.Turtle()
enemyRunner.shapesize(.5)
enemyRunner.penup()
mazeDrawer.pensize(5)
mazeDrawer.pencolor("blue")
mazeDrawer.speed(0)
mazeRunner = t.Turtle(shape="classic")
mazeRunner.shapesize()
mazeRunner.speed(0.5)
mazeRunner.penup()
#---- functions 
def drawDoor(pos):
    mazeDrawer.fd(pos)
    mazeDrawer.penup()
    mazeDrawer.fd(pathWidth*2)
    mazeDrawer.pd()
def drawBarrier(pos):
    mazeDrawer.fd(pos)
    mazeDrawer.left(90)
    mazeDrawer.fd(pathWidth*2)
    mazeDrawer.fd(-pathWidth*2)
    mazeDrawer.right(90)
def drawMaze():
    wallLength=15
    for w in range(numberOfWalls):
        wallLength+=pathWidth
        if w >4:
            mazeDrawer.left(90)
            #where do we draw the door and the barriers inside of a walll length
            doorSpot=r.randint(pathWidth*2,(wallLength-2*pathWidth))
            barrierSpot=r.randint(pathWidth*2,(wallLength-2*pathWidth))
            #check to make sure a door and barrier do not render on top of each other
            while abs(doorSpot-barrierSpot)< pathWidth:
                doorSpot=r.randint(pathWidth*2,(wallLength-2*pathWidth))
            #draw the wall
            if(doorSpot<barrierSpot):
                drawDoor(doorSpot)
                drawBarrier(barrierSpot-doorSpot-pathWidth*2)
                mazeDrawer.fd(wallLength-barrierSpot)
            else:
                drawBarrier(barrierSpot)
                drawDoor(doorSpot-barrierSpot)
                mazeDrawer.fd(wallLength-doorSpot-pathWidth*2)
    for i in range(4):
        mazeDrawer.left(90)
        wallLength+=pathWidth
        mazeDrawer.forward(wallLength)
    mazeDrawer.hideturtle()
def goUp():
    mazeRunner.setheading(90)
    mazeRunner.fd(5)
def goLeft():
    mazeRunner.setheading(180)
    mazeRunner.fd(5)
def goDown():
    mazeRunner.setheading(270)
    mazeRunner.fd(5)
def goRight():
    mazeRunner.setheading(0)
    mazeRunner.fd(5)
def times():
    global timeLeft
    timer.clear()
    timeLeft+=1
    timer.write(f"{timeLeft}")
def go():
    wn
    mazeRunner.fd(1)
    enemyRunner.setheading(enemyRunner.towards(mazeRunner))
    enemyRunner.color("blue")
    enemyRunner.fd(.9)

    canvas=wn.getcanvas()
    x,y=mazeRunner.pos()
    items=canvas.find_overlapping(x+1,-y+1,x-1,-y-1)
    
    if(len(items)>0):
        canvasColor=canvas.itemcget(items[0],"fill")
        if canvasColor=="blue":
            mazeRunner.goto(0,0)
            wn.onkeypress(None,"Space")
            return

    wn.ontimer(go,15)
def pause():
    enemyRunner.speed(None)
    mazeRunner.speed(None)
    timer.speed(None)
#---- events
wn.onkeypress(goUp,"w")
wn.onkeypress(goLeft,"a")
wn.onkeypress(goDown,"s")
wn.onkeypress(goRight,"d")
wn.onkeypress(go,"Return")
wn.ontimer(times,1000)
wn.onkeypress(pause,"p")
wn.listen()
#---- main loop
drawMaze()
wn.mainloop()