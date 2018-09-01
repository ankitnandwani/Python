import datetime

name = input("Enter Name: ")
age = int(input("Enter Age : "))

now = datetime.datetime.now()
year = now.year
target = str((100 - age) + year)

print(name + " will turn 100 in the year " + target)

