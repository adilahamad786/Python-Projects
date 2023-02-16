
import random

var = ["", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

at = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 1

temp=0

def structure():

    print(f"  {var[1]}  |  {var[2]}  |  {var[3]}")
    print(' ---------------')
    print(f"  {var[4]}  |  {var[5]}  |  {var[6]}")
    print(' ---------------')
    print(f"  {var[7]}  |  {var[8]}  |  {var[9]}")

def redusemove(current):
    at.remove(current)

def usermove():

    while True:

        global count
        global var
        global temp

        userinput = int(input("Enter No. b/w 1 to 9 for enter X :- "))

        if userinput in at:
            temp=userinput
            var[userinput] = "X"
            redusemove(userinput)
            count+=1
            structure()

            if (var[1] == var[2] == var[3] == "X" or var[4] == var[5] == var[6] == "X" or var[7] == var[8] == var[
                9] == "X" or var[7] == var[4] == var[1] == "X" or var[8] == var[5] == var[2] == "X" or var[9] == var[
                6] ==
                    var[3] == "X" or var[1] == var[5] == var[9] == "X" or var[3] == var[5] == var[7] == "X"):
                print("*** YOU WIN ***")
                count = 10
                break

            if at == []:
                print("GAME is DROW")
                break

            break

        else:
            print(f" please enter valid No. {at}, Choose Again !  ")

def machinemove():

    global count
    global var

    while True:

        if count == 2 :
            while True:
                machineinput = random.choice(at)
                if machineinput % 2 == 0 or machineinput==5:
                    continue
                else:
                    if temp==1 and machineinput==9 and level!=1:
                        var[machineinput] = "O"
                        redusemove(machineinput)
                        structure()
                        count += 1
                        break
                    elif temp==3 and machineinput==7 and level!=1 and level!=2:
                        var[machineinput] = "O"
                        redusemove(machineinput)
                        structure()
                        count += 1
                        break
                    elif temp==7 and machineinput==3 and level!=1:
                        var[machineinput] = "O"
                        redusemove(machineinput)
                        structure()
                        count += 1
                        break
                    elif temp==9 and machineinput==1 and level!=1 and level!=2:
                        var[machineinput] = "O"
                        redusemove(machineinput)
                        structure()
                        count += 1
                        break
                    elif level==1:
                        var[machineinput] = "O"
                        redusemove(machineinput)
                        structure()
                        count += 1
                        break
                    elif temp%2==0 or temp==5:
                        var[machineinput] = "O"
                        redusemove(machineinput)
                        structure()
                        count += 1
                        break

                    else:
                        continue


            if (var[1] == var[2] == var[3] == "X" or var[4] == var[5] == var[3] == "X" or var[7] == var[8] == var[
                9] == "X" or var[7] == var[4] == var[1] == "X" or var[8] == var[5] == var[2] == "X" or var[9] == var[
                6] ==
                    var[3] == "X" or var[1] == var[5] == var[9] == "X" or var[3] == var[5] == var[7] == "X"):
                print("*** YOU WIN ***")
                count = 10
            break
        else:

            # condition check acording to machine win

            count += 1

            if (var[1] == var[2] == "O") and 3 in at:
                var[3] = "O"
                redusemove(3)
                structure()
                break
            elif (var[1] == var[3] == "O") and 2 in at:
                var[2] = "O"
                redusemove(2)
                structure()
                break
            elif (var[3] == var[2] == "O") and 1 in at:
                var[1] = "O"
                redusemove(1)
                structure()
                break

            elif (var[4] == var[5] == "O") and 6 in at:
                var[6] = "O"
                redusemove(6)
                structure()
                break
            elif (var[5] == var[6] == "O") and 4 in at:
                var[4] = "O"
                redusemove(4)
                structure()
                break
            elif (var[4] == var[6] == "O") and 5 in at:
                var[5] = "O"
                redusemove(5)
                structure()
                break

            elif (var[7] == var[8] == "O") and 9 in at:
                var[9] = "O"
                redusemove(9)
                structure()
                break
            elif (var[8] == var[9] == "O") and 7 in at:
                var[7] = "O"
                redusemove(7)
                structure()
                break
            elif (var[7] == var[9] == "O") and 8 in at:
                var[8] = "O"
                redusemove(8)
                structure()
                break

            elif (var[1] == var[4] == "O") and 7 in at:
                var[7] = "O"
                redusemove(7)
                structure()
                break
            elif (var[1] == var[7] == "O") and 4 in at:
                var[4] = "O"
                redusemove(4)
                structure()
                break
            elif (var[4] == var[7] == "O") and 1 in at:
                var[1] = "O"
                redusemove(1)
                structure()
                break

            elif (var[2] == var[5] == "O") and 8 in at:
                var[8] = "O"
                redusemove(8)
                structure()
                break
            elif (var[2] == var[8] == "O") and 5 in at:
                var[5] = "O"
                redusemove(5)
                structure()
                break
            elif (var[5] == var[8] == "O") and 2 in at:
                var[2] = "O"
                redusemove(2)
                structure()
                break

            elif (var[3] == var[6] == "O") and 9 in at:
                var[9] = "O"
                redusemove(9)
                structure()
                break
            elif (var[3] == var[9] == "O") and 6 in at:
                var[6] = "O"
                redusemove(6)
                structure()
                break
            elif (var[6] == var[9] == "O") and 3 in at:
                var[3] = "O"
                redusemove(3)
                structure()
                break

            elif (var[1] == var[5] == "O") and 9 in at:
                var[9] = "O"
                redusemove(9)
                structure()
                break
            elif (var[1] == var[9] == "O") and 5 in at:
                var[5] = "O"
                redusemove(5)
                structure()
                break
            elif (var[5] == var[9] == "O") and 1 in at:
                var[1] = "O"
                redusemove(1)
                structure()
                break

            elif (var[3] == var[5] == "O") and 7 in at:
                var[7] = "O"
                redusemove(7)
                structure()
                break
            elif (var[3] == var[7] == "O") and 5 in at:
                var[5] = "O"
                redusemove(5)
                structure()
                break
            elif (var[5] == var[7] == "O") and 3 in at:
                var[3] = "O"
                redusemove(3)
                structure()
                break


            # condition check for acording to user win

            if (var[1] == var[2] == "X") and 3 in at:
                var[3] = "O"
                redusemove(3)
                structure()
                break
            elif (var[1] == var[3] == "X") and 2 in at:
                var[2] = "O"
                redusemove(2)
                structure()
                break
            elif (var[3] == var[2] == "X") and 1 in at:
                var[1] = "O"
                redusemove(1)
                structure()
                break

            elif (var[4] == var[5] == "X") and 6 in at:
                var[6] = "O"
                redusemove(6)
                structure()
                break
            elif (var[5] == var[6] == "X") and 4 in at:
                var[4] = "O"
                redusemove(4)
                structure()
                break
            elif (var[4] == var[6] == "X") and 5 in at:
                var[5] = "O"
                redusemove(5)
                structure()
                break

            elif (var[7] == var[8] == "X") and 9 in at:
                var[9] = "O"
                redusemove(9)
                structure()
                break
            elif (var[8] == var[9] == "X") and 7 in at:
                var[7] = "O"
                redusemove(7)
                structure()
                break
            elif (var[7] == var[9] == "X") and 8 in at:
                var[8] = "O"
                redusemove(8)
                structure()
                break

            elif (var[1] == var[4] == "X") and 7 in at:
                var[7] = "O"
                redusemove(7)
                structure()
                break
            elif (var[1] == var[7] == "X") and 4 in at:
                var[4] = "O"
                redusemove(4)
                structure()
                break
            elif (var[4] == var[7] == "X") and 1 in at:
                var[1] = "O"
                redusemove(1)
                structure()
                break

            elif (var[2] == var[5] == "X") and 8 in at:
                var[8] = "O"
                redusemove(8)
                structure()
                break
            elif (var[2] == var[8] == "X") and 5 in at:
                var[5] = "O"
                redusemove(5)
                structure()
                break
            elif (var[5] == var[8] == "X") and 2 in at:
                var[2] = "O"
                redusemove(2)
                structure()
                break

            elif (var[3] == var[6] == "X") and 9 in at:
                var[9] = "O"
                redusemove(9)
                structure()
                break
            elif (var[3] == var[9] == "X") and 6 in at:
                var[6] = "O"
                redusemove(6)
                structure()
                break
            elif (var[6] == var[9] == "X") and 3 in at:
                var[3] = "O"
                redusemove(3)
                structure()
                break

            elif (var[1] == var[5] == "X") and 9 in at:
                var[9] = "O"
                redusemove(9)
                structure()
                break
            elif (var[1] == var[9] == "X") and 5 in at:
                var[5] = "O"
                redusemove(5)
                structure()
                break
            elif (var[5] == var[9] == "X") and 1 in at:
                var[1] = "O"
                redusemove(1)
                structure()
                break

            elif (var[3] == var[5] == "X") and 7 in at:
                var[7] = "O"
                redusemove(7)
                structure()
                break
            elif (var[3] == var[7] == "X") and 5 in at:
                var[5] = "O"
                redusemove(5)
                structure()
                break
            elif (var[5] == var[7] == "X") and 3 in at:
                var[3] = "O"
                redusemove(3)
                structure()
                break

            else:
                while True:
                    n = random.choice(at)
                    if temp % 2 == 0:
                        if n % 2 == 0:
                            var[n] = "O"
                            redusemove(n)
                            structure()
                            break
                        continue

                    else:
                        if n % 2 != 0:
                            var[n] = "O"
                            redusemove(n)
                            structure()
                            break
                        continue
                break


    if (var[1] == var[2] == var[3] == "O" or var[4] == var[5] == var[3] == "O" or var[7] == var[8] == var[
        9] == "O" or var[7] == var[4] == var[1] == "O" or var[8] == var[5] == var[2] == "O" or var[9] == var[
        6] ==
            var[3] == "O" or var[1] == var[5] == var[9] == "O" or var[3] == var[5] == var[7] == "O"):
        print("*** YOU LOSE ***")
        count = 10

def start():

    while count < 10:

        usermove()

        if count == 10:
            continue

        print(" After Computer Move ")

        machinemove()

print(" --------------------------------------------------------------------------------------")
print("|        WELCOME                                                                       |")
print("|                                * TIC TAC TOE *                                       |")
print("|                                                                 By Aadil Sheikh      |")
print(" --------------------------------------------------------------------------------------")

while True:

    check = input(' If you want to play TIC TAC TOE Enter yes other wise enter any key for exit :- ')
    if check !=("yes" or "Yes" or "YES"):
        break

    while True:
        level = int(input("Enter Game Lavel ( 1,2,3 ) : "))
        if level==1 or level==2 or level==3:
            break
        else:
            print("Please Select valid Level 1,2,3 only ! ")
            continue


    var = ["", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    at = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 1

    structure()
    start()

print("* Thank's for play *")