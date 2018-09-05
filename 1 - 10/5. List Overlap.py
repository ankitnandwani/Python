import random

a = random.sample(range(50), random.randint(10,20))
b = random.sample(range(50), random.randint(10,20))

print("a = " + str(a))
print("b = " + str(b))
c = []

for num1 in a:
    if num1 in b:
        c.append(num1)

print("Commons : " + str(set(c)))
