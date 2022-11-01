# Python - 3.10
# Topic - The Pong Game
# Program - Building yet another game




# solution
from turtle import Turtle, Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from fence import Fence

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# create first paddle and manager
paddle_l = Paddle((-360, 0))
paddle_r = Paddle((360, 0))
ball = Ball()
fence = Fence()
scoreboard = Scoreboard()
# screen.tracer(1)


screen.listen()
screen.onkeypress(fun=paddle_r.up, key="Up")
screen.onkeypress(fun=paddle_r.down, key="Down")

screen.onkeypress(fun=paddle_l.up, key="w")
screen.onkeypress(fun=paddle_l.down, key="s")


game_is_on = True
BOUNDARY = 380
SPEED = 0.05
while game_is_on:
   time.sleep(ball.move_speed)
   screen.update()
   ball.move()

   # Detect collision with top & bottom wall
   if ball.ycor() > 280 or ball.ycor() < - 270:
      print("bounce")
      ball.bounce_y()

   # Detect collision with paddle
   if (ball.distance(paddle_l) < 50 and ball.xcor() < -320)   or   (ball.distance(paddle_r) < 50  and ball.xcor() > 320) :
      ball.bounce_x()
      SPEED = SPEED - 0.005 if (SPEED - 0.005) > 0.02 else SPEED

   # Detect R paddle misses
   if ball.xcor() >= BOUNDARY:
      ball.reset_position()
      scoreboard.increase_l_score()

   # Detect L paddle misses
   if ball.xcor() <= -BOUNDARY:
      ball.reset_position()
      scoreboard.increase_r_score()

   


screen.exitonclick()