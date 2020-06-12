"""
course: ICS3U
filename: Nicholas_Address_Book
date: 04/23/20
name: Nicholas Snair
description: This program is an address book that will store names address as well as phone numbers.
"""
# Intro to the program
print("Welcome to the address book program, here you can store personal information.")
# Setup for the array called book putting in putting in 3 lists for name, address, and phone number
book = []
for i in range(5):
    name = input("\033[0;37;40mPlease enter the name you would like to register \033[1;37;40m" )
    address = input("\033[0;37;40mPlease enter the address of this person \033[1;37;40m")
    phone_Number = input("\033[0;37;40mPlease enter the phone number of this person \033[1;37;40m")
    book.append([name, address, phone_Number])
# Me fooling around with if statements so if those exact strings are put in it says your a lier
    if name == 'Nick Snair' and address == '14 Dandeland' and phone_Number == '613 818 7608':
        print('Someone is a lier')

# While the progarm is in a true state loop this
while True:
    print('\033[1;37;40m___________________________________________________________________________________________________\n')
# UI
    print("\033[0;37;40m1. View an existing person's address\n2. Edit an existing person's information\n3. Delete an entry\n4. Add a new entry\n")
# Selection variable
    select = input("Please select an option from above:\033[1;37;40m ")
    print('___________________________________________________________________________________________________\n')
# Used to see an existing persons information
    if select == '1':
        search = input("\033[0;37;40mPlease enter the name of the person:\033[1;37;40m ")
        for a in book:
# Searches in the name list for the information connected to that name
            if search in a[0]:
                print('\033[0;37;40mThe address for','\033[1;37;40m', search,'\033[0;37;40m', 'is','\033[1;37;40m', a[1],'\033[0;37;40m', 'and their phone number is' ,'\033[1;37;40m', a[2],'\033[0;37;40m',)
# Returns an error if the name inputted is not found
            elif search != name:
                print('\033[1;31;40mNot a valid name, returning to menu.')
                break
        continue
# Used to edit an existing persons information
    if select == '2':
        search = input("\033[0;37;40mPlease enter the name of the person:\033[1;37;40m ")
        for a in book:
# Searches in the name list for the information connected to that name
            if search in a[0]:
                print('\033[0;37;40mPlease input the new address for','\033[1;37;40m', search,'\033[0;37;40m',)
                a[1] = input('\033[1;37;40m')
                print('\033[0;37;40mPlease input the new phone number for','\033[1;37;40m', search,'\033[0;37;40m',)
                a[2] = input('\033[1;37;40m')
                print('\033[0;37;40mInfo for', search,'\033[0;37;40m', 'has been changed to','\033[1;37;40m', a[1],'\033[0;37;40m', 'and their phone number is','\033[1;37;40m', a[2],'\033[0;37;40m', '.')
# Returns an error if the name inputted is not found
            elif search != name:
                print('\033[1;31;40mNot a valid name, returning to menu.')
                break
        continue
# Used to delete an existing persons information
    if select == '3':
        search = input("\033[0;37;40mPlease enter the name of the person:\033[1;37;40m ")
        for a in book:
# Searches in the name list for the information connected to that name
            if search in a[0]:
                print('\033[0;37;40mInfo for','\033[1;37;40m', search,'\033[0;37;40m', 'has been deleted!')
                del a[0]
# Returns an error if the name inputted is not found
            elif search != name:
                print('\033[1;31;40mNot a valid name, returning to menu.')
                break
        continue

# Used to add a new persons information
    if select == '4':
        name = input("\033[0;37;40mPlease enter the name you would like to register\033[1;37;40m ")
        address = input("\033[0;37;40mPlease enter the address of this person\033[1;37;40m ")
        phone_Number = input("\033[0;37;40mPlease enter the phone number of this person \033[1;37;40m")
        book.append([name, address, phone_Number])
        print('\033[0;37;40mThe address for','\033[1;37;40m', name,'\033[0;37;40m', 'is','\033[1;37;40m', address,'\033[0;37;40m', 'and their phone number is' ,'\033[1;37;40m', phone_Number,'\033[0;37;40m',)
        print('___________________________________________________________________________________________________')
        continue
