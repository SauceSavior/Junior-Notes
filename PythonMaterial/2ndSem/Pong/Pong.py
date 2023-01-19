import turtle as t
import random as r

wn=t.Screen()

ball=t.Turtle()
ball.shape("circle")
ball.speed(0)
courtHeight=600
courtWidth=1000
wn.screensize(courtWidth+50,courtHeight+50)
courtHeight=600
courtWidth=1000
ballSize=15
man=t.Turtle()
man.speed(0)
man.pensize(3)
paddleWidth=70
fontSettings = ("Arial",80,"normal")
leftScore=0
rightScore=0


def drawField():
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
def resetBall():
    ball.setpos(0,0)
    if r.randint(0,1)==0:
        ball.setheading(r.randint(150,210))
    else:
        ball.setheading(r.randint(-30,30))
def moveBall():
    global leftScore, rightScore
    ball.penup()
    ball.fd(20)
    x,y=ball.pos()
    
    if y>courtHeight/2-ballSize or y<(-courtHeight/2-ballSize):
        ball.setheading(-ball.heading())
    elif y>courtWidth/2-ballSize or y<(-courtWidth/2-ballSize):
        if x>courtWidth/2:
            leftScore+=1
            lScore.clear()
            lScore.write(leftScore,font=fontSettings)
        elif x<-courtWidth/2:
            rightScore+=1
            rScore.clear()
            rScore.write(rightScore,font=fontSettings)
        resetBall()
    else:
        collidePaddle(leftPlayer,ball)
        collidePaddle(rightPlayer,ball)
    
        
        
    wn.ontimer(moveBall,20)


leftPlayer=t.Turtle("square")
leftPlayer.color("red")
leftPlayer.penup()
leftPlayer.speed(0)
leftPlayer.setx(-courtWidth/2)
leftPlayer.turtlesize(4,1)

rightPlayer=t.Turtle("square")
rightPlayer.color("blue")
rightPlayer.penup()
rightPlayer.speed(0)
rightPlayer.setx(courtWidth/2)
rightPlayer.turtlesize(4,1)

rScore=t.turtle(visible=False)
rScore.speed(0)
rScore.penup()
rScore.setpos(courtWidth/4,courtHeight/4)
rScore.write(rightScore,font=fontSettings)

lScore=t.turtle(visible=False)
lScore.speed(0)
lScore.penup()
lScore.setpos(courtWidth/4,courtHeight/4)
lScore.write(leftScore,font=fontSettings)


def upLeft():
    if leftPlayer.ycor()<(courtHeight/2-paddleWidth):
        leftPlayer.sety(leftPlayer.ycor()+20)  
def downLeft():
    if leftPlayer.ycor()>(-courtHeight/2+paddleWidth):
        leftPlayer.sety(leftPlayer.ycor()-20)         
def upRight():
    if rightPlayer.ycor()<(courtHeight/2-paddleWidth):
        rightPlayer.sety(rightPlayer.ycor()+20)  
def downRight():
    if rightPlayer.ycor()>(-courtHeight/2+paddleWidth):
        rightPlayer.sety(rightPlayer.ycor()-20)      
def collidePaddle(paddle,b):
    if paddle.distance(b)<paddleWidth:
        b.setheading(180-b.heading())
        if b.xcor()>0:
            b.setx(b.xcor()+10)
        else:
            b.setx(b.xcor()-10)
        b.fd(10)

wn.onkeypress(resetBall,"r")
wn.onkeypress(upLeft,"w")
wn.onkeypress(downLeft,"s")
wn.onkeypress(upRight,"Up")
wn.onkeypress(downRight,"Down")
wn.listen()        


drawField()
moveBall()
wn.mainloop()
