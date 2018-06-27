n=int(input("n=?"))
t=1
f=1
y=n+1
for i in range(n):
    for i in range(f, y, t):
        print(i, end=" ")
    print()  
    t=t+1  
    f=f+1
    y=y+n