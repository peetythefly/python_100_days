from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("black")
        self.left(90)
        self.up()
        self.goto(STARTING_POSITION)
        self.showturtle()
    
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    
    def finish(self):
        self.goto(STARTING_POSITION)