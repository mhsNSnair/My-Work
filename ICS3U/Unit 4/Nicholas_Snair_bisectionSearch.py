"""
course: ICS3U
filename: Nicholas_Snair_bisectionSearch
date: 03/26/20
name: Nicholas Snair
description: This program will guess the number you are thinking of.
"""
# Welcomes the user
while True:
    restart = False
 # Imports functionality for random integers
    import random
    min = random.randint(0,2000)
    max = random.randint(min+10,2000)
# Every game, the ranges are two random integers between 0 and 2000
    print('\nThink of a number in the range below. \n')
# We subtract one from the second and add one to the first to include all numbers in the range inclusively
    print(min-1,max+1)
# The user can either choose to begin the game, or reroll the numbers if desired
    choice = input("\nTo start press [Y] to re pick the range of numbers press [N]")
    while choice == 'Y' and restart == False:
        if choice == ('Y' or 'N'):
# The first guess will be the average between the two ranges
            guess = (min + max)//2
            print('\nYour secret number you were thinking of?',guess, '\n')

        while True:
            reroll = input("Type [H] if my guess was too high or [L] if it was too low and [C] if it was correct.")
# If we cant search any further, notify the user that the number has been found
# The code below checks to see if the difference between the guess and range is 1, which means that the guess is stuck between 2 values
            if reroll == "L" and abs(guess - max) == 1 or reroll == 'H' and abs(guess - min) ==1:
                print('\nI cant go further you must be lying.')
                exit()
            if reroll == 'H':
# If the user says the guess was high, adjust the range of the guess accordingly
                max = guess
# Finds the average in between the range and prints the output
                guess = (guess+min)//2
                print ('\nIs this your secret number that you were thinking of?', guess,'\n')
                continue
            elif reroll == 'L':
# If the user says the guess was low, adjust the range of the guess accordingly
                min = guess
# Finds the average in between the range and prints the output
                guess = (guess+max)//2
                print ('\nIs this your secret number that you were thinking of?', guess,'\n')
                continue
            elif reroll == 'C':
# Ends the game if the console guesses correctly
                print('\nPerfect thank you for playing.')
# Logic for restarting the game
                while True:
                    answer = input('\nRestart? (y/n): ')
                    if answer in ('y', 'n'):
                        break
                    print('\nInvalid entry please input a valid input.')
#Restarts the program on input
                if answer == 'y':
#We set restart to True so that we can exit both loops
                    restart = True
                    break
                else:
#Exits the game
                    print('\nThank you for using this program!')
                    exit()
            else:
# If anything else is inputted, show an error
                print(' \nI am sorry I did not get that.\n')
                continue
        else:
            continue
