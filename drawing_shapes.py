from turtle import *

pendown()
pencolor("steelblue")


###1_ Square
# sidelength = 100
# goto (0,0)
# for i in range(4):
#     forward(sidelength)
#     right(90)


###_ Hexagon (starts left)
# sidelength_2 = 70
# for j in range(6):
#     right(120)
#     forward(sidelength_2)
#     left(60)


##_2 Hexagonal Pattern
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

    penup()
    goto (30, 0)
    pendown()
    for j in range(6):
        right(120)
        forward(sidelength_2)
        left(60)


###_3 Continuous Hexagon Right
# x_pos = 0
# for j in range(100):
#     right(120)
#     forward(sidelength_2)
#     left(60)
#     penup()
#     goto (x_pos, 0)
#     x_pos += 10
#     pendown()


###4_ Hexagon (Botton Left)
# sidelength = 100
# for i in range(6):
#     backward(sidelength)
#     right(60)
