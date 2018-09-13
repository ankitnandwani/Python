str = input("Enter string : ")
lst = str.split(" ")
lst2 = []
size = len(lst) - 1
while size >= 0:
    lst2.append(lst[size])
    size -= 1

print(' '.join(lst2))