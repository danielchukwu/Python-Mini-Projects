# constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# imports
import random
from turtle import Turtle



class CarManager:
    

    def __init__(self) -> None:
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_a_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1: 
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            rand_color = random.choice( COLORS )
            new_car.color( rand_color )

            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)

            self.cars.append(new_car)


    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT