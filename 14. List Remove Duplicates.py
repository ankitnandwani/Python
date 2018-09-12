def rd(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

def rdus(a):
    return list(set(a))

a = [1,1,1,2,2,3,3,3,3,4,7,9,3,1,4,67,34,12,43,12]
print(a)
print(rd(a))
print(rdus(a))