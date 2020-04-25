
print("this is 4th day ")
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello LockDownPython")

alex = turtle.Turtle()
alex.speed(1)

alex.color("black","red")
alex.begin_fill()
alex.shape("turtle")
alex.color("blue")

for i in range(12):
    alex.penup()
    alex.forward(120)
    alex.pendown()
    alex.forward(10)

    alex.penup()
    alex.forward(20)
    alex.stamp()
    alex.forward(-150)
    alex.left(30)

size = 20
for i in range(30):
    alex.stamp()
    size = size+3
    alex.forward(size)
    alex.right(24)

wn.mainloop()