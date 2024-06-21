from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

# Create the board. 
screen = Screen()
# Set the correct size.
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create the paddles.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()
score.write_score()
# Listen for paddle movement.
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True
speed = 0.1
while game_on:
    screen.update() 
    time.sleep(speed)
    ball.move()
    # Detect collision with top and bottom walls.
    if ball.ycor() > 280 or ball.ycor() < -275:
        # Bounce!
        ball.bounce_wall()
    # Detect collision with paddles.
    print(ball.xcor())
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 
        or
        ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()
        speed *= 0.9
    # Detect a miss by the right player.
    if (ball.xcor() > 400):
        score.increase_right()
        ball.reset_to_start()
        speed = 0.1
        
    # Detect a miss by the left player.
    if (ball.xcor() < -400):
        score.increase_left()
        ball.reset_to_start()
        speed = 0.1        

# Draw a line down the center.

# Score

# Ball

# Collision with wall

# Check for colliding with paddle.

# Check score


# Does it change direction and speed based on where it hits the paddle?

screen.exitonclick()