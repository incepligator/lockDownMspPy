#author : incepligator


import turtle
import time
ws = turtle.Screen()
ws.bgcolor('lightgreen')

alex = turtle.Turtle()

alex.pensize(5)
alex.hideturtle()
alex.color('red')


ws.tracer(0)


for i in range(6000):
    alex.penup()
    alex.goto(0,0)
    alex.setheading(90)
    alex.rt(i*6)
    alex.pendown()
    alex.forward(190)

    time.sleep(1)
    ws.update()
    alex.clear()

ws.mainloop()
