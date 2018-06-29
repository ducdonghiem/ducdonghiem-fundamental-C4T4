from turtle import*
color("blue")
speed(-1)
n=0
for i in range(36):
    for i in range(4):
        forward(5+n)
        right(90)
    left(10)  
    n+=3  
mainloop()