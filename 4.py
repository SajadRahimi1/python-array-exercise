from array import *

def firstWay():
    numbers = array('i')

    lenght = int(input("Lenght of array: "))
    maxNumber = 0
    maxIndex = 0

    for i in range(0,lenght-1):
        inputNumber = int(input("Number: "))
        numbers.append(inputNumber)
        if(inputNumber > maxNumber):
            maxNumber = inputNumber
            maxIndex = i
    
    print("Max number: "+str(maxNumber) +"\n"+ "Index of max number: "+str(maxIndex))
        
def secondWay():
    numbers = array('i')

    lenght = int(input("Lenght of array: "))


    for i in range(0,lenght-1):
        numbers.append(int(input("Number: ")))

    maxNumber = 0
    maxIndex = 0
    for i in range(0,len(numbers)):
        if(numbers[i] > maxNumber):
            maxNumber = numbers[i]
            maxIndex = i
        
    
    print("Max number: "+str(maxNumber) +"\n"+ "Index of max number: "+str(maxIndex))

secondWay()