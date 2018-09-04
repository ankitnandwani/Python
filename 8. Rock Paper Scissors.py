again = 'Y'
while again == 'Y':
    print("1. Rock\n2. Paper\n3. Scissors")
    player1 = int(input("Player 1 Select Response : "))
    player2 = int(input("Player 2 Select Response : "))

    if player1 == player2:
        print("Game Tie.")
    else:
        if player1 == 1:
            if player2 == 2:
                print("Player 2 wins")
            else:
                print("Player 1 wins")
        elif player1 == 2:
            if player2 == 1:
                print("Player 1 wins")
            else:
                print("Player 2 wins")
        else:
            if player2 == 1:
                print("Player 2 wins")
            else:
                print("Player 1 wins")

    again = input("Do you want to play again? Enter Y or N : ")
    while again != 'Y' and again != 'N':
        again = input("Do you want to play again? Enter Y or N : ")