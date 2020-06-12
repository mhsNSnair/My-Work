"""
course: ICS3U
filename: Nicholas_ZODIAC_SIGN_PROBLEM
date: 26/02/20
name: Nicholas Snair
description: Using specific case sensitive dates it
             will print your zodiac sign and symbol
             for that time frame.
"""
# Prompts the user for their abbreviated birthmonth and their day of birth.
print("Please enter your birthmonth. Ex. Feb")
birthmonth = input()
print("Please enter your birthday. Ex. 25")
birthday = int(input())
# If the birthmonth matches one of these down below it will print the coresponding sign and symbol of the zodiac.
if birthday > 31 and birthmonth == 'Jan' or birthday > 29 and birthmonth == 'Feb' or birthday > 31 and birthmonth == 'Mar' or birthday > 30 and birthmonth == 'Apr' or birthday > 31 and birthmonth == 'May' or birthday > 30 and birthmonth == 'Jun' or birthday > 31 and birthmonth == 'Jul' or birthday > 31 and birthmonth == 'Aug' or birthday > 30 and birthmonth == 'Sep' or birthday > 31 and birthmonth == 'Oct' or birthday > 30 and birthmonth == 'Nov' or birthday > 31 and birthmonth == 'Dec':
    print("That is not a real date.")
elif (birthmonth == 'Mar') and (31 >= birthday >= 21) or (birthmonth == 'Apr') and (1 <= birthday <= 19):
    print("Aries The Ram")
elif (birthmonth == 'Apr') and (30 >= birthday >= 20) or (birthmonth == 'May') and (1 <= birthday <= 20):
    print("Taurus The Bull")
elif (birthmonth == 'May') and (31 >= birthday >= 21) or (birthmonth == 'Jun') and (1 <= birthday <= 21):
    print("Gemini The Twins")
elif (birthmonth == 'Jun') and (30 >= birthday >= 22) or (birthmonth == 'Jul') and (1 <= birthday <= 22):
    print("Cancer The Crab")
elif (birthmonth == 'Jul') and (31 >= birthday >= 23) or (birthmonth == 'Aug') and (1 <= birthday <= 22):
    print("Leo The Lion")
elif (birthmonth == 'Aug') and (31 >= birthday >= 23) or (birthmonth == 'Sep') and (1 <= birthday <= 22):
    print("Virgo The Virgin")
elif (birthmonth == 'Sep') and (30 >= birthday >= 23) or (birthmonth == 'Oct') and (1 <= birthday <= 23):
    print("Libra The Scales")
elif (birthmonth == 'Oct') and (31 >= birthday >= 24) or (birthmonth == 'Nov') and (1 <= birthday <= 21):
    print("Scorpio The Scorpion")
elif (birthmonth == 'Nov') and (30 >= birthday >= 22) or (birthmonth == 'Dec') and (1 <= birthday <= 21):
    print("Sagittarius The Archer")
elif (birthmonth == 'Dec') and (31 >= birthday >= 22) or (birthmonth == 'Jan') and (1 <= birthday <= 19):
    print("Capricorn The Goat")
elif (birthmonth == 'Jan') and (31 >= birthday >= 20) or (birthmonth == 'Feb') and (1 <= birthday <= 18):
    print("Aquarius The Water Bearer")
elif (birthmonth == 'Feb') and (29 >= birthday >= 19) or (birthmonth == 'Mar') and (1 <= birthday <= 20):
    print("Pisces The Fishes")
