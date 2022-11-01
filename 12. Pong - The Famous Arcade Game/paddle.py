MOVE_BY = 20
MAX_Y = 260

from turtle import Turtle

class Paddle(Turtle):


   def __init__(self, position) -> None:
      super().__init__()
      self.penup()
      self.color("white")
      self.shape("square")
      self.shapesize(stretch_wid=5, stretch_len=1)
      self.goto(position)

   
   def up(self):
      new_y = self.ycor() + MOVE_BY
      old_x = self.xcor()
      if new_y < MAX_Y:
         self.goto((old_x, new_y))
   
   
   def down(self):
      new_y = self.ycor() - MOVE_BY
      old_x = self.xcor()
      if new_y > -(MAX_Y):
         self.goto((old_x, new_y))



