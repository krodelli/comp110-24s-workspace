"""Test my garden functions."""

__author__ = "730466512"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import lookup_by_kind_and_date
from lessons.garden.garden_helpers import add_by_date


def test_add_by_kind_use_adding__to_herb() -> None:
    """Testing basic use."""
    by_kind: dict[str, list[str]] = {"herb": ["rosemary", "basil"], "lagoon": ["peanut", "beans"]}
    add_by_kind(by_kind, "herb", "thyme")
    assert by_kind == {"herb": ["rosemary", "basil", "thyme"], "lagoon": ["peanut", "beans"]}


def test_add_by_kind_edge_empty() -> None:
    """Testing edge use."""
    by_kind: dict[str, list[str]] = {}
    add_by_kind(by_kind, "herb", "thyme")
    assert by_kind == {"herb": ["thyme"]}


def test_add_by_date_use_adding_new_date() -> None: 
    """Adding new month test."""
    by_date: dict[str, list[str]] = {"April": ["thyme"]}
    add_by_date(by_date, "May", "rosemary")
    assert by_date == {"April": ["thyme"], "May": ["rosemary"]}


def test_add_by_date_edge_empty() -> None:
    """By date is empty to start."""
    by_date: dict[str, list[str]] = {}
    add_by_date(by_date, "April", "thyme")
    assert by_date == {"April": ["thyme"]}


def test_lookup_by_kind_and_date_exists_use() -> None:
    """Make sure basic use works for existing kind and date."""
    by_kind: dict[str, list[str]] = {"herb": ["thyme"]}
    by_date: dict[str, list[str]] = {"April": ["thyme"]}
    new_result: str = lookup_by_kind_and_date(by_kind, by_date, "herb", "April")
    assert new_result == "herbs to plant in April: ['thyme']"


def test_lookup_by_kind_and_date_edge_empty() -> None:
    """Make sure it works for an empty list."""
    by_kind: dict[str, list[str]] = {}
    by_date: dict[str, list[str]] = {"April": "thyme"}
    new_result: str = lookup_by_kind_and_date(by_kind, by_date, "herb", "April")
    assert new_result == "Invalid kind or date."