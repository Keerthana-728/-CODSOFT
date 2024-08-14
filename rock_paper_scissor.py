import random

print("Welcome to Rock, Paper, Scissors!")

user_score = 0
computer_score = 0

while True:

    while True:
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            break
        print("Invalid choice. Please try again!")
        
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    print(result)

    response = input("\nPlay again? (y/n): ").lower()
    if response == "y":
        continue
    elif response == "n":
        break
    else:
        print("Invalid response. Please try again!")

print(f"\nFinal score: User {user_score} - Computer {computer_score}")