"""
course: ICS3U
filename: Nicholas_TRIANGLE_PROBLEM
date: 26/02/20
name: Nicholas Snair
description: Given 3 side lengths it will tell you wether these
             lengths would give you a triangle tha tis Equilatera,
             Isosceles, or Scalene.
"""
# Prompts the user for the side lengths of a triangle.
print("Please enter in the sides lengths of any triangle.")
side1 = float(input())
side2 = float(input())
side3 = float(input())
# If all three of the sides are equal print Equilateral.
if (side1 == side2 == side3):
    print("Your triangle has all equal sides and is an Equilateral triangle.")
# If two of the sides are equal print Isosceles,
elif (side1 == side2) or (side2 == side3) or (side3 == side1):
    print("Your triangle has two equal sides and is an Isosceles triangle.")
# Otherwise if none of the sides are equal print Scalene.
else:
    print("Your triangle has no equal sides and is a Scalene triangle.")
