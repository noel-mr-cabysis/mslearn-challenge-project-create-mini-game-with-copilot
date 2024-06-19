import random

# Write 'hello world' to the console
print('hello world')

# Create a game of rock, paper, scissors, where the user plays against the computer and has the option to play again, also includes if one of the players win, lose or draw
# also the game should inform the player if the option entered by the player is invalid.
# The game should be in a loop so that the user can play multiple times if they want to.
# Check if the minigame is terminated and if it displays your score, informing you of the number of wins and rounds.
# The game should be able to handle invalid inputs and keep track of the number of rounds played and the number of wins by the player.
# Define a function to determine the winner of a round
# The function should take two arguments: the player's choice and the computer's choice
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

def play_game():
    wins = 0
    rounds = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ")
        computer_choice = random.choice(["rock", "paper", "scissors"])

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        rounds += 1
        winner = determine_winner(player_choice, computer_choice)

        if winner == "player":
            wins += 1
            print("You win!")
        elif winner == "computer":
            print("Computer wins!")
        else:
            print("It's a draw!")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print(f"Number of rounds played: {rounds}")
    print(f"Number of wins: {wins}")

play_game()