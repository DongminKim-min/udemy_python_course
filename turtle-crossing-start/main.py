import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
current_level = 1
while game_is_on:
    time.sleep(0.1)
    scoreboard.show_score(current_level)
    screen.update()

    "create random cars and make them move"
    car.create_cars()
    car.move(current_level)
    car.delete_cars()

    "detect collision"
    for a_car in car.cars:
        if abs(a_car.xcor() - player.xcor()) < 25 and abs(a_car.ycor() - player.ycor()) < 25:
            scoreboard.game_over()
            game_is_on = False

    "check if the turtle finished the round / level up"
    if player.check_finish() is True:
        current_level += 1
        scoreboard.show_score(current_level)


screen.exitonclick()