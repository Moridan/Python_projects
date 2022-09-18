import random

exit = False
choices = ["Rock", "Paper", "Scissors"]

while exit == False:
    player = input("Rock, paper or scissors?: ")
    computer = random.choice(choices)
    if player == computer:
        print("It's a draw, try again")
    elif (player == "Rock" and computer == "Scissors") or (player == "Paper" and computer == "Rock") or (player == "Scissors" and computer == "Paper"):
        print(f"{player} beats {computer}, You win!")
    elif player not in ("Scissors" or "Rock" or "Paper"):  #Als user verkeerde input geeft opnieuw proberen.
        print("Invalid choise, try again")
    elif player == 'exit':
        exit = True
    else:
        print(f"{computer} beats {player}, computer has won!")
