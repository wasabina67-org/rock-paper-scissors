from src.utils import Options, get_computer_choice


def test_options_get_names():
    assert Options.get_names() == ["Rock", "Paper", "Scissors"]


def test_options_get_values():
    assert Options.get_values() == [1, 2, 3]


def test_get_computer_choice():
    assert get_computer_choice() in Options.get_values()
