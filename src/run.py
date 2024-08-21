from utils import Options, get_computer_choice


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
    if player_choice == computer_choice:
        result = "It's draw!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
    else:
        result = "You lose!"
    print(result)


if __name__ == "__main__":
    main()
