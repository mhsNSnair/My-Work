"""
course: ICS3U
filename: Nsnai1_Forest
date: 05/22/20
name: Nicholas Snair
description: Go through a Magical forest and see what fun things await.
"""
#Introduction to the forest and what to do
print('Welcome to the Super Happy Magic Forest, where everybody enjoys picnics, fun, and dancing all year round. \nExplore around the area see different places and maybe meet a few people along the way. \nWho knows you might even find something. ')

def oldOak():
    print('\n\033[0;37;40mDescription of the oldOak. You have found the Old Oak.\nIf it is wisdom that you seek then it is wisdom you shall receive.')
    print('Where do you want to go to next - 1:Pixie Housing 2:Happy Bunnies 3:Rainbow Falls')
    choice = int(input('Pick one of the corresponding numbers above.\033[1;32;40m'))

    if choice == 1:
        pixieHousing()
    elif choice == 2:
        happyBunnies()
    elif choice == 3:
        rainbowFalls()
    else:
        print('\033[0;37;40mError')
        oldOak()
"""def oldOak()
Docstring
Print - description of the oldOak. You have found the Old Oak. If it is wisdom that you seek then it is wisdom you shall receive.
Print - tell user what options are next - Pixie Housing, Happy Bunnies, Rainbow Falls.
Print - ask user to pick an option.
If they pick pixie housing, call pixieHousing()
If they pick Happy Bunnies, call happyBunnies()
If they pick Rainbow Falls, call rainbowFalls()
If the entery is invalid print - error, call oldOak()
"""
def rainbowFalls():
    print('\n\033[0;37;40mDescription of the rainbowFalls.\nThe most colourful water in all of the land and almost as pure as the Best Fishing Pond.')
    print('Where do you want to go to next - 1:Old Oak')
    choice = int(input('Pick one of the corresponding numbers above.\033[1;32;40m'))

    if choice == 1:
        oldOak()
    else:
        print('\033[0;37;40mError')
        rainbowFalls()

"""Def rainbowFalls()
Docstring
Print - description of the rainbowFalls. The most colourful water in all of the land and almost as pure as the Best Fishing Pond.
Print - tell user what option is next - Old Oak.
Print - ask user to pick an option.
If they pick old oak, call oldOak()
If the entery is invalid print - error, call rainbowFalls()
"""
def pixieHousing():
    print('\n\033[0;37;40mDescription of the pixieHousing.\nThe best housing service for pixies in this forested land.')
    pixie()
    print('\033[0;37;40mWhere do you want to go to next - 1:Old Oak 2:Lollipop Pond')
    choice = int(input('Pick one of the corresponding numbers above.\033[1;32;40m'))

    if choice == 1:
        oldOak()
    elif choice == 2:
        lollipopPond()
    else:
        print('\033[0;37;40mError')
        pixieHousing()
"""Def pixieHousing()
Docstring
Print - description of the pixieHousing. The best housing service for pixies in this forested land.
Call pixie()
Print - tell user what options are next - Old Oak, Lollipop Pond.
Print - ask user to pick an option.
If they pick old oak, call oldOak()
If they pick lollipop pond, call lollipopPond()
If the entery is invalid print - error, call pixieHousing()
"""
def happyBunnies():
    print('\n\033[0;37;40mDescription of the happyBunnies.\nNot much to say they are just cute happy bunnies have some fun.')
    print('Where do you want to go to next - 1:Old Oak 2:Magic Stones 3:Never Ending Picnic')
    choice = int(input('Pick one of the corresponding numbers above.\033[1;32;40m'))

    if choice == 1:
        oldOak()
    elif choice == 2:
        magicStones()
    elif choice == 3:
        neverEndingPicnic()
    else:
        print('\033[0;37;40mError')
        happyBunnies()
"""Def happyBunnies()
Docstring
Print - description of the happyBunnies. Not much to say they are just cute happy bunnies have some fun.
Print - tell user what options are next - Old Oak, Magic Stones, Never Ending Picnic.
Print - ask user to pick an option.
If they pick old oak, call oldOak()
If they pick magic stones, call magicStones()
If they pick Never ending, call neverEndingPicnic()
If the entery is invalid print - error, call happyBunnies()
"""
def butterflyHorse():
    print('\n\033[0;37;40mDescription of the butterflyHorse.\nWow a horse made of butter and it can fly would you look at that.')
    print('Where do you want to go to next - 1:Lollipop Pond')
    choice = int(input('Pick one of the corresponding numbers above.\033[1;32;40m'))

    if choice == 1:
        lollipopPond()
    else:
        print('\033[0;37;40mError')
        butterflyHorse()

