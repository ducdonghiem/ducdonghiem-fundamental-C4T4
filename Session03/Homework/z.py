n=1
for i in range(10):
    print("*", end=" ")
print()
for i in range(8):
    for i in range(9-n):
        print(" ", end=" ")
    print("*")    
    n+=1    
for i in range(10):
    print("*", end=" ")    