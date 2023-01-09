#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

def moveUp():
  robot.setheading(90)
  robot.fd(50)
def moveDown():
  robot.setheading(270)
  robot.fd(50)
def moveLeft():
  robot.setheading(180)
  robot.fd(50)
def moveRight():
  robot.setheading(0)
  robot.fd(50)
       
       


#----- init screen
wn = trtl.Screen()

wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)
wn.bgpic("maze1.png")
#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()


# for i in range(4):
#   move()
# for i in range(3):
#   turn_left()
# for i in range(4):
#   move()

# for i in range(4):
#   move()
#   for i in range(3):
#     turn_left()
#   move()
#   turn_left()
  
ui=input("w,a,s,d")
#obviously, check for user input

  
  
#---- end robot movement 

wn.mainloop()