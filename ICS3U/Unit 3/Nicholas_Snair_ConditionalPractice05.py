"""
course: ICS3U
filename: Nicholas_GET_TO_THE_ROOT_OF_THE_PROBLEM
date: 26/02/20
name: Nicholas Snair
description: Given 3 numbers it can find the discriminant and
             show the roots for that quadratic
"""
# Imports the library into the project
import math
# Prompts the user for 3 different numbers in order to find the roots  and the discriminant.
print("Type in 3 different numbers and you will be given the discriminant and the roots of the quadratic.")
a = float(input())
b = float(input())
c = float(input())
# calculates the discriminant.
discriminant = b**2 - 4*a*c
# Prints that this is the discriminant.
print("The discriminant is", str(discriminant))
# If the discriminant is greater than 0 calculate the two roots and print them.
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant))/(2*a)
    root2 = (-b - math.sqrt(discriminant))/(2*a)
    print("The equation has two roots at", format(root1, ".2f"), "and" ,format(root2, ".2f"),".")
# If the discriminant is equal to 0 calculate the one root and print it.
elif discriminant == 0:
    root1 = (-b + math.sqrt(discriminant))/(2*a)
    print("The equation has one root at", format(root1, ".2f"),".")
# If the discriminant is less than 0 print The equation has no real roots.
elif discriminant < 0:
    print("The equation has no real roots.")
