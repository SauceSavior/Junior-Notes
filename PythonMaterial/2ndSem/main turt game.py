import turtle as t 

wn=t.Screen()
bob=t.Turtle()
bob.shape("turtle")
bob.shapesize(2)
bob.fillcolor("purple")
bob.speed(0)

def bobClicked(x,y):
    print("bob was clicked")

bob.onclick(bobClicked)





wn.mainloop()