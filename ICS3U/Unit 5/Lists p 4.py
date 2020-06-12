print('Please input a list of numbers')

list = input().split()

for i in range (len (list)):
    list[i]=int (list[i])

maxIndex = 0
maxValue = list[0]

for index in range (1,len (list)):
    if (list[index]>maxValue):
        maxIndex = index
        maxValue = list[index]

print ("The max value",maxValue,"is found at index",maxIndex)
