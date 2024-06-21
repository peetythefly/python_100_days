from turtle import Turtle
import random


class Food(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        # Create initial coordinates.
        self.serve_food()   
    
    def serve_food(self):
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)
        