"""
course: ICS3U
filename: Nicholas_POSTAGE_STAMP_PROBLEM
date: 26/02/20
name: Nicholas Snair
description: Given the weight of a package it will output
             the cost of that package at different intervals
             of weight.
"""
# Prompts the user to input how much their package weights.
print('How much does your package weight?')
weight = float(input())
# Prints how much the package weights,
print("The weight of your package is", weight, "g.")
# If the package weights up to 30g it will print the cost of $1.07.
if weight <= 30:
    cost = 1.07
    print("Cost is $1.07.")
# If the package weights more than 30g but up 50g it will print the cost of $1.30.
elif 30 < weight <= 50:
    cost = 1.30
    print("Cost is $1.30.")
# If the package weights more than 50g but up 100g it will print the cost of $1.94.
elif 50 < weight <= 100:
    cost = 1.94
    print("Cost is $1.94.")
# If the package weights more than 100g it will add an extra $1.15 for every 100 more grams ex. 100g = 1.94, 101g = 3.09, 200g = $3.09, 201g = $4.24
elif 100< weight:
    cost = 1.94 + 1.15*((weight-1)//100%100)
    print("Cost is $",format (cost,".2f"), ".")
