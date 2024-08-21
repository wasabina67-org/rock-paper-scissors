import random
from enum import Enum


class Options(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def get_names(cls):
        return [e.name.capitalize() for e in cls]

    @classmethod
    def get_values(cls):
        return [e.value for e in cls]


def get_computer_choice():
    return random.choice(Options.get_names())


def determine_winner(player_choice, computer_choice):
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
    return result


def to_int(num):
    try:
        return int(num)
    except (ValueError, TypeError):
        return ""
