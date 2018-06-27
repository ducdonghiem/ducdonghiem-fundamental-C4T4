t=1
f=1
y=10
for i in range(9):
    for i in range(f, y, t):
        print(i, end=" ")
    print()  
    t=t+1  
    f=f+1
    y=y+9
    