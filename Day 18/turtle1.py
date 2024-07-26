from turtle import Turtle, Screen


def square(side_length, turtle):
    for num in range(4):
        turtle.forward(side_length)
        turtle.left(90)


tim = Turtle()
tim.shape("turtle")
tim.color("red")
square(100, tim)


screen = Screen()
screen.exitonclick()
