import random


def main():
    options = ["Rock", "Paper", "Scissors"]

    # Player's input
    player_choice = input("Choose Rock, Paper, or Scissors: ")
    if player_choice not in options:
        print("Invalid input.")
        return

    # Computer's choice
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")


if __name__ == "__main__":
    main()
