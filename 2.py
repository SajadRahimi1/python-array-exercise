from array import *
def withBuiltinFuction():
    numbers = array('i')
    inputNumber = int(input("Number: "))
    while(inputNumber != 0):
        numbers.append(inputNumber)
        inputNumber = int(input("Number: "))

    inputSearchNumber = int(input("Search Number: "))    
    print(numbers.index(inputSearchNumber))


def withCustomSearch():
    numbers = array('i')
    print(type(numbers))
    inputNumber = int(input("Number: "))
    while(inputNumber != 0):
        numbers.append(inputNumber)
        inputNumber = int(input("Number: "))

    inputSearchNumber = int(input("Search Number: "))    
    for i in range(0,len(numbers)):
        if (inputSearchNumber == numbers[i]):
            print(i)

withCustomSearch()