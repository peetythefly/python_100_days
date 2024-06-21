from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVEMENT_SPEED = 20

class Snake:


    def __init__(self) -> None:
        # Create the segments and the first 3 segments
        self.segments = []
        # Create the starting segments.
        self.create_snake()
    
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.up()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)
        # Easy reference for the head of the snake.
        self.head = self.segments[0] 
    
    
    def extend(self):
        self.add_segment(self.segments[-1].pos())
    

    def check_collision(self):
        # There's no way to run into the first 3 segments so ignore those. If you 
        # don't then it will think it's colliding with the second segment.
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 17:
                return True
        return False
        
   
    def move(self):
        # Move the whole body except for the head, which is index 0. Do this by 
        # starting with the tail, and having it follow the segment in front of it.
        tail_to_neck = range(len(self.segments) - 1, 0, -1)
        for seg_num in tail_to_neck:
            # Get the position of the segment in front of the current segment.
            new_position = self.segments[seg_num - 1].pos()
            # Move this segment to the position of the one in front of it.
            self.segments[seg_num].goto(new_position)
        # Move the head forward (for now)
        self.head.forward(MOVEMENT_SPEED)     

    
    def turn(self, direction):
        # You can't turn back on yourself. Check if the turtle is 
        # trying to turn in the opposite direction it is already going.
        # Basically, look for a difference of 180 degrees.
        if direction - 180 != self.head.heading() and direction + 180 != self.head.heading():
            self.head.setheading(direction)
    
    def reset_to_start(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]