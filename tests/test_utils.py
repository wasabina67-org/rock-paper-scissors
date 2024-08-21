import pytest

from src.utils import Options, determine_winner, get_computer_choice, to_int


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
        (Options.SCISSORS.value, Options.PAPER.value, "You win!"),
        (Options.ROCK.value, Options.PAPER.value, "You lose!"),
        (Options.PAPER.value, Options.SCISSORS.value, "You lose!"),
        (Options.SCISSORS.value, Options.ROCK.value, "You lose!"),
        (Options.ROCK.value, Options.ROCK.value, "It's draw!"),
        (Options.PAPER.value, Options.PAPER.value, "It's draw!"),
        (Options.SCISSORS.value, Options.SCISSORS.value, "It's draw!")
    ]
)
def test_determine_winner(player_choice, computer_choice, expected_result):
    assert determine_winner(player_choice, computer_choice) == expected_result


@pytest.mark.parametrize(
    "num, expected_num",
    [
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("abc", ""),
        (None, ""),
        (1.23, 1)
    ]
)
def test_to_int(num, expected_num):
    assert to_int(num) == expected_num
