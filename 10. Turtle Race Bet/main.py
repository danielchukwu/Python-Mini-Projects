# # Turtle Event Listeners: we want to use this to listen to events that take place on the keyboard
from turtle import Turtle, Screen

# W = forwards
# S = backwards
# A = counterclockwise
# D = clockwise

tim = Turtle()
screen = Screen()

def move_forwards():
   tim.forward(20)
def move_backwards():
   tim.backward(20)

def move_left():
   tim.setheading( tim.heading() + 10 )
def move_right():
   tim.setheading(  tim.heading() - 10 )

def clear():
   tim.clear()
   tim.penup()
   tim.home()
   tim.pendown()

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=clear, key="c")



screen.exitonclick()
