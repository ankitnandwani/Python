import random
cont = ""
while cont != 'exit':
    target = random.randint(1,9)
    guesscounter = 0
    guessedit = False

    while not guessedit:
        userguess = int(input("Enter your guess : "))
        guesscounter += 1
        if userguess == target:
            print("Congrats! You guessed it correctly in " + str(guesscounter) + " tries.")
            cont = input("Enter 'exit' to quit game now or simply press Enter key to continue playing : ")
            guessedit = True
        elif userguess < target:
            print("Guess a little higher")
        else:
            print("Guess a little lower")

