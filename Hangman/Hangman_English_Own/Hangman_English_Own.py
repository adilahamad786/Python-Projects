import random

def hangman():

    word = random.choice(["pugger", "littlepugger", "tiger", "superman", "thor", "pokemon", "avengers", "savewater", "earth"])

    print('* Welcome to Hangman *')

    print(f'Guess and word : {("_ ") * len(word)}')
    chance = 5
    main=""
    default=""

    while True:

        if chance == 0:
            print("Lost Game !!!")
            break

        enter = input("Please enter Alphabet : ")

        if enter not in "abcdefghijklmnopqrstuvwxyz":
            print("Please Enter only small alphabet like ( abcdefghijklmnopqrstuvwxyz ) ")
            continue

        if enter in default:
            print(f"* Already Entered '{enter}' *")
            continue
        default+=enter

        main=''
        real=""

        for item in word:

            if item in default:
                main = main + item +" "
                real=real+item
            else:
                main = main + "_" + " "
                real=real+"_"+" "
        if real == word:
            print(f"The word is '{word}'")
            print("* you are Win *")
            break

        if enter not in word:
            chance -= 1
            print(f"You are wrong & only {chance} chance remain")

        print("Guess the word :", main)




print(" --------------------------------------------------------------------------------------")
print("|        WELCOME                                                                       |")
print("|                                   * HANGMAN *                                        |")
print("|                                                                 By Aadil Sheikh      |")
print(" --------------------------------------------------------------------------------------")

hangman()

play=input("If you want play again enter y other wise enter any key for exit :")

if play=="y":
    hangman()
else:
    print("* Thank's For Play *")
