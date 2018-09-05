def is_prime(num):
    prime = True
    for i in range(2, int((num/2)+1)):
        if num%i == 0:
            prime = False
            break

    if prime:
        print(str(num) + " is prime")
    else:
        print(str(num) + " is not prime")


num = int(input("Enter number : "))
is_prime(num)