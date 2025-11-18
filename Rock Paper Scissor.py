#rock paper scissors loop

import random

options = ["rock", "paper", "scissors"]

running = True

while running:

    player = None
    computer = random.choice(options)

    print(f"Choose an option from {options}")

    while player not in options:
        player = input("Enter your choice: ").lower()

    print(f"player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
            print("It's a tie")
    elif (player == "rock" and computer == "scissors") or \
    (player == "paper" and computer == "rock") or \
    (player == "scissors" and computer == "paper"):
            print("You win!")
    else:
            print("You lose")
    if not input("Do you want to play again? (y/n): ").lower().startswith("y"):
        running = False
print("Thank you for playing!")