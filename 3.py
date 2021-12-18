from array import *

numbers = array('i')

lenght = int(input("Lenght of array: "))

for i in range(0,lenght):
    numbers.append(int(input("Number: ")))

print([x for x in numbers])

for i in range(0,len(numbers)):
    numbers[i] = numbers[i]*4

print([x for x in numbers])
