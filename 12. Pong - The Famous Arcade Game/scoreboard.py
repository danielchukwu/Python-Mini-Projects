FONT = ('Courier', 50, 'normal')

from re import S
from turtle import Turtle, update


class Scoreboard(Turtle):


   def __init__(self) -> None:
      super().__init__()
      self.l_score = 0
      self.r_score = 0
      self.shape("square")
      self.color("white")
      self.penup()
      self.update_score()
      self.hideturtle()
      
   
   def update_score(self):
      self.clear()
      self.goto(-100, 200)
      self.write(arg=f"{self.l_score}", align="center", font=FONT)
      self.goto(100, 200)
      self.write(arg=f"{self.r_score}", align="center", font=FONT)


   def increase_l_score(self):
      self.l_score += 1
      self.update_score()


   def increase_r_score(self):
      self.r_score += 1
      self.update_score()
      