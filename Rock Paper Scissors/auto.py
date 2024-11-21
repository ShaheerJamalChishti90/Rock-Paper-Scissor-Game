import random
import datetime
x = datetime.datetime.now()

user_name = input("Enter your name here: ").capitalize()

# Define choices
choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0


while True:
    # User input
    # https://chatgpt.com/share/66e9e3d1-b188-800a-bd74-f70b92f6d3d4
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in choices:
        print(f"Invalid choice. Please choose any one of these {tuple(choices)}.")
        continue


    # Computer choice
    computer_choice = random.choice(choices)
    
    # Print choices
    print(f"{user_name} chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score  += 1 
    else:
        print("Computer wins!")
        computer_score += 1

    print(f'User Score = {user_score} | Computer Score = {computer_score}')

    
    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print(f'Final Score:\nUser Score = {user_score}\nComputer Score = {computer_score} \nThanks for playing!')

print(f"{user_name} played this game on {x.strftime("%A %x at %I:%M:%S %p") }")