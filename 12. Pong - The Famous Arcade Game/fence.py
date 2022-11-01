from turtle import Turtle


class Fence(Turtle):


   def __init__(self):
      super().__init__()
      self.color("white")
      self.penup()
      self.goto(x=0, y=300)
      self.pensize(width=5)
      self.pendown()
      self.setheading(270)
      self.draw_fence()
      self.pen(outline=1)

   def draw_fence(self):
      
      for _ in range(15):
         self.forward(20)
         self.penup()
         self.forward(20)
         self.pendown()
