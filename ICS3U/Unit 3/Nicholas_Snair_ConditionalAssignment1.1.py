"""
course: ICS3U
filename: Nicholas_Conditional_Assignment
date: 06/03/20
name: Nicholas Snair
description: *****
"""

print('\033[1;39;40m'"Welcome to the Merivale Computers R Us. We look forward to helping you create the perfect computer for your needs. \n\nTo start you will need to specify if your looking for a \n\nGaming PC :1 \n\nor an \n\nOffice PC :2 \n\n")
pc = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))

if pc == 1:
    print('\033[1;39;40m',"\n ....\n\nFirst, you will need a monitor. For your Gaming PC. Here are three options:\n\n1 - Gaming 1. Gaming 1 description. The cost is Gaming 1 \n\n2 - Gaming 2. Gaming 2 description. The cost is Gaming 2 \n\n3 - Gaming 3. Gaming 3 description. The cost is Gaming 3 \n\n")
    moniter = int(input('Please input your selection (1 or 2 or 3):' '\033[1;31;40m'))
    if moniter == 1:
        moniter = 275.99
        moniterType =  'Gaming 1'
    elif moniter == 2:
        moniter = 149.99
        moniterType = "Gaming 2"
    elif moniter == 3:
        moniter = 149.99
        moniterType = "Gaming 3"

if pc == 2:
    print('\033[1;39;40m',"\n ....\n\nFirst, you will need a monitor. For your Office PC. Here are two options:\n\n1 - 27 inch Dell S2719DGF. This widescreen monitor is nice for watching widescreen movies. The cost is $275.99 \n\n2 - 19 inch Dell P910S. This smaller screen has an aspect ratio of 5:4 and is more economical. The cost is $149.99 \n\n3 - Office 3. Office 3 description. The cost is Office 3 \n\n")
    moniter = int(input('Please input your selection (1 or 2 or 3):' '\033[1;31;40m'))
    if moniter == 1:
        moniter = 275.99
        moniterType =  'Office 1'
    elif moniter == 2:
        moniter = 149.99
        moniterType = "Office 2"
    elif moniter == 3:
        moniter = 149.99
        moniterType = "Office 3"


if pc == 1:
    print('\033[1;39;40m',"\n ....\n\nThe CPU is considered the brain of the computer. Here are two CPU options: \n\n1 - The AMD Ryzen 3 1200 is great for gaming and doesn’t overheat. The Ryzen 3 costs $120.08\n\n2 - Gaming 2. Gaming 2 description. The cost is Gaming 2 \n\n3 - Gaming 3. Gaming 3 description. The cost is Gaming 3 \n\n")
    cpu = int(input('Please input your selection (1 or 2 or 3):' '\033[1;31;40m'))
    if cpu == 1:
        cpu = 120.08
        cpuType =  'AMD Ryzen 3 1200'
    elif cpu == 2:
        cpu = 84.99
        cpuType =  'Gaming 2'
    elif cpu == 3:
        cpu = 84.99
        cpuType =  'Gaming 3'

if pc == 2:
    print('\033[1;39;40m',"\n ....\n\nThe CPU is considered the brain of the computer. Here are two CPU options: \n\n1 - The AMD Ryzen 5 3600 is great for gaming and doesn’t overheat. The Ryzen 5 costs $149.99\n\n2 - The AMD Ryzen 3 2200G is well suited to home office applications such as Microsoft Office. The Ryzen 3 costs $84.99\n\n3 - Office 3. Office 3 description. The cost is Office 3 \n\n")
    cpu = int(input('Please input your selection (1 or 2 or 3):' '\033[1;31;40m'))
    if cpu == 1:
        cpu = 149.99
        cpuType =  'Office 1'
    elif cpu == 2:
        cpu = 84.99
        cpuType =  'Office 2'
    elif cpu == 3:
        cpu = 84.99
        cpuType =  'Office 3'


if pc == 1:
    print('\033[1;39;40m', "\n ....\n\n Keyboards .   Here are two keyboard options: \n\n2 - Gaming 1. Gaming 1 description. The cost is Gaming 1 \n\n2 - Gaming 2. Gaming 2 description. The cost is Gaming 2 \n\n")
    keyboard = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
    if keyboard == 1:
        keyboard = 149.99
        keyboardType =  'Gaming 1'
    elif keyboard == 2:
        keyboard = 84.99
        keyboardType =  'Gaming 2'

if pc == 2:
    print('\033[1;39;40m', "\n ....\n\n Keyboards  .  Here are two keyboard options: \n\n1 - Office 1. Office 1 price \n\n2 - The Office 2. The Office 2 price\n\n")
    keyboard = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
    if keyboard == 1:
        keyboard = 149.99
        keyboardType =  'Office 1'
    elif keyboard == 2:
        keyboard = 84.99
        keyboardType =  'Office 2'



if pc == 1:
    print('\033[1;39;40m', "\n ....\n\nThe Motherboard    . Here are two Motherboard options: \n\n1 - The ASRock MicroATX is . The ASRock MicroATX costs $116.52\n\n2 - Gaming 2. Gaming 2 description. The cost is Gaming 2 \n\n")
    motherboard = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
    if motherboard == 1:
        motherboard = 116.52
        motherboardType =  'ASRock MicroATX'
    elif motherboard == 2:
        motherboard = 84.99
        motherboardType =  'Gaming 2'

