n=int(input("Enter a number:"))
i=2
if n<2:
    print(n, "is not a prime number")
else:    
    while True:
        m=n%i
        if i==n:
            print(n, "is a prime number")
            break    
        if m==0:
            print(n, "is not a prime number")
            break
        i+=1    
