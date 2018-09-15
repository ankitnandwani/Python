import random

scope = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+={}[]|;"
length = random.randint(8,14)
pwdlst = []
while length > 0:
    pwdlst.append(random.choice(scope))
    length -= 1

print(''.join(pwdlst))