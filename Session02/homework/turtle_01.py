from turtle import *

speed (100)
shape("classic")
color("red")  

# Khoi dau:
left(120)

for i in range (4):
    right(90)
    if i % 2 == 0:
        forward(100)
        right(60)
        forward(100)
        right(120)
        forward(100)
        right(60)
        forward(100)
    else:
        forward(100)
        left(60)
        forward(100)
        left(120)
        forward(100)
        left(60)
        forward(100)

exitonclick()
mainloop()
