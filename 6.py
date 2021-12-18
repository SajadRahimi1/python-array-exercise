from array import *

numbers = array('i')

for i in range(20):
    numbers.append(int(input("Number: ")))
evenNumber = []
oddNumber = []
doraghami = []
seraghami = []
modFiveThree = []
modTwoFour = []
for i in numbers:
    if(i %2==0):
        evenNumber.append(i)
    if (i %2 !=0):
        oddNumber.append(i)
    if(i>9 and i<100):
        doraghami.append(i)
    if(i>99 and i<1000):
        seraghami.append(i)
    if(i %2==0 and i%4==0):
        modTwoFour.append(i)
    if(i %3==0 and i%5==0):
        modFiveThree.append(i)

print("Adad joz: "+str(evenNumber) + " tedad: "+str(len(evenNumber)))
print("Adad fard: "+str(oddNumber) + " tedad: "+str(len(oddNumber)))
print("Mod 3 and 5: "+str(modFiveThree))
print("Mod 2 and 4: "+str(modTwoFour))
print("Adad 3 raghami: "+str(seraghami) + " tedad: "+str(len(seraghami)))
print("Adad 2 raghami: "+str(doraghami) + " tedad: "+str(len(doraghami)))





    