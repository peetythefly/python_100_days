import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.title("Playing in Traffic")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.drive()
    # Detect crunch.
    for car in car_manager.car_flood:
        if car.distance(player) < 20:
            game_is_on = False
    if player.ycor() > 280:
        player.finish()
        car_manager.move_factor *= 1.1
        score.increase_level()
        print(f"Move factor is {car_manager.move_factor}.") 

score.game_over()
    
screen.exitonclick()