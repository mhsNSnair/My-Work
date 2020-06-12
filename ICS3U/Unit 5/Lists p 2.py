print('Please input a list of numbers')

list = input().split()

for e in list:
    if int (e) %2==0:
        print (e)
