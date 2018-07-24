from turtle import *

speed (100)
shape("classic")

for i in range (3, 7):
    goc = 360/i
    if i % 2 == 1:
        color("blue")
        for k in range(i):
            forward(100)
            left(goc)
                    
    else:
        color("red")
        for l in range(i):
            forward(100)
            left(goc)
        
exitonclick()
mainloop()