mylist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
myNewlist = []
mylatestlist = []
number = int(input("Enter number : "))

for num in mylist:
    if num<5:
        print(num)

for num in mylist:
    if num<5:
        myNewlist.append(num)

print(myNewlist)

for num in mylist:
    if num<number:
        mylatestlist.append(num)

print(mylatestlist)