if pc == 2:
    print('\033[1;39;40m', "\n ....\n\nThe Motherboard    . Here are two Motherboard options: \n\n1 - The AMD Ryzen 5 3600 is great for gaming and doesn’t overheat. The Ryzen 5 costs $149.99\n\n2 - The AMD Ryzen 3 2200G is well suited to home office applications such as Microsoft Office. The Ryzen 3 costs $84.99\n\n")
    motherboard = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
    if motherboard == 1:
        motherboard = 149.99
        motherboardType =  'Office 1'
    elif motherboard == 2:
        motherboard = 84.99
        motherboardType =  'Office 2'



if pc == 1:
    print('\033[1;39;40m', "\n ....\n\nThe memory storage   . Here are two memory storages options: \n\n1 - The Corsair Vengeance LPX 8GB is . The Corsair Vengeance LPX 8GB costs $50.99\n\n2 - Gaming 2. Gaming 2 description. The cost is Gaming 2 \n\n")
    storage = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
    if storage == 1:
        storage = 50.99
        storageType =  'Corsair Vengeance LPX 8GB'
    elif storage == 2:
        storage = 84.99
        storageType =  'Gaming 2'

if pc == 2:
    print('\033[1;39;40m', "\n ....\n\nThe memory storage   . Here are two memory storages options: \n\n1 - The AMD Ryzen 5 3600 is great for gaming and doesn’t overheat. The Ryzen 5 costs $149.99\n\n2 - The AMD Ryzen 3 2200G is well suited to home office applications such as Microsoft Office. The Ryzen 3 costs $84.99\n\n")
    storage = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
    if storage == 1:
        storage = 149.99
        storageType =  'Office 1'
    elif storage == 2:
        storage = 84.99
        storageType =  'Office 2'



if pc == 1:
    print('\033[1;39;40m', "\n ....\n\nThe Case . Here are three case options: \n\n1 - Gaming 1. Gaming 1 description. The cost is Gaming 1 \n\n2 - Gaming 2. Gaming 2 description. The cost is Gaming 2 \n\n3 - Gaming 3. Gaming 3 description. The cost is Gaming 3 \n\n")
    case = int(input('Please input your selection (1 or 2 or 3):' '\033[1;31;40m'))
    if case == 1:
        case = 149.99
        caseType =  'Gaming 1'
    elif case == 2:
        case = 84.99
        caseType =  'Gaming 2'
    elif case == 3:
        case = 84.99
        caseType =  'Gaming 3'

if pc == 2:
    print('\033[1;39;40m', "\n ....\n\nThe Case . Here are three case options: \n\n1 - The AMD Ryzen 5 3600 is great for gaming and doesn’t overheat. The Ryzen 5 costs $149.99\n\n2 - The AMD Ryzen 3 2200G is well suited to home office applications such as Microsoft Office. The Ryzen 3 costs $84.99\n\n")
    case = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
    if case == 1:
        case = 149.99
        caseType =  'Office 1'
    elif case == 2:
        case = 84.99
        caseType =  'Office 2'



if pc == 1:
    print('\033[1;39;40m', "\n ....\n\nThe power supply. Here are two power supply options: \n\n1 - Gaming 1. Gaming 1 description. The cost is Gaming 1 \n\n2 - Gaming 2. Gaming 2 description. The cost is Gaming 2 \n\n3 - Gaming 3. Gaming 3 description. The cost is Gaming 3 \n\n")
    powerSupply = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
    if powerSupply == 1:
        powerSupply = 149.99
        powerSupplyType =  'Gaming 1'
    elif powerSupply == 2:
        powerSupply = 84.99
        powerSupplyType =  'Gaming 2'

if pc == 2:
    print('\033[1;39;40m', "\n ....\n\nThe power supply. Here are two power supply options: \n\n1 - The AMD Ryzen 5 3600 is great for gaming and doesn’t overheat. The Ryzen 5 costs $149.99\n\n2 - The AMD Ryzen 3 2200G is well suited to home office applications such as Microsoft Office. The Ryzen 3 costs $84.99\n\n")
    powerSupply = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
    if powerSupply == 1:
        powerSupply = 149.99
        powerSupplyType =  'Office 1'
    elif powerSupply == 2:
        powerSupply = 84.99
        powerSupplyType =  'Office 2'



print('\033[1;39;40m','...\n\nYour computer build is complete! Here’s a reminder of your selections:\n\n')
print(format("Component","15"), format("Selection",'25'), 'Cost\n'
     ,format("Monitor","15"), format(moniterType,'25'), '$',float(moniter)
,'\n',format("CPU","15"), format(cpuType,'25'), '$',float(cpu)
,'\n',format("Keyboard","15"), format(keyboardType,'25'), '$',float(keyboard)
,'\n',format("Motherboard","15"), format(motherboardType,'25'), '$',float(motherboard)
,'\n',format("Storage","15"), format(storageType,'25'), '$',float(storage)
,'\n',format("Case","15"), format(caseType,'25'), '$',float(case)
,'\n',format("Power Supply","15"), format(powerSupplyType,'25'), '$',float(powerSupply))
totalCost = moniter + cpu + keyboard + motherboard + storage + case + powerSupply
print(format('Total cost before tax:','42'),'$',totalCost)
finalCost = totalCost*1.13
print(format('Total cost after 13% HST:','42'),'$',format( finalCost, '.2f'))
