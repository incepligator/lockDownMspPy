
import turtle

wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Fibonacci sequence")

alex = turtle.Turtle()
alex.speed(10000)

color = ["brown","green","red","blue","green","red","orange"]

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

#both spiral
x=200
for i in range(x):
    z = i % 2
    alex.color(color[z])
    alex.circle(5*i,20)
    alex.right(90)
    alex.circle(5*i+2,20)
    alex.right(90)

alex.home()
x=50
for i in range(x):
#    z = i % 2
#    alex.color(color[z])
    alex.circle(5*i)
    alex.right(90)
    alex.circle(5*i+2)
    alex.right(90)





#4 flower spiral
# x=100
# for i in range(x):
# #    z=i%2
# #    alex.color(color[z])
#     alex.circle(5*i)
#     alex.right(10)
#     alex.circle(5*i+2)
#     alex.right(10)

#fibonachhi
# make fibonnachi sequence

fibo = [0,1]
i=1

while i <1000:
    fibo.append(fibo[-1]+fibo[-2])
#   fibo.append(i*2)
    i+=1
print(fibo)
alex.color("green")
alex.penup()
alex.right(90)
alex.forward(200)
alex.left(90)
alex.shape("circle")
alex.shapesize(.1)


# mandal bolt
position = []

for i in range(100):

    alex.circle(200,3.6)
    position.append(alex.pos())
    alex.stamp()
    print(position[i])

alex.speed(1000)
i =0

# for xoxo in fibo:
#     if xoxo >99:
#         xoxo = xoxo%99
#         alex.pendown()
#         alex.goto(position[xoxo])
#         print(alex.goto(position[xoxo]))
#     else:
#         alex.pendown()
#         alex.goto(position[xoxo])
#         print(alex.goto(position[xoxo]))


#fibonnaci squence
# j =0
# for i in fibo:
#     if j<99:
#         alex.goto(position[j])
#         alex.pendown()
#         if i>99:
#             i=i%99
#             alex.goto(position[i])
#             alex.penup()
#         else:
#             alex.goto(position[i])
#             alex.penup()
#         j=j+1
#     if j>99:
#         j = i%99
#         alex.goto(position[j])
#         alex.pendown()
#         if i > 99:
#             i = i % 99
#             alex.goto(position[i])
#             alex.penup()
#         else:
#             alex.goto(position[i])
#             alex.penup()
#         j = j + 1

        # if j <99:
        #     alex.goto(position[j + 1])
        #     print(position[j + 1])
        #
        # else:
        #     alex.goto(position[0])
        #     print(position[0])



# # 2x sequebce
for i in range(100):
    alex.color("black")
    alex.up()
    alex.goto(position[i])
    alex.pendown()
    if i*2>99:
        alex.goto(position[(i*2)%100])
    else:
        alex.goto(position[i * 2])
#
#
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

wn.mainloop()


print("Minnesota")