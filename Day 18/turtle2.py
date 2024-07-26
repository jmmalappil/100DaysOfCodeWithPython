from turtle import Turtle, Screen
tom = Turtle()

for _ in range(15):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()

screen = Screen()
screen.exitonclick()