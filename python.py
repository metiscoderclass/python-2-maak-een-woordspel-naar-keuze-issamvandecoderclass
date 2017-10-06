import hangman
import random
print("Welkom bij:")
print("/ __)  /__\  (  )  / __) (_  _)( ___)")
print("( (_-. /(__)\  )(__( (_-..-_)(   )__) ")
print("\___/(__)(__)(____)\___/\____) (____)  ")

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
        print("Je hebt verloren.")

woord=random.choice(woorden)

print(woord)

gebruikte_letter=""

letter = input("type een letter of type ? om het woord te raden. Of exit om te verlaten: ")

while True:
    if letter in woord:
        gebruikte_letter = gebruikte_letter + "," + letter
        print("Dit zijn je gebruikte letters:" + gebruikte_letter)
    elif letter == "?":
        raad=input("Type je woord: ")
        if raad == woord:
            print("Gefeliciteerd, je hebt het woord geraden!")
            break
        else:
            print("je hebt het woord fout geraden ")
            counter += 1
            check()
    elif letter == "exit":
        print ("Ik heb dat je hebt genoten, doei!")
        break
