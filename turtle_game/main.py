import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
scoreboard=Scoreboard()
car_manager=CarManager()
screen.listen()
screen.onkey(player.go_up,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()

    if player.is_finish_line():
        player.gotostart()
        car_manager.levl_up()
        scoreboard.increase_level( )

screen.exitonclick()