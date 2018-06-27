n=int(input("n=?"))
m=n//2
r=n%2
for i in range(m):
    print("1 0", end=" ")
if r>0:
    print("1") 


