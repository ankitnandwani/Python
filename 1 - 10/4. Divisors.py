num = int(input("Enter number : "))
mylist = []
for n in range(2,num):
    if num%n == 0:
        mylist.append(n)

print("Divisors are : " + str(mylist))