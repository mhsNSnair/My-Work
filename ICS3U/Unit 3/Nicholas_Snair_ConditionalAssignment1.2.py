"""
course: ICS3U
filename: Nicholas_Conditional_Assignment
date: 06/03/20
name: Nicholas Snair
description: *****
"""

print('\033[1;39;40m'"Welcome to the Merivale Computers R Us. We look forward to helping you create the perfect computer for your needs.")

print('\033[1;39;40m',"\n ....\n\nFirst, you will need a monitor. For your PC. Here are three options:\n\n1 - Gaming 1. Gaming 1 description. The cost is Gaming 1 \n\n2 - Gaming 2. Gaming 2 description. The cost is Gaming 2 \n\n3 - Gaming 3. Gaming 3 description. The cost is Gaming 3 \n\n")
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

print('\033[1;39;40m',"\n ....\n\nThe CPU is considered the brain of the computer that performs all the calculations the computer needs to in order to have it run smoothly. Here are three CPU options that all come with coolers right out of the box: \n\n1 - Ryzen 3 2200g with Radeon Vega 8 graphics for $154.67.\n This is a great option for entry leveling gaming or office work with a great price and built-in graphics processing that helps display what you are doing on your monitor screen.\n\n2 - Ryzen 5 3600. This performs calculations even faster than the Ryzen 3 and is great for gaming and office work. With more power means that in the future with new technology the Ryzen 5 will be still viable. The cost is $239.99 \n\n3 - Ryzen 9 3900x. The ultimate gaming and office machine. If you want to run powerful programs and games at fast rates and calculate even faster then this is what you want. Top level specifications make it one of the fastest cpu and allow for even the most intense software such as 3D image processing calculations. This comes at a cost of $579.99 \n\n")
cpu = int(input('Please input your selection (1 or 2 or 3):' '\033[1;31;40m'))
if cpu == 1:
        cpu = 154.67
        cpuType =  'Ryzen 3 2200g with Radeon Vega 8 graphics'
elif cpu == 2:
        cpu = 239.99
        cpuType =  'Ryzen 5 3600'
elif cpu == 3:
        cpu = 579.99
        cpuType =  'Ryzen 9 3900x'

if cpu == 154.67:
    print('\033[1;39;40m',"\n ....\n\nSince you have chosen the Ryzen 3 2200g with Radeon Vega 8 graphics you won’t have to worry about spending money on a dedicated graphics card, however, if you want even crisper and clearer images feel free to upgrade to a dedicated graphics card. Press 0 if you want to skip the GPU.")

print('\033[1;39;40m',"\n ....\n\nThe GPU is  ****. Here are some GPU options: \n\n1 - The ASUS PH-GT1030-O2G. The ASUS PH-GT1030-O2G costs $119.99\n\n2 - GTX 1650 Gaming X. This is an entry level gaming graphics card. What this does is display what your cpu calculates and turns it into visuals on your monitor screen. This card works great when running games and for office work with 3D rendering too. This pairs well with resolutions at 1080p (the higher the resolution the more detail and higher image quality there is. This is great for watching media such as movies in high resolutions with great clarity. The cost is $222.98 \n\n3 - GTX 1660ti. If you have a demand for power and want to run games at resolutions of 1440p then this card will work wonders. It has even more power to translate into better visuals for all your office and games. The cost is $374.99 \n\n4 - GTX 2080 Super. If you enjoy playing the most hardware intensive games and 3D image modeling, simulations, and rendering at 2160p or 4k resolutions this card has it all. If you are serious about the best visuals then this GPU is what you need. The cost is $1029.99 \n\n")
gpu = int(input('Please input your selection (1 or 2 or 3 or 4):' '\033[1;31;40m'))
if gpu == 1:
    gpu = 119.99
    gpuType =  'ASUS PH-GT1030-O2G'
elif gpu == 2:
    gpu = 222.98
    gpuType =  'GTX 1650 Gaming X'
elif gpu == 3:
    gpu = 374.99
    gpuType =  'GTX 1660ti'
elif gpu == 4:
    gpu = 1029.99
    gpuType =  'GTX 2080 Super'
elif gpu == 0:
    gpu = 0.00
    gpuType =  '*No additional cost*'

print('\033[1;39;40m',"\n ....\n\nThe RAM is ****. Here are two RAM options: \n\n1 - The Corsair 8GB DDR4 Dram will provide short term memory for your computer that includes opening up internet browser tabs or playing a game or opening up photoshop it all needs RAM. With more ram you are able to have more things running at once with multiple programs at once such as streaming gameplay with a screen recorder and actually running the game. 8gb is perfect for lower level games, office work, and having very few programs open at once. The Corsair 8GB DDR4 Dram costs $54.99\n\n2 - Corsair Vengeance LPX 16GB DDR4 DRAM 3000MHz. Perhaps you are finding you want to have more programs running such as creating videos, research tabs, games open, video editors, and whatever you want then maybe consider getting even more RAM to handle all the memory requirements. With double the capabilities you will be able to run almost any program and others at the same time. With the added speed of 3000MHz means that you are able to run more even faster. The cost is $ \n\n")
ram = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
if ram == 1:
        ram = 54.99
        ramType =  'Corsair 8GB DDR4 DRAM 2600MHz'
