from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    cars = []
    move_distance = STARTING_MOVE_DISTANCE

    def __init__(self):
        super().__init__()
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.goto(320, random.randint(-270, 290))
        self.turtlesize(stretch_len=2)
        CarManager.cars.append(self)

    @staticmethod
    def move():
        for car in CarManager.cars:
            car.forward(CarManager.move_distance)
            if car.xcor() <= -320:
                CarManager.cars.remove(car)
        print(len(CarManager.cars))

    @staticmethod
    def increase_speed():
        CarManager.move_distance += MOVE_INCREMENT
