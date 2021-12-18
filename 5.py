from array import *

numbers = array('i')
for i in range(10):
    numbers.append(int(input("Number: ")))  
inputSearchNumber = int(input("Search Number: "))
found = False
for i in range(0,len(numbers)):
    if (inputSearchNumber == numbers[i]):
        found = True

if(found):
    print("yes")
else:
    print("no")

