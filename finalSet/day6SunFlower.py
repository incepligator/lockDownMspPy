#author : incepligator
#Turtle Flower Example

import turtle
ws = turtle.Screen()
#Define Screen Size
ws.setup(width=1280, height=720)
alex = turtle.Turtle()
alex.speed(0) #for Maximum speed render
alex.pensize(.1)
alex.shape("turtle")

#Petal only
def petal():
    alex.color("black", "yellow")
    alex.begin_fill()
    alex.right(20)
    alex.forward(100)
    alex.left(40)
    alex.forward(100)
    alex.left(140)
    alex.forward(100)
    alex.left(40)
    alex.forward(100)

#seedsInner
for i in range(250):

    if i <200: # total seed number
        alex.penup()    # remove lines in seeds
        alex.forward(i)
        alex.pendown()
        alex.color("black","orange")
        alex.begin_fill()
        alex.stamp()
        alex.left(137.58)   #seed rotation angle
        alex.end_fill()
        i = i + 20
        print("Seed count"+ str(i))
    else:
        alex.penup()
        alex.setposition(0,0)   #go to position origin
        # inner circle radius
        alex.forward((i + 30)/2.5)
        alex.pendown()
        alex.color("black", "yellow")
        alex.begin_fill()
        petal()
        alex.left(22/7)         #Petal rotation
        alex.end_fill()
        i = i + 10
        print("Petal count"+ str(i))

ws.exitonclick()


