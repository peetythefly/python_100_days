from turtle import Turtle,  Screen
import random

screen = Screen()
screen.setup(width=1000, height=600)

# Draw the finish line.
# Splinter will draw it but you can't see him.
splinter = Turtle()
splinter.hideturtle()
splinter.up()
splinter.goto(x=450, y=300)
splinter.pensize(10)
splinter.down()
splinter.goto(x=450, y=-300)

# Create turtles and set their colors.
leo = Turtle(shape="turtle")
leo.color("blue")
mike = Turtle(shape="turtle")
mike.color("orange")
raph = Turtle(shape="turtle")
raph.color("red")
don = Turtle(shape="turtle")
don.color("purple")

# Make a list for anything you want to do to all 4.
turtles = [leo, mike, raph, don]
turtle_names = ["leo", "mike", "raph", "don"]

# We don't want any of them to draw while moving.
for turtle in turtles:
    turtle.up()
    turtle.speed("fastest")
    
# Set each turtle in their starting position.
leo.goto(x=-450, y=210)
mike.goto(x=-450, y=70)
raph.goto(x=-450, y=-70)
don.goto(x=-450, y=-210)
# Let the user place a bet.
favored = screen.textinput(title="TMNT Race", prompt="Which teenage mutant ninja turtle will you bet on? (select leo, mike, raph, or don)")


# Make a random movement function. They move between 1 and 10 spaces each movement. Returns how far they moved.
def rand_move(ninja):
    speed = random.randint(1,20)
    ninja.forward(speed)
    return speed


def give_position(ninja):
    position = ninja.pos()
    # We only care about the x position for the race.
    x = position[0]
    return x


# Populate the initial positions.
x_positions = []
for turtle in turtles:
    position = give_position(turtle)
    x_positions.append(position)

# Start the race. It ends when one of them get to 450 on the x axis.
keep_racing = True
FINISH = 450
while keep_racing:
    # Move them.
    t_index = 0
    for turtle in turtles:
        rand_move(turtle)
        position = give_position(turtle)
        # Track the movements.
        x_positions[t_index] = position
        t_index += 1
        # If there is a winner, mark it since we don't know how far they went past the finish line.
        if position >= FINISH:
            keep_racing = False
    
# Get the turtle that got past the finish line th furthest and make them them winner.
farthest = max(x_positions)
winner_position = x_positions.index(farthest)
winner_name = turtle_names[winner_position]
announcement = ""
if favored == winner_name:
    announcement += "You have won!\n"
else:
    announcement += "You've lost!\n"
# Move splinter to the center to announce the winner.
splinter.up()
splinter.goto(-180,0)
splinter.write(f"{announcement}The winner is {winner_name}!", font=("Arial", 45, "normal"))
print(f"The winner is {winner_name}!")
screen.exitonclick()