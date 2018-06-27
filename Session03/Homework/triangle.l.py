n=1
for i in range(10):
    for i in range(10-n):
        print(" ", end=" ")
    for i in range(n):
        print("*", end=" ")
    print()
    n+=1    