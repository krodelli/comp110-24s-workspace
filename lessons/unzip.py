"""Splitting a dictionary into two lists."""

__author__ = "730466512"


def get_keys(dictionary: dict[str, int]) -> list[str]:
    """Produce a list of all the keys in the input dictionary."""
    keys_list: list[str] = []
    for keys in dictionary:
        keys_list.append(keys)
    return keys_list


def get_values(dictionary: dict[str, int]) -> list[int]:
    """Produce a list of values in the input dictionary."""
    values_list: list[int] = []
    for keys in dictionary:
        values_list.append(dictionary[keys])
    return values_list