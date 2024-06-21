from turtle import Turtle


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto(0, 275)
        self.color("white")
        self.score = 0
        import os
        print(os.getcwd())
        # Get the high score from the saved file.
        with open(file="data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.write_score()
   
    
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}",align="center", font=("Arial", 20, "normal")) 
    

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Write the new high score to the data file.
            with open(file="data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()
   
    def increase_score(self):
        self.score += 1

       