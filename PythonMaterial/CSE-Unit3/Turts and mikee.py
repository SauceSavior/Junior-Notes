#import library alias name
import turtle as t

#global variables
myTurts = []
tShapes=["classic","turtle","square","circle","triangle","arrow","classic","turtle","square","circle","triangle","arrow"]*5
tColors=["red","green","blue","cyan","purple","pink","red","green","blue","cyan","purple","pink"]*5

#creating our turtles
for i in range(len(tShapes)):
     mikey=t.Turtle(shape=tShapes[i])
     mikey.color(tColors[i])
     mikey.penup()
     mikey.speed(0)
     myTurts.append(mikey)


#run the turtles
startx,starty,direction,grow=0,0,90,0
for turt in myTurts:
    turt.goto(startx,starty)
    turt.setheading(direction)
    turt.pendown()
    turt.right(30)
    turt.forward(1+grow)
    direction=turt.heading()
    
    
    startx=turt.xcor()
    starty=turt.ycor()
    grow+=3
while True:        
    for i in range(len(myTurts)-1):
        nextX,nextY=myTurts[i+1].xcor(),myTurts[i+1].ycor()
        myTurts[i].goto(nextX,nextY)





wn=t.Screen()
wn.mainloop()