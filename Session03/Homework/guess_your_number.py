h=100
l=0
numb=(h+l)//2
print("Guess your number game")
print("Now think of a number from 0 to 100")
print("All you have to do is answer to my guess:")
print("'c' if my guess is corect ")
print("'s' if my guess is 'S'maller than your number ")
print("'l' if my guess is 'L'arger than your number")
print("Is", numb , "your number ? ")
g=input()
while True:   
    if g== "s":  
        l=numb
        numb=(l+h)//2
        print("Is", numb , "your number ? ")
        g=input()
    elif g=="l":
        h=numb
        numb=(l+h)//2
        print("Is", numb , "your number ? ")
        g=input()
    elif g=="c":
        print("Too easy for me")
        break        



        