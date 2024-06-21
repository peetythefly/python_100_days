import turtle as turt
import random

turt.colormode(255)
ninja = turt.Turtle()
ninja.shape("turtle")

def rand_color ():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

colors = ((229, 228, 227), (226, 224, 225), (198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205), (109, 67, 85), (39, 35, 34), (223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108), (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59))


# Make a spirograph
ninja.speed("fastest")
circles = 100
for _ in range(circles):
    angle = 360 / circles
    # Change the color
    ninja.color(rand_color())
    # Draw a circle
    ninja.circle(100)
    # Change the angle
    ninja.right(angle)

# Practice moving
for _ in range(4):
    ninja.forward(200)
    ninja.right(90)
ninja.right(180)
for _ in range(15):
    ninja.forward(10)
    ninja.up()
    ninja.forward(10)
    ninja.down()

# Draw all the shapes in a fun way
for i in range(3,11):
    angle = 360 / i
    color_choice = random.choice(colors)
    ninja.color(color_choice)
    for _ in range(i):
        ninja.right(angle)
        ninja.forward(100)

# Walk around randomly.
ninja.width(8)
# Get the random number of times it will walk.
steps = random.randint(100,300)
# Up, down, left, or right
directions = [0, 90, 180, 270]
# Make the turtle walk fast.
ninja.speed(10)
# Start walking
for _ in range(steps):
    # Change the color each time.
    # color_choice = random.choice(colors)
    # ninja.color(color_choice)
    ninja.pencolor(rand_color())
    # Change the direction each time
    turn = random.choice(directions)
    ninja.right(turn)     
    # Walk the same distance each time.
    ninja.forward(30)

screen = turt.Screen()
screen.exitonclick()