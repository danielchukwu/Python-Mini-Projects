import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Python Turtle Graphics")
screen.tracer(0)


# Objects
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


# Event Listeners
screen.listen()
screen.onkeypress(fun=player.up, key="Up")
screen.onkeypress(fun=player.down, key="Down")



# game play
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_a_car()
    car_manager.move()
    
    # Detect player collision with car
    for car in car_manager.cars:
        if car.distance(player) <= 20:
            scoreboard.game_over()
            game_is_on = False

    # check if player has won.
    if player.ycor() >= 290:
        print("Next Level!")
        scoreboard.next_level()
        player.go_to_start()
        car_manager.level_up()
        



screen.exitonclick()