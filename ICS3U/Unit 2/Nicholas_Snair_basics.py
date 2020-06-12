#Varibales based around my date of birth
initialSpeed = 27
gravityFactor = 2
#Asks for a power factor input
print('Enter power factor:')
#Sets the power factor to the next typed in number in red
powerFactor = float(input('\033[1;31;40m'))
#Asks for a points factor input
print('\033[1;37;40m''Enter points factor (between 1.0 and 2.0):')
#Sets the points factor to the next typed in number in red
pointsFactor = float(input('\033[1;31;40m'))
#If the points factor input is less than 1 than display a error and stop the program
if pointsFactor <1:
    print('\033[1;37;40m','ERROR')
    exit()
#If the points factor input is more than 2 than display a error and stop the program
if pointsFactor >2:
    print('\033[1;37;40m','ERROR')
    exit()
#Calculations with extra varibales for eaiser calculations
jumpSpeed = initialSpeed*powerFactor
Height1 = jumpSpeed*1000
gravityFactor2 = gravityFactor*gravityFactor
Height = Height1/gravityFactor2
Points = Height*pointsFactor
#Prints the amount of points you got in red
print('\033[1;37;40m''You gained','\033[1;31;40m',int(Points),'\033[1;37;40m','points!!!!')
if Points == 5670000:
    print('You are the ultimate winner!!')
