from turtle import *

speed(100)
shape("classic")
color("blue")
pensize(2)

n = 24
for i in range (n):
    for k in range(4):
        forward(100)
        right(90)
    right(360/n)
    
exitonclick()
mainloop()