elif ram == 2:
        ram = 104.99
        ramType =  'Corsair Vengeance LPX 16GB DDR4 DRAM 3000MHz'

print('\033[1;39;40m', "\n ....\n\n Keyboards .   Here are two keyboard options: \n\n1 - Redragon K552-RGB. This budget mechanical keyboard is great for those who like the tactile feel of pressing keys down like pushing a button that clicks. It also comes with a customizable backlight for when you want to add a little flair to your roomThe cost is $55.99 1 \n\n2 - Corsair CH-9206015-NA. This keyboard has a membrane feel which feels mushy rather than a snappy button. The added features of 6 programmable keys called macros means you can assign any action to them such as opening up your favourite video game. With volume buttons and pause, play, skip, and backward media buttons allowing quick changes on the fly without having to go into settings. Also comes with a customizable backlight. The cost is $79.99 \n\n3 - Logitech Keyboard K120. An inexpensive barebones keyboard is great for reliability membrane key presses for those who just need functionality and no gimmicks for a great price. The cost is $19.99 \n\n4 - CORSAIR K95 RGB. For the ultimate keyboard with premium Cherry MX Brown mechanical key switches that make typing a dream. The feedback of these keys is unmatched for reliability especially for precise inputs during gaming. With 6 macro keys, a volume scroll wheel, and media buttons put all the features into a reliable typing machine. The cost is $269.99 \n\n")
keyboard = int(input('Please input your selection (1 or 2 or 3 or 4):' '\033[1;31;40m'))
if keyboard == 1:
        keyboard = 55.99
        keyboardType =  'Redragon Mechanical Switch K552-RGB'
elif keyboard == 2:
        keyboard = 79.99
        keyboardType =  'Corsair K55 RGB Membrane Switch'
elif keyboard == 3:
        keyboard = 19.99
        keyboardType =  'Logitech Keyboard K120 Membrane Switch'
elif keyboard == 4:
        keyboard = 269.99
        keyboardType =  'CORSAIR K95 RGB Platinum Mechanical Switch Cherry MX Brown'

print('\033[1;39;40m', "\n ....\n\nThe Motherboard    . Here are two Motherboard options: \n\n1 - The ASRock B450 MicroATX is budget friendly, small size, and provides everything you need without the gimmicks. The ASRock B450 MicroATX costs $116.52\n\n2 -  The MSI B450 Gaming Plus Max ATX is excellent for gaming where you want to have added audio support for great sound quality, better power delivery, better heatsinks, and high speed information receiving. These all boost how under the stress of gaming that you have a reliable motherboard keeping your parts protected. It is slightly larger than the MicroATX size. The cost is139.99\n\n")
motherboard = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
if motherboard == 1:
        motherboard = 116.52
        motherboardType =  'ASRock MicroATX'
elif motherboard == 2:
        motherboard = 139.99
        motherboardType =  'MSI B450 Gaming Plus Max ATX'

print('\033[1;39;40m', "\n ....\n\nThe memory storage   . Here are two memory storage options: \n\n1 - The Seagate BarraCuda 2TB Internal Hard Drive is a storage device like long term memory that stores all your files, games, pictures, movies, and other downloads. With 2TB of memory capacity it would take 4 million pictures to fill the storage or 70 hours of 4k footage. This will satisfy all your memory needs.  The Seagate BarraCuda 2TB Internal Hard Drive costs $64.99\n\n2 - The Seagate 2TB FireCuda Gaming. With gaming in mind this is perfect for increased speeds of downloading and uploading data. Unlike the previous model this has high speed. This means downloading, copying, and uploading files from your hard drive is even faster. This is especially true for games with incredibly fast boot times compared to the previous hard drive. The Seagate 2TB FireCuda Gaming costs $99.99 \n\n")
storage = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
if storage == 1:
        storage = 64.99
        storageType =  'Seagate BarraCuda 2TB Internal Hard Drive'
elif storage == 2:
        storage = 99.99
        storageType =  'Seagate 2TB FireCuda Gaming'

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

