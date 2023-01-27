import turtle as t 
import random as r
import leaderboard as lb
#https://www.geeksforgeeks.org/play-sound-in-python/ 
from playsound import playsound

#https://www.geeksforgeeks.org/how-to-create-custom-turtle-shapes-in-python/
dimondTurtle = t.Turtle()
shape =((0,-2), (10, 2), (4, -8), (7, 10))
t.register_shape('diamond', shape)
dimondTurtle.shape('diamond')
dimondTurtle.hideturtle()

global z
global y
wn=t.Screen()
start=t.Turtle()
bob=t.Turtle()
bob.shape("diamond")
z=2
bob.shapesize(z)
bob.fillcolor("purple")
bob.speed(0)
bob.penup()

timer=20
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
FILENAME='Database.txt'


def updatetimer():
    global timer
    timekeeper.clear()
    if timer<=0:
        timekeeper.write("Times Up!",font=fontStuff)
        bob.hideturtle()
        manageLeaderboard()
    else:
        timer-=1
        timekeeper.write(f"Timer: {timer}",font=fontStuff)
        timekeeper.getscreen().ontimer(updatetimer,interval)

def bobClicked(x,y):
    global z
    if timer<=0:
        timekeeper.write(f"Timer: {timer}",font=fontStuff)
    else:
        print("bob was clicked")
        print(x,y)
        playsound('C:/Users/Clone Troopers/Documents/Junior-Notes/PythonMaterial/2ndSem/heheh-103101.mp3')
        moveBob()
        z=z*.5
        if z<=1:
            z=2
        global score
        score+=1
        scorekeeper.clear()
        scorekeeper.write(f"score: {score}",font=fontStuff)
        
def moveBob():
    bob.color("red")
    bob.stamp()
    bob.color("purple")
    wn.bgcolor("red")
    newX=r.randint(-300,300)
    newY=r.randint(-300,180)
    bob.goto(newX,newY)
    wn.bgcolor("white")
score=0

def manageLeaderboard():
    namesList=lb.getNames(FILENAME)
    scoresList=lb.getScores(FILENAME)
    if(len(scoresList)<5 or score>int(max(scoresList[-1]))):
        name=input("Congrats, you're on the board! \n\tName Please: ")
        lb.updateLeaderboard(FILENAME,namesList,scoresList,name,score)
    else:
        print("did not make it")
    
    lb.draw_leaderboard(False,namesList,scoresList,scorekeeper,10)
    
    
    

bob.onclick(bobClicked)

wn.ontimer(updatetimer,interval)

wn.mainloop()