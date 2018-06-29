list=[5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Duc and here are my sheep sizes:")
print(*list, sep=", ")
m=max(list)
print("Now my biggest sheep has size", m,"let's shear it")
list[list.index(m)]=8
print("After shearing, here is my flock:")
print(*list, sep=", ")
for i in range(3):
    for y in range(7):
        list[y]+=50
    print()    
    print("MONTH", i+1)    
    print("One month has passed, now here is my flock")    
    print(*list, sep=", ")
    m=max(list)
    print("Now my biggest sheep has size", m,"let's shear it")
    list[list.index(m)]=8
    print("After shearing, here is my flock:")
    print(*list, sep=", ")
n=0    
for i in range(7):
    n=list[i]+n   
print()     
print("My flock has size in total:", n)
print("I would get", n,"*2$=", n*2,"$")
