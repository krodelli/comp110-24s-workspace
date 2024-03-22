"""Mutating functions."""

__author__ = "730466512"


def manual_append(numbers: list[int], number: int) -> None:
    """Mutates list by appending number to the end."""
    numbers.append(number)


a: list[int] = [1, 2, 3]
manual_append(a, 2)
print(a)


def double(integers: list[int]) -> None:
    """Mutate input by multiplying every element."""
    index: int = 0
    while index < len(integers):
        integers[index] *= 2
        index += 1 


b: list[int] = [1, 2, 3]
double(b)
print(b)
