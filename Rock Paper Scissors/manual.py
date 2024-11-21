# import random
import datetime
x = datetime.datetime.now()

user_name01 = input("Enter your name here: ").capitalize()
user_name02 = input("Enter your name here: ").capitalize()

# Define choices
choices = ["rock", "paper", "scissors"]

user_score01 = 0
user_score02 = 0


while True:
    # User input
    # https://chatgpt.com/share/66e9e3d1-b188-800a-bd74-f70b92f6d3d4
    user_choice01 = input(f"{user_name01} enter your choice (rock, paper, scissors): ").lower()
    user_choice02 = input(f"{user_name02} enter your choice (rock, paper, scissors): ").lower()
    # if user_choice01 not in choices or user_choice02 not in choices:
    #     print(f"Invalid choice {user_name01 or user_name02}. Please choose any one of these {tuple(choices)}.")
    #     continue
    if user_choice01 not in choices:
        print(f"Invalid choice {user_name01}. Please choose any one of these {tuple(choices)}.")
        continue
    elif user_choice02 not in choices:
        print(f"Invalid choice {user_name02}. Please choose any one of these {tuple(choices)}.")
        continue
    # Computer choice
    # computer_choice = random.choice(choices)
    
    # Print choices
    print(f"{user_name01} chose: {user_choice01}")
    print(f"{user_name02} chose: {user_choice02}")
    
    # Determine winner
    if user_choice01 == user_choice02:
        print("It's a tie!")
    elif (user_choice01 == "rock" and user_choice02 == "scissors") or \
        (user_choice01 == "scissors" and user_choice02 == "paper") or \
        (user_choice01 == "paper" and user_choice02== "rock"):
        print(f"{user_name01} win!")
        user_score01  += 1 
    else:
        print(f"{user_name02} wins!")
        user_score02 += 1

    print(f'{user_name01} Score = {user_score01} | {user_name02} Score = {user_name02}')

    
    # Ask to play again
    play_again = input("Do you guys want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print(f'Final Score:\n{user_name01} Score = {user_score01}\n{user_name02} Score = {user_score02} \nThanks for playing!')

print(f"{user_name01} and {user_name02} played this game on {x.strftime("%A %x at %I:%M:%S %p") }")