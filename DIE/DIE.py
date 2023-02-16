
### *** DIE CREATE BY Aadil Shaikh *** ###

import random

a=" -----------"
b="|           |"
c="|     O     |"
d="|  O     O  |"

print(" --- Welcome to Die Simulator ---")

while True:

    x = random.randint(1, 6)

    if x == 1:
        print(a)
        print(b)
        print(c)
        print(b)
        print(a)
    if x == 2:
        print(a)
        print(b)
        print(d)
        print(b)
        print(a)
    if x == 3:
        print(a)
        print(c)
        print(c)
        print(c)
        print(a)
    if x == 4:
        print(a)
        print(d)
        print(b)
        print(d)
        print(a)
    if x == 5:
        print(a)
        print(d)
        print(c)
        print(d)
        print(a)
    if x == 6:
        print(a)
        print(d)
        print(d)
        print(d)
        print(a)

    while x<=6:

        x = input("If You want to play again, Yes && No : ")

        if (x == "yes" or x == "YES") or x == "Yes":
            x = 50
        elif (x == "NO" or x == "No") or x == "no":
            break
        else:
            print("Please Enter Right Key :- ")
            x=1

    if (x == "NO" or x == "No") or x == "no":
        break

    print(" --- Welcome Back --- ")

print(" --- THANK'S FOR PLAYING --- ")