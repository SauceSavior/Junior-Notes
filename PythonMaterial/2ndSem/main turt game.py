import turtle as t 
import random as r
import leaderboard as lb

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
    if timer<=0:
        timekeeper.write(f"Timer: {timer}",font=fontStuff)
    else:
        print("bob was clicked")
        print(x,y)
        moveBob()
        global score
        score+=1
        scorekeeper.clear()
        scorekeeper.write(f"score: {score}",font=fontStuff)
        
def moveBob():
    newX=r.randint(-300,300)
    newY=r.randint(-300,180)
    bob.goto(newX,newY)

score=0

def manageLeaderboard():
    namesList=lb.getNames(FILENAME)
    scoresList=lb.getScores(FILENAME)
    if(len(scoresList)<5 or score>int(max(scoresList[-1]))):
        lb.updateLeaderboard(FILENAME,namesList,scoresList,"john",18)
        name=input("Congrats, you're on the board! \n\tName Please: ")
        lb.updateLeaderboard(FILENAME,namesList,scoresList,name,score)
    else:
        print("did not make it")
    
    lb.draw_leaderboard(False,namesList,scoresList,scorekeeper,10)




bob.onclick(bobClicked)

wn.ontimer(updatetimer,interval)


wn.mainloop()