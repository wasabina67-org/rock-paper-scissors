from utils import Options, determine_winner, get_computer_choice, to_int


def main():
    options = Options.get_values()

    # Player's input
    player_choice = to_int(input("Choose Rock(1), Paper(2), or Scissors(3): "))
    if player_choice not in options:
        print("Invalid input.")
        return

    # Computer's choice
    computer_choice = get_computer_choice()
    computer_choice_name = Options.get_names()[computer_choice - 1]
    print(f"Computer chose: {computer_choice_name}({computer_choice})")

    # Determine the winner
    print(determine_winner(player_choice, computer_choice))


if __name__ == "__main__":
    main()
