from turtle import *
import turtle             # Allows us to use turtles
wn = turtle.Screen()     # Creates a playground for turtles

wn.bgcolor("gray55")
wn.title("Hello LockDownPython")

alex = turtle.Turtle()   # Create a turtle, assign to alex
#freya = turtle.Turtle()

alex.color("tomato")
alex.pensize(.4 )
alex.shape("turtle")

color = ['red','green','blue','yellow','orange']


#alex.penup()
alex.forward(100)
alex.left(170)
alex.right(90)

alex.stamp()
for i in color:
    alex.color(i)
    alex.forward(200)
    alex.left(144)
    alex.speed(1)



done()

wn.mainloop()