from turtle import *
canh = int(input("Nhap vao so canh:"))
speed(100)
shape("turtle")
color("orange")

# vehinh
for i in range(canh):
    forward(100)
    left(360 / canh )

mainloop()


