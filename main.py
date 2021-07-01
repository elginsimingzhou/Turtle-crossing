import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()

scoreboard = Scoreboard()
scoreboard.display()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    #Detect collision with car
    for car in car_manager.cars_array:
        if player.distance(car)<20:
            scoreboard.game_over()
            game_is_on = False

    #Detect successful crossing
    if player.reset():
        scoreboard.clear()
        scoreboard.level_up()
        car_manager.increase_speed()

screen.exitonclick()
