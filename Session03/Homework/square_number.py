n=int(input("Enter a number:"))
i=1
while True:
    m=n/i
    if m==i:
        print(n, "is a square number")
        break
    if i>n:
        print(n, "is not a square number")
        break   
    i+=1 