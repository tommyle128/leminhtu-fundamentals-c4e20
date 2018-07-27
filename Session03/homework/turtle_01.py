from turtle import *

colors =['red', 'blue', 'brown', 'yellow', 'grey']
speed (100)
shape("classic")

for i in range (3, 8):
    goc = 360/i
    color(colors[i-3])
    for k in range(i):
        forward(100)
        left(goc)

      
exitonclick()
mainloop()