"""Def butterflyHorse()
Docstring
Print - description of the butterflyHorse.
Print - tell user what option is next - Lollipop Pond.
Print - ask user to pick an option.
If they pick Lollipop Pond, call lollipopPond()
If the entery is invalid print - error, call butterflyHorse()
"""
def lollipopPond():
    print('\n\033[0;37;40mDescription of the lollipopPond.\nThe sweetest of all ponds in the land people use this water in a variety of recipes.')
    print('Where do you want to go to next - 1:Pixie Housing 2:Butterfly Horse 3:Dancing Fields')
    choice = int(input('Pick one of the corresponding numbers above.\033[1;32;40m'))

    if choice == 1:
        pixieHousing()
    elif choice == 2:
        butterflyHorse()
    elif choice == 3:
        dancingFields()
    else:
        print('\033[0;37;40mError')
        lollipopPond()
"""Def lollipopPond()
Docstring
Print - description of the lollipopPond. The sweetest of all ponds in the land people use this water in a variety of recipes.
Print - tell user what options are next - Pixie Housing, Butterfly Horse, Dancing Feilds.
Print - ask user to pick an option.
If they pick pixie housing, call pixieHousing()
If they pick Butterfly Horse, call butterflyHorse()
If they pick Dancing Fields, call dancingFields()
If the entery is invalid print - error, call lollipopPond()
"""
def dancingFields():
    print('\n\033[0;37;40mDescription of the dancingFields.\nThese fields only have one rule and that’s that you have to dance.')
    gnome()
    print('\033[0;37;40mWhere do you want to go to next - 1:Lollipop Pond 2:Mystical Crystals of Life 3:Magic Stones 4:Best Fishing Pond')
    choice = int(input('Pick one of the corresponding numbers above.\033[1;32;40m'))

    if choice == 1:
        lollipopPond()
    elif choice == 2:
        mysticalCrystalsOfLife()
    elif choice == 3:
        magicStones()
    elif choice == 4:
        bestFishingPond()
    else:
        print('\033[0;37;40mError')
        dancingFields()
"""Def dancingFields()
Docstring
Print - description of the dancingFeilds. These fields only have one rule and that’s that you have to dance.
Call gnome()
Print - tell user what options are next - Lollipop Pond, Mystical Crystals of Life, Magic Stones, Best Fishing Pond.
Print - ask user to pick an option.
If they pick lollipop pond, call lollipopPond()
If they pick mystical crystals of life call mysticalCrystalsOfLife()
If they pick magic stones, call magicStones()
If they pick best fishing pond, call bestFishingPond()
If the entery is invalid print - error, call dancingFields()
"""
def mysticalCrystalsOfLife():
    print('\n\033[0;37;40mDescription of the mysticalCrystalsOfLife.\nThese crystals are said to have mystical properties that make you live longer.')
    print('Where do you want to go to next - 1:Dancing Fields')
    choice = int(input('Pick one of the corresponding numbers above.\033[1;32;40m'))

    if choice == 1:
        relic()
        dancingFields()
    else:
        print('\033[0;37;40mError')
        mysticalCrystalsOfLife()
"""Def mysticalCrystalsOfLife()
Docstring
Print - description of the oldOak. These crystals are said to have mystical properties that make you live longer.
Print - tell user what option is next - Dancing Fields.
Print - ask user to pick an option.
If they pick dancing fields,call relic(), call dancingFields()
If the entery is invalid print - error, call mysticalCrystalsOfLife()
"""
def magicStones():
    print('\n\033[0;37;40mDescription of the magicStones.\nA place with a bounty of magic stones nobody knows what they do.')
    print('Where do you want to go to next - 1:Happy Bunnies 2:Dancing Fields 3:Best Fishing Pond 4:Cotton Candy Cave')
    choice = int(input('Pick one of the corresponding numbers above.\033[1;32;40m'))

    if choice == 1:
        relic()
        happyBunnies()
    elif choice == 2:
        relic()
        dancingFields()
    elif choice == 3:
        relic()
        bestFishingPond()
    elif choice == 4:
        relic()
        cottonCandyCave()
    else:
        print('\033[0;37;40mError')
        magicStones()
