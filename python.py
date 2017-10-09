import hangman
import random

counter = 0

print("Welkom bij:")
print("/ __)  /__\  (  )  / __) (_  _)( ___)")
print("( (_-. /(__)\  )(__( (_-..-_)(   )__) ")
print("\___/(__)(__)(____)\___/\____) (____)  ")

woorden = ["informatica", "linux", "python", "windows", "telegram", "toetsenbord", "apple", "codecrackers", "robotica", "berichten", "github", "monitor"]

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
gebruikte_letter=""

while True:
    letter = input("Type een letter, of type ? om het woord te raden. Type exit om Galgje te verlaten: ")
    lengte = len(letter)
    if letter in woord:
        print ("Dat is goed,")
        gebruikte_letter = gebruikte_letter + "," + letter
        print("Dit zijn je gebruikte letters:" + gebruikte_letter)
    elif letter in gebruikte_letter:
        print("Dat heb je al gezegd")
    elif letter == "?":
        raad=input("Type je woord: ")
        if raad == woord:
            print("Gefeliciteerd, je hebt het woord geraden!")
            print ("Dit waren je gebruikte letters: " + gebruikte_letter)
            break
        else:
            print("je hebt het woord fout geraden ")
            counter += 1
            check()
    elif lengte >= 2:
        print ("Geen 2 letters graag")
    elif letter == "exit":
        print ("Dit waren je gebruikte letters: " + gebruikte_letter)
        print ("Ik heb dat je hebt genoten, doei!")
        break

    else:
        print("Je letter is fout.")
        gebruikte_letter = gebruikte_letter + "," + letter
        print("Dit zijn je gebruikte letters:" + gebruikte_letter)
        counter += 1
        check()

    if counter == 5:
        print("Je hebt verloren.")
        break
