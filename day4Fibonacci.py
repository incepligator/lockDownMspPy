
import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Fibonacci sequence")

alex = turtle.Turtle()
alex.speed(100)

color = ["black","blue","green","orange","green","red","orange"]

# alex.color("black","red")
# alex.begin_fill()
# alex.shape("turtle")
# alex.color("blue")
#
# #alex.circle(200,60)
#
# alex.circle(200,60)
#
# dis = alex.pos()
# print(dis)
# print(alex.heading())
# alex.home()
# print(alex.distance(dis))
#
# alex.left(30)
# alex.forward(199.999)
# x=100
# for i in range(x):
#
#     alex.circle(5*i)
#
#     alex.circle(-5*i+2)
#     alex.right(90)
#fibonachhi
# make fibonnachi sequence

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
alex.shapesize(.1)

position = []

for i in range(100):

    alex.circle(200,3.6)
    position.append(alex.pos())
    alex.stamp()
    print(position[i])

alex.speed(1000)
i =0

# fibonnaci squence
# for i in fibo:
#     if i<100:
#         alex.pendown()
#         alex.goto(position[i])
#         #alex.goto(position[i + 1])
#         alex.penup()
#     if i>100:
#         j = i%100
#         alex.pendown()
#         alex.goto(position[j])
#         print(position[j])
#         print("this is j "+str(j))
#
#         if j <99:
#             #alex.goto(position[j + 1])
#             print(position[j + 1])
#             alex.penup()
#         else:
#             #alex.goto(position[0])
#             print(position[0])
#             alex.penup()
# 2x sequebce
for i in range(100):
    alex.color(color[0])
    alex.up()
    alex.goto(position[i])
    alex.pendown()
    if i*2>99:
        alex.goto(position[(i*2)%100])
    else:
        alex.goto(position[i * 2])


for i in range(100):
    alex.color(color[1])
    alex.up()
    alex.goto(position[i])
    alex.pendown()
    if i*3>99:
        alex.goto(position[(i*3)%100])
    else:
        alex.goto(position[i *3])
#    alex.color(color[i%7])

for i in range(100):
    alex.color(color[2])
    alex.up()
    alex.goto(position[i])
    alex.pendown()
    if i*4>99:
        alex.goto(position[(i*4)%100])
    else:
        alex.goto(position[i *4])
#    alex.color(color[i%7])
for i in range(100):
    alex.color(color[3])
    alex.up()
    alex.goto(position[i])
    alex.pendown()
    if i*5>99:
        alex.goto(position[(i*5)%100])
    else:
        alex.goto(position[i *5])

wn.mainloop()


print("Minnesota")