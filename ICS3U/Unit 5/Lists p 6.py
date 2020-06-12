print('Please input a list of numbers')

list = input().split()

newList = [0,0,0]

maxValue = 0

if (int (list[0])>int (list[len (list)-1])):
    maxValue = list[0]
else:
    maxValue = list[len (list)-1]


for k in range(len (newList)):
    newList[k] = maxValue


print ("The list", list,"would now be", newList)
