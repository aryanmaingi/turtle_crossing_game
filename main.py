import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.move_up, "Up")
screen.update()
level = 1
game_is_on = True
while game_is_on:
    time.sleep(turtle.level_up_time(level))
    screen.update()
    car.create()
    car.move()

    #detect collision with cars
    for i in car.cars:
        if i.distance(turtle) < 20:
            game_is_on = False
            screen.clear()
            score.game_over()

    #detect reaching end
    if turtle.finish():
        level += 1
        car.level_up()
        score.level_up()
        time.sleep(1)
        turtle.go_to_start()



screen.exitonclick()