import turtle as t 

wn=t.Screen()
scorekeeper=t.Turtle()
scorekeeper.penup()
scorekeeper.goto(100,200)
scorekeeper.pendown()
scorekeeper.speed(0)
fontStuff=font=("Comic Sans",30,"normal")

score=0
def updateScore(x,y):
    global score
    score+=1
    scorekeeper.clear()
    scorekeeper.write(f"score: {score}",font=fontStuff)
wn.onscreenclick(updateScore)




wn.mainloop()