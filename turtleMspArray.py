import turtle             # Allows us to use turtles
wn = turtle.Screen()     # Creates a playground for turtles

wn.bgcolor("lightgreen")
wn.title("Hello LockDownPython")

alex = turtle.Turtle()   # Create a turtle, assign to alex
freya = turtle.Turtle()

alex.shape("turtle")
#alex.circle(50,90)

def room():
    alex.forward(200)
    freya.left(90)
    freya.forward(15)
    freya.left(-90)
    freya.forward(185)

room()

wn.mainloop()
