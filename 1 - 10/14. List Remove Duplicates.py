a = [1,2,3,4,5,5,5,6,6]


def removedups(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)

    return b


print(removedups(a))