from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create(self):
        l = random.randint(1, 6)
        if l == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-200, 280)
            new_car.goto(280, new_y)
            self.cars.append(new_car)


    def move(self):
        for i in self.cars:
            i.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

