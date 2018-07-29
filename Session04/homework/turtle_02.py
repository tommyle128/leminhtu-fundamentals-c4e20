from turtle import *

speed(100)
shape("classic")
color("blue")

n = 54
canh = 100
thay_doi = canh / n

right(135)
for i in range (n):
    for k in range(4):
        forward(canh)
        right(90)
    right(540/n)
    canh -= thay_doi

exitonclick()
mainloop()