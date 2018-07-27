from turtle import *

colors =['red', 'blue', 'brown', 'yellow', 'grey']
speed (100)
shape("classic")

for i in range (5):
    begin_fill()
    fillcolor(colors[i])
    for k in range(2):
        forward(100)
        right(90)
        forward(200)
        right(90)
    forward(100)
    end_fill()




    
    
      
exitonclick()
mainloop()