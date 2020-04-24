import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Hello LockDownPython")

alex = turtle.Turtle()
alex.speed(3)

color = ['red','green','blue','yellow','orange']

alex.color("black","red")
alex.begin_fill()

alex.circle(120,60)
alex.left(120)
alex.circle(120,60)
alex.left(60)
alex.circle(120,60)
alex.left(120)
alex.circle(120,60)
alex.circle(120,60)
alex.left(120)
alex.circle(120,60)
alex.left(60)
alex.circle(120,60)
alex.left(120)
alex.circle(120,60)

alex.left(60)
alex.circle(120,60)
alex.left(120)
alex.circle(120,60)

alex.left(-60)
alex.circle(120,60)
alex.left(120)
alex.circle(120,60)

for i in color:
    alex.color(i)

alex.end_fill()
#new Moon
i=1
while i<180:
    for x in color:
        alex.color(x)
        alex.circle(300,330)
        alex.right(89)
        i+=1

alex.color("black")
alex.end_fill()

# i=1
# while i<37:
#     alex.forward(200)
#     alex.right(170)
#     i+=1
# i= 1
# while i<37:
#     alex.forward(-200)
#     alex.right(170)
#     i+=1
# i= 1
# alex.left(90)
# alex.forward(70)
#
# while i<37:
#     alex.forward(200)
#     alex.right(170)
#     i+=1


#alex.pendown()

wn.mainloop()
