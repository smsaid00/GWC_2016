from turtle import *
window = Screen()

# speed(1)
# penup()
# goto(-180, 0)
# def draw_square(color, length):
#     pendown()
#     pencolor(color)
#     for i in range(4):
#         forward(length)
#         right(90)
#     left(60)
#     for j in range(2):
#         forward(length)
#         right(120)
#     penup()
#     right(180)
#     forward(length*2)
#     pendown()
# for j in range(5):
#     draw_square("maroon", 50)

def circle1(radius, extent, steps):
    pendown()
    forward(radius)
    right(extent)
    forward(steps)
for i in range(360):
    circle1(30, 100, 1)


window.exitonclick
