
import json
from difflib import get_close_matches

data=json.load(open("Data.json"))

print(" --------------------------------------------------------------------------------------")
print("|        WELCOME                                                                       |")
print("|                                * AADL SHAKH *                                        |")
print("|                                                                 DICTIONARY           |")
print(" --------------------------------------------------------------------------------------")

while True:

    def translate(word):

        if word in data:
            return data[word]
        elif word.lower() in data:
            return data[word.lower()]
        elif word.upper() in data:
            return data[word.upper()]
        elif word.title() in data:
            return data[word.title()]
        elif bool(get_close_matches(word, data.keys()))==True:
            print("Did you mean '%s'" % get_close_matches(word, data.keys())[0])
            answar = input("Enter ' y ' otherwise enter other key to exit : ")
            if answar == 'y':
                return data[get_close_matches(word, data.keys())[0]]
            else:
                return ("Sorry Meanning Not Found ( Try Again )")
        else:
            return (f"'{word}' meaning not found")

    word = input("Enter the word otherwise enter e for exit : ")
    if word == 'e':
        print("Thank's for using * Aadil Shaikh * Dictionary ")
        break
    output = translate(word)
    if type(output) == list:
        for item in output:
            print("-> " + item)
    else:
        print("-> " + output)
