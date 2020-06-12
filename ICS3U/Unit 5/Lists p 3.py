print('Please input a list of numbers')

list = input().split()

for i in range (len (list)) :
    list[i]= int (list[i])
for index in range (1,len (list)):
    if (list[index]>list[index-1]):
        print (list[index])
