import random

def random_list():
    a = random.sample(range(50), random.randint(10, 20))
    print(a)
    return a

a = random_list()

def fnl(a):
    print([a[0], a[-1]])

fnl(a)

