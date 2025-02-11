# ///Game choices///
# import random
# Choices=["Rock", "Paper", "Scissors"]

# # //plyer Choices//

# plyer_choices=input("Enter Rock Paper Or Scissors ").lower()

# #// computer choices//

# computer_choice = random.choice(Choices)

# # //winner dicision//

# if plyer_choices ==computer_choice: 
#     print(f"both choices are similar {plyer_choices} its a tie !")
# elif plyer_choices== "rock " and computer_choice =="scissor":
#     print(f"player wins! {plyer_choices} beats {computer_choice}.")
    
# elif plyer_choices== "paper " and computer_choice =="rock":
#     print(f"player wins! {plyer_choices} beats {computer_choice}.")

# elif plyer_choices== "scissors" and computer_choice =="paper":
#     print(f"player wins! {plyer_choices} beats {computer_choice}.")

# else:
#     print(f"Computer Wins!{computer_choice} beats{plyer_choices}.")



import random

# /// Game Choices ///
Choices = ["rock", "paper", "scissors"]

# // Player's Choice //
player_choice = input("Enter Rock, Paper, or Scissors: ").lower()

# // Computer's Choice //
computer_choice = random.choice(Choices)

# // Winner Decision //
if player_choice == computer_choice:
    print(f"Both choices are the same: {player_choice}. It's a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print(f"Player wins! {player_choice} beats {computer_choice}.")
elif player_choice == "paper" and computer_choice == "rock":
    print(f"Player wins! {player_choice} beats {computer_choice}.")
elif player_choice == "scissors" and computer_choice == "paper":
    print(f"Player wins! {player_choice} beats {computer_choice}.")
else:
    print(f"Computer wins! {computer_choice} beats {player_choice}.")


