num = int(input("Enter a number : "))
check = int(input("Enter another number : "))


if num%4 == 0:
    print("Number is multiple of 4")
elif num%2 == 0:
    print("Number is multiple of 2")
else:
    print("Number is odd")

if num%check == 0:
    print(str(num) + " is multiple of " + str(check))
else:
    print(str(num) + " is not a multiple of " + str(check))