from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.shape("circle")
        self.up()
        self.xmove = 10
        self.ymove = 10
    
    
    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    
    def bounce_wall(self):
        self.ymove = -(self.ymove)

        
    def bounce_paddle(self):
        self.xmove = -(self.xmove)
    
    def reset_to_start(self):
        self.goto(0,0)
        self.bounce_paddle()