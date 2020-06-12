#Prompts the user for a 3 digit number
print('Put in a 3 digit number and I will tell you the sum of those digits.')
#Takes the 3 digit input
int1 = int(input())
#If the number is less than a 3 digit number print an ERROR
if int1<100:
    print('ERROR')
#If this ERROR is printed stop the program
    exit()
#If the number is greater than a 3 digit number print an ERROR
if int1>999:
    print('ERROR')
#If this ERROR is printed stop the program
    exit()
#Print the sum 3 digit numbers digits 
print(int1//100%10+int1//10%10+int1%10)
