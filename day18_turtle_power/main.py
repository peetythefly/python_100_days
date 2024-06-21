import turtle as turt
import random

# # Extract the colors from the file. Done once then we put it into a tuple.
# color_extract = colorgram.extract('hirst.Jpeg', 25)
# colors = []
# for color in color_extract:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     new_color = (r, g, b)
#     colors.append(new_color)
# colors = tuple(colors)
# print(colors)

colors = ((229, 228, 227), (226, 224, 225), (198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205), (109, 67, 85), (39, 35, 34), (223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108), (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59))

# Setup the ninja turtle
turt.colormode(255)
ninja = turt.Turtle()
ninja.shape("turtle")
# colors = ["red", "orange", "deeppink", "green", "blue", "purple", "cyan", "brown", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "black"]

def rand_color ():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def dot_and_move():
    ninja.color(random.choice(colors))
    ninja.forward(1)
    ninja.up()
    ninja.forward(50)
    ninja.down()


def reset_line():
    ninja.up()
    ninja.left(90)
    ninja.forward(50)
    ninja.left(90)
    ninja.forward(510)
    ninja.right(180)
    ninja.down()

ninja.speed("fastest")
ninja.pensize(20)
# Get set up
ninja.up()
ninja.right(180)
ninja.forward(250)
ninja.left(90)
ninja.forward(250)
ninja.left(90)
ninja.down()


# Dot chart is 10 x 10
dot_chart = 10
for _ in range(dot_chart):
    # Make a line of 10 dots
    for _ in range(dot_chart):
        dot_and_move()
    # Go back to the beginning of the line.
    reset_line()

ninja.hideturtle()


screen = turt.Screen()
screen.exitonclick()