from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 7
MOVE_INCREMENT = 6


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()

    def create_cars(self):
        if len(self.cars) < 15:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_x = random.randrange(320, 800, 80)
            new_y = random.randrange(-240, 260, 20)
            new_car.goto(new_x, new_y)
            new_car.setheading(180)
            self.cars.append(new_car)

    def move(self, current_level):
        current_speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT*(current_level-1)
        for car in self.cars:
            car.forward(current_speed)

    def delete_cars(self):
        for car in self.cars:
            if car.xcor() < -320:
                self.cars.remove(car)
                self.create_cars()




