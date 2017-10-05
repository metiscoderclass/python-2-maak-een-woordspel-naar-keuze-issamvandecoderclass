import hangman
import random

woorden = ["informatica", "linux", "python", "windows", "telegram", "toetsenbord"]
counter = 0

def check():
    if counter == 1:
        hangman.een()
    elif counter == 2:
        hangman.twee()
    elif counter == 3:
        hangman.drie()
    elif counter == 4:
        hangman.vier()
    elif counter == 5:
        hangman.vijf()

woord=random.choice(woorden)

print(woord)

letter = input("type een letter ")



while True:
    if letter in woord:
        print("Het zit in de geheime woord.")
    elif letter == "?":
        raad=input("Type de woord dan ")
        if raad == woord:
            print("Ooh je hebt het woord geraden ")
            break
        else:
            print("je hebt het woord fout geraden ")
            counter += 1
            check()

