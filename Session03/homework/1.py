menu = ["T-Shirt", "Sweater"]

loop = True
while loop:
    print()
    want = input("Welcome to our shop, what do you want? (C, R, U, D)?", ).lower()
    if want == "r":
        print("Our items:")
        print(*menu, sep=", ")
    elif want =="c":
        menu.append(input("Enter new item: "))
        print("Our items:")
        print(*menu, sep=", ")
    elif want =="u":
        p1 = int(input("Update position: "))
        while p1 > len(menu):
            p1 = int(input("There is no position like you've just entered, please enter position to update again: "))
        else:
            menu[p1-1] = input("New item: ")
            print("Our items:")
            print(*menu, sep=", ")
    elif want =="d":
        p2 = int(input("Delete position: "))
        while p2 > len(menu):
            p2 = int(input("There is no position like you've just entered, please enter position to update again: "))
        else:
            del menu[p2-1]
            print("Our items:")
            print(*menu, sep=", ")
    else:
        loop = False
        



