import turtle
import time

delay = 0.1

win = turtle.Screen()
win.title("Sneaky Snek")
win.bgcolor("green")
win.setup(width=600,height=600)
win.tracer(0) # ??

head = turtle.Turtle()
head.speed(1)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"


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


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_right, "d")
win.onkeypress(go_left, "a")

while True:
    win.update()
    move()
    time.sleep(delay)










