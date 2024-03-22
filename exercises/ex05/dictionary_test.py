"""Tests dictionary function."""

__author__ = "730466512"

# part one, invert testing.  

from exercises.ex05.dictionary import invert
import pytest
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count


def test_invert_basic() -> None:
    """Testing basic functionality with basic example."""
    test: dict[str, int] = {"a": 1, "b": 2}
    assert invert(test) == {1: "a", 2: "b"}


def test_invert_empty() -> None:
    """Testing empty dictionary should return empty."""
    test: dict[str, int] = {}
    assert invert(test) == {}


def test_invert_duplicates() -> None:
    """Testing to make sure duplicates result in key error."""
    with pytest.raises(KeyError):
        test: dict[str, int] = {"a": 1, "b": 1}
        invert(test)

# part 2 favorite color. 


def test_favorite_color_basic() -> None:
    """Makes sure it works with a basic example of strings."""
    test: dict[str, str] = {"Kate": "red", "Mark": "red", "Bob": "yellow"}
    assert favorite_color(test) == "red"


def test_favorite_color_no_duplicates() -> None:
    """Makes sure it returns the color appearing first if there is a tie."""
    test: dict[str, str] = {"Kate": "red", "Mark": "yellow", "Bob": "blue"}
    assert favorite_color(test) == "red"


def test_favorite_color_empty() -> None:
    """Make sure it works with an empty input dictionary."""
    test: dict[str, str] = {}
    assert favorite_color(test) == ""

# part 3 count.
    

def test_count_no_repeats() -> None:
    """Running with a basic example works correctly each name appears once."""
    test: list[str] = ["Kate", "Bob", "Sue"]
    assert count(test) == {"Kate": 1, "Bob": 1, "Sue": 1}


def test_count_multiple() -> None:
    """Makes sure it counts the names properly when there are duplicates in input."""
    test: list[str] = ["Kate", "Kate", "Bob"]
    assert count(test) == {"Kate": 2, "Bob": 1}


def test_count_empty() -> None:
    """Makes sure an empty list returns an empty dictionary."""
    test: list[str] = []
    assert count(test) == {}


# part four alphabetizer 


def test_alphabetizer_basic() -> None:
    """Works properly for basic example."""
    test: list[str] = ["cat", "dog", "car", "annoy"]
    assert alphabetizer(test) == {'a': ["annoy"], 'c': ["cat", "car"], 'd': ["dog"]}


def test_alphabetizer_capitalization() -> None:
    """Works to count everything as lowercase."""
    test: list[str] = ["cat", "dog", "Car", "annoy"]
    assert alphabetizer(test) == {'a': ["annoy"], 'c': ["cat", "Car"], 'd': ["dog"]}


def test_alphabetizer_one_entry() -> None:
    """Works with only one entry."""
    test: list[str] = ["dog"]
    assert alphabetizer(test) == {'d': ["dog"]}

# part five update attendance 


def test_update_attendance_basic_adding_on() -> None:
    """Works for a basic example adding information from another day of the week."""
    test: dict[str, list[str]] = {"Monday": ["Kate", "Bob"], "Tuesday": ["Kate"]}
    update_attendance(test, "Wednesday", "Kate")
    assert test == {"Monday": ["Kate", "Bob"], "Tuesday": ["Kate"], "Wednesday": ["Kate"]}


def test_update_attendance_add_student() -> None:
    """Works to add a student to a day of the week."""
    test: dict[str, list[str]] = {"Monday": ["Kate", "Bob"], "Tuesday": ["Kate"]}
    update_attendance(test, "Monday", "Eliza")
    assert test == {"Monday": ["Kate", "Bob", "Eliza"], "Tuesday": ["Kate"]}


def test_update_attendance_empty() -> None:
    """Makes sure it works for an empty list input."""
    test: dict[str, list[str]] = {}
    update_attendance(test, "Monday", "Kate")
    assert test == {"Monday": ["Kate"]}