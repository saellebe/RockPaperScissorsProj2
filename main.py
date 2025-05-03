import random
import os

# Art for different choices
def display_choice(choice):
    if choice == "rock":
        return("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
        """)
    elif choice == "paper":
        return("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
        """)
    elif choice == "scissors":
        return("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        """)

def decide_winner(player, opponent):
    if player == opponent:
        return "It's a tie!"
    elif (player == "rock" and opponent == "scissors") or \
         (player == "paper" and opponent == "rock") or \
         (player == "scissors" and opponent == "paper"):
        return "You won! "
    else:
        return "You lost! "

def play_game():
    choices = ["rock", "paper", "scissors"]
    game_active = True

    while game_active:
        invalid_input = False
        player_choice = input("Select rock, paper, or scissors (or type 'q' to quit): ").lower().strip()

        if player_choice == 'q':
            print("Thanks for playing! Goodbye.")
            break

        if player_choice not in choices:
            print("Invalid input, please choose rock, paper, or scissors.\n")
            continue

        opponent_choice = random.choice(choices)
        print(f"\nYou chose {player_choice} {display_choice(player_choice)}")
        print(f"The opponent chose {opponent_choice} {display_choice(opponent_choice)}")
        print(decide_winner(player_choice, opponent_choice))

        play_again = input("\nWould you like to play again? (yes/no): ").lower().strip()
        if play_again != "yes":
            game_active = False
            print("Thanks for playing!")

        # Clear the screen for a fresh start on the next round
        os.system("cls" if os.name == "nt" else "clear")

play_game()
