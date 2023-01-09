import turtle as t 

wn=t.Screen()
timer=5
fontStuff=font=("Comic Sans",30,"normal")
interval=1000

timekeeper=t.Turtle()
timekeeper.penup()
timekeeper.hideturtle()
timekeeper.goto(-100,200)
timekeeper.pendown()
timekeeper.speed(0)


def updatetimer():
    global timer
    timekeeper.clear()
    if timer<=0:
        timekeeper.write("Times Up!",font=fontStuff)
    else:
        timer-=1
        timekeeper.write(f"Timer: {timer}",font=fontStuff)
        timekeeper.getscreen().ontimer(updatetimer,interval)
    

wn.ontimer(updatetimer,interval)





wn.mainloop()