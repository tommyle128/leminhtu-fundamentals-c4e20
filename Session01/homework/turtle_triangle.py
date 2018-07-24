from turtle import *

speed (100)
shape("classic")
pencolor("green")  

begin_fill()
for i in range (3):
    forward(100)
    left(120)
fillcolor("yellow")
end_fill()

exitonclick()
mainloop()