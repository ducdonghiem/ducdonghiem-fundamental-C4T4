from turtle import*
# speed(-1)
for i in range (4):
    forward(100)
    right(90)

begin_fill()
color("red")
left(60)
forward(100)
right(120)
forward(100)  
end_fill()

penup()
right(30)
forward(100)
right(90)
forward(60)
pendown()

begin_fill()
color("blue")
right(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
end_fill()

penup()
left(90)
forward(50)
left(90)
forward(50)
pendown()

begin_fill()
color("yellow")
for i in range(4):
    forward(30)
    right(90)
end_fill()

mainloop()
