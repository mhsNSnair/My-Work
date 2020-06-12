#Asks the user to input 3 numbers
print('Type in 3 numbers and you will be given the average of them together.')
#Takes the 3 inputs
int1 = float(input())
int2 = float(input())
int3 = float(input())
#Adds the numbers together for easier calculations
int4= int1+int2+int3
#Divides the sum of the 3 by 3 and rounds to 1 decimal place and moves the number over by 5 spaces
print(format(int4/3,'5.1f'))
