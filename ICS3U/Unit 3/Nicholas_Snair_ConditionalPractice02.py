"""
course: ICS3U
filename: Nicholas_UPPERCASE/LOWERCASE_PROBLEM
date: 26/02/20
name: Nicholas Snair
description: Given a letter it will use the ord function to
             output that the letter is uppercase or lowercase.
"""
# Prompts the user to enter in a letter.
print("Please enter a letter.")
letter = ord(input())
# If the number from the ord fuction is inbetween 65 and 90 print UPPERCASE.
if (65<=letter <= 90):
    print ("Your letter was an UPPERCASE letter.")
# If the number from the ord fuction is greater than 122 print ERROR that is not a number.
elif (letter >= 122):
    print("ERROR that is not a number.")
# If the number from the ord fuction is greater than 91 print lowercase.
elif (letter >= 91):
    print("Your letter was a lowercase letter.")
# If the number from the ord fuction is less than 64 print ERROR that is not a number.
elif (letter <= 64):
    print("ERROR that is not a number.")
