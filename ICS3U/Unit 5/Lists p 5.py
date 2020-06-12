
print('Please input a list of numbers')


sum = 0

list = input().split()

for s in range (len (list)):
    sum+=int (list[s])

print ("The sum is",sum)
