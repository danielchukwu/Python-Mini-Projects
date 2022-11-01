STARTING_POSITIONS = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0),]
MOVE_DISTANCE = 20

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

import time
from turtle import Turtle, Screen

class Snake:


   def __init__(self) -> None:
      self.segments = []
      self.create_snake(3)
      self.head = self.segments[0]  # We created this variable for easier access to the head. Because we will be using it a lot in our code

   def create_snake(self, num):
      for position in STARTING_POSITIONS:
         self.add_segment(position)

   def restart_game(self):
      for segment in self.segments:
         segment.hideturtle()
      self.__init__()

   def add_segment(self, position):
      segment = Turtle(shape="square")
      segment.color("white")
      segment.penup()
      segment.goto(position)
      self.segments.append(segment)

   def extend(self):
      self.add_segment( self.segments[-1].position() )

   def move(self):
      for i in range(len(self.segments) - 1, 0, -1):
         new_x = self.segments[i-1 ].xcor()
         new_y = self.segments[i-1].ycor()
         self.segments[i].goto((new_x, new_y))

      self.segments[0].forward(MOVE_DISTANCE)

   def up(self):
      if self.head.heading() != DOWN:
         self.segments[0].setheading(90)

   def down(self):
      if self.head.heading() != UP:
         self.segments[0].setheading(270)

   def left(self):
      if self.head.heading() != RIGHT:
         self.segments[0].setheading(180)

   def right(self):
      if self.head.heading() != LEFT:
         self.segments[0].setheading(0)