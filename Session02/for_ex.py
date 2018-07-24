from turtle import *

shape("turtle")
speed(-1)

length = 5

for i in range(400):
    forward(length)
    left(90)
    length += 10

exitonclick()
mainloop()