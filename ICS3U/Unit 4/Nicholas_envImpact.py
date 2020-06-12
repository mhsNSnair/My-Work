"""
course: ICS3U
filename: Nicholas_envImpact
date: 04/01/20
name: Nicholas Snair
description: This program is a database taht will teach you the enviromental impacts of computers in the context of highschools.
"""
#Welcomes the user to the program
print ("\033[1;37;40m\nWelcome to the environmental impact database, here you will learn about the impact of computers in highschools.")
#Prompts the user for the different parts of information
#All code is placed within the while loop in order to return to this section of code after specific functions
while True:
    loop = False
    print("\033[1;37;40m\n1. Negative effects of computer use on human health \n2. Measures that help reduce the impact of computers on human health\n3. Government agencies & community partners that provide resources & guidance for environmental stewardship\n4. Exit program")
    choice = input("\nSelect a group of information by inputting the number listed on the left\033[1;31;40m ")
#Selecting each info for each category
    if choice == '1':
#Effects on human health
        print("\033[1;37;40m\nSince technology is more prominate in todays society online work and research is used alot in schooling. \nThough you may be learning, extended exposure to computers can affect your health. \n-Sleep deprivation due to the duration of usage, always being tired and not being able to focus. \n-Strained Vision due to the brighness and duration of usage, \n making your eyesight worse and having a possibllity of needing glasses. \n-Muscle and joint pain due to sitting and typing for an extended period of time, arthritis and muscle fatigue. \n-Anti social due to lack of social interation, loneliness and possibly depression. ")#[2]
        loop = True
    elif choice == '2':
#Reducing effects on human health
        print("\033[1;37;40m\n-Instead of going at schools projects all at once take breaks in between \nto reduce the risk of joint and muscle pain as well as eye strain \n-Adjust the level of brightness and turn on blue light filters in order to reduce eye strain \n-Limit the amount of usage and go outside to make social interations so that you are not lonely.")#[2]
        loop = True
    elif choice == '3':
#Organizations that aid in providing regulation
        print("\033[1;37;40m\nBelow are some companies that provide enviromental stewardship \n-Cartier Resources Inc.\n-Softrock Minerals Ltd.\n-Casa Minerals\n-Independence Gold Corp.\n-Canadian International Minerals Inc.")#[1]
        loop = True
    elif choice == '4':
        print("\033[1;37;40m\nThanks for using our program!")
        exit()
    else:
        print("\033[1;37;40m\nI didn't catch that, try again.")
    if loop == True:
#Asks the user if they want to restart the program, which means selecting a new category if yes is chosen
        while loop == True:
            back = str(input("\nGo back? (y/n):\033[1;31;40m "))
            if back in ('y','n'):
                break
            print("\033[1;37;40m\nOops! I didn't get that")
#Restarts the program if the user inputs 'y'
        if back == 'y':
            continue
#Else the program closes
        else:
            print("\033[1;37;40m\nThanks for using this database!")
            break




"""
“CSR in Canada – Environmental Stewardship,” Natural Resources Canada, 31-Jan-2019. [Online]. Available:
https://www.nrcan.gc.ca/mining-materials/mining/corporate-social-responsibility/17275. [Accessed: 02-Apr-2020].[1]

“The Real Effects of Technology on Your Health,” EverydayHealth.com, 15-Nov-2017. [Online]. Available:
https://www.everydayhealth.com/emotional-health/internet-addiction/real-effects-technology-on-your-health/. [Accessed: 02-Apr-2020].[2]
"""
