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
    return random.choice(Options.get_values())


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        result = "It's draw!"
    elif (
        (
            player_choice == Options.ROCK.value
            and computer_choice == Options.SCISSORS.value
        )
        or (
            player_choice == Options.PAPER.value
            and computer_choice == Options.ROCK.value
        )
        or (
            player_choice == Options.SCISSORS.value
            and computer_choice == Options.PAPER.value
        )
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
