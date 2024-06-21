from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self, shape: str = "square", undobuffersize: int = 1000, visible: bool = False) -> None:
        self.car_flood = []
        self.move_factor = 1
        
    def create_car(self):
        car_chance = random.randint(1, 6)
        if car_chance == 6:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.up()
            car.left(180)
            car.color (random.choice(COLORS))
            y_pos = random.randint(-250, 250)
            car.goto(300, y_pos)
            car.showturtle()
            self.car_flood.append(car) 
    
    
    def drive(self):
        for auto in self.car_flood:
            auto.forward(MOVE_INCREMENT * self.move_factor)
            while len(self.car_flood) > 20:
                self.car_flood.pop(0)