from turtle import Turtle


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto(0, 255)
        self.color("white")
        self.right_score = 0
        self.left_score = 0
        self.write_score()
   
    
    def write_score(self):
        self.clear()
        self.write(f"{self.left_score} : {self.right_score}",align="center", font=("Arial", 40, "normal")) 
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over",align="center", font=("Arial", 40, "normal")) 
    
    def increase_right (self):
        self.right_score += 1
        self.write_score()

       
    def increase_left (self):
        self.left_score += 1
        self.write_score()