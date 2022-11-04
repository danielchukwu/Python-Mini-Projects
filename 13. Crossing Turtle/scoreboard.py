# constants
FONT = ("Courier", 14, "normal")


# imports
from turtle import Turtle

class Scoreboard(Turtle):
    

    def __init__(self) -> None:
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(x=-230, y=260)
        self.refresh_level()
        self.hideturtle()


    def refresh_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)


    def next_level(self):
        self.level += 1
        self.refresh_level()

    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=FONT)
