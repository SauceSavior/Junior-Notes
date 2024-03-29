from turtle import Screen, Turtle

COLOR = (0.502,0.898,1.0)  # (154, 0, 254)
TARGET = (1,1,1)  # (221, 122, 80)

screen = Screen()
screen.tracer(False)

WIDTH, HEIGHT = screen.window_width(), screen.window_height()

deltas = [(hue - COLOR[index]) / HEIGHT for index, hue in enumerate(TARGET)]

turtle = Turtle()
turtle.color(COLOR)

turtle.penup()
turtle.goto(-WIDTH/2, HEIGHT/2)
turtle.pendown()

direction = 1

for distance, y in enumerate(range(HEIGHT//2, -HEIGHT//2, -1)):

    turtle.forward(WIDTH * direction)
    turtle.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
    turtle.sety(y)

    direction *= -1

screen.tracer(True)
screen.exitonclick()