import random

a = random.sample(range(50), random.randint(10, 20))
b = random.sample(range(50), random.randint(10, 20))

print(a)
print(b)

c = [num for num in a if num in b]
print(set(c))