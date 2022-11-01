import re
from turtle import Turtle

HIGH_SCORE_FILENAME = "./20. Build the Snake Game Part 1_ Animation & Coordinates/high_score.txt"

class Scoreboard(Turtle):


   def __init__(self) -> None:
      super().__init__()
      self.score = 0
      self.high_score = self.get_high_score()
      self.color("white")
      self.penup()
      self.goto(0, 250)
      self.update_scoreboard()
      self.hideturtle()  # this hides the turtle and makes the self.write(...) show up


   def get_high_score(self):
      """Get or Create the high_score.txt file"""
      try:
         # get high score
         with open(HIGH_SCORE_FILENAME) as file:
            contents = file.read()
            score_str = re.findall("\d*[0-9]", contents)[0]
            return int(score_str)

      except FileNotFoundError:
         # if high score file doesn't exist. create one.
         self.update_file_high_score(0)


   def update_file_high_score(self, score):
      with open(HIGH_SCORE_FILENAME, mode="w") as file:
         file.write(f"CURRENT HIGH SCORE = {score}")
         return 0


   def update_scoreboard(self):
      self.clear()
      self.write(f"Score: {self.score}   HighScore: {self.high_score}", align="center", font=('Arial', 18, 'bold'))


   def increase_score(self):
      self.score += 1
      self.update_scoreboard()


   def increase_high_score(self):
      if self.score > self.high_score:
         self.high_score = self.score
         self.update_scoreboard()

         # update high_score.txt file
         self.update_file_high_score(self.high_score)

   

   def refresh_scoreboard(self):
      self.score = 0
      self.update_scoreboard()
