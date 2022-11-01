import random
from turtle import Turtle
import turtle

class Food(Turtle):

   def __init__(self) -> None:
      super().__init__()
      self.shape("circle")
      self.penup()
      self.shapesize(0.5, 0.5)
      self.color("blue")
      self.speed("fastest")
      self.change_position()

   def change_position(self):
      new_x = random.randint(-280, 280)
      new_y = random.randint(-280, 280)
      self.goto(new_x, new_y)
      