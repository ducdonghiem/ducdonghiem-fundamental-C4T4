menu=["T-Shirt", "Sweater", "Jeans", "Skirt"]
while True:
    want=input("Welcome to our shop, what do you want (C, R, U, D)?").lower()
    if want=="r":
        print("Our items: ", *menu, sep=", ")
    elif want=="c":
        item=input("Enter new item: ")
        menu.append(item)
        print("Our items:", *menu, sep=", ")
    elif want=="u":
        update=int(input("Update position? "))
        new=input("New item? ")
        menu[update-1]=new
        print("Our items:", *menu, sep=", ")
    elif want=="d":
        delete=int(input("Delete position? "))
        del menu[delete-1]    
        print("Our items:", *menu, sep=", ")
    else:
        print("Bye")
        break
    



