#author : incepligator

from turtle import *
from cmath import phase

# TODO: use _multiple turtles_ to trace points with different escape times (awesome)
# TODO: optimize sort order to avoid awkward radial lines

def z_n_escape_time(c, n):
    z = 0
    for i in range(n):
        z = z**2 + c
        if abs(z)>2:
            return i
    return False

def mandelbrot_edge(resolution, iterations, edge):
    points=[]
    x_coordinates = [-2+i*(3/resolution) for i in range(int(resolution*1.5))]
    y_coordinates = [1-j*(2/resolution) for j in range(resolution)]
    for x in x_coordinates:
        for y in y_coordinates:
            if z_n_escape_time(complex(x,y),iterations) in edge:
                points.append((x,y))
    points = sorted(points, key=lambda p: phase(complex(p[0],p[1])))
    return points

def draw_boundary(protagonist, boundary_points, speed):
    protagonist.speed(speed)
    protagonist.penup()
    protagonist.setheading(protagonist.towards(boundary_points[0][0],boundary_points[0][1]))
    protagonist.forward(protagonist.distance(boundary_points[0][0],boundary_points[0][1]))
    protagonist.pendown()
    for p in boundary_points[1:]:
        protagonist.setheading(protagonist.towards(p[0],p[1]))
        protagonist.forward(protagonist.distance(p[0],p[1]))

def main():
    setting = Screen()
    setting.title("Julia T. Gaston and the Case of the Complex Quadratic Polynomial")
    setting.bgcolor('#C2EBFF')
    protagonist = RawTurtle(setting)
    protagonist.shape("turtle")
    points = [(190*p[0],190*p[1]) for p in mandelbrot_edge(300, 500, list(range(60,500)))]
    draw_boundary(protagonist, points, 10)
    setting.mainloop()

main()
