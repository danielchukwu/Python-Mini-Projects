STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()


    def up(self):
        self.forward(MOVE_DISTANCE)


    def down(self):
        if self.ycor() > STARTING_POSITION[1]:
            self.backward(MOVE_DISTANCE)


    def go_to_start(self):
        self.goto(STARTING_POSITION)