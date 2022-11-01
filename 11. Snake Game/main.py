# Python - 3.10
# Topic - Snake Game
# Program - Building the famous snake game from back in the 90's. Using the turtle module




# solution
import time
from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time


# Screen setups
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(0,0,0)
screen.tracer(n=0)

# Objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# Event Listeners
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


# Play game
game_is_on = True
speed = 0.3
while game_is_on:
   screen.update()
   time.sleep(speed)
   snake.move()


   # Detect collision with food.
   if snake.head.distance(food) <= 15:
      food.change_position()
      scoreboard.increase_score()
      snake.extend()

      # increase speed
      if (scoreboard.score % 5 == 0 and speed != 0.1 ):   # increase speed after 5th score
         speed = abs(speed - 0.020)
         print("boost up")

   # Detect collision with wall.
   if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
      scoreboard.increase_high_score()
      scoreboard.refresh_scoreboard()
      snake.restart_game()

   # Detect collision with snake body
   for segment in snake.segments[1:]:
      if snake.head.distance(segment) < 10:
         scoreboard.increase_high_score()
         scoreboard.refresh_scoreboard()
         snake.restart_game()




screen.exitonclick()