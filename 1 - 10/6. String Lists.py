line = input("Enter string : ")

reverse = line[::-1]

if line == reverse:
    print("String is palindrome")
else:
    print("Not Palindrome")