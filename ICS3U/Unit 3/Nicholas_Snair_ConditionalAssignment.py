"""
course: ICS3U
filename: Nicholas_Conditional_Assignment
date: 06/03/20
name: Nicholas Snair/Michael Van Staden
description: This program will help you build a computer and show you the prices for it.
"""

#Start Pc and let it continue even after reset (Michael)
while True:
  # This is the intro to the program stating the name of it and its purpose to build you a computer and show you its price.(Nick)
  print('\033[1;39;40m'"Welcome to the Merivale Computers R Us. We look forward to helping you create the perfect computer for your needs.")

  # This will display the user with multiple options for a CPU saying what it is used for and what each different one is capable of, as well as the price.(Nick)
  print('\033[1;39;40m',"\n ....\n\nTo start you will need to pick a CPU. The central processing unit or CPU is what handles all the calculations your computer needs in order to run. This includes running software such as Windows and video games. The more cores and processing power speed (GHz) represent how powerful the CPU is at calculating and executing programs/software with more cores at higher processing power speed being better. Here are three CPU options that all come with coolers right out of the box: \n\n1 - Ryzen 3 2200g with Radeon Vega 8 graphics for $154.67.\n This is a great option for entry leveling gaming or office work with a great price and built-in graphics processing that helps display what you are doing on your monitor screen. It has 4 cores and 3.7 GHz processing speed.\n\n2 - Ryzen 5 3600. This performs calculations even faster than the Ryzen 3 and is great for gaming and office work. With more power means that in the future with new technology the Ryzen 5 will be still viable. It has 4.2 GHz processing speed and 6 cores. The cost is $239.99 \n\n3 - Ryzen 9 3900x. The ultimate gaming and office machine. If you want to run powerful programs and games at fast rates and calculate even faster then this is what you want. Top level specifications make it one of the fastest cpu and allow for even the most intense software such as 3D image processing calculations. It has 12 cores and 4.6 GHz processing speed. This comes at a cost of $579.99 \n\n")
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
  # This prompts the user that if they chose the Ryzen 3 2200g, that it  has a built-in graphics card so that they don’t need to get a GPU but they can buy a dedicated one if they need to.
  if cpu == 154.67:
    print('\033[1;39;40m',"\n ....\n\nSince you have chosen the Ryzen 3 2200g with Radeon Vega 8 graphics you won’t have to worry about spending money on a dedicated graphics card, however, if you want even crisper and clearer images feel free to upgrade to a dedicated graphics card. Press 0 if you want to skip the GPU.")

  # This will display the user with multiple options for a GPU saying what it is used for and what each different one is capable of, as well as the price. (Michael)
  print('\033[1;39;40m',"\n ....\n\nNext you will need to pick a GPU. The graphics processing unit or GPU uses its many cores to perform many calculations like  CPU but just focuses on processing graphics to your monitor. The more cores the more calculations which help produce higher resolution images. Resolution dictates how clear and crisp an image is. The higher resolution the better image and common resolutions are 1080p, 1440p, 2160p). Here are some GPU options: \n\n1 - ASUS GT 1030. This is for very basic graphics such as 1080p movies but will struggle to run video games. The ASUS GT 1030 costs $119.99\n\n2 - MSI GTX 1650 Gaming X. This is an entry level gaming graphics card for 1080p. This will also run 3D image rendering for office work or artwork fairly well. The MSI GTX 1650 Gaming X costs $222.98 \n\n3 - ASUS ROG Strix RTX 2060. This card is excellent for high quality gaming at 1440p resolution and perfect for image rendering and office graphics work. The ASUS ROG Strix RTX 2060 costs $519.99 \n\n4 - EVGA RTX 2080 Super. This card is for the most difficult graphics processing and is used in professional 3D filmmaking. It runs games at a beautiful 2160p resolution. The EVGA RTX 2080 Super costs $979.99 \n\n")
  gpu = int(input('Please input your selection (1 or 2 or 3 or 4):' '\033[1;31;40m'))
  if gpu == 1:
    gpu = 119.99
    gpuType =  'ASUS GT 1030'
  elif gpu == 2:
    gpu = 222.98
    gpuType =  'MSI GTX 1650 Gaming X'
  elif gpu == 3:
    gpu = 519.99
    gpuType =  'Asus ROG Strix RTX 2060'
  elif gpu == 4:
    gpu = 979.99
    gpuType =  'EVGA RTX 2080 Super'
  elif gpu == 0:
    gpu = 0.00
    gpuType =  'Included in CPU'

  #This will display the user with multiple options for a monitor saying what it is used for and what each different one is capable of, as well as the price.(Nick)
  print('\033[1;39;40m',"\n ....\n\nNext you will need to pick a Monitor. To display what your graphics card is outputting you will need a monitor. For your PC. This is where your GPU inputs its calculations and the monitor takes these calculations and displays them. Depending on the power of your chosen GPU you can select different monitor's that have different resolutions (1080p, 1440p, 2160p). Here are three options:\n\n1 - Acer SB220Q. This an entry level monitor with 1080p resolution across 21.5 inches. The cost is $120.15\n\n2 - Acer V277U. This 1440p monitor displays great images across 27 inches. The cost is $304.68\n\n3 - LG 27UL500-W. This is a high end 2160p monitor that spans 27 inches. The cost is $424.98 \n\n")
  monitor = int(input('Please input your selection (1 or 2 or 3):' '\033[1;31;40m'))
  if monitor == 1:
        monitor = 120.15
        monitorType =  'Acer SB220Q 1080p'
  elif monitor == 2:
        monitor = 304.68
        monitorType = "Acer V277U"
  elif monitor == 3:
        monitor = 424.98
        monitorType = "LG 27UL500-W"

  # This will display the user with multiple options for a RAM saying what it is used for and what each different one is capable of, as well as the price.(Nick)
  print('\033[1;39;40m',"\n ....\n\nNext you will need to pick RAM. Random access memory or RAM is like a short term memory of your brain for a computer. Opening up tabs on your search engine, running video games, and other tasks all take up RAM memory. The higher the amount of RAM memory you have the more programs you can have running at one time. Common RAM memory is 8gb typically used for few tasks running at a time and 16gb is for running a lot of tasks at one time. RAM uses transmitted data at different speeds such as 2600MHz and 3000MHz which dictate how fast this data can be transmitted with higher being faster.. Here are two RAM options: \n\n1 - The Corsair 8GB DDR4 Dram will provide short term memory for your computer that includes opening up internet browser tabs or playing a game or opening up photoshop it all needs RAM. With more ram you are able to have more things running at once with multiple programs at once such as streaming gameplay with a screen recorder and actually running the game. 8gb is perfect for lower level games, office work, and having very few programs open at once. It has a speed of 2600Mhz The Corsair 8GB DDR4 Dram costs $54.99\n\n2 - Corsair Vengeance LPX 16GB DDR4 DRAM 3000MHz. Perhaps you are finding you want to have more programs running such as creating videos, research tabs, games open, video editors, and whatever you want then maybe consider getting even more RAM to handle all the memory requirements. With double the capabilities you will be able to run almost any program and others at the same time. With the added speed of 3000MHz means that you are able to run even faster. The cost is $104.99 \n\n")
  ram = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
  if ram == 1:
        ram = 54.99
        ramType =  'Corsair 8GB DDR4 DRAM 2600MHz'
  elif ram == 2:
        ram = 104.99
        ramType =  'Corsair Vengeance LPX 16GB DDR4 DRAM 3000MHz'

  # This will display the user with multiple options for a Storage saying what it is used for and what each different one is capable of, as well as the price. (Michael)
  print('\033[1;39;40m', "\n ....\n\nNext you will need to pick a HDD. HDD stands for hard disk drive that uses disks to write and information from the computer. This is like your long term memory in your brain. It stores important files like photos, download programs, and video game save files. The amount of storage dictates how much you can store before you can not store anymore. 2TB is an average HDD storage and is capable of holding 4 million photos or 70 4k footage. The write speed dictates how fast you can download files and save files and the read speed dictates how fast you can open files and run files like loading video games. This speed is dependent on the revolutions per minute or RPM of the disks (how fast the discs spin to receive/send information) and higher RPM is better. Here are two memory storage options: \n\n1 -Seagate BarraCuda 2TB. This has one of the best HDD speeds of 7200 RPM allowing super fast read/write speeds. The Seagate BarraCuda 2TB costs $64.99\n\n2 - The Seagate 2TB FireCuda Gaming. With gaming in mind this is used for fast boot times for your system and games. Gaming requires lots of information to load such as loading levels. This HDD uses flash technology to speed this up drastically despite its slower read/write speeds with 5400 RPM. The Seagate 2TB FireCuda Gaming costs $99.99 \n\n")
  storage = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
  if storage == 1:
        storage = 64.99
        storageType =  'Seagate BarraCuda 2TB'
  elif storage == 2:
        storage = 99.99
        storageType =  'Seagate 2TB FireCuda Gaming'

  # This will display the user with multiple options for a power supply saying what it is used for and what each different one is capable of, as well as the price.(Nick)
  print('\033[1;39;40m', "\n ....\n\nThe power supply unit or PSU is what takes electricity from the outlet (AC) and turns into usable electricity (DC) for your computer parts. This powers all the components and with different components the more power (Watts) it needs in order to run. We recommend 750 Watt PSU and it covers any power demand your computer has. Efficiency measured and certified by their 80+ ratings. This can be Bronze, Silver, Gold, and Platinum ratings with Platinum being the best. Here are two power supply options: \n\n1 - Corsair 750 Watt, 80+ Platinum Certified, Fully Modular. This is the ultimate power and efficiency power supply. With 80+ Platinum certified guarantees peak efficiency and with 750 watts of power delivery ensures all your parts get the power they need. With fully modular wires means you only have to plug in what requires the power and leave out the other cables to make your cable management in your case cleaner. The cost is $175.99.\n\n2 - Corsair 750 Watt Semi-Modular 80 Plus Bronze. This semi-modular power supply ensures that cable management is easier by being able to remove some unused cables and with 750 watts of power capable of running your entire system. It’s 80+ Bronze certification ensures that the system is fairly efficient. The cost is $114.99\n\n")
  powerSupply = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
  if powerSupply == 1:
        powerSupply = 175.99
        powerSupplyType =  'Corsair 750 Watt, 80+ Platinum Certified'
  elif powerSupply == 2:
        powerSupply = 114.99
        powerSupplyType =  'Corsair 750 Watt, 80+ Bronze Certified'

  # This will display the user with multiple options for a Motherboard saying what it is used for and what each different one is capable of, as well as the price.(Michael)
  print('\033[1;39;40m', "\n ....\n\nNext you will need to pick a motherboard. The motherboard is what holds your main components like RAM, CPU, and GPU. It takes the power from the PSU and gives the power to the components. It acts like the central nervous system giving information to the components and taking the components calculations to transmit them in order for your programs to run. They come in many sizes such as MicroATX and ATX with ATX being larger. Larger motherboards usually contain more features and possibilities for expansion.. Here are two Motherboard options: \n\n1 - The ASRock B450 MicroATX is budget friendly, small size, and provides everything you need without the gimmicks. The ASRock B450 MicroATX costs $116.52\n\n2 -  The MSI B450 Gaming Plus Max ATX is excellent for gaming where you want to have added audio support for great sound quality, better power delivery, better heatsinks, and high speed information receiving. These all boost how under the stress of gaming that you have a reliable motherboard keeping your parts protected. It is slightly larger than the MicroATX size. The cost is $139.99\n\n")
  motherboard = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
  if motherboard == 1:
        motherboard = 116.52
        motherboardType =  'ASRock MicroATX'
  elif motherboard == 2:
        motherboard = 139.99
        motherboardType =  'MSI B450 Gaming Plus Max ATX'

  # This will display the user with multiple options for a case showing the different dimensions for them.(Nick)
  print('\033[1;39;40m', "\n ....\n\nNext you will need to pick a case. The case is what holds all the computer parts together and protects them. It also has fans built in to cool your components down so they will work better. They tend to be plastic and metal but some have tempered glass side panels to show off the components inside the computer. . Here are three case options: \n\n1 - Corsair Carbide SPEC-05 Mid-Tower. This is a great budget case with no gimmicks and will fit all your components. With the included fan and many air vents it will keep your components cool and protected. The tempered glass side panel is great for showing off your components. The cost is $59.99\n\n2 -Cooler Master MasterBox Lite Mid-Tower. This has 3 fans with RGB lighting and tempered glass side panels to show off your components. This will help cool your components and make your components look cool. The cost is $89.99")
  case = int(input('Please input your selection (1 or 2):' '\033[1;31;40m'))
  if case == 1:
        case = 59.99
        caseType =  'Corsair Carbide SPEC-05 Mid-Tower'
  elif case == 2:
        case = 89.99
        caseType =  'Cooler Master MasterBox Lite Mid-Tower'

  # This will display the user with multiple options for a Keyboard saying what it is used for and what each different one is capable of, as well as the price. (Michael)
  print('\033[1;39;40m', "\n ....\n\nNext you will need to pick a keyboard. The keyboard is where you type and transmit data to computer parts. These are calculated, translated, and then turned into action on your screen just like how you inputted what parts you wanted. These keyboards have switches behind the buttons. Membrane switches feel squishy and soft while mechanical switches feel tactile and responsive. Mechanical switches are usually more expensive with companies like Cherry MX producing high quality switches raising the price of a keyboard drastically. Here are two keyboard options: \n\n1 - Redragon K552-RGB. This budget mechanical keyboard is great for those who like the tactile feel of pressing keys down like pushing a button that clicks. It also comes with a customizable backlight for when you want to add a little flair to your roomThe cost is $55.99 1 \n\n2 - Corsair CH-9206015-NA. This keyboard has a membrane feel which feels mushy rather than a snappy button. The added features of 6 programmable keys called macros means you can assign any action to them such as opening up your favourite video game. With volume buttons and pause, play, skip, and backward media buttons allowing quick changes on the fly without having to go into settings. Also comes with a customizable backlight. The cost is $79.99 \n\n3 - Logitech Keyboard K120. An inexpensive barebones keyboard is great for reliability membrane key presses for those who just need functionality and no gimmicks for a great price. The cost is $19.99 \n\n4 - CORSAIR K95 RGB. For the ultimate keyboard with premium Cherry MX Brown mechanical key switches that make typing a dream. The feedback of these keys is unmatched for reliability especially for precise inputs during gaming. With 6 macro keys, a volume scroll wheel, and media buttons put all the features into a reliable typing machine. The cost is $269.99 \n\n")
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
        keyboardType =  'CORSAIR K95 RGB Platinum Mechanical Switch Cherry MX '

  # This will display the user with multiple options for a mouse saying what it is used for and what each different one is capable of, as well as the price. (Michael)
  print('\033[1;39;40m', "\n ....\n\nThe mouse uses buttons (left-click and right-click) and a sensor (tracks the movement of the mouse) to transmit data to the computer parts. These are calculated, translated, and then turned into action on your screen. The sensor is measured in DPI which means dots per square inch and the higher the number represents how accurate your movement of the mouse is tracked.\n\n1 - Logitech G903 LIGHTSPEED. For fast, wireless, and accurate mouse inputs especially for professional gaming this is perfect for you. With 12,000DPI you are assured that you have near maximum precision. The cost is $94.99 1 \n\n2 - Razer Mamba Elite. For fast, wired, and accurate mouse inputs especially for gaming this mouse is perfect for you. With 16,000 DPI you are assured maximum precision. The cost is $98.79  \n\n3 - Logitech M100. For a reliable, well-built, and budget friendly wired mouse this is perfect for you. With 1000 DPI it is not very precise but does what it needs to. The cost is $12.38 \n\n4 - Logitech Wireless Mouse M185. For a reliable, well-built, and budget friendly wireless mouse this is perfect for you. With 1000 DPI it is not very precise but does what it needs to. The cost is $14.88  \n\n")
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


  # This will display the user with multiple options for a headphones saying what it is used for and what each different one is capable of, as well as the price.(Michael)
  print('\033[1;39;40m', "\n ....\n\nHeadphones turn what happens in your program into sound (through speakers) or sending sound to programs (through a microphone). Program sound can be listening to music or hearing footsteps in your video game helping with immersion. Sending sound can be telling google what to search or talking to others. Key qualities of a good headset is good speaker quality, good microphone quality, and how comfortable they are to wear. Here are three case options: \n\n1 - Logitech Stereo Gaming Headset G230. If a budget friendly, comfortable, fold-away microphone, and durable headset is what you want then this headset is right for you. The cost is $49.01 \n\n2 - Logitech G432 DTS:X. With peak sound quality, folding microphone, simulated surround sound to help locate where sounds come from which is very important for gaming then this headset is for you. The cost is $69.98 \n\n3 - HyperX Cloud Alpha Pro Gaming Headset. This headset has a detachable microphone, unparalleled sound quality, unparalleled comfortability, and lightweight means you can rely on these and wear them without even feeling them on you at all. For music enthusiasts or gamers that want the best out of their headset this is for them. The cost is $134.99 \n\n")
  headphones = int(input('Please input your selection (1 or 2 or 3):' '\033[1;31;40m'))
  if headphones == 1:
        headphones = 49.01
        headphonesType =  'Logitech Stereo Gaming Headset G230'
  elif headphones == 2:
        headphones = 69.98
        headphonesType =  'Logitech G432 7.1 Virtual Surround Sound '
  elif headphones == 3:
        headphones = 134.99
        headphonesType =  'HyperX Cloud Alpha Pro Gaming Headset '

  # This code tells you that you are at the need of the program and it prints the cost of each code shows you your subtotal as well as your total with tax added in.(Nick)
  print('\033[1;39;40m','...\n\nYour computer build is complete! Here’s a reminder of your selections:\n\n')
  print(format("Component","15"), format("Selection",'45'), 'Cost\n'
     ,format("CPU","15"), format(cpuType,'45'), '$',float(cpu)
  ,'\n',format("GPU","15"), format(gpuType,'45'), '$',float(gpu)
  ,'\n',format("Monitor","15"), format(monitorType,'45'), '$',float(monitor)
  ,'\n',format("RAM","15"), format(ramType,'45'), '$',float(ram)
  ,'\n',format("HDD","15"), format(storageType,'45'), '$',float(storage)
  ,'\n',format("PSU","15"), format(powerSupplyType,'45'), '$',float(powerSupply)
  ,'\n',format("Motherboard","15"), format(motherboardType,'45'), '$',float(motherboard)
  ,'\n',format("Case","15"), format(caseType,'45'), '$',float(case)
  ,'\n',format("Keyboard","15"), format(keyboardType,'45'), '$',float(keyboard)
  ,'\n',format("Mouse","15"), format(mouseType,'45'), '$',float(mouse)
  ,'\n',format("Headphones","15"), format(headphonesType,'45'), '$',float(headphones))
  totalCost = monitor + cpu + keyboard + motherboard + storage + case + powerSupply + ram + gpu + mouse + headphones
  print(format('Total cost before tax:','62'),'$',format(totalCost, '.2f'))
  finalCost = totalCost*1.13
  print(format('Total cost after 13% HST:','62'),'$',format( finalCost, '.2f'))
  #Clear the screen and start the build process (Michael)
  RestartBuild=int(input('If you would like to build another computer press 1'))
  if RestartBuild==1:
    import os
    os.system('clear')


