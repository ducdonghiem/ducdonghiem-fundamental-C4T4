n=int(input("Enter a number:"))
i=1
while True:
    m=n//(10**i)
    i+=1
    if m<1:
        print(n, "has", i-1, "digit(s)")
        break