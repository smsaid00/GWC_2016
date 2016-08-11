from turtle import *

###1_ Square
# def draw_square(color, length):
#     pendown()
#     pencolor(color)
#     forward(length)
#     right(90)
#
# for j in range(4):
#     draw_square("magenta", 50)


###2_ Triangle
# def draw_triangle(color, length):
#     pendown()
#     pencolor(color)
#     forward(length)
#     right(120)
#
# for i in range(3):
#     draw_triangle("royalblue", 60)


##3_ Hexagonal Patterns
def draw_hexagon(color, length, distance)
    pendown()
    pencolor(color)
    right(120)
    forward()
    left(length)
    penup()
     goto(distance, 0)

sidelength_2 = 70
# goto (100,0)
for p in range(20):
    for j in range(6):
        right(120)
        forward(sidelength_2)
        left(60)
    penup()
    goto (10, 0)
    pendown()
    for j in range(6):
        right(120)
        forward(sidelength_2)
        left(60)

for j in range(10):
    draw_hexagon("magenta", 50, 10)



###4_ Cirlcle
# def draw_circle(color, steps)
#     pendown()
#     pencolor(color)
#     forward(1)
#     right(1)
# for j in range("magenta",  )

###5_ Circle 2
# def circle(radius, extent, steps)
#     pendown()
