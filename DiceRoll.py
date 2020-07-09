import random

def roll(sides=6):
    numRolled = random.randint(1,sides)
    return numRolled

def main():
    sides = 6
    rolling = True
    while rolling:
        rollAgain = input("Press ENTER to roll. Press Q to quit. ")
        if rollAgain.lower() != "q":
            numRolled = roll(sides)
            print ("You rolled a ", numRolled)

        else:
            rolling = False

    print("Thanks for playing.")

main()