from turtle import Turtle,  Screen

ninja = Turtle()
screen = Screen()


def move_forwards():
    ninja.forward(5)


def turn_left():
    ninja.left(5)


def turn_right():
    ninja.right(5)


def move_backwards():
    ninja.backward(5)
    

def clear_screen():
    ninja.clear()
    ninja.hideturtle()
    ninja.up()
    ninja.home()
    ninja.down()
    ninja.showturtle()
    
screen.listen() 
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_screen)



screen.exitonclick()