print('\033[1;39;40m', "\n ....\n\nThe mouse . Here are four case options: \n\n1 - Logitech G903 LIGHTSPEED. For fast, wireless, and accurate mouse inputs especially for professional gaming this is perfect for you. The cost is $94.99 1 \n\n2 - Razer Mamba Elite. For fast, wired, abd accurate mouse inputs especially for gaming this mouse is perfect for you. The cost is $98.79  \n\n3 - Logitech M100. For reliable, well-built, and budget friendly wired mouse this is perfect for you. The cost is $12.38 \n\n4 - Logitech Wireless Mouse M185. For reliable, well-built, and budget friendly wireless mouse this is perfect for you. The cost is $14.88  \n\n")
mouse = int(input('Please input your selection (1 or 2 or 3 or 4):' '\033[1;31;40m'))
if mouse == 1:
        mouse= 94.99
        mouseType =  'Logitech G903 LIGHTSPEED'
elif mouse == 2:
        mouse = 98.79
        mouseType =  'Razer Mamba Elite'
elif mouse == 3:
        mouse = 12.38
        mouseType =  'Logitech M100'
elif mouse == 4:
        mouse = 14.88
        mouseType =  'Logitech Wireless Mouse M185'

print('\033[1;39;40m', "\n ....\n\nThe headphones . Here are three case options: \n\n1 - Logitech Stereo Gaming Headset G230. If a budget friendly, comfortable, fold-away microphone, and durable headset is what you want then this headset is right for you/ Gaming 1 description. The cost is $49.00 \n\n2 - Logitech G432 DTS:X. With peak sound quality, folding microphone, simulated surround sound to help locate where sounds come from which is very important for gaming then this headset is for you. The cost is $69.98 \n\n3 - HyperX Cloud Alpha Pro Gaming Headset. This headset has a detachable microphone, unparalleled sound quality, unparalleled comfortability, and lightweight means you can rely on these and wear them without even feeling them on you at all. For music enthusiasts or gamers that want the best out of their headset this is for them.   The cost is $134.99 \n\n")
headphones = int(input('Please input your selection (1 or 2 or 3):' '\033[1;31;40m'))
if headphones == 1:
        headphones = 49.00
        headphonesType =  'Logitech Stereo Gaming Headset G230'
elif headphones == 2:
        headphones = 69.98
        headphonesType =  'Logitech G432 7.1 Virtual Surround Sound'
elif headphones == 3:
        headphones = 134.99
        headphonesType =  'HyperX Cloud Alpha Pro Gaming Headset '

print('\033[1;39;40m', "\n ....\n\nThe power supply. Here are two power supply options: \n\n1 - Corsair 750 Watt, 80+ Platinum Certified, Fully Modular. This is the ultimate power and efficiency power supply. With 80+ Platinum certified guarantees peak efficiency and with 750 watts of power delivery ensures all your parts get the power they need. With fully modular wires means you only have to plug in what requires the power and leave out the other cables to make your cable management in your case cleaner. The cost is 175.99.\n\n2 - Corsair 750 Watt Semi-Modular 80 Plus Bronze. This semi-modular power supply ensures that cable management is easier by being able to remove some unused cables and with 750 watts of power capable of running your entire system. It’s 80+ Bronze certification ensures that the system is fairly efficient. The cost is 114.99\n\n")
powerSupply = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
if powerSupply == 1:
        powerSupply = 175.99
        powerSupplyType =  'Corsair 750 Watt, 80+ Platinum Certified'
elif powerSupply == 2:
        powerSupply = 114.99
        powerSupplyType =  'Corsair 750 Watt, 80+ Bronze Certified'


# This code tells you that you are at the need of the program and it prints the cost of each code shows you your subtotal as well as your total with tax added in.
print('\033[1;39;40m','...\n\nYour computer build is complete! Here’s a reminder of your selections:\n\n')
print(format("Component","15"), format("Selection",'45'), 'Cost\n'
     ,format("Monitor","15"), format(moniterType,'45'), '$',float(moniter)
,'\n',format("CPU","15"), format(cpuType,'45'), '$',float(cpu)
,'\n',format("GPU","15"), format(gpuType,'45'), '$',float(gpu)
,'\n',format("Ram","15"), format(ramType,'45'), '$',float(ram)
,'\n',format("Keyboard","15"), format(keyboardType,'45'), '$',float(keyboard)
,'\n',format("Motherboard","15"), format(motherboardType,'45'), '$',float(motherboard)
,'\n',format("Storage","15"), format(storageType,'45'), '$',float(storage)
,'\n',format("Case","15"), format(caseType,'45'), '$',float(case)
,'\n',format("Mouse","15"), format(mouseType,'45'), '$',float(mouse)
,'\n',format("Headphones","15"), format(headphonesType,'45'), '$',float(headphones)
,'\n',format("Power Supply","15"), format(powerSupplyType,'45'), '$',float(powerSupply))
totalCost = moniter + cpu + keyboard + motherboard + storage + case + powerSupply + ram + gpu + mouse + headphones
print(format('Total cost before tax:','62'),'$',format(totalCost, '.2f'))
finalCost = totalCost*1.13
print(format('Total cost after 13% HST:','62'),'$',format( finalCost, '.2f'))
