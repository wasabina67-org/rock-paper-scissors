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