"""
Cases:(Nick)
“CORSAIR CARBIDE SPEC-05 Mid-Tower Gaming Case, Black - CC-9011138-WW,” Amazon.ca: Computers & Tablets. [Online]. Available: https://www.amazon.ca/CORSAIR-Carbide-SPEC-05-Mid-Tower-Gaming/dp/B07BH23K53. [Accessed: 07-Mar-2020].
“Cooler Master MasterBox Lite 5 RGB ATX Mid-Tower with 3 RGB Fans Tempered Glass Side Panel & External Cases MCW-L5S3-KGNN-02,” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/Cooler-Master-MasterBox-Mid-Tower-MCW-L5S3-KGNN-02/dp/B075N2898D/ref=sr_1_1?keywords=Cooler+Master+MasterBox+Lite+Mid-Tower&qid=1583546974&s=electronics&sr=1-1. [Accessed: 07-Mar-2020].

CPU:(Nick)
“AMD Ryzen 3 2200G Processor with Radeon Vega 8 Graphics,” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/AMD-YD2200C5FBBOX-Processor-Radeon-Graphics/dp/B079D3DBNM/ref=sr_1_1?keywords=Ryzen+3+2200g+with+Radeon+Vega+8+graphics&qid=1583536800&s=electronics&sr=1-1. [Accessed: 06-Mar-2020].
“AMD Ryzen 5 3600 6-Core, 12-thread unlocked desktop processor with Wraith Stealth cooler.,” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/AMD-Ryzen-3600-12-thread-processor/dp/B07STGGQ18/ref=sr_1_1_sspa?keywords=Ryzen+5+3600&qid=1583536863&s=electronics&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFWWlJVREQ1MkFFUk4mZW5jcnlwdGVkSWQ9QTA4MTc3ODIxV0NET1dNT1hOTE9UJmVuY3J5cHRlZEFkSWQ9QTA4NzIxMDgxUFFWODJSOEFKR0k0JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ. [Accessed: 06-Mar-2020].
“AMD Ryzen 9 3900X 12-core, 24-thread unlocked desktop processor with Wraith Prism LED Cooler,” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/AMD-Ryzen-3900X-24-thread-processor/dp/B07SXMZLP9/ref=sr_1_1?keywords=Ryzen+9+3900x&qid=1583536936&s=electronics&sr=1-1. [Accessed: 06-Mar-2020].

GPU:(Michael)
Built in Ryzen 3 2200g Radeon Vega 8 graphics ($0 additional dollars)
“ASUS PH-GT1030-O2G GeForce GT 1030 2GB Phoenix Fan OC Edition HDMI DVI Graphics Card,” Amazon.ca: Computers & Tablets. [Online]. Available: https://www.amazon.ca/ASUS-PH-GT1030-O2G-GeForce-Phoenix-Graphics/dp/B071JV26GH/ref=sr_1_1?keywords=ASUS+PH-GT1030-O2G&qid=1583537420&sr=8-1. [Accessed: 06-Mar-2020].
“MSI Gaming GeForce GTX 1650 128-Bit HDMI/DP 4GB GDRR5 HDCP Support DirectX 12 Dual Fan VR Ready OC Graphics Card (GTX 1650 Gaming X 4G),” Amazon.ca: Computers & Tablets. [Online]. Available: https://www.amazon.ca/GeForce-128-Bit-Support-DirectX-Graphics/dp/B07QTMRJTK. [Accessed: 07-Mar-2020].
“ASUS ROG Strix GeForce RTX 2060 Overclocked 6G GDDR6 HDMI DP 1.4 Gaming Graphics Card (ROG-STRIX-RTX-2060-O6G),” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/ASUS-Strix-GeForce®-Overclocked-GDDR6/dp/B07MLTTDXS/ref=sr_1_1?keywords=ASUS+ROG+Strix+GeForce+RTX+2060+Overclocked+6G+GDDR6+HDMI+DP+1.4+Gaming+Graphics+Card+(ROG-STRIX-RTX-2060-O6G)&qid=1583544036&s=electronics&sr=1-1. [Accessed: 07-Mar-2020].
“EVGA GeForce RTX 2080 Super Black Gaming, 08G-P4-3081-KR, 8GB GDDR6,” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/EVGA-GeForce-Super-Gaming-08G-P4-3081-KR/dp/B07VJPNG1M/ref=sr_1_1?keywords=EVGA+GeForce+RTX+2080+Super+Black+Gaming,+08G-P4-3081-KR,+8GB+GDDR6&qid=1583543936&s=electronics&sr=1-1. [Accessed: 07-Mar-2020].

RAM:(Nick)
“Corsair 8GB DDR4 Dram C16 Memory Kit for DDR4 Systems 8  DDR4 2666 (PC4 21300) DDR4 2666 CMK8GX4M1A2666C16,” Amazon.ca: Computers & Tablets. [Online]. Available: https://www.amazon.ca/Corsair-Memory-Systems-21300-CMK8GX4M1A2666C16/dp/B0123ZAQJE/ref=sr_1_1?keywords=Corsair+8GB+DDR4+Dram+C16+Memory+Kit+for+DDR4+Systems+8+DDR4+2666+(PC4+21300)+DDR4+2666+CMK8GX4M1A2666C16&qid=1583537240&sr=8-1. [Accessed: 06-Mar-2020].
“Corsair Vengeance LPX 16GB DDR4 DRAM 3000MHz C15 Memory ...” [Online]. Available: https://www.amazon.com/Corsair-Vengeance-3000MHz-Systems-CMK16GX4M2B3000C15B/dp/B014JESKRW. [Accessed: 07-Mar-2020].

HDD:(Michael)
“Seagate BarraCuda 2TB Internal Hard Drive HDD 3.5 Inch SATA 6 Gb/s 7200 RPM 256MB Cache 3.5-Inch (ST2000DM008),” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/Seagate-Barracuda-Internal-Drive-3-5-Inch/dp/B07H2RR55Q/ref=sr_1_1?keywords=Seagate+BarraCuda+2TB+Internal+Hard+Drive+HDD+3.5+Inch+SATA+6+Gb/s+7200+RPM+256MB+Cache+3.5-Inch+(ST2000DM008)&qid=1583540283&s=electronics&sr=1-1. [Accessed: 07-Mar-2020].
“Seagate 2TB FireCuda Gaming 2.5 inch SSHD SATA 6Gb/s Flash Accelerated (8GB) Performance Hard Drive (ST2000LXZ01/LX001),” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/Seagate-FireCuda-Hybrid-Performance-Accelerated/dp/B07H2F3741/ref=sr_1_1?keywords=Seagate+2TB+FireCuda+Gaming+2.5+inch+SSHD+SATA+6Gb/s+Flash+Accelerated+(8GB)+Performance+Hard+Drive+(ST2000LXZ01/LX001)+Gaming&qid=1583540343&s=electronics&sr=1-1. [Accessed: 07-Mar-2020].

Headphones:(Michael)
“Logitech Stereo Gaming Headset G230 (981-000541),” Amazon.ca: Computers & Tablets. [Online]. Available: https://www.amazon.ca/Logitech-Stereo-Gaming-Headset-981-000541/dp/B00BFOEY4I/ref=sr_1_2?keywords=Logitech+G230&qid=1583432849&sr=8-2. [Accessed: 06-Mar-2020].
“Logitech G432 DTS:X 7.1 Surround Sound Wired PC Gaming Headset (Leatherette),” Amazon.ca: Computers & Tablets. [Online]. Available: https://www.amazon.ca/Logitech-G432-DTS-Surround-Leatherette/dp/B07MRMHML9/ref=sr_1_1?keywords=Logitech+G432&qid=1583432953&sr=8-1. [Accessed: 06-Mar-2020].
“HyperX Cloud Alpha Pro Gaming Headset for PC, PS4 & Xbox One, Nintendo Switch (HX-HSCA-RD/AM),” Amazon.ca: Computers & Tablets. [Online]. Available: https://www.amazon.ca/HyperX-Headset-Nintendo-HX-HSCA-RD-AM/dp/B074NBSF9N/ref=sr_1_2?keywords=hyperx+cloud+alpha&qid=1583432999&sr=8-2. [Accessed: 06-Mar-2020].

Mouse: (Michael)
“Logitech G903 LIGHTSPEED Wireless Gaming Mouse (910-005083),” Amazon.ca: Computers & Tablets. [Online]. Available: https://www.amazon.ca/Logitech-G903-LIGHTSPEED-Wireless-910-005083/dp/B073843BYK/ref=sr_1_3?crid=1253TQ4DQN80K&keywords=logitech+g+pro+wireless+mouse&qid=1583433737&sprefix=logitech+g+pro,aps,163&sr=8-3&th=1. [Accessed: 06-Mar-2020].
“Razer Mamba Elite Wired Gaming Mouse: 16,000 DPI Optical Sensor - Chroma RGB Lighting - 9 Programmable Buttons - Mechanical Switches,” Amazon.ca: Computers & Tablets. [Online]. Available: https://www.amazon.ca/Razer-Mamba-Elite-Programmable-Ergonomic/dp/B07F816PH9/ref=sr_1_3?crid=ODTOLRBHONZX&keywords=razer+deathadder+elite&qid=1583433812&sprefix=razer+deatha,aps,162&sr=8-3. [Accessed: 06-Mar-2020].
“Logitech M100 USB Optical Wired Mouse, Black (910-001601),” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/Logitech-Optical-Wired-Mouse-910-001601/dp/B003B4BBFK/ref=sr_1_2?keywords=logitech+m100&qid=1583434027&sr=8-2. [Accessed: 06-Mar-2020].
“Logitech Wireless Mouse M185 - Swift Gray (910-002225),” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/Logitech-Wireless-Mouse-M185-910-002225/dp/B004YAVF8I/ref=ac_session_sims_147_3/147-0258617-5870840?_encoding=UTF8&pd_rd_i=B004YAVF8I&pd_rd_r=dfddedfa-a501-4f38-ae5a-8870a73dca0c&pd_rd_w=X4Jno&pd_rd_wg=64hNb&pf_rd_p=d1812b8f-898a-4ea6-9dd6-baa296b93dd5&pf_rd_r=4CVFAFJJY8998ZARHNDX&psc=1&refRID=4CVFAFJJY8998ZARHNDX. [Accessed: 06-Mar-2020].

Keyboard:(Michael)
“Redragon K552-RGB Mechanical Gaming Keyboard 87 Keys Small Compact RGB Backlit Keyboard USB Wired Kumara with Blue Switches Metal Construction for Windows PC Game - Black (RGB),” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/Redragon-K552-RGB-Mechanical-Keyboard-Construction/dp/B019O9BLVY/ref=sr_1_1_sspa?keywords=redragon+mech&qid=1583434126&s=electronics&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE5SE44TVk0Q0M4U0omZW5jcnlwdGVkSWQ9QTA3ODc4NDUxRzE0RlNRSlg0UklUJmVuY3J5cHRlZEFkSWQ9QTEwNDM2NDYzTE1PV1VERkdMWkpWJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ. [Accessed: 06-Mar-2020].
“Corsair CH-9206015-NA Gaming K55 RGB Keyboard, Backlit LED,” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/Corsair-CH-9206015-NA-Gaming-Keyboard-Backlit/dp/B01M4LIKLI/ref=sr_1_4?keywords=membrane+keyboard&qid=1583434332&s=electronics&sr=1-4. [Accessed: 06-Mar-2020].
“Logitech Keyboard K120,” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/Logitech-920-002478-Keyboard-K120/dp/B003ELVLKU/ref=sr_1_7?keywords=keyboard&qid=1583434541&s=electronics&sr=1-7. [Accessed: 06-Mar-2020].
“CORSAIR K95 RGB PLATINUM Mechanical Gaming Keyboard - USB Passthrough & Media Controls - Cherry MX Brown,” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/CORSAIR-PLATINUM-Mechanical-Gaming-Keyboard/dp/B01MS0I1ZK/ref=sr_1_2?crid=7Y45WLKM4P0V&keywords=k95+platinum+rgb&qid=1583434593&s=electronics&sprefix=k95+,electronics,158&sr=1-2&th=1. [Accessed: 06-Mar-2020].

Motherboard:(Michael)
“ASRock MicroATX Motherboard (B450M PRO4),” Amazon.ca: Computers & Tablets. [Online]. Available: https://www.amazon.ca/ASRock-MicroATX-Motherboard-B450M-PRO4/dp/B07FVYKFXF/ref=sr_1_1?keywords=ASRock+B450M+PRO4+Micro+ATX+AM4+Motherboard&qid=1583021165&sr=8-1. [Accessed: 06-Mar-2020].
“MSI Performance Gaming AMD Ryzen 2ND and 3rd Gen AM4 M.2 USB 3 DDR4 DVI HDMI Crossfire ATX Motherboard (B450 Gaming Plus Max),” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/MSI-Performance-Gaming-Crossfire-Motherboard/dp/B07XHH4YG4/ref=sr_1_1?keywords=MSI+Performance+Gaming+AMD+Ryzen+2ND+and+3rd+Gen+AM4+M.2+USB+3+DDR4+DVI+HDMI&qid=1583541191&s=electronics&sr=1-1. [Accessed: 07-Mar-2020].

PSU:(Nick)
“Corsair HX Series, HX750, 750 Watt, 80 Platinum Certified, Fully Modular Power Supply,” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/Corsair-CP-9020137-NA-Platinum-Performance-Supply/dp/B01N6PEBNL/ref=sr_1_1?keywords=Corsair+HX+Series,+HX750,+750+Watt,+80++Platinum+Certified,+Fully+Modular+Power+Supply&qid=1583541297&s=electronics&sr=1-1. [Accessed: 07-Mar-2020].
“Corsair CP-9020131-NA TX Series TX750M 750W 80 Plus Gold Modular Power Supply,” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/Corsair-CP-9020131-NA-TX750M-Modular-Supply/dp/B00FZLD2O0/ref=sr_1_1_sspa?keywords=Corsair+750+Watt,+80++Bronze+Certified&qid=1583548335&s=electronics&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNUZNOU9TMTFFSTdLJmVuY3J5cHRlZElkPUEwMzI4NDcwMTA2MUQ5OVYxM0pGTCZlbmNyeXB0ZWRBZElkPUEwOTk2MjkzWTFKNjU0TDg2SlkxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ. [Accessed: 07-Mar-2020].

Monitor: (Nick)
“Acer SB220Q bi 21.5’ Full HD (1920 x 1080) IPS Ultra-Thin Zero Frame Monitor (HDMI & VGA port),” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/Acer-SB220Q-Ultra-Thin-Frame-Monitor/dp/B07CVL2D2S/ref=sr_1_1?keywords=Acer+SB220Q+bi+21.5"+Full+HD+(1920+x+1080)+IPS+Ultra-Thin+Zero+Frame+Monitor+(HDMI+&+VGA+port)&qid=1583540895&s=electronics&sr=1-1. [Accessed: 07-Mar-2020].
“Acer V277U 27’ WQHD 2560 X 1440 IPS FreeSync Monitor with Speakers,” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/Acer-V277U-FreeSync-Monitor-Speakers/dp/B07M9V8XNQ/ref=sr_1_1?keywords=Acer+V277U&qid=1583540735&s=electronics&sr=1-1. [Accessed: 07-Mar-2020]
“LG 27UL500-W 27-Inch UHD (3840 x 2160) IPS Monitor with Radeon Freesync Technology and HDR10, White,” Amazon.ca: Electronics. [Online]. Available: https://www.amazon.ca/LG-27UL500-W-27-Inch-Freesync-Technology/dp/B07PGL2WVS/ref=sr_1_1?keywords=LG+27UL500-W+27-Inch+UHD+(3840+x+2160)+IPS+Monitor+with+Radeon+Freesync+Technology+and+HDR10,+White&qid=1583540613&s=electronics&sr=1-1. [Accessed: 07-Mar-2020].
"""
