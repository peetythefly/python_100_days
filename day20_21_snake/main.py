from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Slithering Snake")
# Disable tracing so that we don't see each segment move one at a time.
screen.tracer(0)

# Create the snake.
snake = Snake()
# Create the food.
food = Food()
score = Score()

screen.listen()
screen.onkey(lambda: snake.turn(90), 'Up')
screen.onkey(lambda: snake.turn(180), 'Left')
screen.onkey(lambda: snake.turn(0), 'Right')
screen.onkey(lambda: snake.turn(270), 'Down')

game_on = True
while game_on:
    # Update after each movement so that it looks like the whole body moves at once.
    screen.update()    
    time.sleep(0.1)
    # Move the snake.
    snake.move()
    # Check if food is eaten. If the snake barenly passes the food the distance 
    # is just above 18. Go less than 17 for a buffer.
    if snake.head.distance(food.pos()) < 17:
        # Make the snake longer.
        snake.extend()
        # Add to the score and show the new value.
        score.increase_score()
        score.write_score()
        # Get a new food.
        food.serve_food()
    
    # Detect snake collision.
    if snake.check_collision():
        score.reset_score()
        snake.reset_to_start()
    
    # Detect wall collision.
    if abs(snake.head.pos()[0]) > 280 or abs(snake.head.pos()[1]) > 280:
        score.reset_score()
        snake.reset_to_start()

score.game_over()

screen.exitonclick()