import turtle             # Allows us to use turtles
wn = turtle.Screen()     # Creates a playground for turtles

wn.bgcolor("gray55")
wn.title("Hello LockDownPython")

alex = turtle.Turtle()   # Create a turtle, assign to alex
freya = turtle.Turtle()

alex.color("tomato")
alex.pensize(6)

color = ['red','green','blue','yellow','green']

for i in color:
    alex.color(i)
    alex.forward(130)
    alex.left(144)


alex.shape("turtle")

#alex.circle(50,90)

def room():
    alex.forward(200)
    freya.left(90)
    freya.forward(15)
    freya.left(-90)
    freya.forward(185)
    alex.forward(130)  # Tell alex to move forward by 50 units
    alex.left(144)  # Tell alex to turn by 90 degrees
    alex.forward(130)  # Complete the second side of a rectangle
    alex.left(144)
    alex.forward(130)
    alex.left(144)
    alex.forward(130)
    alex.left(144)
    alex.forward(130)

def room1():

    freya.forward(130)  # Tell alex to move forward by 50 units
    freya.left(144)  # Tell alex to turn by 90 degrees
    freya.forward(130)  # Complete the second side of a rectangle
    freya.left(144)
    freya.forward(130)
    freya.left(144)
    freya.forward(130)
    freya.left(144)
    freya.forward(130)

room()
room1()
wn.mainloop()
