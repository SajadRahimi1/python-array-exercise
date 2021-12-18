numbers = []

for i in range(10):
    numbers.append(int(input("Number: ")))

sum = 0
for i in numbers:
    sum = sum+i

print(sum)