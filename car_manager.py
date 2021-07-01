from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        super().__init__()
        self.cars_array=[]
        self.set_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1,6)

        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.setheading(180)
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.setpos(280, random.randint(-250, 250))
            self.cars_array.append(new_car)

        else:
            pass

    def move(self):

        for car in self.cars_array:

            car.forward(self.set_speed)

    def increase_speed(self):
        self.set_speed += MOVE_INCREMENT

