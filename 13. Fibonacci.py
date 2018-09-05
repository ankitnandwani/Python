numbers = int(input("Enter number of numbers to generate : "))
fibb = []
a = 0
b = 1

for i in range(0, numbers):
    sum = a + b
    fibb.append(sum)
    a = b
    b = sum

print(fibb)