"""Def magicStones()
Docstring
Print - description of the magicStones. A place with a bounty of magic stones nobody knows what they do.
Print - tell user what options are next - Happy Bunnies, Dancing Fields, Best Fishing Pond, Cotton Candy Cave.
Print - ask user to pick an option.
If they pick Happy Bunnies,call relic(), call happyBunnies()
If they pick dancing fields,call relic(), call dancingFields()
If they pick best fishing pond ever,call relic(), call bestFishingPond()
If they pick cotton candy cave,call relic(), call cottonCandyCave()
If the entery is invalid print - error, call magicStones()
"""
def bestFishingPond():
    print('\n\033[0;37;40mDescription of the bestFishingPond.\nThe best fishing pond in all of the forest, due to how pure the water is you can find all kinds of fish.')
    print('Where do you want to go to next - 1:Magic Stones 2:Dancing Fields')
    choice = int(input('Pick one of the corresponding numbers above.\033[1;32;40m'))

    if choice == 1:
        magicStones()
    elif choice == 2:
        dancingFields()
    else:
        print('\033[0;37;40mError')
        bestFishingPond()
"""Def bestFishingPond()
Docstring
Print - description of the bestFishingPond. The best fishing pond in all of the forest, due to how pure the water is you can find all kinds of fish.
Print - tell user what options are next - Magic Stones, Dancing Fields.
Print - ask user to pick an option.
If they pick magic stones, call magicStones()
If they pick dancing fields, call dancingFields()
If the entery is invalid print - error, call bestFishingPond()
"""
def cottonCandyCave():
    print('\n\033[0;37;40mDescription of the cottonCandyCave.\nThe sweetest cave out there careful you don’t eat too much.')
    print('Where do you want to go to next - 1:Magic Stones 2:Never Ending Picnic')
    choice = int(input('Pick one of the corresponding numbers above.'))

    if choice == 1:
        magicStones()
    elif choice == 2:
        neverEndingPicnic()
    else:
        print('\033[0;37;40mError')
        cottonCandyCave()
"""Def cottonCandyCave()
Docstring
Print - description of the cottonCandyCave. The sweetest cave out there careful you don’t eat too much.
Print - tell user what options are next - Magic Stones, Never Ending Picnic.
Print - ask user to pick an option.
If they pick magic stones, call magicStones()
If they pick never ending picnic, call neverEndingPicnic()
If the entery is invalid print - error, call cottonCandyCave()
"""
def neverEndingPicnic():
    print('\n\033[0;37;40mDescription of the neverEndingPicnic.\nCome on join the picnic you can eat as much as you want.')
    mushroom()
    print('\033[0;37;40mWhere do you want to go to next - 1:Happy Bunnies 2:Cotton Candy Cave')
    choice = int(input('Pick one of the corresponding numbers above.\033[1;32;40m'))

    if choice == 1:
        relic()
        happyBunnies()

    elif choice == 2:
        relic()
        cottonCandyCave()

    else:
        print('\033[0;37;40mError')
        neverEndingPicnic()
"""Def neverEndingPicnic()
Docstring
Print - description of the neverEndingPicnic. Come on join the picnic you can eat as much as you want.
Call mushroom()
Print - tell user what options are next - Happy Bunnies, Cotton Candy Cave.
Print - ask user to pick an option.
If they pick Happy Bunnies,call relic(), call happyBunnies()
If they pick cotton candy cave,call relic(), call cottonCandyCave()
If the entery is invalid print - error, call neverEndingPicnic()
"""
def relic():
    import random
    relic = random.randint(1,10)
    if relic == 1:
        print('\n\033[0;37;40mAs you were leaving you tripped over a strange looking ancient relic and decided to take it with you. As you were walking with the relic it strated to shake and glow and then all of a sudden you...')
        oldOak()
"""Def relic()
Docstring
Import Random module
Assign a range to a variable
if variable = 1
    Print - description of the character
    Call oldOak()
"""
def pixie():
    import random
    twinkle = random.randint(1,3)
    if twinkle == 2:
        print('You see a \033[1;35;40mfairy\033[0;37;40m outside one of their homes and she comes up to you and says that she hopes you enjoy your stay.')
"""Def pixie()
Docstring
Import Random module
Assign a range to a variable
if variable = 2
    Print - description of the character
"""
def gnome():
    import random
    herbert = random.randint(1,5)
    if herbert == 4:
        print('As you enter the dancing feilds you see a \033[0;36;40mshort gnome\033[0;37;40m looking guy who looks like he is doing some work on the fields. You decide to leave him be')
"""Def gnome()
Docstring
Import Random module
Assign a range to a variable
if variable = 4
    Print - description of the character
"""
def mushroom():
    import random
    trevor = random.randint(1,20)
    if trevor == 15:
        print('You stumble upon a \033[0;33;40mmushroom\033[0;37;40m who seems to be scared and pleading for his life. You assure him that you are not going to eat him and go on your way.')
"""Def mushroom()
Docstring
Import Random module
Assign a range to a variable
if variable = 15
    Print - description of the character
"""
oldOak()
