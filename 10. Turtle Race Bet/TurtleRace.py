# Python - 3.10
# Topic - Turtle Racing Game
# Program - Create a turtle racing game using our turtle package




# solution
import random
from turtle import Turtle, Screen



screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

color_list = ['black', 'green', 'red', 'blue', 'purple', 'yellow']
y_positions = [-70, -40, -10, 20, 50, 80]
turtles_list = []

for i in range(0, 6):
   tim = Turtle(shape="turtle")
   tim.penup()
   tim.color( color_list[i] )
   tim.goto( x=-220, y= y_positions[i] )
   turtles_list.append(tim)


if user_bet:
   race_is_on = True

while race_is_on:

   for turtle in turtles_list:
      if turtle.xcor() > 230:
         race_is_on = False
         winning_color = turtle.pencolor()
         if (winning_color == user_bet):
            print(f"You've won! The {winning_color} turtle is the winner.")
         else:
            print(f"You've lost! The {winning_color} turtle is the winner.")

      rand_distance = random.randint(0, 10)
      turtle.forward( rand_distance )


screen.exitonclick()
