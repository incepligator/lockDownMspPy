
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

#alex.circle(200,60)

alex.circle(200,60)

dis = alex.pos()
print(dis)
print(alex.heading())
alex.home()
print(alex.distance(dis))

alex.left(30)
alex.forward(199.999)



wn.mainloop()