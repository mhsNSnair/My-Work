"""
course: ICS3U
filename: Nicholas_Conditional_Assignment
date: 06/03/20
name: Nicholas Snair
description: *****
"""

print('\033[1;39;40m'"Welcome to the Merivale Computers R Us. We look forward to helping you create the perfect computer for your needs. \n\n First, you will need a monitor. Here are two options:\n\n 1 - 27 inch Dell S2719DGF. This widescreen monitor is nice for watching widescreen movies. The cost is $275.99 \n\n 2 - 19 inch Dell P910S. This smaller screen has an aspect ratio of 5:4 and is more economical. The cost is $149.99 \n\n Please input your selection (1 or 2):")
moniter = int(input('\033[1;31;40m'))
if moniter == 1:
    moniter = 275.99
    moniterType =  'Dell S2719DGF'
elif moniter == 2:
    moniter = 149.99
    moniterType = "Dell P910S"

print('\033[1;39;40m', "\n ....\n\nThe CPU is considered the brain of the computer. Here are two CPU options: \n\n1 - The AMD Ryzen 5 3600 is great for gaming and doesn’t overheat. The Ryzen 5 costs $149.99\n\n2 - The AMD Ryzen 3 2200G is well suited to home office applications such as Microsoft Office. The Ryzen 3 costs $84.99\n\nPlease input your selection (1 or 2):")
cpu = int(input('\033[1;31;40m'))
if cpu == 1:
    cpu = 149.99
    cpuType =  'AMD Ryzen 5 3600'
elif cpu == 2:
    cpu = 84.99
    cpuType =  'AMD Ryzen 3 2200G'

print('\033[1;39;40m', "\n ....\n\nThe CPU is considered the brain of the computer. Here are two CPU options: \n\n1 - The AMD Ryzen 5 3600 is great for gaming and doesn’t overheat. The Ryzen 5 costs $149.99\n\n2 - The AMD Ryzen 3 2200G is well suited to home office applications such as Microsoft Office. The Ryzen 3 costs $84.99\n\nPlease input your selection (1 or 2):")
keyboard = int(input('\033[1;31;40m'))
if keyboard == 1:
    keyboard = 149.99
    keyboardType =  'AMD Ryzen 5 3600'
elif keyboard == 2:
    keyboard = 84.99
    keyboardType =  'AMD Ryzen 3 2200G'

print('\033[1;39;40m', "\n ....\n\nThe CPU is considered the brain of the computer. Here are two CPU options: \n\n1 - The AMD Ryzen 5 3600 is great for gaming and doesn’t overheat. The Ryzen 5 costs $149.99\n\n2 - The AMD Ryzen 3 2200G is well suited to home office applications such as Microsoft Office. The Ryzen 3 costs $84.99\n\nPlease input your selection (1 or 2):")
motherboard = int(input('\033[1;31;40m'))
if motherboard == 1:
    motherboard = 149.99
    motherboardType =  'AMD Ryzen 5 3600'
elif motherboard == 2:
    motherboard = 84.99
    motherboardType =  'AMD Ryzen 3 2200G'

print('\033[1;39;40m', "\n ....\n\nThe CPU is considered the brain of the computer. Here are two CPU options: \n\n1 - The AMD Ryzen 5 3600 is great for gaming and doesn’t overheat. The Ryzen 5 costs $149.99\n\n2 - The AMD Ryzen 3 2200G is well suited to home office applications such as Microsoft Office. The Ryzen 3 costs $84.99\n\nPlease input your selection (1 or 2):")
storage = int(input('\033[1;31;40m'))
if storage == 1:
    storage = 149.99
    storageType =  'AMD Ryzen 5 3600'
elif storage == 2:
    storage = 84.99
    storageType =  'AMD Ryzen 3 2200G'

print('\033[1;39;40m', "\n ....\n\nThe CPU is considered the brain of the computer. Here are two CPU options: \n\n1 - The AMD Ryzen 5 3600 is great for gaming and doesn’t overheat. The Ryzen 5 costs $149.99\n\n2 - The AMD Ryzen 3 2200G is well suited to home office applications such as Microsoft Office. The Ryzen 3 costs $84.99\n\nPlease input your selection (1 or 2):")
case = int(input('\033[1;31;40m'))
if case == 1:
    case = 149.99
    caseType =  'AMD Ryzen 5 3600'
elif case == 2:
    case = 84.99
    caseType =  'AMD Ryzen 3 2200G'

print('\033[1;39;40m', "\n ....\n\nThe CPU is considered the brain of the computer. Here are two CPU options: \n\n1 - The AMD Ryzen 5 3600 is great for gaming and doesn’t overheat. The Ryzen 5 costs $149.99\n\n2 - The AMD Ryzen 3 2200G is well suited to home office applications such as Microsoft Office. The Ryzen 3 costs $84.99\n\nPlease input your selection (1 or 2):")
powerSupply = int(input('\033[1;31;40m'))
if powerSupply == 1:
    powerSupply = 149.99
    powerSupplyType =  'AMD Ryzen 5 3600'
elif powerSupply == 2:
    powerSupply = 84.99
    powerSupplyType =  'AMD Ryzen 3 2200G'

print('\033[1;39;40m','...\n\nYour computer build is complete! Here’s a reminder of your selections:\n\n')
print(format("Component","15"), format("Selction",'15'), 'Cost\n'
     ,format("Moniter","15"), format(moniterType,'15'), '$',float(moniter)
,'\n',format("CPU","15"), format(cpuType,'15'), '$',float(cpu)
,'\n',format("Keyboard","15"), format(keyboardType,'15'), '$',float(keyboard)
,'\n',format("Motherboard","15"), format(motherboardType,'15'), '$',float(motherboard)
,'\n',format("Storage","15"), format(storageType,'15'), '$',float(storage)
,'\n',format("Case","15"), format(caseType,'15'), '$',float(case)
,'\n',format("Power Supply","15"), format(powerSupplyType,'15'), '$',float(powerSupply))
totalCost = moniter + cpu + keyboard + motherboard + storage + case + powerSupply
print(format('Total cost before tax:','30'),'$',totalCost)
finalCost = totalCost*1.13
print(format('Total cost after 13% HST:','30'),'$', finalCost)
