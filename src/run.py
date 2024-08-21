from utils import Options, determine_winner, get_computer_choice


def main():
    options = Options.get_names()

    # Player's input
    player_choice = input("Choose Rock, Paper, or Scissors: ")
    if player_choice not in options:
        print("Invalid input.")
        return

    # Computer's choice
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    print(determine_winner(player_choice, computer_choice))


if __name__ == "__main__":
    main()
