def number_game(a):
    print()

import random as rand
print("-----------------------------------")
print("Welcome to my number guessing game!")
print("-----------------------------------")
print('''Instructions:
    The player must pick a difficulty from Level 1 to 3, where the player
    will guess the number based on the range given and the number of
    guesses that they have.\n''')
print("""The difficulties are as follows:
    Level 1: Range (1-10), 2 Guesses
    Level 2: Range (1-100), 5 Guesses
    Level 3: Range (1-500), 10 Guesses""")
menu = 0
while menu == 0:
    print("-----------------------------------")
    difficulty = int(input("Please Enter the Level You Wish to Play: "))
    print("-----------------------------------")

    if difficulty == 1:
        numguess = rand.randint(1, 10)
        print(numguess)
        print("The program now has chosen a number in the range of 1-10...")
        guess = int(input("Enter Your First Guess: "))
        
        if guess == numguess:
            print("Congrats, You Have Guessed Correctly!")
            print("Your Number: " + str(guess))
            print("The Computer's Number: " + str(numguess))
        
    elif difficulty == 2:
        numguess = rand.randint(1, 100)
    elif difficulty == 3:
        numguess = rand.randint(1, 500)
    else:
        print("INVALID Difficulty, Please Try Again.")
