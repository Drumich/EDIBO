import turtle
import time

delay = 0.5

win = turtle.Screen()
win.title("Sneaky Snake")
win.bgcolor("green")
win.setup(width=600,height=600)
win.tracer(0) # ??

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,100)
head.direction = "down"


def move():
    if head.direction == "up":
        y = head.ycor() 
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


while True:
    win.update()
    move()
    time.sleep(delay)


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"



win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")









