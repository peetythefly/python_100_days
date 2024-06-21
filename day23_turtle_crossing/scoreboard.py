FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.up()
        self.goto(-280, 255)
        self.color("black")
        self.level = 1
        self.write_score()
   
    
    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left", font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over",align="center", font=("Arial", 40, "normal")) 
    
    def increase_level (self):
        self.level += 1
        self.write_score()