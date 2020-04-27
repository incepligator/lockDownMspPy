

if i > 100:
    j = i % 100
    alex.pendown()
    alex.goto(position[j])
    print(position[j])
    alex.goto(position[j + 1])
    print(position[j + 1])
    alex.penup()