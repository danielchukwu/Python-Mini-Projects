import turtle

class StateManager(turtle.Turtle):


   def __init__(self) -> None:
      super().__init__()
      self.penup()
      self.hideturtle()
      
   def add_state(self, pos, state):
      print(pos)
      self.goto(pos)
      self.write(arg=state, align="center", font=("Courier", 8, "normal"))