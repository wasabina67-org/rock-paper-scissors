import pytest

from src.utils import Options, determine_winner, get_computer_choice


def test_options_get_names():
    assert Options.get_names() == ["Rock", "Paper", "Scissors"]


def test_options_get_values():
    assert Options.get_values() == [1, 2, 3]


def test_get_computer_choice():
    assert get_computer_choice() in Options.get_values()


@pytest.mark.parametrize(
    "player_choice, computer_choice, expected_result",
    [
        (Options.ROCK.value, Options.SCISSORS.value, "You win!"),
        (Options.PAPER.value, Options.ROCK.value, "You win!"),
        (Options.SCISSORS.value, Options.PAPER.value, "You win!")
    ]
)
def test_determine_winner(player_choice, computer_choice, expected_result):
    assert determine_winner(player_choice, computer_choice) == expected_result
