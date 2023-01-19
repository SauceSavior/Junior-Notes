import turtle as t
import random as r

wn=t.Screen()

ball=t.Turtle()
ball.shape("circle")
ball.speed(0)

courtHeight=600
courtWidth=1000
ballSize=15


def drawField():
    pass

def resetBall():
    ball.setpos(0,0)
    if r.randint(0,1)==0:
        ball.setheading(r.randint(150,210))
    else:
        ball.setheading(r.randint(-30,30))
    

def move():
    ball.fd(20)
    x,y=ball.pos()
    
    if y>courtHeight/2-ballSize or y<(-courtHeight/2-ballSize):
        ball.setheading(-ball.heading())
    if y>courtWidth/2-ballSize or y<(-courtWidth/2-ballSize):
        ball.setheading(-ball.heading())
        
        

wn.onkeypress(resetBall,"r")
wn.listen()        



wn.mainloop()