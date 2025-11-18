#rock paper scissors loop until I win

import random

options = ["rock", "paper", "scissors"]

while True:

    player = None
    computer = random.choice(options)

    print(f"Choose an option from {options}")

    while player not in options:
        player = input("Enter your choice: ").lower()

    print(f"player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
            print("It's a tie")
    elif player == "rock" and computer == "scissors":
            print("You win!")
            break
    elif player == "paper" and computer == "rock":
            print("You win!")
            break
    elif player == "scissors" and computer == "paper":
            print("You win!")
            break
    else:
            print("You lose")