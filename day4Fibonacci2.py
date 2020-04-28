
import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Fibonacci sequence")

alex = turtle.Turtle()
alex.speed(100)

color = ["black","blue","green","red","purple","red","orange"]

fibo = [0,1]
i=1

while i <100:
    fibo.append(fibo[-1]+fibo[-2])
#   fibo.append(i*2)
    i+=1
print(fibo)
alex.penup()
alex.right(90)
alex.forward(200)
alex.left(90)
alex.shape("circle")
alex.shapesize(.01)

position = []

for i in range(100):

    alex.circle(200,3.6)
    position.append(alex.pos())
    alex.stamp()
    print(position[i])

alex.speed(1000)
i =0

for i in range(100):
    alex.color(color[0])
    alex.up()
    alex.goto(position[i])
    alex.pendown()
    if i*5>99:
        alex.goto(position[(i*5)%100])
    else:
        alex.goto(position[i * 5])


# for i in range(100):
#     alex.color(color[1])
#     alex.up()
#     alex.goto(position[i])
#     alex.pendown()
#     if i*3>99:
#         alex.goto(position[(i*3)%100])
#     else:
#         alex.goto(position[i *3])
# #    alex.color(color[i%7])
#
# for i in range(100):
#     alex.color(color[2])
#     alex.up()
#     alex.goto(position[i])
#     alex.pendown()
#     if i*4>99:
#         alex.goto(position[(i*4)%100])
#     else:
#         alex.goto(position[i *4])
# #    alex.color(color[i%7])
# for i in range(100):
#     alex.color(color[3])
#     alex.up()
#     alex.goto(position[i])
#     alex.pendown()
#     if i*5>99:
#         alex.goto(position[(i*5)%100])
#     else:
#         alex.goto(position[i *5])
#
# for i in range(100):
#     alex.color(color[4])
#     alex.up()
#     alex.goto(position[i])
#     alex.pendown()
#     if i*>99:
#         alex.goto(position[(i*6)%100])
#     else:
#         alex.goto(position[i *6])

wn.mainloop()